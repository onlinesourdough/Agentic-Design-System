from __future__ import annotations

import importlib.util
import shutil
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
ENGINE = ROOT / "workspace/engine"
sys.path.insert(0, str(ENGINE))

AUDIT_SPEC = importlib.util.spec_from_file_location(
    "ads_audit", ENGINE / "audit_design_system.py"
)
if AUDIT_SPEC is None or AUDIT_SPEC.loader is None:
    raise ImportError("cannot load ADS audit")
audit = importlib.util.module_from_spec(AUDIT_SPEC)
sys.modules["ads_audit"] = audit
AUDIT_SPEC.loader.exec_module(audit)

TRACE_SPEC = importlib.util.spec_from_file_location(
    "ads_audit_tracer", ENGINE / "audit_tracer.py"
)
if TRACE_SPEC is None or TRACE_SPEC.loader is None:
    raise ImportError("cannot load ADS audit tracer")
audit_tracer = importlib.util.module_from_spec(TRACE_SPEC)
sys.modules["ads_audit_tracer"] = audit_tracer
TRACE_SPEC.loader.exec_module(audit_tracer)


class AuditTests(unittest.TestCase):
    def test_repository_scope_is_healthy_and_read_only(self):
        before = audit_tracer._fingerprint(ROOT)
        result = audit.audit_design_system(ROOT, "repository")
        after = audit_tracer._fingerprint(ROOT)
        self.assertEqual(result.status, "PASS", result.as_dict())
        self.assertEqual(before, after)

    def test_isolated_pass_fail_blocked_and_recovery_cases(self):
        results = audit_tracer.trace_cases(ROOT)
        self.assertEqual(results["healthy"]["status"], "PASS")
        self.assertEqual(results["stale"]["status"], "FAIL")
        self.assertEqual(results["contradictory"]["status"], "FAIL")
        self.assertEqual(results["missing_evidence"]["status"], "BLOCKED")
        self.assertTrue(results["read_only"])
        self.assertTrue(
            any(
                "failed and recovered work is discoverable" in item
                for item in results["healthy"]["evidence"]
            )
        )

    def test_valid_first_design_does_not_hide_malformed_second_ledger(self):
        with tempfile.TemporaryDirectory() as temporary:
            copied_root = Path(temporary) / "checkout"
            shutil.copytree(ROOT, copied_root, ignore=audit_tracer._ignore)
            broken = copied_root / "workspace/designs/zz-malformed-ledger"
            shutil.copytree(
                copied_root / "workspace/designs/ads-business-freedom-content-e2e-r1",
                broken,
            )
            (broken / "history/runs.jsonl").write_text(
                "not a JSON ledger record\n", encoding="utf-8"
            )

            result = audit.audit_design_system(copied_root, "workspace")

            self.assertEqual(result.status, "FAIL", result.as_dict())
            self.assertTrue(
                any(
                    "zz-malformed-ledger ledger line 1 is invalid JSON" in finding
                    for finding in result.evidence
                ),
                result.as_dict(),
            )


if __name__ == "__main__":
    unittest.main()
