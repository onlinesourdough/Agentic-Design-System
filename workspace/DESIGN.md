---
version: r1
name: Gustav Online constraint thumbnails
description: Two calm, warm, editorial 16:9 thumbnail directions—one human founder queue and one constraint diagnosis board—for plausible future long-form videos.
colors:
  primary: "#2b1b12"
  on-primary: "#fffaf1"
  background: "#f8f2e8"
  surface: "#fffdf7"
  surface-muted: "#efe4d4"
  border: "#d8c3aa"
  on-surface: "#2b1b12"
  on-surface-muted: "#6f594a"
  walnut: "#5a3d30"
  terracotta: "#b86f36"
  gustav-orange: "#f36f2b"
  technical-cyan: "#72d9ed"
  focus: "#2b6f98"
  success: "#3b6f55"
  error: "#9f3e2c"
typography:
  display:
    fontFamily: Geist Sans, Arial, Helvetica Neue, ui-sans-serif, system-ui, sans-serif
    fontSize: 104px
    fontWeight: 760
    lineHeight: 0.88
    letterSpacing: -0.055em
  landmark:
    fontFamily: Geist Pixel, Geist Mono, monospace
    fontSize: 88px
    fontWeight: 400
    lineHeight: 0.92
    letterSpacing: -0.045em
  label:
    fontFamily: Geist Mono, SFMono-Regular, Consolas, Liberation Mono, monospace
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.09em
  body:
    fontFamily: Geist Sans, Arial, Helvetica Neue, ui-sans-serif, system-ui, sans-serif
    fontSize: 22px
    fontWeight: 520
    lineHeight: 1.3
    letterSpacing: -0.015em
rounded:
  label: 8px
  panel: 22px
  frame: 28px
  full: 9999px
spacing:
  xs: 6px
  sm: 12px
  md: 20px
  lg: 32px
  xl: 48px
  xxl: 72px
  safe: 48px
components:
  thumbnail-frame:
    backgroundColor: "{colors.background}"
    textColor: "{colors.on-surface}"
    width: 1280px
    height: 720px
    padding: "{spacing.safe}"
  founder-queue:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    accentColor: "{colors.gustav-orange}"
  constraint-board:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    activeColor: "{colors.gustav-orange}"
    rounded: "{rounded.panel}"
  safe-area:
    inset: "{spacing.safe}"
    bottomRightReserve: 168px × 74px
  focus-ring:
    backgroundColor: "{colors.focus}"
    size: 3px
---

# Gustav Online constraint thumbnails

## Overview

This direction turns two business-system stories into one recognizable Gustav
Online / onlinesourdough thumbnail family. The family uses warm paper, walnut,
terracotta, Gustav orange, scarce technical annotation, and direct short copy.
It stays human and editorial: no shock expression, logo wall, fake result,
agent swarm, or generic AI gloss.

The shared visual idea is **one constraint made visible**. Topic 01 shows the
constraint as a founder-owned queue converging on Gustav. Topic 02 shows the
constraint as a diagnosis board where Offer, Ops, and Demand are compared and
Demand is the current worked example. The compositions intentionally differ:
one is portrait-led and dark; the other is diagram-led and light.

## Portable direction and ownership

This `DESIGN.md` is the canonical, portable, human-readable visual direction
for the two thumbnail concepts. The browser preview, two SVGs, two PNGs,
contact-sheet capture, selected portrait/font files, and OpenPencil source and
review export are companions. None replaces this file or creates a live
dependency for the receiving owner.

- **Scope and non-goals:** ADS owns the visual direction, composition,
  hierarchy, typography, color, portrait treatment, diagrams, editable sources,
  export boundary, and visual Review. ADS does not claim the videos exist,
  approve a thesis or script, select source footage, perform content production,
  package a release, publish, or accept the handoff for Gustav.
- **Review, revision, and acceptance:** Revision `r1` needs exact-dimension
  export checks, full-size and 320×180 visual inspection, responsive browser
  inspection, live OpenPencil inspection, deterministic checks, and independent
  `ADS Review` PASS bound to every selected source companion. The generated
  `ADS-HANDOFF/1` remains `PENDING` until Gustav Anderson / Gustav Online
  separately accepts it.
- **Known limitations:** These are thumbnail directions and future-content
  planning artifacts, not final video titles, scripts, footage, upload packages,
  performance predictions, or publication claims. The owner portrait is a
  candid elevator mirror image, so Topic 01 reads as personal documentation
  rather than a studio talking-head. OpenPencil v0.8.4 may approximate local
  Geist fonts, but its fixed composition and layer structure remain inspectable;
  the exact SVG/PNG pair is the reviewed rendering boundary. Receiver
  acceptance and any later content-production review remain pending.

## Adaptive reference decision

The selected mode is `explore`. Owner constraints, prior accepted ADS brand
truth, and the tracked portrait have precedence. Supplied creator URLs and the
local screenshot kit are visual signals only.

### Compared direction A — human queue

- **Lenses:** cinematic-human plus warm-tactile.
- **Frame:** real founder in an ordinary environment, cropped with restraint;
  large direct statement; small paper slips converge into one visible queue.
- **Positive signals:** person plus environment, short copy, one clear story
  tension, warm grading, space for words.
- **Avoid:** copied portrait treatment, reaction face, metric, fake studio,
  heavy outline, logo, or dramatic before/after claim.
- **Selection:** chosen for Topic 01 because the story is personal founder
  dependency and the portrait is an approved owner asset.

### Compared direction B — diagnostic board

- **Lenses:** warm-tactile plus evidence-led.
- **Frame:** one paper workbench with three labeled diagnostic lanes and one
  selected constraint; a large editorial headline stays separate from the
  diagram.
- **Positive signals:** plain-language systems framing, one explanatory
  diagram, visible method contrast, restrained annotation.
- **Avoid:** copied whiteboard layout, SaaS dashboard, logo strip, numeric
  claim, arrows as decoration, or an installed-stack story.
- **Selection:** chosen for Topic 02 because the decision is diagnostic and the
  method must be legible without relying on a face.

The result deliberately keeps both selected frames because the requested
outcome is two topical thumbnails. Their shared palette, type, safe area,
paper-rule texture, label rhythm, and corner language make them one family.

## Thumbnail 01 — The founder-owned queue

### Message

`THE WORK WAITED FOR ME` is the reviewed thumbnail cue. It is sharper than the
working title while remaining honest: useful work existed, but production and
approval decisions repeatedly converged on Gustav. The present/past ambiguity
does not claim a complete fix; the small `FOUNDER QUEUE` label names the
mechanism.

### Composition

- Canvas: exact 1280×720.
- Gustav’s real portrait occupies the left 47%. Preserve the elevator, phone,
  and candid posture; do not cut out, reshape, retouch, or synthesize him.
- A translucent walnut wash and warm orange edge integrate the cool metal
  environment with the family palette without flattening the photograph.
- A diagonal paper seam moves from the portrait into a walnut reading field.
- The headline occupies the upper-right two-thirds in three lines. `WAITED` is
  Gustav orange; the other words are warm paper.
- Three small paper queue slips—`VISUAL`, `VERSION`, `APPROVAL`—sit on one
  terracotta line that terminates at a single orange `ME` node. The diagram is
  supporting evidence, not a second headline.
- Keep all essential copy inside 48px. Keep the bottom-right 168×74 timestamp
  reserve free of essential meaning.

### Typography and contrast

Use Geist Sans 96–110px at heavy weight for the statement, Geist Mono 15–17px
for owner/queue labels, and no serif. Warm paper on walnut exceeds the required
thumbnail contrast; orange is used for the single tension word and is backed by
dark walnut. Do not add a stroke or glow around the portrait or type.

## Thumbnail 02 — The real constraint

### Message

`THE REAL CONSTRAINT` is the reviewed cue. `OFFER / OPS / DEMAND` makes the
method concrete. Demand is highlighted only as this story’s worked example; the
thumbnail does not claim Demand is always the answer.

### Composition

- Canvas: exact 1280×720.
- Use a full warm-cream reading field with a faint tactile paper grid.
- The large two-line headline sits left, with `REAL` in terracotta and the
  remaining words in walnut.
- A paper diagnosis board sits right. Three unequal horizontal lanes are
  labeled `OFFER`, `OPS`, and `DEMAND`; each has its own simple constraint mark.
- `DEMAND` receives the orange selection field and a visible `CURRENT` label.
  A terracotta line connects it to the small `SMALLEST COMPLETE CHANGE` note.
- Do not depict software, agents, automation, or a process stack. This is a
  thinking method, not installed tooling.
- Keep all essential copy inside 48px. The lower-right timestamp reserve
  remains plain cream/paper.

### Typography and contrast

Use Geist Pixel for the landmark headline where available, falling back to
Geist Mono. Use Geist Mono for `OFFER / OPS / DEMAND` and method annotations.
Walnut on cream and paper is the primary contrast pair; the orange selection
also carries the word `CURRENT`, so state does not depend on color alone.

## Family system

### Color roles

- Cream `#f8f2e8` and paper `#fffdf7`: primary editorial field.
- Walnut `#2b1b12` / `#5a3d30`: reading contrast, structure, and the Topic 01
  founder-owned field.
- Terracotta `#b86f36`: constraint line and explanatory annotations.
- Gustav orange `#f36f2b`: one human/tension signal per composition.
- Technical cyan `#72d9ed`: reserved and unused in the two final thumbnails;
  there is no technical subsystem that needs it.

### Type roles

- Geist Sans: direct human claim and accessible preview prose.
- Geist Pixel: one Topic 02 landmark to connect with accepted onlinesourdough
  visual language.
- Geist Mono: compact evidence, queue, owner, and diagnosis labels.
- Maximum visible thumbnail copy is one short headline plus necessary method
  labels. Avoid sentences, subtitles, fake captions, and tool names.

### Material and shape

Use flat paper fields, one-pixel warm rules, clipped portrait edges, irregular
but controlled line segments, 8px labels, 22px boards, and a subtle paper-grid
texture. Avoid glass cards, neon glow, 3D objects, fake tape, heavy grain, or
ornamental craft effects.

### Safe crop and YouTube-card behavior

- Essential copy and meaning stay at least 48px from each canvas edge.
- The lower-right 168×74 area is not used for essential text or the selected
  state because YouTube may place duration UI there.
- At approximately 320×180, the headline must read first, the portrait or
  three-lane structure second, and the tiny evidence labels may become texture
  without carrying unique meaning.
- No clipping, overlap, or linked-asset loss is allowed in either SVG or PNG.

## Preview and accessibility

The supporting `index.html` shows both exact exports at large 16:9 size and
again at 320×180. It provides a skip link, semantic header/main/section/footer
landmarks, ordered headings, descriptive alt text, local-only assets,
keyboard-visible 3px focus, and a reduced-motion query. There is no automatic
motion. The required proof-state fixtures are explicit, inert labels for the
workbench only; they are not false thumbnail interaction states.

## OpenPencil companion

`openpencil/youtube-thumbnails-r1.op` is a truthful editable Topic 02
composition with a fixed 1280×720 root frame, editable headline, method labels,
paper board, lane geometry, current-state marker, and smallest-change note.
`openpencil/exports/topic-02-real-constraint.png` is the reviewed comparison
export boundary and is byte-identical to the exact browser-rendered SVG PNG.
The OpenPencil top-bar export action did not yield a downloadable artifact in
the Codex built-in browser, so this file is not misrepresented as a native UI
export. The exact SVG remains the portable vector master for this thumbnail;
the live canvas proves `.op` rendering and editability.

The selected route requires the verified v0.8.4 workbench to start on strict
`127.0.0.1`, return its machine-readable URL, and expose the actual `.op`
document in the Codex-compatible built-in browser. The reviewer verifies the
real document and layer/canvas state. A printed URL or chat PNG/SVG alone is not
proof. Because receiver review is pending, the workbench stays alive after the
Build handoff; a later explicit stop performs cleanup.

## Source decisions

- **source:heroui-ui-library** — rejected for this static visual surface. No UI
  library or adapter is needed.
- **source:desengs-inspiration** — retain only the already audited principle of
  concise editorial grouping. No component, copy, layout, or asset is reused.
- **source:openpencil-optional-adapter** — explicitly selected for Topic 02 in
  this run. Start only the pinned verified v0.8.4 bytes; use the real supervised
  surface; copy no upstream UI, template, or design content. OpenPencil remains
  optional for other ADS routes.
- **Creator/reference pointers** — Frederik Pahuus and Andreas Elmstrøm channel
  and video URLs, plus the local screenshot kit, contribute only the supplied
  signals: real founder/environment, short prominent copy, one diagram,
  restrained editorial scenes, and a clear method contrast. No layout,
  branding, arrow, metric, portrait treatment, or screenshot byte is copied.

## Asset notes and provenance

- `assets/gustav-portrait.jpg` — byte-unchanged approved Gustav Online source
  from revision `87b59cdb069206e37425b8742cb7727e95caa4c1`; SHA-256
  `4b1001c1b9ef3ec23c46e0d745210671609488b608fdb6b31c0bad9307644ebd`.
  Owner-supplied and used only in Topic 01.
- `assets/fonts/geist-sans-variable.woff2`,
  `assets/fonts/geist-mono-variable.woff2`, and
  `assets/fonts/geist-pixel-square.woff2` — byte-unchanged tracked Geist 1.7.0
  fonts with the carried SIL Open Font License in `assets/fonts/LICENSE.txt`.
- `assets/thumbnail-01-founder-queue.svg` and
  `assets/thumbnail-02-real-constraint.svg` — original ADS-owned 1280×720
  editable vector compositions authored for this run.
- Matching `.png` files — exact 1280×720 browser-rendered review exports of the
  SVG masters. No generated raster ingredient is used.
- `assets/youtube-thumbnails-contact-sheet.png` — browser-rendered proof view
  showing both directions at large 16:9 and 320×180 card scale.
- `openpencil/youtube-thumbnails-r1.op` — original ADS-owned editable Topic 02
  reconstruction created from this canonical direction; it uses no embedded
  third-party image or template.
- OpenPencil release `v0.8.4` is MIT-licensed at release commit
  `c51d7ed41a96068a09127bbc096fee143fce0b22`; observed upstream main
  `9c810776dab546076a5d9db791a49d9e8048dbd7`; selected VSIX SHA-256
  `7ce6cde22f7e8584de2faca0279f6d74438675291c2547a7d99230fc0e629342`.
  Its runtime is temporary and not committed or included.

## Do's and Don'ts

- Do make one constraint visible in each thumbnail.
- Do keep the short headline readable at 320×180.
- Do preserve Gustav’s real candid portrait without synthetic alteration.
- Do let Topic 01 feel human/dark and Topic 02 methodical/light.
- Do keep Demand as a current worked example, not a universal diagnosis.
- Do reserve final choice for Gustav and receiver acceptance.
- Don't invent revenue, subscriber, conversion, client, performance,
  completion, installed-stack, or before/after claims.
- Don't copy a creator layout, brand, arrow language, metric, or portrait
  treatment.
- Don't use clickbait faces, purple AI gradients, agents, robots, tool logos,
  SaaS gloss, or literal bread imagery.
- Don't let the `.op`, preview, or PNG replace canonical `DESIGN.md`.

## Review target

The independent reviewer compares `BRIEF.md`, this direction, both SVGs, both
PNGs, the contact-sheet/preview, the unchanged portrait and fonts, and the live
Topic 02 OpenPencil canvas. PASS requires exact dimensions, readable hierarchy
at 1280×720 and approximately 320×180, safe crop, sufficient contrast, no
clipping/overlap/missing assets, no accidental URL or third-party brand
contamination, clear topic distinction, and complete path/hash binding for the
selected cross-owner handoff.
