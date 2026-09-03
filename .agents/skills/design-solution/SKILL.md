---
name: design-solution
description: Internal design method for turning a resolved ADS brief into a canonical portable DESIGN.md and inspectable preview for websites, applications, workspaces, dashboards, reports, slides, or content visuals. Use through the Agentic Design System primary route.
---

# Design solution — internal method

The public route is `$agentic-design-system`. This skill is the focused
authoring method it calls; it does not own the ledger or gallery.

## Establish the job

1. Read the active `BRIEF.md` from `workspace/` or the explicitly selected
   example and preserve resolved facts.
2. Name the intended outcome and receiving owner/reuse scope, audience/job,
   current constraint, primary action or decision, surfaces/form factors, real
   content/data, required states, material brand/content/technical/accessibility/
   legal/delivery constraints, source rights/provenance, proof, named Review
   owner, and separate receiver-acceptance decision.
3. Ask one question only when a missing answer would materially change the
   direction; otherwise state the smallest reasonable assumption.
4. Reduce the interface to the smallest composition that completes that job.
   Keep active work in `workspace/`; only the primary route decides when a
   result becomes a curated example.

## Set the direction

1. When references or an unresolved direction are present, use the primary
   skill's adaptive-reference method. Decompose each caller-owned pointer into
   its role, target surface, hierarchy, composition, typography, color and
   contrast, imagery or material, density and rhythm, motion or interaction,
   positive signals, avoidances, rights, and confidence. Do not copy caller
   bytes into ADS.
2. Choose one visual idea and explain why it fits the job. A `direct` route
   continues immediately; a `discover` route resolves only its one named gap;
   an `explore` route compares two directions by default and stops after one is
   selected.
3. Write `DESIGN.md` in the pinned Google Design.md format. Define semantic
   colors, typography, spacing, shape language, layout, components, states, and
   explicit do/don't rules.
4. Make hierarchy, content density, and responsive collapse deliberate. Use
   optical rhythm rather than uniform cards and spacing everywhere.
5. Use real draft copy and believable non-sensitive data. Write one clear CTA
   for a landing page and decision-first labels for dashboards.
6. Represent hover, active, visible focus, loading, empty, error, success, and
   permission/offline states when the brief makes them relevant.
7. Use optional references such as awesome-design-md to study variety, never to
   copy a brand or make it the default.
8. Keep the ownership boundary explicit. ADS owns visual direction,
   brand/style/voice expression, composition, motion direction, and selected
   reusable visual assets. A receiving Project owns implementation after
   acceptance; ACS owns editorial/content production, edit/render execution,
   packaging, and publication. If a missing sibling decision materially blocks
   design, return a bounded route suggestion to the caller; never run ACS or
   invent its content.

## Make it inspectable

1. Build semantic, responsive `index.html` using only local assets.
2. Include a skip link, useful landmarks, labels, keyboard-visible focus, and
   reduced-motion behavior where motion exists. Place actionable error text by
   its control or group and associate it programmatically.
3. Keep the preview faithful to `DESIGN.md`; do not hide missing behavior behind
   decorative screenshots.
4. Inspect desktop and mobile widths, then run `npm run check`.

## Hand off

After `review-design` passes, run
`npm run handoff -- <directory> <output> --receiving-owner <owner>`. Confirm the
output contains canonical `DESIGN.md`, `BRIEF.md`, copied `REVIEW.md` or
`proof.json`, and versioned `HANDOFF.md`. Add preview, individual assets, or
CSS/design-token/Tailwind exports only through explicit selections for that
outcome. Pre-existing selected previews/assets/native files need exact Review
path/hash evidence. Deterministic CSS/design-token/Tailwind outputs are instead
generated from the reviewed `DESIGN.md` and bound to its hash in the binder.
Confirm its receiving outcome, all included hashes,
provenance/licensing, review, limitations, and pending or explicit receiver
acceptance. No export tooling is required when exports are unselected. Only an
explicitly selected OpenPencil route adds a reviewed `.op` source and PNG/SVG
exports; follow the primary skill's binding rather than duplicating upstream
instructions here.
The receiving owner becomes canonical for its accepted implementation or
production copy; `DESIGN.md` remains the handed-off visual source of truth and
this repository remains a design workbench, not a runtime dependency.
The brief-selected mode and named Review owner gate generation: in both modes
the evidence reviewer must match that declared Review owner, never the CLI
receiver. A matching independent PASS is sufficient for `independent`, while
`owner` returns `waiting-owner` until the exact Review owner records the bound
PASS. Receiver acceptance remains separate. The receiver copies an accepted
snapshot; it never live-syncs this workspace or recursively invokes ADS.
