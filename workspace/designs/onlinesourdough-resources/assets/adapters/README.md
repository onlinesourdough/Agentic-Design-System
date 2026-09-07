# Resources adapter proof

The carried Resources preview integrates one small, ADS-owned
`heroui-disclosure` adapter. It uses the existing native `button`,
`aria-expanded`, `aria-controls`, keyboard handler, and visible focus contract
to make the AI Literacy disclosure readable in the static preview.

The adapter is an original CSS/state adaptation, not copied HeroUI code and
not a dependency. HeroUI was selected for this one interaction because its
Apache-2.0 source and React Aria foundation make the accessibility state model
worth studying; the static HTML preview cannot justify importing a React/Tailwind
runtime. The exact source decision is recorded in `docs/SOURCE_AUDIT.md`.
It remains an optional companion to canonical `DESIGN.md`; a selected
cross-owner snapshot binds its relative path, SHA-256, provenance, and license
boundary in `HANDOFF.md`.

Proof surface:

- `../index.html` loads this local stylesheet.
- The `AI Literacy` disclosure exposes a real name, `aria-expanded`,
  `aria-controls`, Enter/Space behavior, hover, and `:focus-visible`.
- `npm run check` scans the example and its local assets; the review method
  checks the same interaction at desktop and mobile widths.
