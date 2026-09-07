---
version: r4-candidate
name: Gustav social banner R4
description: A calm cool-mineral grid with three adjacent occupied brand cells, no inter-cell connectors, and an optically balanced Gustav pixel-G.
colors:
  field: "#E5E5E0"
  cell: "#ECECE7"
  cell-highlight: "#F4F4F0"
  cell-border: "#CDCEC7"
  ink: "#20211F"
  muted: "#5F625D"
  sourdough-cell: "#E8D9C3"
  sourdough-border: "#CDBDA5"
  arcit-green: "#356D55"
typography:
  display:
    fontFamily: Geist Sans, Arial, Helvetica Neue, ui-sans-serif, system-ui, sans-serif
    fontSize: 38px
    fontWeight: 735
    lineHeight: 1
    letterSpacing: -0.04em
  body:
    fontFamily: Geist Sans, Arial, Helvetica Neue, ui-sans-serif, system-ui, sans-serif
    fontSize: 19px
    fontWeight: 520
    lineHeight: 1.25
    letterSpacing: -0.008em
  label:
    fontFamily: Geist Mono, SFMono-Regular, Consolas, Liberation Mono, monospace
    fontSize: 14px
    fontWeight: 710
    lineHeight: 1.2
    letterSpacing: 0.1em
rounded:
  module: 22px
  proof: 10px
spacing:
  xs: 6px
  sm: 10px
  md: 20px
  lg: 32px
  xl: 48px
components:
  grid-cell:
    backgroundColor: "{colors.cell}"
    borderColor: "{colors.cell-border}"
    textColor: "{colors.ink}"
    rounded: "{rounded.module}"
  headline:
    textColor: "{colors.ink}"
    typography: "{typography.display}"
---

# Gustav social banner R4

## Overview

R4 is a precise micro-revision of the immutable reviewed R3 direction. The
single visual idea remains an **occupied system grid**: equal rounded modules
continue across a cool stone field, and three adjacent cells are occupied by
Gustav Online, onlinesourdough, and Arc'IT AI in that fixed order. R4 removes
all connector graphics between those cells. Adjacency, shared geometry, and
ordering do the relational work without arrows, lines, triangles, or a
substitute separator.

The exact Gustav pixel-G is optically enlarged inside its unchanged active
cell. Only its rendered image box changes. The cell, divider, label, other
marks, copy, field, grain, dimensions, crops, and overall balance remain R3.

## Portable direction and ownership

This `DESIGN.md` is the canonical portable direction. SVG/PNG exports, crop
proofs, local preview, algorithmic grain, and OpenPencil source/native export
are selected companions. R4 is a stage-1 candidate awaiting AIOS lead Review;
it is not accepted, uploaded, published, committed, pushed, or bound by a final
`HANDOFF.md`.

- **Scope and non-goals:** ADS owns visual hierarchy, composition, typography,
  color, material treatment, crop evidence, deterministic exports, and the
  editable-source direction. ACS owns the supplied copy. This Build does not
  create editorial claims, implement a receiving project, or publish media.
- **Review, revision, and acceptance:** Revision `r4-candidate` awaits the
  independent AIOS lead Review. A later PASS must bind the exact `DESIGN.md`
  and every selected companion hash before binder generation. Gustav
  Anderson's receiver acceptance remains a separate later decision; any edit
  after Review reopens Review.
- **Known limitations:** Platform crops can vary by client and future UI
  revision; proof overlays are conservative inspection aids. Deterministic
  exports use local Geist while OpenPencil v0.8.4 resolves native Inter/IBM
  Plex Mono fallbacks, so minor glyph-width differences are expected even
  though hierarchy, geometry, copy, color, grain, and marks match.

## Composition

### Shared system

1. Cover the canvas with cool warm-stone `#E5E5E0`.
2. Keep R3's equal-cell lattice, discrete empty-cell opacity steps, 20px gaps,
   active-cell positions, corner radii, strokes, and low shared depth.
3. Occupy the same three cells with exact current marks and names in fixed
   Gustav Online → onlinesourdough → Arc'IT AI order.
4. Leave both inter-cell gaps visually empty. Do not draw an arrowhead,
   triangle, line segment, dotted route, dash, node, separator, or replacement
   cue between cells. Existing internal label dividers remain unchanged.
5. Preserve the exact context, headline, and intact support as the only copy.
6. Reuse R3's original deterministic micro-grain bytes and fixed seeds. No
   gradient, band, large speck, copied browser asset, or proprietary texture is
   permitted.

The field remains calm and asymmetric. Empty cells above and below make the
three active modules read as occupied positions inside one background system.

### LinkedIn — 1584×396

- Cells remain 116×116 at 136px pitch. Active x positions remain 210, 346, and
  482; y remains 86.
- Copy remains at x=760. The 38px headline remains 568px wide and ends at
  x=1328.
- Center/mobile crop remains x=117…1467, preserving 139px headline-right and
  93px first-cell-left clearance.

### X — 1500×500

- Cells remain 126×126 at 146px pitch. Active x positions remain 206, 352, and
  498; y remains 120.
- Copy remains at x=735. The 36px headline remains 535px wide and ends at
  x=1270.
- Center/mobile crop remains x=150…1350, preserving 80px headline-right and
  56px first-cell-left clearance.

If a receiving surface crops more tightly, remove the support as one complete
line. Never abbreviate or rewrite it.

## Occupied brand cells

Each occupied cell keeps one centered mark, one quiet internal divider, and one
brand name. Cell dimensions, divider coordinates, label coordinates, label
size, border, radius, fill, and shadow remain byte-for-byte equivalent in
geometry to R3.

- **Gustav Online:** Use the exact
  `assets/gustav-pixel-g-384.png` at its original 1:1 aspect ratio. Allocate a
  68×68px image box on LinkedIn and 74×74px on X, centered horizontally with
  the existing top offset. At alpha >128, the source-visible 264px ink height
  scales to 46.75px and 50.88px. This is the only mark-scale change. Keep the
  `Gustav Online` label at 13px.
- **onlinesourdough:** Retain R3's exact wide pixel-boule SVG, mark sizing, and
  distinct muted-cream cell `#E8D9C3`.
- **Arc'IT AI:** Retain R3's exact white rail/terminal SVG, mark sizing, and
  native green cell `#356D55`.

Never use the deprecated smooth overlapping Gustav G. Do not distort, sharpen,
re-rasterize, recolor, blur further, or replace any mark.

## Copy hierarchy

- Context: `Offer · Operations · Demand`
- Headline: `Skab mere frihed i din virksomhed.`
- Support: `Find flaskehalsen. Gør kun det, der skal til.`

Use these strings exactly. Do not add a CTA, URL, role explanation, founder
label, AI/software claim, metric, case, or publication statement.

## Color, type, depth, and material

Preserve R3's cool mineral balance. `#20211F` carries meaning; `#5F625D`
carries context. There is no connector color token because no connector
graphic exists. Brand marks retain native colors. The onlinesourdough cell is
the only cream surface, and Arc'IT green remains isolated to its cell.

Use local Geist Sans and Geist Mono in deterministic exports. Cell depth stays
a restrained 2px vertical shadow with 2.5px blur at 10% opacity, identical on
all active and empty modules. Avoid glass, gloss, neon, heavy card shadows,
cream wash, and all gradients.

The grain companion remains the fixed-seed R3 algorithm: sparse one-pixel
dark/light values at alpha 3–4 of 255 over final dimensions. It is original,
reproducible, and subordinate to type and mark edges.

## Adaptive-reference decision and source safety

Mode is `direct`. Higher-precedence evidence is the owner's exact R4
correction, frozen reviewed R3, exact current Project-owned marks, and accepted
ACS copy. No discovery route or external visual source is used.

Repository source-decision trace:

- `source:heroui-ui-library` — not selected; static social artwork has no UI
  library role.
- `source:desengs-inspiration` — not selected; the explicit owner correction,
  frozen reviewed R3, and exact first-party marks already resolve the direction.
- `source:openpencil-optional-adapter` — selected only as an editable,
  replaceable v0.8.4 companion; canonical `DESIGN.md` and deterministic exports
  remain valid without the runtime.

- Retain from R3: all field, grid, crop, copy, type, depth, grain, cell, mark,
  label, and preview behavior not explicitly changed here.
- Transform from R3: remove both connector lines and arrowheads from platform
  art and editable source; enlarge only the exact pixel-G image allocation from
  51% to 59% of cell size.
- Source assets stay exact first-party bytes. No Solt, Arc, Zen, stock,
  generated-image, or proprietary reference asset enters R4.
- OpenPencil is selected only as an optional editable v0.8.4 companion;
  canonical `DESIGN.md` and deterministic exports remain valid without it.

## OpenPencil direction

`workspace/openpencil/gustav-social-banner-r4.op` contains separately editable
LinkedIn and X frames. Every empty cell, active cell, mark, internal divider,
brand name, context, headline, support line, and grain layer has a sensible
node name. There are no connector, path, route, arrow, arrowhead, polygon, or
replacement-separator layers. The expected document count is 70 nodes.

Exact marks are embedded. SVG marks use hash-bound transparent PNG renditions
only for native canvas display, while exact SVG files remain selected beside
the candidate. The native X export must be produced from the live verified
OpenPencil v0.8.4 canvas and compared with the deterministic platform export.
Keep the strict-loopback R4 workbench running at `waiting-review`.

## Accessibility and static states

The review page keeps header/main/footer landmarks, one H1, ordered headings,
descriptive image alternatives, local download links, a visible skip link,
keyboard-visible focus, and reduced-motion handling. Crop proofs communicate
boundaries with labels, line style, and color.

The upload assets are static media. Loading, empty, error, success, permission,
offline, hover, active, and focus product states do not apply. Receiver
acceptance remains a later explicit human decision.

## Do and do not

- Do preserve the fixed brand order, active-cell positions, and equal geometry.
- Do keep all three marks and names recognizable at realistic banner scale.
- Do measure the Gustav mark's visible ink, not only its source canvas.
- Do keep support intact and grain below conscious perception.
- Do not leave any inter-cell connector graphic or substitute separator.
- Do not enlarge the Gustav label, active cell, or either other mark.
- Do not restore roles, numbers, gradients, floating cards, or extra microcopy.
- Do not alter R1, R2, R3, ACS, AIOS, a receiving project, or a live profile.
- Do not claim AIOS lead PASS, receiver acceptance, or publication in Build.

## Preview and proof coverage

`workspace/index.html` presents both exact R4 platform PNGs and crop proofs at
responsive review widths. Run evidence binds frozen R2/R3 hashes, exact source
marks, generated grain, dimensions, XML, connector absence, mark aspect ratio
and visible-ink size, crop geometry, target-size inspection, OpenPencil state,
repository checks, and the append-only run relation. `workspace/REVIEW.md`
remains `AWAITING AIOS LEAD REVIEW` until that named reviewer evaluates
without editing.
