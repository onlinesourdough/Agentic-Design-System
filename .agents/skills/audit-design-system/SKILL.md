---
name: audit-design-system
description: Audit accumulated ADS design and handoff evidence in an explicit repository or workspace scope without mutation.
metadata:
  version: "1.0.0"
---

# Audit Agentic Design System

Use this periodic accumulated-state route through the primary
agentic-design-system skill. It is separate from deterministic repository
checks (which test known invariants) and review-design (which judges one
design and handoff). The audit reads whether current ADS truth and accumulated
proof still agree.

The repository scope also checks that `DESIGN.md` remains canonical across
active and curated work; cross-owner handoffs expose identity/revision,
receiver/outcome, hashes, provenance/licensing, review, limitations, and
acceptance; and sibling boundaries remain suggestion-only with no automatic
ADS-to-ACS chain.

The aggregate `workspace` scope examines every valid design-local ledger in
`workspace/designs/`; it never selects an `audit-proof` fixture or an
alphabetically first design. Historical curated snapshots and preserved legacy
ledgers are checked for their own provenance without requiring them to invent
new failure/recovery records.

1. Select exactly one scope: repository, workspace, or both.
2. Run python3 workspace/engine/audit_design_system.py --scope <scope>.
3. Return exactly the reported PASS, FAIL, or BLOCKED, with scope, evidence,
   gaps, and the smallest next action. Missing required evidence is BLOCKED,
   never an assumed pass.
4. Route findings to ADS Build/Review. Use AIOS improvement triage only when
   the audited work originated in AIOS.

The route starts and remains read-only. It never repairs, exports, promotes,
creates an issue or run, appends the ledger, or calls an external System.
OpenPencil is checked only when explicitly selected evidence exists; minimal
portable handoffs remain valid without it, preview, assets, token/theme
exports, or companion tooling.
