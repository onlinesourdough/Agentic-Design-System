#!/usr/bin/env python3
"""Deterministic filesystem proof for the Agentic Design System route."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from shutil import copyfile
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
    example_path: Optional[Path]
    previous_run_id: Optional[str]
    previous_run_relation: Optional[str]
    inspected_prior_runs: int
    failure_path: Optional[Path]
    recovery_path: Optional[Path]
    preview_status: str
    review_status: str


def repository_root() -> Path:
    """Derive the root from this file rather than the caller's cwd."""

    return Path(__file__).resolve().parents[2]


def _relative(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def _write_json(path: Path, value: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
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
    path.parent.mkdir(parents=True, exist_ok=True)
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
        "      <p>This curated example was created or resumed by the ADS tracer.</p>\n"
        '      <button type="button">Review proof</button>\n'
        "    </main>\n"
        "  </body>\n"
        "</html>\n"
    )


def _ensure_promoted_example(root: Path, slug: str, run_id: str, proof_ref: str) -> Path:
    directory = root / "examples" / slug
    directory.mkdir(parents=True, exist_ok=True)
    if not (directory / "index.html").exists():
        source_workspace = root / "workspace"
        copyfile(source_workspace / "BRIEF.md", directory / "BRIEF.md")
        copyfile(source_workspace / "DESIGN.md", directory / "DESIGN.md")
        (directory / "index.html").write_text(_generated_preview(slug), encoding="utf-8")
        (directory / "README.md").write_text(
            f"# Curated {slug} proof\n\n"
            f"This standalone example was deliberately promoted by ADS run `{run_id}`.\n\n"
            "It carries its brief, design direction, local preview, and proof without importing ADS.\n",
            encoding="utf-8",
        )
    else:
        for name in ("BRIEF.md", "DESIGN.md", "README.md"):
            if not (directory / name).exists():
                raise TraceError(f"cannot resume incomplete example: examples/{slug}/{name}")
    _write_json(
        directory / "proof.json",
        {
            "curated": True,
            "example": slug,
            "review": "PASS",
            "route": ROUTE,
            "source_proof_ref": proof_ref,
            "source_run_id": run_id,
            "status": "succeeded",
        },
    )
    gallery = root / "examples" / "index.html"
    if not gallery.exists():
        gallery.parent.mkdir(parents=True, exist_ok=True)
        gallery.write_text(
            '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><style>:focus-visible{outline:3px solid #d06b45}</style></head><body><main><h1>Curated ADS examples</h1></main></body></html>\n',
            encoding="utf-8",
        )
    gallery_text = gallery.read_text(encoding="utf-8")
    marker = f'data-tracer-example="{slug}"'
    if marker not in gallery_text:
        link = f'<p {marker}><a href="{slug}/index.html">Open {slug} proof example</a></p>'
        gallery.write_text(gallery_text.replace("</main>", f"{link}</main>", 1), encoding="utf-8")
    gallery_readme = root / "examples" / "README.md"
    if gallery_readme.exists():
        readme_text = gallery_readme.read_text(encoding="utf-8")
        if slug not in readme_text:
            gallery_readme.write_text(
                f"{readme_text.rstrip()}\n\n- [{slug} proof]({slug}/index.html)\n",
                encoding="utf-8",
            )
    return directory


def trace_once(
    root: Path,
    *,
    slug: str = "clean-clone-proof",
    promote_example: bool = False,
    simulate_failure: bool = False,
    recover: bool = False,
    preview: bool = False,
    review: bool = False,
    timestamp: str = DEFAULT_TIMESTAMP,
) -> TraceResult:
    """Perform one deterministic route and preserve its evidence."""

    root = root.resolve()
    if not SLUG_PATTERN.fullmatch(slug):
        raise TraceError("slug must use lowercase letters, numbers, and hyphens")
    if simulate_failure and recover:
        raise TraceError("choose either --simulate-failure or --recover")
    if promote_example:
        preview = True
        review = True
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", timestamp):
        raise TraceError("timestamp must use UTC form YYYY-MM-DDTHH:MM:SSZ")

    ledger_path = root / "workspace" / "history" / "runs.jsonl"
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
    run_dir = root / "workspace" / "runs" / run_id
    if run_dir.exists():
        raise TraceError(f"run directory already exists: {_relative(run_dir, root)}")
    run_dir.mkdir(parents=True)
    output_path = run_dir / "output.json"
    proof_path = run_dir / "proof.json"
    failure_path: Optional[Path] = None
    recovery_path: Optional[Path] = None
    action = "resume" if (root / "examples" / slug).exists() else "create"
    _write_json(
        run_dir / "input.json",
        {
            "action": action,
            "example_slug": slug,
            "input_ref": input_ref,
            "request_kind": "design-example",
            "route": ROUTE,
        },
    )

    if simulate_failure:
        status = "failed"
        preview_status = "not-run"
        review_status = "not-run"
        output = {
            "action": action,
            "example_slug": slug,
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
            preview_status, preview_findings = _preview_check(root / "workspace" / "index.html")
            if preview_status != "ready":
                raise TraceError("workspace preview failed: " + ", ".join(preview_findings))
        if review:
            review_status, review_findings = _review_check(root / "workspace" / "index.html")
            if review_status != "PASS":
                raise TraceError("workspace review failed: " + ", ".join(review_findings))
        status = "succeeded"
        recovered_from = failed_prior.get("run_id") if recover and failed_prior else None
        output = {
            "action": action,
            "example_slug": slug,
            "previous_run_id": previous_run_id,
            "previous_run_relation": previous_relation,
            "recovered_from": recovered_from,
            "result": "The ADS design-example route completed deterministically.",
            "route": ROUTE,
            "run_id": run_id,
            "status": status,
        }
        assertions = [
            "the primary skill inspected relevant prior runs",
            "the route recorded preview and review status",
            "output and proof were written under workspace/runs",
        ]
        if recover:
            recovery_path = run_dir / "recovery.json"
            _write_json(
                recovery_path,
                {
                    "action": "reroute the design example after its recorded failure",
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

    _write_json(output_path, output)
    _write_json(
        proof_path,
        {
            "assertions": assertions,
            "curated_example_ref": f"examples/{slug}/" if promote_example else None,
            "failure_ref": _relative(failure_path, root) if failure_path else None,
            "input_ref": input_ref,
            "ledger_ref": f"workspace/history/runs.jsonl#{run_id}",
            "preview": preview_status,
            "previous_run_id": previous_run_id,
            "previous_run_relation": previous_relation,
            "proof_ref": _relative(proof_path, root),
            "recovery_ref": _relative(recovery_path, root) if recovery_path else None,
            "review": review_status,
            "run_id": run_id,
            "status": status,
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

    example_path = None
    if promote_example:
        example_path = _ensure_promoted_example(root, slug, run_id, _relative(proof_path, root))
    _write_json(
        root / "workspace" / "state" / "active.json",
        {
            "example_slug": slug,
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
        example_path=example_path,
        previous_run_id=previous_run_id,
        previous_run_relation=previous_relation,
        inspected_prior_runs=len(relevant),
        failure_path=failure_path,
        recovery_path=recovery_path,
        preview_status=preview_status,
        review_status=review_status,
    )


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run the deterministic ADS filesystem proof.")
    parser.add_argument("--root", type=Path, default=None, help="checkout root to operate on")
    parser.add_argument("--slug", default="clean-clone-proof", help="lowercase example slug")
    parser.add_argument("--promote-example", action="store_true", help="curate this route into examples/")
    parser.add_argument("--simulate-failure", action="store_true", help="record a recoverable fixture failure")
    parser.add_argument("--recover", action="store_true", help="recover the latest failed route for this slug")
    parser.add_argument("--preview", action="store_true", help="check the local workspace preview")
    parser.add_argument("--review", action="store_true", help="run the dependency-light review fixture")
    parser.add_argument("--timestamp", default=DEFAULT_TIMESTAMP, help="UTC timestamp for deterministic evidence")
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    args = _parser().parse_args(argv)
    try:
        result = trace_once(
            (args.root or repository_root()),
            slug=args.slug,
            promote_example=args.promote_example,
            simulate_failure=args.simulate_failure,
            recover=args.recover,
            preview=args.preview,
            review=args.review,
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
    print(f"output: {_relative(result.output_path, root)}")
    print(f"proof: {_relative(result.proof_path, root)}")
    print(f"ledger: {_relative(result.ledger_path, root)}")
    if result.failure_path:
        print(f"failure: {_relative(result.failure_path, root)}")
    if result.recovery_path:
        print(f"recovery: {_relative(result.recovery_path, root)}")
    print(
        f"curated_example: {_relative(result.example_path, root)}/"
        if result.example_path
        else "curated_example: none"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
