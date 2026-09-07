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

1. Require one valid `workspace/designs/<slug>/` selection. Never overwrite, merge, or infer another direction. A new selected design owns `BRIEF.md`, canonical `DESIGN.md`, optional `index.html`, and any design-local `runs/`, `state/`, `history/`, `handoffs/`, or optional `openpencil/` companions.
2. Inspect the selected history, brief, and canonical `DESIGN.md`. The brief must make outcome, receiver/reuse scope, audience/job, constraints, rights, exact review mode (`independent` or `owner`), distinct named Review owner, and separate receiver acceptance inspectable. When the caller supplies visual evidence or the direction remains unresolved, read [`references/adaptive-references.md`](references/adaptive-references.md), apply its owner-first precedence, and record exactly one `direct`, `discover`, or `explore` decision as subordinate route evidence.
3. Use `$design-solution` only if authoring or revising the direction/preview is needed. Preserve resolved facts. `DESIGN.md` remains the portable source of visual truth.
4. Preview with `npm run preview -- --design <slug>` only when an HTML surface is selected. Inspect its relevant desktop/mobile, focus, reduced-motion, and selected states. Direction-only work needs no HTML or browser, but cannot substitute for rendered-task proof when new source adoption is selected. Use `$review-design` without editing. Its reviewer must match the brief’s Review owner and bind the current DESIGN SHA-256 plus every selected pre-existing companion hash. Owner mode returns `waiting-owner` until that identity acts.
5. For cross-owner delivery, first read [the canonical handoff contract](../../../docs/contract.md#cross-owner-and-optional-native-handoff) and [binder/evidence format](../../../docs/HANDOFF_TEMPLATE.md), then run `npm run handoff -- --design <slug> --output handoffs/<revision> --receiving-owner <owner>`. They own the exact review, integrity, rights, and acceptance gates; the command generates the immutable `ADS-HANDOFF/1` binder. Receiver acceptance is a separate `PENDING` decision.
6. Use `$openpencil-workbench` only when the brief deliberately selects an OpenPencil companion. It starts verified v0.8.4 bytes at strict loopback, opens the existing selected document in the Codex-compatible built-in browser, and proves that the actual editable `.op` document is visible through the supervised surface. A printed URL or chat-rendered PNG/SVG alone is not live-surface proof. Do not invent a canvas API, use an OS browser, or claim native editing when the supervised surface is absent. Fresh sessions seed English (`en-US`) before upstream UI initialization. Keep the workbench running, with its machine-readable URL, when the selected outcome is `waiting-review`; cleanup is a later explicit `stop`; otherwise stop it after proof.
7. Append one small run record only under the selected design’s history. A recovery is a new run linked to its failed predecessor. Recovered snapshots retain their original provenance and acceptance state; they are not fresh review evidence.

## Boundaries

ADS owns visual direction, hierarchy, brand/style/voice expression, composition, typography, color, imagery, interaction/motion direction, and selected reusable visual assets. Receiving projects own implementation after acceptance. ACS owns editorial/content production, edit/render, packaging, and publication. A material sibling gap yields only a bounded suggestion; never auto-run ACS or create a recursive runtime chain.

The periodic `$audit-design-system` route is read-only and returns exactly `PASS`, `FAIL`, or `BLOCKED`; it never creates a run, export, handoff, or issue.
