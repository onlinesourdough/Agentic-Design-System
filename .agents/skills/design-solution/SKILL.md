---
name: design-solution
description: Author canonical portable DESIGN.md and selected visual companions from a resolved ADS brief. Use through the Agentic Design System primary route.
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

Direction-only work is inspectable through `DESIGN.md`; no HTML or render
tooling is required unless the adaptive route needs rendered-task proof for
new source adoption. Build companions only when selected for the outcome.
For an HTML preview:

1. Build semantic `index.html` using only local assets, responsive when relevant.
2. Include a skip link, useful landmarks, labels, keyboard-visible focus, and
   reduced-motion behavior where motion exists. Place actionable error text by
   its control or group and associate it programmatically.
3. Keep the preview faithful to `DESIGN.md`; do not hide missing behavior behind
   decorative screenshots.
4. Inspect the selected surface's relevant viewports (desktop and mobile for
   responsive work), then run applicable repository checks.

## Hand off

Return the direction and selected companion paths to the primary route for
`review-design`, evidence, and any cross-owner generation. Apply
[the canonical handoff contract](../../../docs/contract.md#cross-owner-and-optional-native-handoff)
when ownership crosses; [the validation recipe](../../../docs/validation.md#handoff)
provides command syntax. Same-owner work needs no binder. The primary route
coordinates review-mode gates and immutable snapshot delivery; the receiver
owns its separate acceptance decision.
