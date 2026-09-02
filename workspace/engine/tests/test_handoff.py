from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path
from typing import Optional


ROOT = Path(__file__).resolve().parents[3]
SCRIPT = ROOT / "workspace/engine/create-handoff.mjs"
TRACER = ROOT / "workspace/engine/handoff_tracer.mjs"
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
        self,
        source: Path,
        output: Path,
        *arguments: str,
        receiving_owner: Optional[str] = "Receiving repository owner",
        cwd: Path = ROOT,
    ) -> dict:
        result = self._invoke(
            source,
            output,
            *arguments,
            receiving_owner=receiving_owner,
            cwd=cwd,
        )
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

    def _write_review(
        self,
        source: Path,
        *,
        reviewer: str = "ADS Review",
        result: str = "PASS",
        companions: tuple[str, ...] = (),
    ) -> None:
        lines = [
            "# Review evidence",
            "",
            f"Reviewer: {reviewer}",
            f"Result: {result}",
            "Reviewed DESIGN.md SHA-256: "
            f"`{hashlib.sha256(source.joinpath('DESIGN.md').read_bytes()).hexdigest()}`",
        ]
        for relative in companions:
            digest = hashlib.sha256(source.joinpath(relative).read_bytes()).hexdigest()
            lines.append(
                f"Reviewed source companion: `{relative}` — SHA-256 `{digest}`"
            )
        source.joinpath("REVIEW.md").write_text(
            "\n".join(lines) + "\n", encoding="utf-8"
        )

    def _record_reviewed_companion(self, source: Path, relative: str) -> None:
        review = source.joinpath("REVIEW.md")
        digest = hashlib.sha256(source.joinpath(relative).read_bytes()).hexdigest()
        review.write_text(
            review.read_text(encoding="utf-8").rstrip()
            + f"\nReviewed source companion: `{relative}` — SHA-256 `{digest}`\n",
            encoding="utf-8",
        )

    def _minimal_source(self, root: Path) -> Path:
        source = root / "source"
        source.mkdir(parents=True)
        source.joinpath("BRIEF.md").write_text(
            """# Minimal portable brief

- **Receiving outcome:** Apply the approved visual direction in the named receiving repository.
- **Source/reference rights, provenance, and licensing:** ADS-owned fixture text under the repository license; no external assets.
- **Review mode:** independent
- **Review owner:** ADS Review
- **Receiver acceptance:** The named receiving repository separately decides whether to accept the generated snapshot.
""",
            encoding="utf-8",
        )
        source.joinpath("DESIGN.md").write_text(
            """---
name: Minimal portable direction
version: 1.0.0
---

# Minimal portable direction

- **Known limitations:** This fixture proves the handoff contract, not a rendered implementation.
""",
            encoding="utf-8",
        )
        self._write_review(source)
        return source

    def test_minimal_handoff_needs_no_preview_assets_exports_or_tool_install(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = self._minimal_source(root)
            output = root / "handoff"

            result = self._run_from(source, output, cwd=root)

            self.assertFalse((root / "node_modules").exists())
            self.assertEqual(
                {path.name for path in output.iterdir()},
                {"BRIEF.md", "DESIGN.md", "REVIEW.md", "HANDOFF.md"},
            )
            self.assertEqual(
                {item["path"] for item in result["handoff"]["artifacts"]},
                {"BRIEF.md", "DESIGN.md", "REVIEW.md"},
            )
            self.assertEqual(
                result["companions"],
                {
                    "reviewedSourceCompanions": [],
                    "deterministicDerivedExports": [],
                },
            )
            binder = output.joinpath("HANDOFF.md").read_text(encoding="utf-8")
            self.assertIn("Contract: `ADS-HANDOFF/1`", binder)
            self.assertIn("Review mode: independent", binder)
            self.assertIn("Review owner: ADS Review", binder)
            self.assertIn("Reviewer: ADS Review", binder)
            self.assertIn("Reviewed DESIGN.md SHA-256:", binder)
            self.assertEqual(result["handoff"]["review"]["reviewOwner"], "ADS Review")
            self.assertEqual(
                result["handoff"]["review"]["reviewedSourceCompanions"], []
            )
            self.assertEqual(
                result["handoff"]["review"]["deterministicDerivedExports"], []
            )
            self.assertIn("Preview: not selected", binder)
            self.assertIn("Assets and token/theme exports: not selected", binder)

    def test_missing_review_and_unnamed_reviewer_preserve_output(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for case in ("missing", "unnamed"):
                with self.subTest(case=case):
                    source = self._minimal_source(root / case)
                    if case == "missing":
                        source.joinpath("REVIEW.md").unlink()
                    else:
                        review = source.joinpath("REVIEW.md")
                        review.write_text(
                            review.read_text(encoding="utf-8").replace(
                                "Reviewer: ADS Review\n", ""
                            ),
                            encoding="utf-8",
                        )
                    output = root / f"{case}-handoff"
                    output.mkdir()
                    sentinel = output / "preserve.txt"
                    sentinel.write_text("keep", encoding="utf-8")

                    result = self._invoke(source, output)

                    self.assertNotEqual(result.returncode, 0)
                    expected = (
                        "requires REVIEW.md or proof.json"
                        if case == "missing"
                        else "lacks a non-empty named reviewer"
                    )
                    self.assertIn(expected, result.stderr)
                    self.assertEqual(sentinel.read_text(encoding="utf-8"), "keep")

    def test_owner_review_waits_for_named_owner_decision(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = self._minimal_source(root)
            source.joinpath("assets").mkdir()
            source.joinpath("assets/selected.svg").write_text(
                "<svg/>\n", encoding="utf-8"
            )
            brief = source.joinpath("BRIEF.md")
            brief.write_text(
                brief.read_text(encoding="utf-8").replace(
                    "**Review mode:** independent", "**Review mode:** owner"
                ).replace("**Review owner:** ADS Review", "**Review owner:** Gustav Anderson"),
                encoding="utf-8",
            )
            output = root / "handoff"
            output.mkdir()
            sentinel = output / "preserve.txt"
            sentinel.write_text("keep", encoding="utf-8")

            for case, reviewer in (
                ("missing", ""),
                ("wrong", "ADS Review"),
                ("case-mismatch", "gustav anderson"),
            ):
                with self.subTest(case=case):
                    self._write_review(source, reviewer=reviewer)
                    waiting = self._invoke(
                        source,
                        output,
                        "--asset",
                        "assets/selected.svg",
                        receiving_owner="Agentic Content System",
                    )

                    self.assertEqual(waiting.returncode, 2)
                    self.assertEqual(
                        json.loads(waiting.stderr)["status"], "waiting-owner"
                    )
                    self.assertEqual(sentinel.read_text(encoding="utf-8"), "keep")

            self._write_review(source, reviewer="Gustav Anderson")
            missing_source_hash = self._invoke(
                source,
                output,
                "--asset",
                "assets/selected.svg",
                receiving_owner="Agentic Content System",
            )
            self.assertEqual(missing_source_hash.returncode, 2)
            self.assertIn("selected source companion", missing_source_hash.stderr)
            self.assertEqual(sentinel.read_text(encoding="utf-8"), "keep")

            self._write_review(
                source,
                reviewer="Gustav Anderson",
                companions=("assets/selected.svg",),
            )
            accepted = self._run_from(
                source,
                output,
                "--asset",
                "assets/selected.svg",
                receiving_owner="Agentic Content System",
            )
            self.assertEqual(accepted["receivingOwner"], "Agentic Content System")
            self.assertEqual(accepted["handoff"]["review"]["mode"], "owner")
            self.assertEqual(
                accepted["handoff"]["review"]["reviewOwner"],
                "Gustav Anderson",
            )
            self.assertEqual(
                accepted["handoff"]["review"]["reviewer"],
                "Gustav Anderson",
            )

    def test_independent_reviewer_must_match_declared_review_owner(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = self._minimal_source(root)
            self._write_review(source, reviewer="Gustav Anderson")
            output = root / "handoff"
            output.mkdir()
            sentinel = output / "preserve.txt"
            sentinel.write_text("keep", encoding="utf-8")

            denied = self._invoke(
                source,
                output,
                receiving_owner="Agentic Content System",
            )

            self.assertEqual(denied.returncode, 1)
            self.assertIn(
                "does not match BRIEF.md Review owner ADS Review", denied.stderr
            )
            self.assertEqual(sentinel.read_text(encoding="utf-8"), "keep")

    def test_stale_design_or_unreviewed_asset_is_denied(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = self._minimal_source(root)
            output = root / "handoff"
            source.joinpath("DESIGN.md").write_text(
                source.joinpath("DESIGN.md").read_text(encoding="utf-8")
                + "\nChanged after Review.\n",
                encoding="utf-8",
            )

            stale = self._invoke(source, output)

            self.assertNotEqual(stale.returncode, 0)
            self.assertIn("does not bind the current DESIGN.md", stale.stderr)
            self._write_review(source)
            source.joinpath("assets").mkdir()
            source.joinpath("assets/unreviewed.svg").write_text(
                "<svg/>\n", encoding="utf-8"
            )

            unreviewed = self._invoke(
                source, output, "--asset", "assets/unreviewed.svg"
            )

            self.assertNotEqual(unreviewed.returncode, 0)
            self.assertIn("does not list selected source companion", unreviewed.stderr)
            self.assertFalse(output.exists())

    def test_explicit_preview_asset_and_export_selection(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "source"
            shutil.copytree(SOURCE, source)
            assets = source / "assets"
            assets.mkdir(exist_ok=True)
            assets.joinpath("selected.svg").write_text("<svg/>\n", encoding="utf-8")
            assets.joinpath("unselected.svg").write_text("<svg/>\n", encoding="utf-8")
            self._record_reviewed_companion(source, "assets/selected.svg")
            output = root / "handoff"

            result = self._run_from(
                source,
                output,
                "--preview",
                "--asset",
                "assets/selected.svg",
                "--export",
                "css",
                "--export",
                "tokens",
                "--export",
                "tailwind",
            )

            for name in (
                "index.html",
                "assets/selected.svg",
                "theme.css",
                "tokens.json",
                "tailwind.theme.json",
            ):
                self.assertTrue(output.joinpath(name).is_file(), name)
            self.assertFalse(output.joinpath("assets/unselected.svg").exists())
            companion_boundary = result["companions"]
            review = result["handoff"]["review"]
            design_sha256 = hashlib.sha256(
                source.joinpath("DESIGN.md").read_bytes()
            ).hexdigest()
            self.assertEqual(review["reviewOwner"], "ADS Review")
            self.assertEqual(
                {
                    item["path"]
                    for item in companion_boundary["reviewedSourceCompanions"]
                },
                {"index.html", "assets/selected.svg"},
            )
            self.assertEqual(
                review["reviewedSourceCompanions"],
                companion_boundary["reviewedSourceCompanions"],
            )
            self.assertNotIn("theme.css", source.joinpath("REVIEW.md").read_text())
            derived = {
                item["path"]: item
                for item in companion_boundary["deterministicDerivedExports"]
            }
            self.assertEqual(
                review["deterministicDerivedExports"],
                companion_boundary["deterministicDerivedExports"],
            )
            self.assertEqual(
                set(derived), {"theme.css", "tokens.json", "tailwind.theme.json"}
            )
            for name, item in derived.items():
                self.assertEqual(item["derivedFromDesignSha256"], design_sha256)
                self.assertEqual(
                    item["sha256"],
                    hashlib.sha256(output.joinpath(name).read_bytes()).hexdigest(),
                )
            binder = output.joinpath("HANDOFF.md").read_text(encoding="utf-8")
            self.assertIn("## Review and derivation boundary", binder)
            self.assertIn("Reviewed source companions:", binder)
            self.assertIn("Deterministic derived exports:", binder)
            self.assertIn(
                f"derived from reviewed DESIGN.md SHA-256 `{design_sha256}`", binder
            )
            for name in (
                "index.html",
                "assets/selected.svg",
                "theme.css",
                "tokens.json",
                "tailwind.theme.json",
            ):
                self.assertIn(f"`{name}`", binder)

    def test_selected_export_requires_tooling_before_output_replacement(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = self._minimal_source(root)
            output = root / "handoff"
            output.mkdir()
            sentinel = output / "preserve.txt"
            sentinel.write_text("keep", encoding="utf-8")

            result = self._invoke(
                source,
                output,
                "--export",
                "tokens",
                cwd=root,
            )

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Selected token exports require", result.stderr)
            self.assertEqual(sentinel.read_text(encoding="utf-8"), "keep")

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
            self.assertIn("ADS-HANDOFF/1", handoff)
            self.assertIn("Handoff ID:", handoff)
            self.assertIn("Handoff revision:", handoff)
            self.assertIn("Receiving repository owner", handoff)
            self.assertIn("Receiving outcome:", handoff)
            self.assertIn("Acceptance state: PENDING", handoff)
            self.assertIn("## Included snapshot and integrity", handoff)
            self.assertIn("## Provenance and licensing", handoff)
            self.assertIn("## Known limitations", handoff)
            self.assertIn("c51d7ed41a96068a09127bbc096fee143fce0b22", handoff)
            self.assertIn(
                included["openpencil"]["sourceCompanion"]["sha256"], handoff
            )
            self.assertEqual(
                {
                    item["path"]
                    for item in included["handoff"]["review"][
                        "reviewedSourceCompanions"
                    ]
                },
                {
                    "openpencil/route-console.op",
                    "openpencil/exports/route-console.png",
                },
            )
            for name in ("BRIEF.md", "DESIGN.md", "REVIEW.md", "HANDOFF.md"):
                self.assertTrue((root / "fallback" / name).is_file())
            for name in (
                "index.html",
                "assets",
                "theme.css",
                "tokens.json",
                "tailwind.theme.json",
            ):
                self.assertFalse((root / "fallback" / name).exists())
            manifest = {
                item["path"]: item["sha256"]
                for item in included["handoff"]["artifacts"]
            }
            self.assertIn("BRIEF.md", manifest)
            self.assertIn("DESIGN.md", manifest)
            self.assertEqual(
                manifest["DESIGN.md"],
                hashlib.sha256(SOURCE.joinpath("DESIGN.md").read_bytes()).hexdigest(),
            )
        self.assertEqual(before, fingerprint(SOURCE))

    def test_accepted_snapshot_is_immutable_and_revision_uses_new_output(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "source"
            shutil.copytree(SOURCE, source)
            accepted_output = root / "accepted"

            first = self._run_from(source, accepted_output)
            binder_path = accepted_output / "HANDOFF.md"
            binder = binder_path.read_text(encoding="utf-8").replace(
                "Acceptance state: PENDING", "Acceptance state: ACCEPTED"
            )
            binder_path.write_text(binder, encoding="utf-8")
            accepted_before = fingerprint(accepted_output)

            design_path = source / "DESIGN.md"
            revised, replacements = re.subn(
                r"^version:\s*[^\n]+$",
                "version: test-revision",
                design_path.read_text(encoding="utf-8"),
                count=1,
                flags=re.MULTILINE,
            )
            self.assertEqual(replacements, 1)
            design_path.write_text(revised, encoding="utf-8")
            denied = self._invoke(source, accepted_output)

            self.assertNotEqual(denied.returncode, 0)
            self.assertIn("Accepted handoff snapshots are immutable", denied.stderr)
            self.assertEqual(accepted_before, fingerprint(accepted_output))

            self._write_review(source)
            second = self._run_from(source, root / "revision")
            self.assertEqual(first["handoff"]["id"], second["handoff"]["id"])
            self.assertNotEqual(
                first["handoff"]["revision"], second["handoff"]["revision"]
            )
            self.assertEqual(second["handoff"]["acceptance"], "PENDING")

    def test_missing_human_readable_contract_metadata_preserves_output(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for field in ("Receiving outcome", "Review owner"):
                with self.subTest(field=field):
                    source = root / field.lower().replace(" ", "-") / "source"
                    shutil.copytree(SOURCE, source)
                    brief_path = source / "BRIEF.md"
                    brief = brief_path.read_text(encoding="utf-8")
                    brief = brief.replace(f"**{field}:**", f"**Missing {field}:**", 1)
                    brief_path.write_text(brief, encoding="utf-8")
                    output = source.parent / "handoff"
                    output.mkdir()
                    sentinel = output / "preserve.txt"
                    sentinel.write_text("keep", encoding="utf-8")

                    result = self._invoke(source, output)

                    self.assertNotEqual(result.returncode, 0)
                    self.assertIn(
                        f"BRIEF.md lacks a non-empty **{field}:**", result.stderr
                    )
                    self.assertEqual(sentinel.read_text(encoding="utf-8"), "keep")

    def test_surface_sibling_and_revision_tracer(self):
        with tempfile.TemporaryDirectory() as temporary:
            tool = self._tool(Path(temporary))
            result = subprocess.run(
                [
                    "node",
                    str(TRACER),
                    "--openpencil-tool",
                    str(tool),
                ],
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            proof = json.loads(result.stdout)
            self.assertEqual(proof["portableContract"], "ADS-HANDOFF/1")
            self.assertEqual(proof["reviewGate"]["mode"], "independent")
            self.assertEqual(proof["reviewGate"]["reviewOwner"], "ADS Review")
            self.assertEqual(proof["reviewGate"]["reviewer"], "ADS Review")
            self.assertTrue(proof["reviewGate"]["designSha256Bound"])
            self.assertTrue(proof["reviewGate"]["selectedSourceCompanionsBound"])
            self.assertTrue(proof["reviewGate"]["derivedExportsBoundToDesign"])
            self.assertTrue(
                proof["surfaces"]["websiteApplication"]["designCanonical"]
            )
            self.assertTrue(proof["surfaces"]["dashboardSlide"]["designCanonical"])
            content = proof["surfaces"]["contentVisual"]
            self.assertEqual(content["origin"], "ACS-originated brief fixture")
            self.assertTrue(content["acceptedSnapshotImmutable"])
            self.assertFalse(content["adsRuntimeRequiredByReceiver"])
            self.assertTrue(content["selectedSnapshotOnly"])
            self.assertFalse(content["liveSync"])
            self.assertFalse(content["recursiveRequest"])
            self.assertEqual(content["nextRevisionAcceptance"], "PENDING")
            self.assertEqual(proof["contentGap"]["routing"], "suggestion-only")
            self.assertFalse(proof["contentGap"]["invoked"])

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
