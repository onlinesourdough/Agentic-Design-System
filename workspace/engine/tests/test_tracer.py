from __future__ import annotations

import importlib.util
import json
import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path


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
            "workspace/designs",
            "workspace/learning",
            "docs",
        ):
            (root / relative).mkdir(parents=True, exist_ok=True)
        (root / "docs/SOURCE_AUDIT.md").write_text(
            (ROOT / "docs/SOURCE_AUDIT.md").read_text(encoding="utf-8"),
            encoding="utf-8",
        )
        return temporary, root

    def test_create_resume_preview_review_and_in_place_curation(self):
        temporary, root = self._root()
        self.addCleanup(temporary.cleanup)

        first = tracer.trace_once(
            root,
            slug="clean-clone-proof",
            preview=True,
            review=True,
            curate=True,
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
        self.assertTrue(first.design_path.is_dir())
        self.assertEqual(second.run_id, "run-0002")
        self.assertEqual(second.action, "resume")
        self.assertEqual(second.previous_run_id, "run-0001")
        self.assertEqual(second.previous_run_relation, "predecessor")
        proof = json.loads(first.proof_path.read_text(encoding="utf-8"))
        self.assertIn(
            "the standalone route required no AIOS or sibling System runtime",
            proof["assertions"],
        )
        records = [
            json.loads(line)
            for line in (root / "workspace/designs/clean-clone-proof/history/runs.jsonl").read_text().splitlines()
            if line.strip()
        ]
        self.assertEqual(len(records), 2)
        self.assertEqual(records[1]["previous_run_relation"], "predecessor")
        self.assertNotIn("raw", (root / "workspace/designs/clean-clone-proof/history/runs.jsonl").read_text().lower())

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
            curate=True,
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
            for line in (root / "workspace/designs/recovery-proof/history/runs.jsonl").read_text().splitlines()
            if line.strip()
        ]
        self.assertEqual(records[0]["status"], "failed")
        self.assertEqual(records[1]["recovery"]["from_run_id"], failed.run_id)

    def test_curation_runs_preview_and_review_by_default(self):
        temporary, root = self._root()
        self.addCleanup(temporary.cleanup)
        result = tracer.trace_once(root, slug="not-ready", curate=True)
        self.assertEqual(result.preview_status, "ready")
        self.assertEqual(result.review_status, "PASS")
        self.assertTrue(result.design_path.joinpath("proof.json").is_file())

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

    def test_incomplete_existing_design_fails_without_overwriting_owner_files(self):
        temporary, root = self._root()
        self.addCleanup(temporary.cleanup)
        design = root / "workspace/designs/incomplete-owner-design"
        design.mkdir()
        brief = "# Owner brief\n\nDo not overwrite.\n"
        direction = "# Owner direction\n\nDo not overwrite.\n"
        (design / "BRIEF.md").write_text(brief, encoding="utf-8")
        (design / "DESIGN.md").write_text(direction, encoding="utf-8")

        with self.assertRaisesRegex(tracer.TraceError, "cannot resume incomplete"):
            tracer.trace_once(root, slug="incomplete-owner-design")

        self.assertEqual((design / "BRIEF.md").read_text(encoding="utf-8"), brief)
        self.assertEqual((design / "DESIGN.md").read_text(encoding="utf-8"), direction)
        self.assertFalse((design / "index.html").exists())
        self.assertFalse((design / "history").exists())
        self.assertFalse((design / "runs").exists())
        self.assertFalse((design / "state").exists())

    def test_symlinked_design_and_output_paths_fail_without_external_writes(self):
        temporary, root = self._root()
        self.addCleanup(temporary.cleanup)
        outside = Path(temporary.name) / "outside"
        outside.mkdir()
        alias = root / "workspace/designs/escaped-design"
        os.symlink(outside, alias)

        with self.assertRaisesRegex(tracer.TraceError, "must not traverse a symlink"):
            tracer.trace_once(root, slug="escaped-design")
        self.assertEqual(list(outside.iterdir()), [])

        created = tracer.trace_once(root, slug="safe-design")
        history = created.design_path / "history"
        shutil.rmtree(history)
        os.symlink(outside, history)

        with self.assertRaisesRegex(tracer.TraceError, "must not traverse a symlink"):
            tracer.trace_once(root, slug="safe-design")
        self.assertEqual(list(outside.iterdir()), [])

    def test_cli_requires_explicit_design_slug(self):
        with self.assertRaises(SystemExit):
            tracer._parser().parse_args([])


if __name__ == "__main__":
    unittest.main()
