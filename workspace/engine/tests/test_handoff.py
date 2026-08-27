from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path
from typing import Optional


ROOT = Path(__file__).resolve().parents[3]
SCRIPT = ROOT / "workspace/engine/create-handoff.mjs"
SOURCE = ROOT / "workspace"


def fingerprint(directory: Path) -> str:
    digest = hashlib.sha256()
    for path in sorted(item for item in directory.rglob("*") if item.is_file()):
        if "handoff" in path.parts:
            continue
        digest.update(path.relative_to(directory).as_posix().encode())
        digest.update(path.read_bytes())
    return digest.hexdigest()


class HandoffTests(unittest.TestCase):
    def _invoke(
        self,
        source: Path,
        output: Path,
        *arguments: str,
        receiving_owner: Optional[str] = "Receiving repository owner",
        cwd: Path = ROOT,
    ) -> subprocess.CompletedProcess[str]:
        command = ["node", str(SCRIPT), str(source), str(output)]
        if receiving_owner is not None:
            command.extend(["--receiving-owner", receiving_owner])
        command.extend(arguments)
        return subprocess.run(
            command,
            cwd=cwd,
            check=False,
            capture_output=True,
            text=True,
        )

    def _run_from(
        self, source: Path, output: Path, *arguments: str
    ) -> dict:
        result = self._invoke(source, output, *arguments)
        self.assertEqual(result.returncode, 0, result.stderr)
        return json.loads(result.stdout)

    def _run(self, output: Path, *arguments: str) -> dict:
        return self._run_from(SOURCE, output, *arguments)

    def _openpencil_arguments(self, tool: Path) -> list[str]:
        return [
            "--openpencil",
            "--openpencil-tool",
            str(tool),
            "--openpencil-source",
            "openpencil/route-console.op",
            "--openpencil-export",
            "openpencil/exports/route-console.png",
            "--openpencil-version",
            "v0.8.4",
            "--openpencil-release-revision",
            "c51d7ed41a96068a09127bbc096fee143fce0b22",
            "--openpencil-revision",
            "9c810776dab546076a5d9db791a49d9e8048dbd7",
            "--openpencil-provenance",
            "ADS-owned HTML imported through the verified release.",
            "--openpencil-review",
            "PASS",
            "--openpencil-limitations",
            "Importer CSS approximation remains visible.",
        ]

    def test_ordinary_success_and_tool_unavailable_fallback_are_non_destructive(self):
        before = fingerprint(SOURCE)
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            tool = root / "op"
            tool.write_text('#!/bin/sh\nprintf \'{"version":"0.8.4"}\\n\'\n')
            tool.chmod(tool.stat().st_mode | 0o111)

            ordinary = self._run(root / "ordinary")
            included = self._run(
                root / "included", *self._openpencil_arguments(tool)
            )
            fallback = self._run(
                root / "fallback",
                *self._openpencil_arguments(root / "missing-op"),
            )

            self.assertEqual(ordinary["openpencil"]["status"], "not-requested")
            self.assertEqual(included["openpencil"]["status"], "included")
            self.assertEqual(fallback["openpencil"]["status"], "fallback")
            self.assertFalse((root / "fallback/openpencil").exists())
            self.assertTrue(
                (root / "included/openpencil/route-console.op").is_file()
            )
            handoff = (root / "included/HANDOFF.md").read_text(encoding="utf-8")
            self.assertIn("Receiving repository owner", handoff)
            self.assertIn("c51d7ed41a96068a09127bbc096fee143fce0b22", handoff)
            self.assertIn(included["openpencil"]["source"]["sha256"], handoff)
            for name in (
                "DESIGN.md",
                "index.html",
                "theme.css",
                "tokens.json",
                "tailwind.theme.json",
                "HANDOFF.md",
            ):
                self.assertTrue((root / "fallback" / name).is_file())
        self.assertEqual(before, fingerprint(SOURCE))

    def test_missing_owner_fails_before_output_deletion(self):
        before = fingerprint(SOURCE)
        for owner in (None, "   "):
            with self.subTest(owner=owner), tempfile.TemporaryDirectory() as temporary:
                output = Path(temporary) / "handoff"
                output.mkdir()
                sentinel = output / "preserve.txt"
                sentinel.write_text("keep", encoding="utf-8")

                result = self._invoke(
                    SOURCE, output, receiving_owner=owner
                )

                self.assertNotEqual(result.returncode, 0)
                self.assertIn("non-empty --receiving-owner", result.stderr)
                self.assertEqual(sentinel.read_text(encoding="utf-8"), "keep")
        self.assertEqual(before, fingerprint(SOURCE))

    def test_excess_positionals_fail_before_output_deletion(self):
        before = fingerprint(SOURCE)
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "handoff"
            output.mkdir()
            sentinel = output / "preserve.txt"
            sentinel.write_text("keep", encoding="utf-8")

            result = self._invoke(SOURCE, output, "excess-positional")

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("at most a source and output", result.stderr)
            self.assertEqual(sentinel.read_text(encoding="utf-8"), "keep")
        self.assertEqual(before, fingerprint(SOURCE))

    def test_unsafe_output_targets_are_denied_without_source_changes(self):
        cases = (
            "repository-root",
            "selected-source",
            "repository-ancestor",
            "source-ancestor",
        )
        for case in cases:
            with self.subTest(case=case), tempfile.TemporaryDirectory() as temporary:
                container = Path(temporary) / "container"
                repository = container / "repository"
                source = repository / "fixtures/source"
                source.mkdir(parents=True)
                (source / "proof.txt").write_text("unchanged", encoding="utf-8")
                before = fingerprint(source)
                outputs = {
                    "repository-root": repository,
                    "selected-source": source,
                    "repository-ancestor": container,
                    "source-ancestor": source.parent,
                }

                result = self._invoke(
                    source, outputs[case], cwd=repository
                )

                self.assertNotEqual(result.returncode, 0)
                self.assertIn("Unsafe handoff output", result.stderr)
                self.assertTrue(source.is_dir())
                self.assertEqual(before, fingerprint(source))

    def test_lexical_artifact_escape_falls_back_without_copying_it(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "source"
            shutil.copytree(SOURCE, source)
            outside = root / "outside.op"
            outside.write_text("outside", encoding="utf-8")
            tool = self._tool(root)
            arguments = self._openpencil_arguments(tool)
            arguments[arguments.index("--openpencil-source") + 1] = "../outside.op"
            before = fingerprint(source)

            result = self._run_from(source, root / "handoff", *arguments)

            self.assertEqual(result["openpencil"]["status"], "fallback")
            self.assertIn("escapes the selected source", result["openpencil"]["reason"])
            self.assertFalse((root / "handoff/openpencil").exists())
            self.assertEqual(before, fingerprint(source))

    def test_symlink_artifact_escape_falls_back_without_copying_it(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "source"
            shutil.copytree(SOURCE, source)
            outside = root / "outside.op"
            outside.write_text("outside", encoding="utf-8")
            escape = source / "openpencil/escape.op"
            os.symlink(outside, escape)
            tool = self._tool(root)
            arguments = self._openpencil_arguments(tool)
            arguments[arguments.index("--openpencil-source") + 1] = (
                "openpencil/escape.op"
            )
            before = fingerprint(source)

            result = self._run_from(source, root / "handoff", *arguments)

            self.assertEqual(result["openpencil"]["status"], "fallback")
            self.assertIn(
                "resolves outside the selected source",
                result["openpencil"]["reason"],
            )
            self.assertFalse((root / "handoff/openpencil").exists())
            self.assertEqual(before, fingerprint(source))

    def _tool(self, root: Path) -> Path:
        tool = root / "op"
        tool.write_text('#!/bin/sh\nprintf \'{"version":"0.8.4"}\\n\'\n')
        tool.chmod(tool.stat().st_mode | 0o111)
        return tool


if __name__ == "__main__":
    unittest.main()
