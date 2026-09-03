---
name: review-design
description: Internal review method for a canonical portable DESIGN.md, selected companions, preview, ownership boundary, and cross-owner acceptance readiness. Use through the Agentic Design System primary route.
---

# Review design — internal method

The public route is `$agentic-design-system`. This method evaluates without
editing and returns evidence for the System run; it does not own promotion.

Evaluate without editing. Return `PASS` only when every required check passes;
otherwise return `REVISE` with the smallest concrete correction.
Apply viewport, interaction, and rendered-accessibility checks to a preview only
when one is selected. For a direction-only review, evaluate the corresponding
instructions in `DESIGN.md` and record receiving-surface validation as a
limitation rather than inventing preview proof.

The brief selects review mode as `independent` or `owner` and declares one
non-empty `Review owner` separately from the receiving project. Name the
reviewer and require that identity to match the declared Review owner in either
mode. Bind the exact reviewed `DESIGN.md` SHA-256. List each pre-existing
selected preview, asset, editable source, and native export as a `Reviewed
source companion` with its SHA-256; unlisted source companions cannot enter
that handoff revision. CSS, design-token, and Tailwind outputs are deterministic
derivatives of that reviewed `DESIGN.md`: the generator hashes and binds them
to the DESIGN hash, so Review must not pretend they existed beforehand. When
owner mode is selected, return `waiting-owner` until the exact declared Review
owner records the complete bound PASS. Independent mode needs no second review;
receiver acceptance remains a separate post-generation decision.

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
   appropriate. Error feedback is adjacent to its control or group and
   programmatically associated. Mobile does not lose content or action access.
7. **Originality and source safety:** References informed principles rather
   than reproducing a third-party brand, layout, proprietary asset, or long
   skill passage. Caller media remains an owned pointer with provenance,
   rights, revision/hash when available, signals, role, confidence, and target
   surface. The selected `direct`, `discover`, or `explore` evidence respects
   owner-first precedence; discovery evaluates only one concrete gap and
   selects at most one primary source plus one optional adapter. The ADS
   baseline is original fallback vocabulary, never a template or brand.
8. **Contract:** `BRIEF.md` and canonical portable `DESIGN.md` agree; any
   selected preview, asset, export, or tool source agrees with both. Design.md
   lint and applicable repository checks pass. Optional companions do not
   replace `DESIGN.md`. Cross-owner `HANDOFF.md` records
   `ADS-HANDOFF/1`, identity/revision, receiving owner/outcome, source revision,
   all included paths/hashes, provenance/licensing, Review, limitations, and an
   explicit acceptance state; accepted snapshots cannot be overwritten. The
   named Review owner/reviewer, brief-selected mode, reviewed DESIGN hash, and
   selected source-companion hashes agree with the generated binder. Any
   deterministic derived exports expose their own integrity hashes plus the
   reviewed DESIGN hash from which they were generated.
9. **Optional native source:** When OpenPencil was explicitly selected, use a
   real supervised upstream surface to open the `.op` source and export the
   declared PNG/SVG boundary. Compare that export with `DESIGN.md`; verify the
   source audit, paths, hashes, provenance, upstream version/revision, review,
   limitations, and receiving owner in `HANDOFF.md`. When it was not selected
   or is unavailable, verify that the required portable handoff plus only any
   independently selected companions remains valid; absence of `.op` is not
   itself a failure.
10. **Ownership and sibling route:** ADS decisions stay visual and expressive;
    receiving implementation stays with its Project, and editorial/content
    production plus edit/render/package/publish execution stays with ACS when
    relevant. Either may enter first. A material sibling gap produces only a
    bounded suggestion to the caller; no automatic call, invented content,
    recursion, or deterministic chain passes Review.

Return:

```text
Review: design
Reviewer: <named reviewer>
Result: PASS | REVISE
Reviewed DESIGN.md SHA-256: `<sha256>`
Reviewed source companion: `<pre-existing-selected/source-relative-path>` — SHA-256 `<sha256>`
Checks: [job, specificity, voice, composition, states, accessibility, source safety, contract, optional native source, ownership and sibling route]
Next: create handoff | revise
Findings: [only material failures]
```
