---
version: r1
name: Gustav Online social banners
description: One warm-paper unfinished-workbench direction that keeps Gustav Online as the public front door and makes the Business Freedom promise readable across LinkedIn and X.
colors:
  primary: "#2b1b12"
  on-primary: "#fffaf1"
  background: "#f7efe1"
  surface: "#fffaf1"
  paper: "#fbf4e8"
  border: "#d9c8b2"
  on-surface: "#2b1b12"
  on-surface-muted: "#6f5b4c"
  gustav-orange: "#d9672e"
  terracotta: "#bd6435"
  olive: "#74734d"
  aios-background: "#17334a"
  aios-cyan: "#84dce8"
  arcit-green: "#356d55"
  arcit-sand: "#e8dfc8"
  focus: "#176b9b"
typography:
  headline:
    fontFamily: Geist Sans, Arial, Helvetica Neue, ui-sans-serif, system-ui, sans-serif
    fontSize: 58px
    fontWeight: 720
    lineHeight: 0.98
    letterSpacing: -0.045em
  body:
    fontFamily: Geist Sans, Arial, Helvetica Neue, ui-sans-serif, system-ui, sans-serif
    fontSize: 24px
    fontWeight: 520
    lineHeight: 1.25
    letterSpacing: -0.01em
  label:
    fontFamily: Geist Mono, SFMono-Regular, Consolas, Liberation Mono, monospace
    fontSize: 18px
    fontWeight: 650
    lineHeight: 1.2
    letterSpacing: 0.085em
rounded:
  module: 16px
  proof: 20px
  frame: 24px
  full: 9999px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  safe: 56px
  section: 80px
components:
  public-promise:
    textColor: "{colors.on-surface}"
    typography: "{typography.headline}"
  constraint-line:
    backgroundColor: "{colors.terracotta}"
    size: 3px
  aios-proof-module:
    backgroundColor: "{colors.aios-background}"
    textColor: "{colors.aios-cyan}"
    rounded: "{rounded.module}"
  arcit-practice-module:
    backgroundColor: "{colors.arcit-green}"
    textColor: "{colors.arcit-sand}"
    rounded: "{rounded.module}"
  focus-ring:
    backgroundColor: "{colors.focus}"
    size: 3px
---

# Gustav Online social banners

## Overview

The visual idea is **the open workbench**. A tactile field of useful modules is
already in motion, but the field remains deliberately incomplete. One thin
terracotta line passes through the active parts and stops at one open slot. It
shows the onlinesourdough method in miniature: find one present constraint and
make the smallest complete change. The large calm field at right gives the
single public promise room to work like a landing-page hero.

This is one coherent business, not a portfolio of disconnected apps. Gustav
Online remains the public/person-led entrance. onlinesourdough appears as the
method. Offer, Operations, and Demand appear as problem areas. AIOS and Arc’IT
are each confined to one supporting tile, never elevated above Gustav Online.

## Portable direction and ownership

This `DESIGN.md` is the canonical, portable, human-readable visual direction for
the Gustav Online LinkedIn and X social banners. The two exact PNG exports,
their editable SVG compositions, the selected background seed and marks, the
browser preview, and crop/readability proof are companions. None replaces this
file or creates a receiving runtime dependency.

- **Scope and non-goals:** ADS owns the direction, visual hierarchy, composition,
  brand-role separation, typography, color, background treatment, line, crop
  proof, editable vector sources, and selected raster exports. It does not own
  public approval, profile copy outside the supplied banner words, platform alt
  text, upload, publication, or profile operation.
- **Review, revision, and acceptance:** Revision `r1` needs deterministic checks,
  direct browser/crop inspection, exact-dimension proof, and a bound independent
  review from `AIOS lead thread 01a066aa-ec32-7c51-a185-178ff44df838`.
  Receiver acceptance is separate and remains `PENDING` until Gustav Anderson
  explicitly accepts the generated `ADS-HANDOFF/1` snapshot. A later direction
  uses a new revision and re-acceptance.
- **Sibling boundary:** The brief supplies approved public copy and source-media
  decisions, so no ACS editorial route is needed. A future caption, campaign,
  profile rewrite, publishing package, or upload remains receiver/ACS work and
  is not invented here.
- **Known limitations:** Platform presentation can change, compress images, or
  shift avatar geometry. The crop proof uses the observed 2026-09-03 desktop
  presentation and must be rechecked at upload time. The selected AI-generated
  seed's upstream generation prompt is unavailable; it is disclosed and used
  only for noncritical background material. The SVG sources depend on the
  included Geist fonts and selected seed/marks for faithful rerendering. The
  exports prove design and legibility, not public performance, owner acceptance,
  or successful platform upload.

## Exact public copy

Keep these words unchanged on both banners:

- Prehead: `FOR FOUNDER-LED VIRKSOMHEDER`
- Headline: `Byg en virksomhed, der ikke venter på dig.`
- Support: `Enklere arbejde · ansvarlig AI · software du kan forstå og eje`
- CTA/domain: `gustavonline.com`

LinkedIn breaks only the headline after `virksomhed,`. X uses the same headline
break and breaks the support after `AI ·` for rendered-width legibility. Do not
rewrite the claim, add a result, or introduce a second CTA.

## Composition

The selected seed supplies warm paper grain, soft physical module shadows, and
faint empty slots. A deterministic SVG layer reduces it to one brand system:

1. Keep the active field in the left 42% and mostly above the vertical midpoint.
2. Use one actual onlinesourdough mark for `METHOD`, one restrained orange
   `G/O` tile for the public front door, and quiet `OFFER`, `OPS`, and `DEMAND`
   role labels. These are supporting wayfinding, not separate product claims.
3. Confine `AIOS / PROOF` to one dark navy/cyan tile and `ARC’IT / DFY` to one
   green/sand tile. Both stay left of the promise and may be covered by an avatar.
4. Thread one 3px terracotta rule through the active field. End it at one empty,
   terracotta-outline slot. Never branch it, turn it into data flow, or connect
   it to every faint slot.
5. Place the prehead, two-line headline, support, and domain in one flush-left
   group in the right/center safe field. No logo competes with the headline.

The source reference's modular rhythm is learned, not copied. Module count,
labels, positions, colors, symbols, line route, depth, and copy arrangement are
ADS-owned and specific to Gustav's brand hierarchy.

## Platform map and crop safety

| Surface  | Exact source | Proof display | Promise box               | Nonessential/avatar field      |
| -------- | ------------ | ------------- | ------------------------- | ------------------------------ |
| LinkedIn | 1584×396 PNG | 1128×282      | `x=690–1528`, `y=66–350`  | lower-left `x=0–430`, `y=230+` |
| X        | 1500×500 PNG | 600×200       | `x=720–1452`, `y=104–438` | lower-left `x=0–430`, `y=320+` |

At the proof widths, the LinkedIn headline renders near 38px and X near 24px.
The LinkedIn support renders near 15px; the X support uses two short lines near
10px. The domain remains distinct. Crop overlays must show the complete promise
box beyond the avatar circle and inside the outer 4% guard. The design tolerates
loss of any lower-left tile without changing the message.

## Color

Warm cream/paper is the dominant field. Walnut `#2b1b12` carries every public
word. Terracotta `#bd6435` is the only cross-module line. Gustav orange
`#d9672e` marks only the public/front-door tile. Muted olive may identify the
Operations material. AIOS uses one flat `#17334a` tile with `#84dce8` type.
Arc’IT uses one `#356d55` tile with sand/cream detail. These bounded accents
must not become a multibrand rainbow or imply a common software suite.

Avoid blue-purple AI gradients, neon glow, black/orange technology art, glossy
app icons, glass panels, oversaturated orange fields, and full-width dark bands.

## Typography

Use the owner-approved self-hosted Geist 1.7.0 files. Geist Sans carries the
headline, support, domain, and the restrained `G/O` monogram. The headline uses
a variable weight around 720, tight `-0.045em` spacing, and 0.98 line height.
Geist Mono carries the uppercase prehead and small module labels. Use optical
rather than mathematically uniform spacing: a short gap after the prehead, a
larger pause after the headline, then compact support/domain rhythm.

No condensed techno face, pseudo-code, icon font, all-caps headline, or display
pixel treatment appears in the public promise.

## Depth, shape, and material

The seed may show shallow physical relief, soft warm shadows, paper fiber, and
subtle imperfect surfaces. Deterministic role labels remain flat and crisp.
Module corners stay between 14px and 18px; the open slot uses only a 2px outline.
The AIOS and Arc’IT tiles are matte. Do not add glassmorphism, bevelled app-store
badges, chrome, lens flare, 3D logos, or deep floating shadows.

## Imagery, marks, and source safety

- `assets/gustav-social-banner-r1-background-seed.png` is the selected unchanged
  textless AI-generated background input. Critical text, marks, and linework do
  not come from it.
- `assets/onlinesourdough-mark.svg` is an existing approved method mark and
  appears once in the supporting tile field.
- `assets/arcitai-mark.svg` is an existing approved Arc’IT mark and appears once,
  inside the bounded done-for-you tile only.
- The owner-supplied Solt Wagner JPEG remains external reference evidence only.
  No third-party logo, icon, badge, character, app identity, or pixel arrangement
  enters the source or handoff.
- Exact final image-generation prompt provenance: `None — deterministic
SVG/Chrome raster export from the selected supplied seed.` The seed's own
  upstream prompt is unavailable in the supplied artifact metadata and is not
  reconstructed.

## Editable sources and export

`assets/gustav-social-banner-r1-linkedin.svg` and
`assets/gustav-social-banner-r1-x.svg` are the deterministic editable source
compositions. Each declares its exact canvas, uses local relative companions,
and carries provenance metadata. The ADS export script opens each source in a
local headless Chrome surface at device scale 1 and writes the exact PNG. The
script checks the PNG signature and dimensions after export. Re-exporting from
different browser/font rasterizer versions may change bytes while preserving
the declared visual direction; the reviewed snapshot binds the supplied bytes.

## Preview interaction and states

The browser preview is an inspection workbench, not a mock social application.
It shows both exact exports, their source dimensions, displayed proof widths,
and desktop-profile avatar overlays. A native `Show crop proof` / `Hide crop
proof` button toggles safe-area outlines using `aria-pressed`.

- Default: banners appear without engineering marks.
- Hover/active: the inspection control changes border and background without
  moving layout.
- Focus: a visible 3px blue outline and offset appears on keyboard focus.
- Pressed: avatar, edge guard, and promise box overlays become visible and are
  also explained in text.
- Loading/error/offline/permission/success: not applicable to the delivered
  static local images; a missing image retains meaningful alt text in preview.
- Reduced motion: overlay transitions become instantaneous; no other motion is
  present.

## Accessibility and legibility

Walnut on cream exceeds normal-text contrast requirements. Small supporting
module labels are nonessential and may disappear under an avatar; every public
word uses the larger promise group. The preview uses a skip link, semantic
header/main/section/footer landmarks, one H1, ordered headings, useful image
alternatives, a labeled native button, `aria-pressed`, visible focus, and a
reduced-motion query. The receiver should add concise platform alt text when
uploading and recheck any platform-provided crop before publication.

Suggested upload alt text, subject to receiver approval: `Warm cream Gustav
Online banner with an unfinished modular workbench at left and the promise Byg
en virksomhed, der ikke venter på dig at right.`

## Do / don't

Do keep one promise, one line, one open slot, warm material, large quiet space,
and clearly subordinate proof/delivery tiles. Do preserve the exact words and
the lower-left avatar tolerance. Do treat the field as one business method.

Do not copy the reference layout, ship third-party identities, create a grid of
apps, add fake product UI or metrics, place essential words under an avatar,
make AIOS or Arc’IT the umbrella brand, imply autonomous business operation, or
rewrite Business Freedom as maximum automation.

## Source decisions

- **source:heroui-ui-library** — rejected as a visual or runtime dependency.
  Native HTML controls are sufficient for this static preview and avoid adding
  an unrelated UI aesthetic.
- **source:desengs-inspiration** — not selected. The resolved Solt Wagner and
  Andreas Elmstrøm observations already supply the relevant composition and
  hierarchy principles; no DesEngs asset or layout is copied.
- **source:solt-wagner-composition-reference** — learn only modular rhythm,
  populated-to-open progression, and lower-left avatar tolerance. Reject all
  literal assets, app identities, badges, and exact placement.
- **source:andreas-elmstroem-landing-page-principle** — use one direct promise,
  repeated cleanly, while profile context and the owned domain carry the next
  action. Do not reproduce his portrait integration or layout.
- **source:generated-background-seed** — select as disclosed, noncritical
  background material because it improves tactile paper quality. All public
  words and brand-role cues remain deterministic above it.
- **source:existing-ads-brand-companions** — select the approved Geist fonts,
  onlinesourdough mark, Arc’IT mark, and prior warm-paper palette within their
  documented roles.
- **source:openpencil-optional-adapter** — not selected. Editable SVG is the
  smallest practical deterministic source and the portable route stays green
  without OpenPencil.
- **source:external-ui-libraries** — not selected. The preview needs only local
  semantic HTML, CSS, and a small native-button script.

## Delivery checklist

- Exact 1584×396 LinkedIn PNG plus SVG source.
- Exact 1500×500 X PNG plus SVG source.
- Selected background seed, two approved marks, and two Geist font files with
  license.
- Responsive preview and direct LinkedIn/X desktop crop proof.
- Exact file hashes and dimension/format evidence.
- Independent review bound to this `DESIGN.md` and every selected companion.
- Versioned `ADS-HANDOFF/1`, receiving owner Gustav Anderson, acceptance
  `PENDING`, no promotion and no live-profile mutation.
