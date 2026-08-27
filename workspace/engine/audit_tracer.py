#!/usr/bin/env python3
"""Isolated proof cases for the read-only ADS audit route."""

from __future__ import annotations

import hashlib
import json
import re
import shutil
import tempfile
from pathlib import Path
from typing import Dict

import audit_design_system as audit
import tracer


def repository_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _ignore(_directory: str, names: list[str]) -> set[str]:
    ignored = {
        name for name in names if name in {".git", "node_modules", "__pycache__"}
    }
    if "handoff" in names:
        ignored.add("handoff")
    return ignored


def _fingerprint(root: Path) -> str:
    digest = hashlib.sha256()
    for path in sorted(item for item in root.rglob("*") if item.is_file()):
        digest.update(path.relative_to(root).as_posix().encode("utf-8"))
        digest.update(path.read_bytes())
    return digest.hexdigest()


def _prepare_seed(source: Path, destination: Path) -> None:
    shutil.copytree(source, destination, ignore=_ignore)
    transient_slugs = []
    for proof_path in sorted((destination / "examples").glob("*/proof.json")):
        proof = json.loads(proof_path.read_text(encoding="utf-8"))
        if re.fullmatch(r"run-\d{4,}", str(proof.get("source_run_id", ""))):
            transient_slugs.append(proof_path.parent.name)
            shutil.rmtree(proof_path.parent)
    if transient_slugs:
        gallery_path = destination / "examples/index.html"
        gallery = gallery_path.read_text(encoding="utf-8")
        readme_path = destination / "examples/README.md"
        readme = readme_path.read_text(encoding="utf-8")
        for slug in transient_slugs:
            gallery = re.sub(
                rf'<p data-tracer-example="{re.escape(slug)}">.*?</p>',
                "",
                gallery,
            )
            readme = re.sub(
                rf"\n- \[{re.escape(slug)} proof\]\({re.escape(slug)}/index\.html\)",
                "",
                readme,
            )
        gallery_path.write_text(gallery, encoding="utf-8")
        readme_path.write_text(readme, encoding="utf-8")
    runs = destination / "workspace/runs"
    state = destination / "workspace/state"
    shutil.rmtree(runs)
    shutil.rmtree(state)
    runs.mkdir(parents=True)
    state.mkdir(parents=True)
    (destination / "workspace/history/runs.jsonl").write_text("", encoding="utf-8")
    tracer.trace_once(destination, slug="audit-proof", simulate_failure=True)
    tracer.trace_once(
        destination,
        slug="audit-proof",
        recover=True,
        preview=True,
        review=True,
        promote_example=True,
    )


def _run_read_only(root: Path, scope: str) -> audit.AuditResult:
    before = _fingerprint(root)
    result = audit.audit_design_system(root, scope)
    after = _fingerprint(root)
    if before != after:
        raise RuntimeError(f"audit mutated its {scope} scope")
    return result


def trace_cases(source: Path) -> Dict[str, object]:
    with tempfile.TemporaryDirectory() as temporary:
        base = Path(temporary)
        healthy = base / "healthy"
        _prepare_seed(source, healthy)
        pass_result = _run_read_only(healthy, "both")

        stale = base / "stale"
        shutil.copytree(healthy, stale)
        with (stale / "README.md").open("a", encoding="utf-8") as stream:
            stream.write(
                "\npython3 workspace/engine/retired-audit-route.py --scope both\n"
            )
        stale_result = _run_read_only(stale, "repository")

        contradictory = base / "contradictory"
        shutil.copytree(healthy, contradictory)
        records = [
            json.loads(line)
            for line in (
                contradictory / "workspace/history/runs.jsonl"
            ).read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
        recovery_path = contradictory / records[-1]["recovery"]["ref"]
        recovery = json.loads(recovery_path.read_text(encoding="utf-8"))
        recovery["from_run_id"] = "run-contradiction"
        recovery_path.write_text(
            json.dumps(recovery, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        contradictory_result = _run_read_only(contradictory, "workspace")

        blocked = base / "blocked"
        shutil.copytree(healthy, blocked)
        first = json.loads(
            (blocked / "workspace/history/runs.jsonl")
            .read_text(encoding="utf-8")
            .splitlines()[0]
        )
        (blocked / first["proof_ref"]).unlink()
        blocked_result = _run_read_only(blocked, "workspace")

        results = {
            "healthy": pass_result.as_dict(),
            "stale": stale_result.as_dict(),
            "contradictory": contradictory_result.as_dict(),
            "missing_evidence": blocked_result.as_dict(),
            "read_only": True,
        }
        expected = {
            "healthy": "PASS",
            "stale": "FAIL",
            "contradictory": "FAIL",
            "missing_evidence": "BLOCKED",
        }
        for name, status in expected.items():
            actual = results[name]["status"]
            if actual != status:
                raise RuntimeError(f"{name} expected {status}, received {actual}")
        return results


def main() -> int:
    print(json.dumps(trace_cases(repository_root()), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
