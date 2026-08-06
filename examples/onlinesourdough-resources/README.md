# resources.onlinesourdough — Resources design direction

This is a fresh, self-contained design direction for the Resources product. It
keeps the warm Online Sourdough material language and exact supplied pixel
folder, while reducing the navigation to a quiet documentation-like shell:
Explore is always open, the other three groups are simple disclosures, and
Account / Need help are pinned to the bottom of the desktop rail.

## Files

- `BRIEF.md`: resolved product need, IA, states, constraints, and proof.
- `DESIGN.md`: portable tokens, composition fingerprint, and implementation
  rules.
- `index.html`: static hash-routed preview with responsive drawer behavior,
  themes, search, route pages, and explicit states.
- `assets/resources-folder-transparent.png`: exact 640×640 folder asset from
  the current read-only Resources implementation.
- `assets/fonts/`: local Geist Sans, Geist Mono, Geist Pixel, and license.

The preview has no runtime dependency on the application repository. Private or
not-yet-public work is represented with honest internal routes and status text.
