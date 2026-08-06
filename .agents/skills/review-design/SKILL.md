---
name: review-design
description: Review a DESIGN.md and browser preview for job fit, originality, realistic content, responsive behavior, accessibility, complete states, and handoff readiness. Use after a Design-template direction is built and before it is accepted by or copied into the receiving project or repository.
---

# Review design

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

Return:

```text
Review: design
Result: PASS | REVISE
Checks: [job, specificity, voice, composition, states, accessibility, source safety, contract]
Next: create handoff | revise
Findings: [only material failures]
```
