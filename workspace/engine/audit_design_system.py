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
    "workspace/designs/index.html",
    "workspace/designs/ads-business-freedom-content-e2e-r1/BRIEF.md",
    "workspace/designs/ads-business-freedom-content-e2e-r1/DESIGN.md",
    "workspace/designs/ads-business-freedom-content-e2e-r1/REVIEW.md",
    "workspace/designs/ads-business-freedom-content-e2e-r1/index.html",
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


def _owned_run_path(design: Path, root: Path, run_id: object, reference: object) -> Optional[Path]:
    if not isinstance(run_id, str) or not run_id:
        return None
    owning_run = (design / "runs" / run_id).resolve()
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
    selected = root / "workspace/designs/ads-business-freedom-content-e2e-r1"
    design_text = (selected / "DESIGN.md").read_text(encoding="utf-8")
    brief_text = (selected / "BRIEF.md").read_text(encoding="utf-8")
    for marker in (
        "This `DESIGN.md` is the canonical",
        "## Portable direction and ownership",
        "**Known limitations:**",
    ):
        if marker not in design_text:
            findings.append(f"active DESIGN.md lacks portable contract marker {marker}")
    brief_markers = (
        "**Receiving outcome:**",
        "**Source/reference rights, provenance, and licensing:**",
        "**Ownership boundary:**",
    )
    if "**Review and acceptance owner:**" not in brief_text:
        brief_markers += (
            "**Review mode:**",
            "**Review owner:**",
            "**Receiver acceptance:**",
        )
    for marker in brief_markers:
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
    op_source = selected / "openpencil/route-console.op"
    op_export = selected / "openpencil/exports/route-console.png"
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
                f"source decision resolves {len(sources)} source roles into selected DESIGN.md",
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


def _legacy_owned_run_path(
    design: Path, root: Path, run_id: object, reference: object
) -> Optional[Path]:
    """Resolve a preserved pre-collection workspace/runs reference locally."""

    if not isinstance(run_id, str) or not isinstance(reference, str):
        return None
    prefix = f"workspace/runs/{run_id}/"
    if not reference.startswith(prefix):
        return None
    candidate = (design / "runs" / run_id / reference[len(prefix) :]).resolve()
    try:
        candidate.relative_to((design / "runs" / run_id).resolve())
        candidate.relative_to(root.resolve())
    except ValueError:
        return None
    return candidate


def _run_reference(
    design: Path,
    root: Path,
    run_id: object,
    reference: object,
    *,
    legacy: bool,
) -> Optional[Path]:
    current = _owned_run_path(design, root, run_id, reference)
    if current is not None:
        return current
    if legacy:
        return _legacy_owned_run_path(design, root, run_id, reference)
    return None


def _audit_design_ledger(
    root: Path, design: Path, findings: List[str], gaps: List[str], *, legacy: bool
) -> List[str]:
    evidence: List[str] = []
    label = design.relative_to(root).as_posix()
    history = design / "history/runs.jsonl"
    runs_root = design / "runs"
    if not history.is_file():
        gaps.append(
            f"{label} required ledger is unavailable: history/runs.jsonl"
        )
        return evidence
    if not runs_root.is_dir():
        gaps.append(f"{label} required run root is unavailable: runs/")
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
            findings.append(f"{label} ledger line {line_number} is invalid JSON: {exc.msg}")
            continue
        if not isinstance(record, dict):
            findings.append(f"{label} ledger line {line_number} is not an object")
            continue
        if set(record) != LEDGER_FIELDS:
            findings.append(
                f"{label} ledger line {line_number} contradicts the ADS ledger contract"
            )
        records.append(record)
    if not records:
        if not findings:
            gaps.append(f"{label} required accumulated run evidence is unavailable")
        return evidence

    by_id: Dict[object, Dict[str, Any]] = {}
    failed: List[Dict[str, Any]] = []
    recovered: List[Dict[str, Any]] = []
    for record in records:
        run_id = record.get("run_id")
        if not isinstance(run_id, str) or not run_id:
            findings.append(f"{label} ledger record lacks a valid run_id")
            continue
        if run_id in by_id:
            findings.append(f"{label} ledger repeats run_id {run_id}")
        previous = record.get("previous_run_id")
        relation = record.get("previous_run_relation")
        if previous is None and relation is not None:
            findings.append(f"{label} {run_id} has a relation without a predecessor")
        if previous is not None and previous not in by_id:
            findings.append(f"{label} {run_id} points to a later or unavailable predecessor")
        if previous is not None and relation not in {"predecessor", "recovery"}:
            findings.append(f"{label} {run_id} has an invalid predecessor relation")

        for field in ("output_ref", "proof_ref"):
            reference = _run_reference(
                design, root, run_id, record.get(field), legacy=legacy
            )
            if reference is None:
                findings.append(f"{label} {run_id} has an escaping or invalid {field}")
            elif not reference.is_file():
                gaps.append(f"{label} required {field} is unavailable for {run_id}")

        if record.get("status") == "failed":
            failed.append(record)
            failure = record.get("failure")
            failure_ref = failure.get("ref") if isinstance(failure, dict) else None
            failure_path = _run_reference(
                design, root, run_id, failure_ref, legacy=legacy
            )
            if failure_path is None:
                findings.append(f"{label} {run_id} has invalid failure evidence")
            elif not failure_path.is_file():
                gaps.append(f"{label} required failure evidence is unavailable for {run_id}")
            else:
                value = _read_json(
                    failure_path, f"failure evidence for {run_id}", findings
                )
                if value and (
                    value.get("run_id") != run_id or not value.get("code")
                ):
                    findings.append(f"{label} failure evidence for {run_id} is contradictory")

        recovery = record.get("recovery")
        if isinstance(recovery, dict):
            recovered.append(record)
            recovery_path = _run_reference(
                design, root, run_id, recovery.get("ref"), legacy=legacy
            )
            failed_id = recovery.get("from_run_id")
            if (
                relation != "recovery"
                or previous != failed_id
                or failed_id not in by_id
                or by_id[failed_id].get("status") != "failed"
            ):
                findings.append(
                    f"{label} recovery {run_id} contradicts its failed predecessor"
                )
            if recovery_path is None:
                findings.append(f"{label} {run_id} has invalid recovery evidence")
            elif not recovery_path.is_file():
                gaps.append(f"{label} required recovery evidence is unavailable for {run_id}")
            else:
                value = _read_json(
                    recovery_path, f"recovery evidence for {run_id}", findings
                )
                if value and (
                    value.get("run_id") != run_id
                    or value.get("from_run_id") != failed_id
                    or value.get("status") != "recovered"
                ):
                    findings.append(f"{label} recovery evidence for {run_id} is contradictory")
        by_id[run_id] = record

    if not legacy:
        if not failed:
            gaps.append(f"{label} retained failed work is unavailable")
        if not recovered:
            gaps.append(f"{label} discoverable recovered work is unavailable")

    curated = 0
    for proof_path in sorted(design.glob("proof.json")):
        proof = _read_json(proof_path, str(proof_path.relative_to(root)), findings)
        if not proof or not proof.get("source_run_id"):
            continue
        source = by_id.get(proof["source_run_id"])
        if source is None:
            if RUN_ID_PATTERN.fullmatch(str(proof["source_run_id"])):
                findings.append(f"curated proof {proof_path.relative_to(root)} cites an unavailable run")
            continue
        elif source.get("status") != "succeeded" or proof.get("review") != "PASS":
            findings.append(
                f"curated proof {proof_path.relative_to(root)} contradicts its source run"
            )
        else:
            curated += 1
    if not legacy and not curated:
        gaps.append("curated proof linked to accumulated run evidence is unavailable")

    active_path = design / "state/active.json"
    if not legacy and not active_path.is_file():
        gaps.append("required active-state evidence is unavailable")
    elif not legacy:
        active = _read_json(active_path, "active state", findings)
        if active and active.get("latest_run_id") != records[-1].get("run_id"):
            findings.append("active state contradicts the latest ledger record")

    if not findings and not gaps:
        if legacy:
            evidence.extend(
                [
                    f"{label} preserved legacy ledger has {len(records)} scoped run records",
                    f"{label} retains provenance without requiring newly manufactured failure or recovery evidence",
                ]
            )
        else:
            evidence.extend(
                [
                    f"{label} managed ledger has {len(records)} scoped run records",
                    f"{label} failed and recovered work is discoverable ({len(failed)} failed, {len(recovered)} recovered)",
                    f"{label} has {curated} curated proof item(s) resolving to a successful reviewed run",
                ]
            )
    return evidence


def _workspace_audit(
    root: Path, findings: List[str], gaps: List[str]
) -> List[str]:
    evidence: List[str] = []
    collection = root / "workspace/designs"
    if not collection.is_dir():
        gaps.append("workspace design collection is unavailable")
        return evidence

    ledger_designs = 0
    legacy_snapshots = 0
    for design in sorted(path for path in collection.iterdir() if path.is_dir()):
        if not (design / "BRIEF.md").is_file() or not (design / "DESIGN.md").is_file():
            continue
        ledger = design / "history/runs.jsonl"
        if ledger.is_file():
            legacy = (design / "history/MIGRATION.json").is_file() or any(
                line.startswith('{"run_id"') and "workspace/runs/" in line
                for line in ledger.read_text(encoding="utf-8").splitlines()
            )
            evidence.extend(
                _audit_design_ledger(root, design, findings, gaps, legacy=legacy)
            )
            ledger_designs += 1
        elif (design / "history").is_dir():
            gaps.append(
                f"{design.relative_to(root)} has history without history/runs.jsonl"
            )
        elif (design / "proof.json").is_file():
            proof = _read_json(
                design / "proof.json",
                f"legacy curated proof {design.relative_to(root)}",
                findings,
            )
            if proof and proof.get("review") == "PASS" and proof.get("status") == "succeeded":
                legacy_snapshots += 1
            elif proof:
                findings.append(
                    f"legacy curated proof {design.relative_to(root)} lacks PASS succeeded provenance"
                )

    if not ledger_designs:
        gaps.append("workspace has no managed or preserved design ledger to audit")
    if not findings and not gaps:
        evidence.append(
            f"workspace audit inspected {ledger_designs} design ledger(s) and {legacy_snapshots} legacy curated snapshot(s)"
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
