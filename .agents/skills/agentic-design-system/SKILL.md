---
name: agentic-design-system
description: Create, review, or hand off one explicitly selected portable visual direction in ADS. DESIGN.md remains canonical; optional previews, assets, and OpenPencil sources stay design-local companions.
---

# Agentic Design System

Use this public ADS route for a resolved visual-direction request across websites, applications, dashboards, reports, slides, or content surfaces. It does not implement the receiving project or produce/publish ACS content.

## Required-read footprint

Read only the selected design and the route-specific method; do not preload other designs, historical handoffs, or source collections.

| Need                | Required read                                                          | Typical size        |
| ------------------- | ---------------------------------------------------------------------- | ------------------- |
| Resume or create    | `workspace/designs/<slug>/history/runs.jsonl`, `BRIEF.md`, `DESIGN.md` | small, design-local |
| Preview/review      | selected `index.html`, `REVIEW.md` if present                          | selected only       |
| Cross-owner handoff | selected `BRIEF.md`, `DESIGN.md`, review evidence, selected companions | selected only       |
| OpenPencil          | `$openpencil-workbench` and the selected `.op`/export                  | selected only       |

“Typical size” is a bounded reading scope, not a measured token-saving claim. Read `docs/SOURCE_AUDIT.md` only when the brief selects or changes a source decision, and `docs/validation.md` only when executing the relevant proof.

## Route

1. Require one valid `workspace/designs/<slug>/` selection. Never overwrite, merge, or infer another direction. A new selected design owns `BRIEF.md`, canonical `DESIGN.md`, `index.html`, and any design-local `runs/`, `state/`, `history/`, `handoffs/`, or optional `openpencil/` companions.
2. Inspect the selected history, brief, and canonical `DESIGN.md`. The brief must make outcome, receiver/reuse scope, audience/job, constraints, rights, exact review mode (`independent` or `owner`), distinct named Review owner, and separate receiver acceptance inspectable.
3. Use `$design-solution` only if authoring or revising the direction/preview is needed. Preserve resolved facts. `DESIGN.md` remains the portable source of visual truth.
4. Preview with `npm run preview -- --design <slug>` and inspect relevant desktop/mobile, focus, reduced-motion, and selected states. Use `$review-design` without editing. Its reviewer must match the brief’s Review owner and bind the current DESIGN SHA-256 plus every selected pre-existing companion hash. Owner mode returns `waiting-owner` until that identity acts.
5. For cross-owner delivery, run `npm run handoff -- --design <slug> --output handoffs/<revision> --receiving-owner <owner>`. It generates the immutable `ADS-HANDOFF/1` binder. Receiver acceptance is a separate `PENDING` decision.
6. Use `$openpencil-workbench` only when the brief deliberately selects an OpenPencil companion. It starts verified v0.8.4 bytes at strict loopback, opens the existing selected document in the Codex-compatible built-in browser, and proves its reviewed export. Do not invent a canvas API, use an OS browser, or claim native editing when the supervised surface is absent. Fresh sessions seed English (`en-US`) before upstream UI initialization. Stop the workbench after proof unless a lead is actively inspecting it.
7. Append one small run record only under the selected design’s history. A recovery is a new run linked to its failed predecessor. Recovered snapshots retain their original provenance and acceptance state; they are not fresh review evidence.

## Boundaries

ADS owns visual direction, hierarchy, brand/style/voice expression, composition, typography, color, imagery, interaction/motion direction, and selected reusable visual assets. Receiving projects own implementation after acceptance. ACS owns editorial/content production, edit/render, packaging, and publication. A material sibling gap yields only a bounded suggestion; never auto-run ACS or create a recursive runtime chain.

The periodic `$audit-design-system` route is read-only and returns exactly `PASS`, `FAIL`, or `BLOCKED`; it never creates a run, export, handoff, or issue.
