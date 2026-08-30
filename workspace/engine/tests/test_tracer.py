from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from shutil import copyfile


ROOT = Path(__file__).resolve().parents[3]
TRACER_PATH = ROOT / "workspace" / "engine" / "tracer.py"
SPEC = importlib.util.spec_from_file_location("ads_tracer", TRACER_PATH)
if SPEC is None or SPEC.loader is None:
    raise ImportError(f"cannot load tracer from {TRACER_PATH}")
tracer = importlib.util.module_from_spec(SPEC)
sys.modules["ads_tracer"] = tracer
SPEC.loader.exec_module(tracer)


class TracerTests(unittest.TestCase):
    def _root(self):
        temporary = tempfile.TemporaryDirectory()
        root = Path(temporary.name) / "checkout"
        for relative in (
            "workspace/history",
            "workspace/runs",
            "workspace/state",
            "workspace/learning",
            "examples",
            "docs",
        ):
            (root / relative).mkdir(parents=True, exist_ok=True)
        for filename in ("BRIEF.md", "DESIGN.md", "index.html"):
            copyfile(ROOT / "workspace" / filename, root / "workspace" / filename)
        copyfile(ROOT / "examples" / "index.html", root / "examples" / "index.html")
        copyfile(
            ROOT / "docs" / "SOURCE_AUDIT.md",
            root / "docs" / "SOURCE_AUDIT.md",
        )
        (root / "workspace/history/runs.jsonl").write_text("", encoding="utf-8")
        return temporary, root

    def test_create_resume_preview_review_and_promotion(self):
        temporary, root = self._root()
        self.addCleanup(temporary.cleanup)

        first = tracer.trace_once(
            root,
            slug="clean-clone-proof",
            preview=True,
            review=True,
            promote_example=True,
        )
        second = tracer.trace_once(
            root,
            slug="clean-clone-proof",
            preview=True,
            review=True,
        )

        self.assertEqual(first.run_id, "run-0001")
        self.assertEqual(first.action, "create")
        self.assertEqual(first.status, "succeeded")
        self.assertTrue(first.example_path and first.example_path.is_dir())
        self.assertEqual(second.run_id, "run-0002")
        self.assertEqual(second.action, "resume")
        self.assertEqual(second.previous_run_id, "run-0001")
        self.assertEqual(second.previous_run_relation, "predecessor")
        proof = json.loads(first.proof_path.read_text(encoding="utf-8"))
        self.assertIn(
            "the standalone route required no AIOS or sibling System runtime",
            proof["assertions"],
        )
        gallery = (root / "examples/index.html").read_text(encoding="utf-8")
        self.assertIn("clean-clone-proof/index.html", gallery)

        records = [
            json.loads(line)
            for line in (root / "workspace/history/runs.jsonl").read_text().splitlines()
            if line.strip()
        ]
        self.assertEqual(len(records), 2)
        self.assertEqual(records[1]["previous_run_relation"], "predecessor")
        self.assertNotIn("raw", (root / "workspace/history/runs.jsonl").read_text().lower())

    def test_failure_recovery_is_linked_and_single_use(self):
        temporary, root = self._root()
        self.addCleanup(temporary.cleanup)

        failed = tracer.trace_once(root, slug="recovery-proof", simulate_failure=True)
        recovered = tracer.trace_once(
            root,
            slug="recovery-proof",
            recover=True,
            preview=True,
            review=True,
            promote_example=True,
        )

        self.assertEqual(failed.status, "failed")
        self.assertTrue(failed.failure_path and failed.failure_path.is_file())
        self.assertEqual(recovered.previous_run_id, failed.run_id)
        self.assertEqual(recovered.previous_run_relation, "recovery")
        self.assertTrue(recovered.recovery_path and recovered.recovery_path.is_file())
        with self.assertRaisesRegex(tracer.TraceError, "unresolved failed run"):
            tracer.trace_once(root, slug="recovery-proof", recover=True)

        records = [
            json.loads(line)
            for line in (root / "workspace/history/runs.jsonl").read_text().splitlines()
            if line.strip()
        ]
        self.assertEqual(records[0]["status"], "failed")
        self.assertEqual(records[1]["recovery"]["from_run_id"], failed.run_id)

    def test_promotion_runs_preview_and_review_by_default(self):
        temporary, root = self._root()
        self.addCleanup(temporary.cleanup)
        result = tracer.trace_once(root, slug="not-ready", promote_example=True)
        self.assertEqual(result.preview_status, "ready")
        self.assertEqual(result.review_status, "PASS")
        self.assertTrue(result.example_path and result.example_path.is_dir())

    def test_source_decision_resolves_three_materially_different_roles(self):
        temporary, root = self._root()
        self.addCleanup(temporary.cleanup)
        result = tracer.trace_once(
            root,
            slug="source-decision-proof",
            preview=True,
            review=True,
            source_decision=True,
        )
        self.assertEqual(
            {source["Role"] for source in result.source_decision or []},
            {
                "UI/library source",
                "inspiration/reference source",
                "optional tool adapter",
            },
        )
        proof = json.loads(result.proof_path.read_text(encoding="utf-8"))
        self.assertEqual(len(proof["source_decision"]), 3)


if __name__ == "__main__":
    unittest.main()
