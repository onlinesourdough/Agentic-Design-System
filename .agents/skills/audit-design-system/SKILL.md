---
name: audit-design-system
description: Read-only ADS-local route for checking accumulated portable-design, handoff, ownership-boundary, and evidence drift in an explicit scope.
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
