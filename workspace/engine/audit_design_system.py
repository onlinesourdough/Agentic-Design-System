#!/usr/bin/env python3
"""Read-only accumulated-state audit for Agentic Design System."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple


AUDIT_SCOPES = ("repository", "workspace", "both")
LEDGER_FIELDS = {
    "failure",
    "finished_at",
    "input_ref",
    "output_ref",
    "previous_run_id",
    "previous_run_relation",
    "proof_ref",
    "recovery",
    "run_id",
    "started_at",
    "status",
}
REPOSITORY_EVIDENCE = (
    "AGENTS.md",
    "README.md",
    ".agents/skills/agentic-design-system/SKILL.md",
    ".agents/skills/design-solution/SKILL.md",
    ".agents/skills/review-design/SKILL.md",
    ".agents/skills/audit-design-system/SKILL.md",
    "docs/SOURCE_AUDIT.md",
    "docs/HANDOFF_TEMPLATE.md",
    "docs/contract.md",
    "docs/validation.md",
    "workspace/BRIEF.md",
    "workspace/DESIGN.md",
    "workspace/REVIEW.md",
    "workspace/index.html",
    "workspace/engine/checks.mjs",
    "workspace/engine/create-handoff.mjs",
    "workspace/engine/handoff_tracer.mjs",
    "workspace/engine/tracer.py",
    "workspace/engine/audit_design_system.py",
)
ROUTE_DOCUMENTS = (
    "AGENTS.md",
    "README.md",
    "docs/contract.md",
    "docs/validation.md",
    ".agents/skills/agentic-design-system/SKILL.md",
    ".agents/skills/audit-design-system/SKILL.md",
)
ENGINE_PATH = re.compile(r"workspace/engine/[A-Za-z0-9_.-]+\.(?:py|mjs)")
RUN_ID_PATTERN = re.compile(r"^run-\d{4,}$")
SOURCE_FIELDS = (
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
EXPECTED_SOURCE_ROLES = {
    "UI/library source",
    "inspiration/reference source",
    "optional tool adapter",
}


@dataclass(frozen=True)
class AuditResult:
    status: str
    scope: str
    evidence: List[str]
    gaps: List[str]
    next_action: str

    def as_dict(self) -> Dict[str, Any]:
        return {
            "status": self.status,
            "scope": self.scope,
            "evidence": self.evidence,
            "gaps": self.gaps,
            "next_action": self.next_action,
        }


def repository_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _result(
    status: str, scope: str, evidence: Iterable[str], gaps: Iterable[str]
) -> AuditResult:
    if status == "PASS":
        next_action = "No action; keep the audit read-only."
    elif status == "FAIL":
        next_action = (
            "Route the finding to ADS Build/Review; use AIOS improvement triage "
            "only for AIOS-originated work."
        )
    else:
        next_action = "Restore or provide the listed scoped evidence, then rerun."
    return AuditResult(status, scope, list(evidence), list(gaps), next_action)


def _scoped_path(root: Path, reference: object) -> Optional[Path]:
    if not isinstance(reference, str) or not reference:
        return None
    candidate = (root / reference).resolve()
    try:
        candidate.relative_to(root.resolve())
    except ValueError:
        return None
    return candidate


def _owned_run_path(root: Path, run_id: object, reference: object) -> Optional[Path]:
    if not isinstance(run_id, str) or not run_id:
        return None
    owning_run = (root / "workspace" / "runs" / run_id).resolve()
    candidate = _scoped_path(root, reference)
    if candidate is None:
        return None
    try:
        candidate.relative_to(owning_run)
    except ValueError:
        return None
    return candidate


def _read_json(
    path: Path, label: str, findings: List[str]
) -> Optional[Dict[str, Any]]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        findings.append(f"{label} is not readable JSON: {exc}")
        return None
    if not isinstance(value, dict):
        findings.append(f"{label} must be a JSON object")
        return None
    return value


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _parse_source_trace(text: str) -> Tuple[List[Dict[str, str]], List[str]]:
    findings: List[str] = []
    marker = "## Current design/source trace"
    if marker not in text:
        return [], ["SOURCE_AUDIT lacks the current design/source trace"]
    body = text.split(marker, 1)[1]
    if "\n## " in body:
        body = body.split("\n## ", 1)[0]
    sections = re.split(r"(?m)^### ", body)
    sources: List[Dict[str, str]] = []
    for section in sections[1:]:
        lines = section.strip().splitlines()
        source = {"Source": lines[0].strip()}
        current_field: Optional[str] = None
        for line in lines[1:]:
            match = re.match(r"^- \*\*(.+?):\*\*\s+(.+)$", line)
            if match:
                current_field = match.group(1)
                source[current_field] = match.group(2).strip()
            elif current_field and line.startswith("  "):
                source[current_field] += " " + line.strip()
        missing = [field for field in SOURCE_FIELDS if not source.get(field)]
        if missing:
            findings.append(
                f"source trace {source['Source']} lacks {', '.join(missing)}"
            )
        sources.append(source)
    if len(sources) < 3:
        findings.append("source trace has fewer than three materially different sources")
    roles = {source.get("Role") for source in sources}
    missing_roles = EXPECTED_SOURCE_ROLES - roles
    if missing_roles:
        findings.append(
            "source trace lacks roles: " + ", ".join(sorted(missing_roles))
        )
    return sources, findings


def _repository_audit(
    root: Path, findings: List[str], gaps: List[str]
) -> List[str]:
    evidence: List[str] = []
    for relative_path in REPOSITORY_EVIDENCE:
        if not (root / relative_path).is_file():
            gaps.append(f"required repository evidence is unavailable: {relative_path}")
    if gaps:
        return evidence

    for relative_path in ROUTE_DOCUMENTS:
        text = (root / relative_path).read_text(encoding="utf-8")
        for target in ENGINE_PATH.findall(text):
            if not (root / target).is_file():
                findings.append(
                    f"documented command target is stale or unavailable: {target}"
                )

    contract_text = "\n".join(
        (root / path).read_text(encoding="utf-8")
        for path in ("docs/contract.md", "docs/validation.md")
    ).lower()
    for boundary in (
        "deterministic checks",
        "per-design review",
        "periodic system audit",
    ):
        if boundary not in contract_text:
            findings.append(f"audit lifecycle boundary is undocumented: {boundary}")

    source_text = (root / "docs/SOURCE_AUDIT.md").read_text(encoding="utf-8")
    design_text = (root / "workspace/DESIGN.md").read_text(encoding="utf-8")
    brief_text = (root / "workspace/BRIEF.md").read_text(encoding="utf-8")
    for marker in (
        "This `DESIGN.md` is the canonical",
        "## Portable direction and ownership",
        "**Known limitations:**",
    ):
        if marker not in design_text:
            findings.append(f"active DESIGN.md lacks portable contract marker {marker}")
    for marker in (
        "**Receiving outcome:**",
        "**Source/reference rights, provenance, and licensing:**",
        "**Ownership boundary:**",
        "**Review and acceptance owner:**",
    ):
        if marker not in brief_text:
            findings.append(f"active BRIEF.md lacks capability boundary {marker}")
    sources, source_findings = _parse_source_trace(source_text)
    findings.extend(source_findings)
    for source in sources:
        marker = source.get("DESIGN marker", "").strip("§")
        if marker and marker not in design_text:
            findings.append(
                f"active DESIGN.md does not resolve source trace marker {marker}"
            )

    openpencil_selected = "source:openpencil-optional-adapter" in design_text
    op_source = root / "workspace/openpencil/route-console.op"
    op_export = root / "workspace/openpencil/exports/route-console.png"
    if openpencil_selected:
        for path in (op_source, op_export):
            if not path.is_file():
                gaps.append(
                    "selected OpenPencil evidence is unavailable: "
                    + path.relative_to(root).as_posix()
                )
        if gaps:
            return evidence

    handoff = (root / "workspace/engine/create-handoff.mjs").read_text(
        encoding="utf-8"
    )
    for marker in (
        'status: "not-requested"',
        'status: "fallback"',
        'status: "included"',
        'contract: "ADS-HANDOFF/1"',
        "DESIGN.md",
        "artifactManifest",
        "receivingOutcome",
        "Acceptance state: PENDING",
        "Accepted handoff snapshots are immutable",
        "receivingOwner",
    ):
        if marker not in handoff:
            findings.append(f"handoff route lacks optionality marker {marker}")

    template = (root / "docs/HANDOFF_TEMPLATE.md").read_text(encoding="utf-8")
    for marker in (
        "ADS-HANDOFF/1",
        "Handoff ID:",
        "Receiving outcome:",
        "Included snapshot and integrity",
        "Provenance and licensing",
        "Acceptance state:",
    ):
        if marker not in template:
            findings.append(f"handoff template lacks contract marker {marker}")

    public_contract = "\n".join(
        (root / path).read_text(encoding="utf-8")
        for path in ("AGENTS.md", "README.md", "docs/contract.md")
    )
    for marker in (
        "ADS owns visual direction",
        "ACS owns editorial/content production",
        "Either ADS",
        "never auto-run",
        "ADS-to-ACS",
    ):
        if marker not in public_contract:
            findings.append(f"public capability boundary lacks {marker}")

    if openpencil_selected and (
        op_source.suffix != ".op" or op_export.suffix not in {".png", ".svg"}
    ):
        findings.append("OpenPencil source/export boundary uses unexpected file types")

    if not findings:
        evidence.extend(
            [
                "deterministic checks, per-design Review, and periodic audit are distinct",
                f"source decision resolves {len(sources)} source roles into workspace/DESIGN.md",
                "DESIGN.md is canonical and the versioned cross-owner handoff is discoverable",
                "minimal handoff and explicit optional-companion/OpenPencil routes are discoverable",
                "ADS/ACS ownership and suggestion-only sibling routing are explicit",
            ]
        )
        if openpencil_selected:
            evidence.extend(
                [
                    f"OpenPencil source SHA-256 {_sha256(op_source)}",
                    f"reviewed OpenPencil export SHA-256 {_sha256(op_export)}",
                ]
            )
        else:
            evidence.append(
                "OpenPencil is not selected; the minimal portable handoff remains sufficient"
            )
    return evidence


def _workspace_audit(
    root: Path, findings: List[str], gaps: List[str]
) -> List[str]:
    evidence: List[str] = []
    history = root / "workspace/history/runs.jsonl"
    runs_root = root / "workspace/runs"
    if not history.is_file():
        gaps.append(
            "required workspace evidence is unavailable: workspace/history/runs.jsonl"
        )
        return evidence
    if not runs_root.is_dir():
        gaps.append("required workspace evidence is unavailable: workspace/runs/")
        return evidence

    records: List[Dict[str, Any]] = []
    for line_number, line in enumerate(
        history.read_text(encoding="utf-8").splitlines(), start=1
    ):
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError as exc:
            findings.append(f"ledger line {line_number} is invalid JSON: {exc.msg}")
            continue
        if not isinstance(record, dict):
            findings.append(f"ledger line {line_number} is not an object")
            continue
        if set(record) != LEDGER_FIELDS:
            findings.append(f"ledger line {line_number} contradicts the ADS ledger contract")
        records.append(record)
    if not records:
        gaps.append("required accumulated run evidence is unavailable")
        return evidence

    by_id: Dict[object, Dict[str, Any]] = {}
    failed: List[Dict[str, Any]] = []
    recovered: List[Dict[str, Any]] = []
    for record in records:
        run_id = record.get("run_id")
        if not isinstance(run_id, str) or not run_id:
            findings.append("ledger record lacks a valid run_id")
            continue
        if run_id in by_id:
            findings.append(f"ledger repeats run_id {run_id}")
        previous = record.get("previous_run_id")
        relation = record.get("previous_run_relation")
        if previous is None and relation is not None:
            findings.append(f"{run_id} has a relation without a predecessor")
        if previous is not None and previous not in by_id:
            findings.append(f"{run_id} points to a later or unavailable predecessor")
        if previous is not None and relation not in {"predecessor", "recovery"}:
            findings.append(f"{run_id} has an invalid predecessor relation")

        for field in ("output_ref", "proof_ref"):
            reference = _owned_run_path(root, run_id, record.get(field))
            if reference is None:
                findings.append(f"{run_id} has an escaping or invalid {field}")
            elif not reference.is_file():
                gaps.append(f"required {field} is unavailable for {run_id}")

        if record.get("status") == "failed":
            failed.append(record)
            failure = record.get("failure")
            failure_ref = failure.get("ref") if isinstance(failure, dict) else None
            failure_path = _owned_run_path(root, run_id, failure_ref)
            if failure_path is None:
                findings.append(f"{run_id} has invalid failure evidence")
            elif not failure_path.is_file():
                gaps.append(f"required failure evidence is unavailable for {run_id}")
            else:
                value = _read_json(
                    failure_path, f"failure evidence for {run_id}", findings
                )
                if value and (
                    value.get("run_id") != run_id or not value.get("code")
                ):
                    findings.append(f"failure evidence for {run_id} is contradictory")

        recovery = record.get("recovery")
        if isinstance(recovery, dict):
            recovered.append(record)
            recovery_path = _owned_run_path(root, run_id, recovery.get("ref"))
            failed_id = recovery.get("from_run_id")
            if (
                relation != "recovery"
                or previous != failed_id
                or failed_id not in by_id
                or by_id[failed_id].get("status") != "failed"
            ):
                findings.append(f"recovery {run_id} contradicts its failed predecessor")
            if recovery_path is None:
                findings.append(f"{run_id} has invalid recovery evidence")
            elif not recovery_path.is_file():
                gaps.append(f"required recovery evidence is unavailable for {run_id}")
            else:
                value = _read_json(
                    recovery_path, f"recovery evidence for {run_id}", findings
                )
                if value and (
                    value.get("run_id") != run_id
                    or value.get("from_run_id") != failed_id
                    or value.get("status") != "recovered"
                ):
                    findings.append(f"recovery evidence for {run_id} is contradictory")
        by_id[run_id] = record

    if not failed:
        gaps.append("retained failed work is unavailable")
    if not recovered:
        gaps.append("discoverable recovered work is unavailable")

    curated = 0
    for proof_path in sorted((root / "examples").glob("*/proof.json")):
        proof = _read_json(proof_path, str(proof_path.relative_to(root)), findings)
        if not proof or not proof.get("source_run_id"):
            continue
        source = by_id.get(proof["source_run_id"])
        if source is None:
            if RUN_ID_PATTERN.fullmatch(str(proof["source_run_id"])):
                findings.append(
                    f"curated proof {proof_path.relative_to(root)} cites an unavailable run"
                )
            continue
        elif source.get("status") != "succeeded" or proof.get("review") != "PASS":
            findings.append(
                f"curated proof {proof_path.relative_to(root)} contradicts its source run"
            )
        else:
            curated += 1
    if not curated:
        gaps.append("curated proof linked to accumulated run evidence is unavailable")

    active_path = root / "workspace/state/active.json"
    if not active_path.is_file():
        gaps.append("required active-state evidence is unavailable")
    else:
        active = _read_json(active_path, "active state", findings)
        if active and active.get("latest_run_id") != records[-1].get("run_id"):
            findings.append("active state contradicts the latest ledger record")

    if not findings and not gaps:
        evidence.extend(
            [
                f"ledger has {len(records)} scoped run records",
                f"failed and recovered work is discoverable ({len(failed)} failed, {len(recovered)} recovered)",
                f"{curated} curated proof item resolves to a successful reviewed run",
            ]
        )
    return evidence


def audit_design_system(root: Path, scope: str) -> AuditResult:
    if scope not in AUDIT_SCOPES:
        raise ValueError(f"scope must be one of: {', '.join(AUDIT_SCOPES)}")
    root = root.resolve()
    findings: List[str] = []
    gaps: List[str] = []
    evidence: List[str] = []
    if scope in {"repository", "both"}:
        evidence.extend(_repository_audit(root, findings, gaps))
    if scope in {"workspace", "both"}:
        evidence.extend(_workspace_audit(root, findings, gaps))
    if gaps:
        return _result("BLOCKED", scope, evidence, gaps)
    if findings:
        return _result("FAIL", scope, findings, [])
    return _result("PASS", scope, evidence, [])


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Read-only ADS System audit.")
    parser.add_argument("--scope", choices=AUDIT_SCOPES, required=True)
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = _parser().parse_args(argv)
    result = audit_design_system(repository_root(), args.scope)
    print(json.dumps(result.as_dict(), sort_keys=True))
    return {"PASS": 0, "FAIL": 1, "BLOCKED": 2}[result.status]


if __name__ == "__main__":
    raise SystemExit(main())
