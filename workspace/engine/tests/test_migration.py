from __future__ import annotations

import hashlib
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
DESIGN = ROOT / "workspace" / "designs" / "gustav-social-banner-r1"
MIGRATION = DESIGN / "history" / "MIGRATION.json"


class MigrationTests(unittest.TestCase):
    def test_r1_singleton_ledger_and_relocated_artifacts_are_preserved(self):
        migration = json.loads(MIGRATION.read_text(encoding="utf-8"))

        self.assertEqual(migration["schema"], "ADS-DESIGN-MIGRATION-MAP/1")
        historical = migration["historical_ledger"]
        preserved = ROOT / historical["preserved_path"]
        self.assertEqual(
            hashlib.sha256(preserved.read_bytes()).hexdigest(), historical["sha256"]
        )

        for artifact in migration["legacy_path_map"]:
            current = ROOT / artifact["current_path"]
            self.assertTrue(current.is_file(), artifact["current_path"])
            self.assertEqual(
                hashlib.sha256(current.read_bytes()).hexdigest(),
                artifact["sha256"],
                artifact["current_path"],
            )

        records = {
            record["run_id"]: record
            for line in (DESIGN / "history" / "runs.jsonl").read_text(
                encoding="utf-8"
            ).splitlines()
            if line.strip()
            for record in (json.loads(line),)
        }
        for reference in migration["record_refs"]:
            record = records[reference["run_id"]]
            for field, current_path in reference["current"].items():
                self.assertEqual(record[field], current_path)
                self.assertTrue((ROOT / current_path).is_file(), current_path)

        self.assertEqual(
            migration["immutable_paths_not_rewritten"],
            ["workspace/designs/gustav-social-banner-r1/handoffs/gustav-social-banner-r1/"],
        )


if __name__ == "__main__":
    unittest.main()
