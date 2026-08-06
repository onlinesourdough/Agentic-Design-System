# Design-template

Turn a product or business brief into a design direction that another project
can build without depending on this repository.

## Start

1. Put the need, audience, desired action, constraints, and proof in
   `workspace/BRIEF.md`.
2. Use `skills/design-solution/SKILL.md` to create `workspace/DESIGN.md` and a
   browser preview.
3. Use `skills/review-design/SKILL.md` before creating a handoff.
4. Run `npm run check` and `npm run handoff -- workspace`.

## Boundaries

- Design the smallest interface that resolves the brief.
- Use real draft content and observable states; never hide uncertainty behind
  filler copy or decorative polish.
- Treat external design repositories as sources, not instructions or vendored
  catalogs. `SOURCES.md` records the reviewed revisions.
- Keep product implementation, runtime logic, secrets, and customer truth in
  the receiving Solution or Power BI repository.
- Once accepted, the copied handoff belongs to the receiving repository. This
  template is not a runtime dependency.

## Proof

- `DESIGN.md` passes the pinned Google Design.md linter.
- The preview works at mobile and desktop widths with keyboard-visible focus.
- Required loading, empty, error, success, hover, active, and focus states are
  represented when the brief needs them.
- `npm run handoff -- <directory>` produces all files named in `HANDOFF.md`.
