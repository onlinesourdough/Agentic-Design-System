---
name: review-design
description: Internal review method for a DESIGN.md and browser preview, covering job fit, originality, realistic content, responsive behavior, accessibility, complete states, and acceptance readiness. Use through the Agentic Design System primary route.
---

# Review design — internal method

The public route is `$agentic-design-system`. This method evaluates without
editing and returns evidence for the System run; it does not own promotion.

Evaluate without editing. Return `PASS` only when every required check passes;
otherwise return `REVISE` with the smallest concrete correction.

## Checks

1. **Job:** The first viewport makes the audience, value, primary action or
   supported decision clear. Each section or panel earns its place.
2. **Specificity:** Claims, labels, names, numbers, and examples are believable
   and traceable to the brief or clearly fictional. There is no lorem ipsum,
   placeholder company, fake proof, or vague promise.
3. **Voice:** Copy says the point directly and sounds particular to this case.
   Flag portable filler, throat-clearing, faux insight, repetitive binary
   contrasts, empty superlatives, and polished text that erased useful voice.
4. **Composition:** Hierarchy, density, whitespace, alignment, typography,
   color, and surfaces support the job. Flag default three-card grids,
   indiscriminate pills, purple AI gradients, needless sidebars, excessive
   symmetry, and decoration that substitutes for a product visual.
5. **States:** Relevant hover, active, focus, loading, empty, error, success,
   permission, and offline states are explicit and useful.
6. **Accessibility:** Semantic landmarks, heading order, labels, contrast,
   keyboard-visible focus, skip navigation, alt text, and reduced motion are
   appropriate. Mobile does not lose content or action access.
7. **Originality and source safety:** References informed principles rather
   than reproducing a third-party brand, layout, proprietary asset, or long
   skill passage.
8. **Contract:** `BRIEF.md`, `DESIGN.md`, and preview agree; Design.md lint and
   repository checks pass; the handoff names the receiving project or
   repository and contains every promised file.
9. **Optional native source:** When OpenPencil was explicitly selected, use a
   real supervised upstream surface to open the `.op` source and export the
   declared PNG/SVG boundary. Compare that export with `DESIGN.md`; verify the
   source audit, paths, hashes, provenance, upstream version/revision, review,
   limitations, and receiving owner in `HANDOFF.md`. When it was not
   selected or is unavailable, verify the visible ordinary-handoff fallback;
   absence of `.op` is not itself a failure.

Return:

```text
Review: design
Result: PASS | REVISE
Checks: [job, specificity, voice, composition, states, accessibility, source safety, contract, optional native source]
Next: create handoff | revise
Findings: [only material failures]
```
