from __future__ import annotations

import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path
from typing import Optional, Tuple


ROOT = Path(__file__).resolve().parents[3]
CHECKS = ROOT / "workspace/engine/checks.mjs"


class SkillShelfTests(unittest.TestCase):
    def _fixture(self) -> Tuple[tempfile.TemporaryDirectory, Path]:
        temporary = tempfile.TemporaryDirectory()
        root = Path(temporary.name)
        shelf = root / ".agents/skills"
        shelf.mkdir(parents=True)
        self._write_skill(shelf, "primary")
        self._write_index(shelf, ["primary"])
        return temporary, root

    def _write_skill(
        self, shelf: Path, folder: str, declared_name: Optional[str] = None
    ) -> Path:
        path = shelf / folder / "SKILL.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            "---\n"
            f"name: {declared_name or folder}\n"
            "description: Fixture skill.\n"
            "metadata:\n"
            '  version: "1.0.0"\n'
            "---\n\n"
            "# Fixture\n",
            encoding="utf-8",
        )
        return path

    def _write_index(self, shelf: Path, skills: list[str]) -> None:
        links = "\n".join(
            f"- [`{skill}`]({skill}/SKILL.md)" for skill in skills
        )
        (shelf / "README.md").write_text(
            f"# Local skills\n\n{links}\n", encoding="utf-8"
        )

    def _run(self, root: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["node", str(CHECKS), "--root", str(root), "--skills-only"],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )

    def test_valid_direct_skill_shelf_passes(self):
        temporary, root = self._fixture()
        self.addCleanup(temporary.cleanup)

        result = self._run(root)

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["skills"], ["primary"])

    def test_malformed_nested_mismatched_and_unexpected_entries_fail(self):
        cases = {
            "malformed": (
                lambda shelf: (shelf / "primary/SKILL.md").write_text(
                    "---\nname: primary\n", encoding="utf-8"
                ),
                "malformed frontmatter",
            ),
            "nested": (
                lambda shelf: self._write_skill(
                    shelf, "primary/nested", "nested"
                ),
                "nested SKILL.md is not allowed",
            ),
            "name-mismatch": (
                lambda shelf: self._write_skill(
                    shelf, "primary", "different"
                ),
                "does not match folder primary",
            ),
            "unexpected-file": (
                lambda shelf: (shelf / "NOTES.md").write_text(
                    "unexpected", encoding="utf-8"
                ),
                "unexpected skill shelf file",
            ),
        }
        for case, (mutate, expected) in cases.items():
            with self.subTest(case=case):
                temporary, root = self._fixture()
                try:
                    mutate(root / ".agents/skills")
                    result = self._run(root)
                    self.assertNotEqual(result.returncode, 0, result.stdout)
                    self.assertIn(expected, result.stderr)
                finally:
                    temporary.cleanup()

    def test_skill_tree_symlink_fails(self):
        temporary, root = self._fixture()
        self.addCleanup(temporary.cleanup)
        outside = root / "outside.yaml"
        outside.write_text("outside", encoding="utf-8")
        os.symlink(outside, root / ".agents/skills/primary/linked.yaml")

        result = self._run(root)

        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn("skill tree contains a symlink", result.stderr)

    def test_metadata_schema_rejects_missing_unquoted_invalid_and_duplicate_versions(self):
        cases = (
            ('metadata:\n  version: "1.0.0"\n', ''),
            ('"1.0.0"', '1.0.0'),
            ('"1.0.0"', '"01.0.0"'),
            ('"1.0.0"', '"1.0.0-01"'),
            ('  version: "1.0.0"', '  version: "1.0.0"\n  version: "2.0.0"'),
            ('description: Fixture skill.', 'description: ""'),
            ('description: Fixture skill.', 'description: - item'),
            ('description: Fixture skill.', 'description: # comment'),
            ('description: Fixture skill.', 'description: ? key'),
            ('description: Fixture skill.', 'description: 1e3'),
            ('description: Fixture skill.', 'description: 2026-09-12'),
            ('description: Fixture skill.', 'description: on'),
            ('description: Fixture skill.', 'description: Task:'),
            ('description: Fixture skill.', 'description: true '),
            ('description: Fixture skill.', 'description: null '),
            ('name: primary', 'name: primary\nname: primary'),
        )
        for old, new in cases:
            with self.subTest(new=new):
                temporary, root = self._fixture()
                try:
                    payload = root / ".agents/skills/primary/SKILL.md"
                    payload.write_text(payload.read_text().replace(old, new))
                    result = self._run(root)
                    self.assertNotEqual(result.returncode, 0, result.stdout)
                finally:
                    temporary.cleanup()

    def test_quoted_yaml_indicators_are_valid_strings(self):
        for value in ("- item", "# comment", "? key", "1e3", "2026-09-12", "on", "Task:", "true ", "null "):
            with self.subTest(value=value):
                temporary, root = self._fixture()
                try:
                    payload = root / ".agents/skills/primary/SKILL.md"
                    payload.write_text(payload.read_text().replace("Fixture skill.", json.dumps(value)))
                    result = self._run(root)
                    self.assertEqual(result.returncode, 0, result.stderr)
                finally:
                    temporary.cleanup()

    def test_semver_prerelease_and_build_are_valid(self):
        temporary, root = self._fixture()
        self.addCleanup(temporary.cleanup)
        payload = root / ".agents/skills/primary/SKILL.md"
        payload.write_text(payload.read_text().replace('"1.0.0"', "'2.1.0-rc.1+build.42'"))
        result = self._run(root)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_missing_skill_reference_fails_and_existing_reference_passes(self):
        temporary, root = self._fixture()
        self.addCleanup(temporary.cleanup)
        payload = root / ".agents/skills/primary/SKILL.md"
        payload.write_text(payload.read_text() + "\n[Reference](references/route.md)\n")
        self.assertNotEqual(self._run(root).returncode, 0)
        reference = payload.parent / "references/route.md"
        reference.parent.mkdir()
        reference.write_text("# Route\n")
        result = self._run(root)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_index_requires_each_real_skill_once_and_no_unknown_skill(self):
        cases = (
            (["primary", "primary"], "document primary/SKILL.md exactly once"),
            ([], "document primary/SKILL.md exactly once"),
            (["primary", "unknown"], "lists unknown skill unknown/SKILL.md"),
        )
        for documented, expected in cases:
            with self.subTest(documented=documented):
                temporary, root = self._fixture()
                try:
                    self._write_index(root / ".agents/skills", documented)
                    result = self._run(root)
                    self.assertNotEqual(result.returncode, 0, result.stdout)
                    self.assertIn(expected, result.stderr)
                finally:
                    temporary.cleanup()


if __name__ == "__main__":
    unittest.main()
