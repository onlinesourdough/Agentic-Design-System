#!/usr/bin/env python3
"""Deterministic filesystem proof for the Agentic Design System route."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


DEFAULT_TIMESTAMP = "2026-08-24T00:00:00Z"
ROUTE = "design-example"
RUN_ID_PATTERN = re.compile(r"^run-(\d{4,})$")
SLUG_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


class TraceError(RuntimeError):
    """Raised when a route cannot preserve its evidence."""


@dataclass(frozen=True)
class TraceResult:
    run_id: str
    status: str
    slug: str
    action: str
    output_path: Path
    proof_path: Path
    ledger_path: Path
    design_path: Path
    previous_run_id: Optional[str]
    previous_run_relation: Optional[str]
    inspected_prior_runs: int
    failure_path: Optional[Path]
    recovery_path: Optional[Path]
    preview_status: str
    review_status: str
    source_decision: Optional[List[Dict[str, str]]]


def repository_root() -> Path:
    """Derive the root from this file rather than the caller's cwd."""

    return Path(__file__).resolve().parents[2]


def _relative(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def _exists_or_symlink(path: Path) -> bool:
    """Include broken links: they are never a safe collection component."""

    return path.exists() or path.is_symlink()


def _assert_managed_path(root: Path, path: Path, *, directory: bool = False) -> None:
    """Reject lexical escapes, symlink traversals, and incompatible collisions."""

    try:
        relative = path.relative_to(root)
    except ValueError as exc:
        raise TraceError(f"managed path escapes repository root: {path}") from exc
    cursor = root
    for index, part in enumerate(relative.parts):
        cursor = cursor / part
        if cursor.is_symlink():
            raise TraceError(f"managed path must not traverse a symlink: {_relative(cursor, root)}")
        if not _exists_or_symlink(cursor):
            continue
        is_leaf = index == len(relative.parts) - 1
        if not is_leaf and not cursor.is_dir():
            raise TraceError(f"managed path has a non-directory parent: {_relative(cursor, root)}")
        if is_leaf and directory and not cursor.is_dir():
            raise TraceError(f"managed directory collides with a non-directory: {_relative(cursor, root)}")


def _require_regular_file(root: Path, path: Path, label: str) -> None:
    _assert_managed_path(root, path)
    if path.is_symlink() or not path.is_file():
        raise TraceError(f"{label} must be a regular file: {_relative(path, root)}")


def _ensure_managed_directory(root: Path, path: Path) -> None:
    _assert_managed_path(root, path, directory=True)
    if not _exists_or_symlink(path):
        path.mkdir(parents=True)
    _assert_managed_path(root, path, directory=True)


def _write_json(path: Path, value: Dict[str, Any]) -> None:
    if path.parent.is_symlink() or not path.parent.is_dir():
        raise TraceError(f"output parent is unavailable: {path.parent}")
    if path.is_symlink() or (path.exists() and not path.is_file()):
        raise TraceError(f"output path is not a regular file: {path}")
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _read_ledger(path: Path) -> List[Dict[str, Any]]:
    if not path.exists():
        return []
    records: List[Dict[str, Any]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError as exc:
            raise TraceError(f"ledger line {line_number} is not valid JSON") from exc
        if not isinstance(record, dict):
            raise TraceError(f"ledger line {line_number} must be an object")
        records.append(record)
    return records


def _next_run_id(records: List[Dict[str, Any]]) -> str:
    numbers = []
    for record in records:
        match = RUN_ID_PATTERN.match(str(record.get("run_id", "")))
        if match:
            numbers.append(int(match.group(1)))
    return f"run-{max(numbers, default=0) + 1:04d}"


def _append_ledger(path: Path, record: Dict[str, Any]) -> None:
    if path.parent.is_symlink() or not path.parent.is_dir():
        raise TraceError(f"ledger parent is unavailable: {path.parent}")
    if path.is_symlink() or (path.exists() and not path.is_file()):
        raise TraceError(f"ledger path is not a regular file: {path}")
    with path.open("a", encoding="utf-8") as stream:
        stream.write(json.dumps(record, sort_keys=True) + "\n")


def _preview_check(path: Path) -> Tuple[str, List[str]]:
    if not path.is_file():
        return "error", [f"preview missing: {path}"]
    text = path.read_text(encoding="utf-8")
    required = {
        "main landmark": "<main",
        "viewport": "viewport",
        "skip link": "skip-link",
        "visible focus": ":focus-visible",
        "reduced motion": "prefers-reduced-motion",
    }
    missing = [label for label, marker in required.items() if marker not in text]
    return ("ready", []) if not missing else ("error", missing)


def _review_check(path: Path) -> Tuple[str, List[str]]:
    preview_status, findings = _preview_check(path)
    if preview_status != "ready":
        return "REVISE", findings
    text = path.read_text(encoding="utf-8").lower()
    generic = [phrase for phrase in ("lorem ipsum", "john doe", "acme corp") if phrase in text]
    return ("REVISE", generic) if generic else ("PASS", [])


def _source_decision_check(root: Path, design_path: Path) -> List[Dict[str, str]]:
    """Resolve the canonical source audit into the selected semantic direction."""

    audit_path = root / "docs" / "SOURCE_AUDIT.md"
    if not audit_path.is_file() or not design_path.is_file():
        raise TraceError(
            "source decision requires docs/SOURCE_AUDIT.md and a selected DESIGN.md"
        )
    text = audit_path.read_text(encoding="utf-8")
    marker = "## Current design/source trace"
    if marker not in text:
        raise TraceError("SOURCE_AUDIT lacks the current design/source trace")
    body = text.split(marker, 1)[1]
    if "\n## " in body:
        body = body.split("\n## ", 1)[0]
    required = (
        "Role",
        "Revision/version",
        "License/reuse boundary",
        "Maintenance/availability",
        "Framework/accessibility fit",
        "Visual reason",
        "Learned versus copied",
        "Active use or rejection",
        "DESIGN marker",
    )
    sources: List[Dict[str, str]] = []
    findings: List[str] = []
    for section in re.split(r"(?m)^### ", body)[1:]:
        lines = section.strip().splitlines()
        source: Dict[str, str] = {"Source": lines[0].strip()}
        current_field: Optional[str] = None
        for line in lines[1:]:
            match = re.match(r"^- \*\*(.+?):\*\*\s+(.+)$", line)
            if match:
                current_field = match.group(1)
                source[current_field] = match.group(2).strip()
            elif current_field and line.startswith("  "):
                source[current_field] += " " + line.strip()
        missing = [field for field in required if not source.get(field)]
        if missing:
            findings.append(
                f"{source['Source']} lacks {', '.join(missing)}"
            )
        sources.append(source)
    expected_roles = {
        "UI/library source",
        "inspiration/reference source",
        "optional tool adapter",
    }
    actual_roles = {source.get("Role") for source in sources}
    if len(sources) < 3 or not expected_roles.issubset(actual_roles):
        findings.append(
            "source decision must include UI/library, inspiration/reference, "
            "and optional tool adapter roles"
        )
    design = design_path.read_text(encoding="utf-8")
    for source in sources:
        design_marker = source.get("DESIGN marker", "").strip("§")
        if design_marker and design_marker not in design:
            findings.append(
                f"{_relative(design_path, root)} does not resolve marker {design_marker}"
            )
    if findings:
        raise TraceError("source decision failed: " + "; ".join(findings))
    return sources


def _generated_preview(slug: str) -> str:
    return (
        "<!doctype html>\n"
        '<html lang="en">\n'
        "  <head>\n"
        '    <meta charset="utf-8" />\n'
        '    <meta name="viewport" content="width=device-width, initial-scale=1" />\n'
        f"    <title>{slug} — ADS proof</title>\n"
        "    <style>\n"
        "      :focus-visible { outline: 3px solid #d06b45; outline-offset: 4px; }\n"
        "      @media (prefers-reduced-motion: reduce) { * { transition: none !important; } }\n"
        "    </style>\n"
        "  </head>\n"
        "  <body>\n"
        '    <a class="skip-link" href="#proof">Skip to proof</a>\n'
        '    <main id="proof" tabindex="-1">\n'
        f"      <h1>{slug}</h1>\n"
        "      <p>This selected design was created or resumed by the ADS tracer.</p>\n"
        '      <button type="button">Review proof</button>\n'
        "    </main>\n"
        "  </body>\n"
        "</html>\n"
    )


def _ensure_selected_design(root: Path, slug: str) -> Tuple[Path, str]:
    directory = root / "workspace" / "designs" / slug
    _assert_managed_path(root, directory, directory=True)
    if _exists_or_symlink(directory):
        for name in ("BRIEF.md", "DESIGN.md", "index.html"):
            _require_regular_file(root, directory / name, f"cannot resume incomplete selected design: {slug}/{name}")
        return directory, "resume"

    _ensure_managed_directory(root, directory)
    try:
        (directory / "BRIEF.md").write_text(
            "# Deterministic ADS design brief\n\n"
            "- **Receiving outcome:** Exercise the ADS selected-design proof route.\n"
            "- **Source/reference rights, provenance, and licensing:** Repository-owned fixture text; no external asset is selected.\n"
            "- **Ownership boundary:** ADS owns the direction; any receiver separately owns implementation.\n"
            "- **Review mode:** independent\n"
            "- **Review owner:** ADS Review\n"
            "- **Receiver acceptance:** The named receiver separately accepts any generated handoff.\n",
            encoding="utf-8",
        )
        (directory / "DESIGN.md").write_text(
            "---\nname: Deterministic ADS selected design\nversion: 1.0.0\n---\n\n"
            "# Deterministic ADS selected design\n\n"
            "## Portable direction and ownership\n\n"
            "This `DESIGN.md` is the canonical portable human-readable visual direction.\n\n"
            "**Scope and non-goals:** Prove the isolated selected-design workflow only.\n\n"
            "**Review, revision, and acceptance:** ADS Review records evidence; receiver acceptance remains separate.\n\n"
            "**Known limitations:** This fixture does not claim a production rendering.\n\n"
            "source:heroui-ui-library\nsource:desengs-inspiration\nsource:openpencil-optional-adapter\n",
            encoding="utf-8",
        )
        (directory / "index.html").write_text(_generated_preview(slug), encoding="utf-8")
    except Exception:
        # A partial creation is an incomplete selection on the next run, never
        # a cue to overwrite owner files.
        raise
    return directory, "create"


def _prepare_trace_outputs(root: Path, design_path: Path, run_id: str, *, curate: bool) -> None:
    """Validate every mutable collection path before creating a run artifact."""

    for name in ("history", "runs", "state"):
        _assert_managed_path(root, design_path / name, directory=True)
    ledger_path = design_path / "history" / "runs.jsonl"
    if _exists_or_symlink(ledger_path):
        _require_regular_file(root, ledger_path, "run ledger")
    run_dir = design_path / "runs" / run_id
    _assert_managed_path(root, run_dir, directory=True)
    if _exists_or_symlink(run_dir):
        raise TraceError(f"run directory already exists: {_relative(run_dir, root)}")
    active_path = design_path / "state" / "active.json"
    if _exists_or_symlink(active_path):
        _require_regular_file(root, active_path, "active state")
    if curate and _exists_or_symlink(design_path / "proof.json"):
        _require_regular_file(root, design_path / "proof.json", "curated proof")
    for name in ("history", "runs", "state"):
        _ensure_managed_directory(root, design_path / name)


def trace_once(
    root: Path,
    *,
    slug: str,
    curate: bool = False,
    simulate_failure: bool = False,
    recover: bool = False,
    preview: bool = False,
    review: bool = False,
    source_decision: bool = False,
    timestamp: str = DEFAULT_TIMESTAMP,
) -> TraceResult:
    """Perform one deterministic route and preserve its evidence."""

    root = root.resolve()
    if not SLUG_PATTERN.fullmatch(slug):
        raise TraceError("slug must use lowercase letters, numbers, and hyphens")
    if simulate_failure and recover:
        raise TraceError("choose either --simulate-failure or --recover")
    if curate:
        preview = True
        review = True
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", timestamp):
        raise TraceError("timestamp must use UTC form YYYY-MM-DDTHH:MM:SSZ")
    design_path, action = _ensure_selected_design(root, slug)
    source_records = (
        _source_decision_check(root, design_path / "DESIGN.md")
        if source_decision
        else None
    )

    ledger_path = design_path / "history" / "runs.jsonl"
    _assert_managed_path(root, design_path / "history", directory=True)
    if _exists_or_symlink(ledger_path):
        _require_regular_file(root, ledger_path, "run ledger")
    records = _read_ledger(ledger_path)
    input_ref = f"fixture://agentic-design-system/example/{slug}"
    relevant = [record for record in records if record.get("input_ref") == input_ref]
    recovered_failures = {
        recovery.get("from_run_id")
        for record in relevant
        if isinstance(recovery := record.get("recovery"), dict)
        and recovery.get("from_run_id")
    }
    failed_prior = next(
        (
            record
            for record in reversed(relevant)
            if record.get("status") == "failed"
            and record.get("run_id") not in recovered_failures
        ),
        None,
    )
    if recover and failed_prior is None:
        raise TraceError("--recover requires a previous unresolved failed run")

    if recover:
        previous_run_id = failed_prior.get("run_id")
        previous_relation = "recovery"
    else:
        previous = relevant[-1] if relevant else None
        previous_run_id = previous.get("run_id") if previous else None
        previous_relation = "predecessor" if previous_run_id else None

    run_id = _next_run_id(records)
    _prepare_trace_outputs(root, design_path, run_id, curate=curate)
    run_dir = design_path / "runs" / run_id
    run_dir.mkdir()
    output_path = run_dir / "output.json"
    proof_path = run_dir / "proof.json"
    failure_path: Optional[Path] = None
    recovery_path: Optional[Path] = None
    _write_json(
        run_dir / "input.json",
        {
            "action": action,
            "design_slug": slug,
            "input_ref": input_ref,
            "request_kind": "selected-design",
            "route": ROUTE,
        },
    )

    if simulate_failure:
        status = "failed"
        preview_status = "not-run"
        review_status = "not-run"
        output = {
            "action": action,
            "design_slug": slug,
            "previous_run_id": previous_run_id,
            "previous_run_relation": previous_relation,
            "result": "The deterministic review fixture stopped before preview.",
            "route": ROUTE,
            "run_id": run_id,
            "status": status,
        }
        failure_path = run_dir / "failure.json"
        _write_json(
            failure_path,
            {
                "code": "DESIGN_REVIEW_FIXTURE",
                "message": "The deterministic failure fixture was requested.",
                "recoverable": True,
                "run_id": run_id,
            },
        )
        assertions = [
            "the primary skill inspected relevant prior runs",
            "the failed route preserved a failure artifact",
            "the failed predecessor remains available for recovery",
        ]
    else:
        preview_status = "not-requested"
        review_status = "not-requested"
        if preview:
            preview_status, preview_findings = _preview_check(design_path / "index.html")
            if preview_status != "ready":
                raise TraceError("selected preview failed: " + ", ".join(preview_findings))
        if review:
            review_status, review_findings = _review_check(design_path / "index.html")
            if review_status != "PASS":
                raise TraceError("selected review failed: " + ", ".join(review_findings))
        status = "succeeded"
        recovered_from = failed_prior.get("run_id") if recover and failed_prior else None
        output = {
            "action": action,
            "design_slug": slug,
            "previous_run_id": previous_run_id,
            "previous_run_relation": previous_relation,
            "recovered_from": recovered_from,
            "result": "The ADS selected-design route completed deterministically.",
            "route": ROUTE,
            "run_id": run_id,
            "status": status,
        }
        assertions = [
            "the primary skill inspected relevant prior runs",
            "the route recorded preview and review status",
            "output and proof were written under the selected design runs directory",
            "the standalone route required no AIOS or sibling System runtime",
        ]
        if recover:
            recovery_path = run_dir / "recovery.json"
            _write_json(
                recovery_path,
                {
                    "action": "reroute the selected design after its recorded failure",
                    "from_run_id": failed_prior.get("run_id"),
                    "run_id": run_id,
                    "status": "recovered",
                },
            )
            assertions = [
                "the primary skill inspected a prior failed run",
                "the route completed after the recorded failure",
                "recovery evidence points to the failed predecessor",
            ]

    if source_records:
        assertions.append(
            "the source decision resolved three materially different roles"
        )
    _write_json(output_path, output)
    _write_json(
        proof_path,
        {
            "assertions": assertions,
            "curated_design_ref": f"workspace/designs/{slug}/" if curate else None,
            "failure_ref": _relative(failure_path, root) if failure_path else None,
            "input_ref": input_ref,
            "ledger_ref": f"workspace/designs/{slug}/history/runs.jsonl#{run_id}",
            "preview": preview_status,
            "previous_run_id": previous_run_id,
            "previous_run_relation": previous_relation,
            "proof_ref": _relative(proof_path, root),
            "recovery_ref": _relative(recovery_path, root) if recovery_path else None,
            "review": review_status,
            "run_id": run_id,
            "status": status,
            "source_decision": source_records,
        },
    )
    _append_ledger(
        ledger_path,
        {
            "failure": (
                {"code": "DESIGN_REVIEW_FIXTURE", "ref": _relative(failure_path, root)}
                if failure_path
                else None
            ),
            "finished_at": timestamp,
            "input_ref": input_ref,
            "output_ref": _relative(output_path, root),
            "previous_run_id": previous_run_id,
            "previous_run_relation": previous_relation,
            "proof_ref": _relative(proof_path, root),
            "recovery": (
                {"from_run_id": failed_prior.get("run_id"), "ref": _relative(recovery_path, root)}
                if recovery_path and failed_prior
                else None
            ),
            "run_id": run_id,
            "started_at": timestamp,
            "status": status,
        },
    )

    if curate:
        _write_json(
            design_path / "proof.json",
            {
                "curated": True,
                "design": slug,
                "review": "PASS",
                "route": ROUTE,
                "source_proof_ref": _relative(proof_path, root),
                "source_run_id": run_id,
                "status": "succeeded",
            },
        )
    _write_json(
        design_path / "state" / "active.json",
        {
            "design_slug": slug,
            "latest_run_id": run_id,
            "preview": preview_status,
            "review": review_status,
            "status": status,
            "updated_at": timestamp,
        },
    )
    return TraceResult(
        run_id=run_id,
        status=status,
        slug=slug,
        action=action,
        output_path=output_path,
        proof_path=proof_path,
        ledger_path=ledger_path,
        design_path=design_path,
        previous_run_id=previous_run_id,
        previous_run_relation=previous_relation,
        inspected_prior_runs=len(relevant),
        failure_path=failure_path,
        recovery_path=recovery_path,
        preview_status=preview_status,
        review_status=review_status,
        source_decision=source_records,
    )


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run the deterministic ADS filesystem proof.")
    parser.add_argument("--root", type=Path, default=None, help="checkout root to operate on")
    parser.add_argument(
        "--slug",
        required=True,
        help="lowercase selected design slug; selects exactly one collection member",
    )
    parser.add_argument("--curate", action="store_true", help="mark this selected route as curated in place")
    parser.add_argument("--simulate-failure", action="store_true", help="record a recoverable fixture failure")
    parser.add_argument("--recover", action="store_true", help="recover the latest failed route for this slug")
    parser.add_argument("--preview", action="store_true", help="check the local workspace preview")
    parser.add_argument("--review", action="store_true", help="run the dependency-light review fixture")
    parser.add_argument(
        "--source-decision",
        action="store_true",
        help="trace audited source roles into the selected DESIGN.md",
    )
    parser.add_argument("--timestamp", default=DEFAULT_TIMESTAMP, help="UTC timestamp for deterministic evidence")
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    args = _parser().parse_args(argv)
    try:
        result = trace_once(
            (args.root or repository_root()),
            slug=args.slug,
            curate=args.curate,
            simulate_failure=args.simulate_failure,
            recover=args.recover,
            preview=args.preview,
            review=args.review,
            source_decision=args.source_decision,
            timestamp=args.timestamp,
        )
    except TraceError as exc:
        print(f"trace failed: {exc}", file=sys.stderr)
        return 1
    root = (args.root or repository_root()).resolve()
    print(f"route: {ROUTE}")
    print(f"slug: {result.slug}")
    print(f"action: {result.action}")
    print(f"inspected_prior_runs: {result.inspected_prior_runs}")
    print(f"run: {result.run_id}")
    print(f"status: {result.status}")
    print(f"preview: {result.preview_status}")
    print(f"review: {result.review_status}")
    print(
        f"source_decision: passed ({len(result.source_decision)} roles)"
        if result.source_decision
        else "source_decision: not-requested"
    )
    print(f"output: {_relative(result.output_path, root)}")
    print(f"proof: {_relative(result.proof_path, root)}")
    print(f"ledger: {_relative(result.ledger_path, root)}")
    if result.failure_path:
        print(f"failure: {_relative(result.failure_path, root)}")
    if result.recovery_path:
        print(f"recovery: {_relative(result.recovery_path, root)}")
    print(
        f"selected_design: {_relative(result.design_path, root)}/"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
