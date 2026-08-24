---
name: design-solution
description: Internal design method for turning a resolved ADS brief into a focused DESIGN.md and inspectable browser preview. Use through the Agentic Design System primary route when a landing page, application interface, workspace, dashboard, or report needs visual direction.
---

# Design solution — internal method

The public route is `$agentic-design-system`. This skill is the focused
authoring method it calls; it does not own the ledger or gallery.

## Establish the job

1. Read the active `BRIEF.md` from `workspace/` or the explicitly selected
   example and preserve resolved facts.
2. Name the audience, current constraint, one primary action or decision, real
   content/data, required states, constraints, proof, and receiving project or
   repository.
3. Ask one question only when a missing answer would materially change the
   direction; otherwise state the smallest reasonable assumption.
4. Reduce the interface to the smallest composition that completes that job.
   Keep active work in `workspace/`; only the primary route decides when a
   result becomes a curated example.

## Set the direction

1. Choose one visual idea and explain why it fits the job.
2. Write `DESIGN.md` in the pinned Google Design.md format. Define semantic
   colors, typography, spacing, shape language, layout, components, states, and
   explicit do/don't rules.
3. Make hierarchy, content density, and responsive collapse deliberate. Use
   optical rhythm rather than uniform cards and spacing everywhere.
4. Use real draft copy and believable non-sensitive data. Write one clear CTA
   for a landing page and decision-first labels for dashboards.
5. Represent hover, active, visible focus, loading, empty, error, success, and
   permission/offline states when the brief makes them relevant.
6. Use optional references such as awesome-design-md to study variety, never to
   copy a brand or make it the default.

## Make it inspectable

1. Build semantic, responsive `index.html` using only local assets.
2. Include a skip link, useful landmarks, labels, keyboard-visible focus, and
   reduced-motion behavior where motion exists.
3. Keep the preview faithful to `DESIGN.md`; do not hide missing behavior behind
   decorative screenshots.
4. Inspect desktop and mobile widths, then run `npm run check`.

## Hand off

After `review-design` passes, run `npm run handoff -- <directory>`. Confirm the
output contains `DESIGN.md`, preview/assets, `theme.css`, `tokens.json`,
`tailwind.theme.json`, and `HANDOFF.md`. The receiving project or repository
becomes the canonical owner; this repository remains a design workbench, not a
dependency.
