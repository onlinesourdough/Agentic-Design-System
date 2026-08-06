---
version: alpha
name: resources.onlinesourdough Resources
description: A warm, folder-led decision library that helps founders move from a current constraint to a useful next step.
colors:
  primary: "#2b1b12"
  on-primary: "#fffaf1"
  background: "#f8f2e8"
  surface: "#fffaf1"
  surface-soft: "#f1eadf"
  paper: "#fffdf7"
  border: "#e5d7c6"
  border-strong: "#d4bd9f"
  on-surface: "#2b1b12"
  on-surface-muted: "#806c5c"
  accent: "#b86f36"
  accent-dark: "#663715"
  focus: "#2b6f98"
  success: "#3b6f55"
  on-success: "#fffaf1"
  error: "#9f3e2c"
  dark-background: "#18120e"
  dark-surface: "#221813"
  dark-surface-soft: "#2a1e17"
  dark-paper: "#302219"
  dark-border: "#3c2b21"
  dark-border-strong: "#69462d"
  dark-on-surface: "#fff2df"
  dark-on-surface-muted: "#c6ad94"
typography:
  display:
    fontFamily: Geist Pixel, Geist Mono, monospace
    fontSize: 58px
    fontWeight: 400
    lineHeight: 1.02
    letterSpacing: -0.04em
  headline:
    fontFamily: Geist Sans, Arial, Helvetica Neue, ui-sans-serif, system-ui, sans-serif
    fontSize: 23px
    fontWeight: 680
    lineHeight: 1.12
    letterSpacing: -0.025em
  body:
    fontFamily: Geist Sans, Arial, Helvetica Neue, ui-sans-serif, system-ui, sans-serif
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.58
    letterSpacing: 0em
  label:
    fontFamily: Geist Mono, SFMono-Regular, Consolas, Liberation Mono, monospace
    fontSize: 10px
    fontWeight: 560
    lineHeight: 1.3
    letterSpacing: 0.06em
  wordmark:
    fontFamily: Geist Pixel, Geist Mono, monospace
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: -0.03em
rounded:
  control: 8px
  folder: 12px
  panel: 12px
  holder: 24px
spacing:
  xs: 4px
  sm: 8px
  md: 14px
  lg: 22px
  xl: 34px
  section: 54px
  container: 1120px
  sidebar: 250px
  sidebar-collapsed: 76px
  topbar: 62px
components:
  sidebar:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface-muted}"
    padding: "{spacing.md}"
  sidebar-link:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface-muted}"
    rounded: "{rounded.control}"
    padding: "{spacing.sm}"
  sidebar-link-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-surface}"
    rounded: "{rounded.control}"
    padding: "{spacing.sm}"
  folder-paper:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.on-surface}"
    rounded: "{rounded.control}"
    padding: "{spacing.md}"
  folder-front:
    backgroundColor: "{colors.accent-dark}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.folder}"
    padding: "{spacing.md}"
  folder-shelf:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-surface-muted}"
    rounded: "{rounded.holder}"
    padding: "{spacing.sm}"
  orientation-panel:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.on-surface}"
    rounded: "{rounded.panel}"
    padding: "{spacing.lg}"
  primary-action:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.control}"
    padding: "{spacing.sm}"
  status-success:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-success}"
    rounded: "{rounded.control}"
    padding: "{spacing.xs}"
  focus-ring:
    backgroundColor: "{colors.focus}"
    size: 2px
  divider:
    backgroundColor: "{colors.border}"
    height: 1px
  dark-page:
    backgroundColor: "{colors.dark-background}"
    textColor: "{colors.dark-on-surface}"
  dark-surface:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.dark-on-surface}"
---

# resources.onlinesourdough Resources

## Overview

### Design read

Resources is a modular business decision and delivery system. The first job is
orientation: name the current constraint, choose the right working area, and
know what can be opened next. The page is therefore a quiet library shell with
one physical metaphor — four compact folders held by a low transparent shelf —
and a clear orientation surface beneath it. It is not a marketplace, generic
course catalogue, or dashboard of abstract categories.

### Product brief

- **Audience:** Founders and small teams working through a business, software,
  AI, or ownership decision.
- **Primary action:** Open `Begin`, understand the decision system, and choose a
  next step.
- **IA:** Explore is permanently visible and contains Begin, Featured, and
  What's New. Open Source, Courses, and Projects are simple expandable groups.
- **Home proof:** The first view shows the product statement, four compact
  top-level folders, their low transparent holder treatment, and the first
  useful orientation surface.
- **Route proof:** Explore, Open Source, Business Architecture, AIOS Desktop,
  Search, Account, and Need help are inspectable without external systems.

### Composition fingerprint

- **Page rhythm:** A narrow documentation rail, a quiet utility header, one
  restrained identity statement, one compact four-folder shelf, then the
  two-column VSL/orientation surface. Lower route pages use ruled lists and one
  useful right column instead of repeated cards.
- **First viewport:** Desktop shows the expanded rail, product statement, and
  the four folders near the first reading surface. Mobile keeps the statement
  and folder shelf intact, with navigation in a clean drawer.
- **Content density:** Dense in navigation and metadata, open in the primary
  reading surface. Rows carry route, access, duration, and outcome so copy is
  useful without becoming a wall of text.
- **Typography contrast:** Geist Pixel identifies Resources and one page
  statement. Geist Sans carries reading text. Geist Mono marks routes, labels,
  dates, statuses, and true ordered Blueprint steps.
- **Image role:** The supplied transparent pixel folder appears as a small
  orientation artifact and brand cue. CSS-native paper/folder shapes carry the
  four destinations so the asset is not stretched into a generic card grid.
- **Shape language:** Thin warm rules, paper indexes, square-ish controls, low
  transparent folder sleeves, and warm folder fronts. Surfaces are used only
  where they represent a real working object or reading panel.
- **Motion character:** Short, quiet transitions. Folder paper lifts slightly
  on hover/focus while the low transparent shelf stays still. Drawer, group
  disclosure, search, and theme transitions are functional and respect reduced
  motion.
- **Signature moment:** The four working areas read as a single shelf because
  the transparent lower sleeves align across the row, without adding a heavy
  base or another navigation taxonomy.
- **Anti-pattern:** No numbered sidebar categories, permanently floating
  folders, abstract labels, duplicate AIOS entries, public URLs for private
  repositories, decorative card stacks, or marketplace language.

### Reference translation

- **Current `onlinesourdough-resources` source:** Use its exact locked IA,
  warm token family, Geist font files, and supplied pixel-folder asset. Do not
  copy application code or preserve the removed folder-holder omission.
- **Historical Workbench Resources preview:** Use its restrained grid field,
  hero rhythm, compact folder proportions, low transparent shelf, and useful
  VSL/orientation surface as the visual baseline. Keep the newer IA and sidebar
  behavior rather than restoring the historical navigation model.
- **AIHero/Matt Pocock screenshots:** Use the simplicity of the documentation
  rail, visible hierarchy, and primary/right-column rhythm. Do not copy its
  brand, identity, assets, exact layout, copy, or product model.
- **Workbench ArcitAI and Crypto Club previews:** Use only the migration
  workflow and proof that a preview can show real routes and states. They are
  preserved references, not component templates for Resources.

## Colors

Warm cream is the page field; paper white marks reading surfaces; brown carries
the product and folder fronts; terracotta is reserved for active folder detail
and small accents; blue is reserved for keyboard focus. Dark mode turns the
paper field into warm brown-black and keeps the same hierarchy rather than
introducing a second neon palette. Muted text remains readable on both themes.

## Typography

Geist Pixel is intentionally scarce: the wordmark, one display statement, and
selected stage titles. Geist Sans is the default for headings, body, controls,
and navigation. Geist Mono is for route labels, access states, dates, shortcuts,
and the ordered Blueprint index. Never use pixel type for long paragraphs.

## Layout

Use a 1120px maximum reading shell with a 250px desktop sidebar and a 62px
utility header. The desktop main surface uses a 1.15fr/0.85fr relationship in
the orientation section. The four folders are a four-column shelf at wide
widths and two columns below 760px; the transparent lower shelf remains visible
on every folder at every width. At 900px the sidebar becomes a drawer and the
main surface retains the same reading order. The collapsed desktop rail is 76px
wide and keeps the Resources mark plus an always-visible reopen control.

## Elevation & Depth

Use borders, tonal shifts, and the physical paper overlap before shadows. The
transparent folder shelf uses only an inset highlight and blur; the orientation
panel gets one restrained paper shadow. Drawers and search overlays may float
above the page. Do not shadow every navigation item or list row.

## Shapes

Controls use an 8px radius, reading panels 12px, and the low transparent shelf a
broad 24px lower curve. Status labels are compact and rectangular; they are not
decorative pills. Folder tabs, paper corners, and divider rules are the visual
vocabulary.

## Components

### Navigation

Explore is a real visible section with no chevron or collapse action. Open
Source, Courses, and Projects each have an explicit disclosure button with
`aria-expanded`, a visibly smaller child indent, and an active route treatment.
The desktop collapse control keeps the logo and tooltip-like label available;
the mobile drawer adds a close action and backdrop. Account and Need help live
in a flex-pinned bottom region.

### Home folder shelf

Each folder is a link with a paper index behind a compact warm folder front. The
four folders are Explore, Open Source, Courses, and Projects in that order. A
34px transparent shelf overlaps only the lowest part of each folder, aligned as
one continuous treatment across the row. It must sit low enough that it supports
the folders without bisecting their titles or descriptions.

### Orientation and reading rows

The main VSL/orientation panel uses the supplied pixel folder image, a short
`Begin` outcome, duration, and one primary action. Featured and What's New sit
below as two flat ruled lists with route, access, and update metadata. Rows have
hover, active, and visible keyboard-focus states without becoming individual
decorative cards.

### Route and state behavior

Search exposes a labeled field, a short loading state, specific results, and an
empty result with a recovery hint. Course rows use the only numbering in the
preview: the true ordered `01`–`08` Blueprint steps, with honest Paid/locked
states and a login path. Internal project pages use local routes and say when a
public source is not available. Account and Need help show validation errors and
recoverable success feedback. An offline note explains that the static preview
does not send email or load private content.

## Do's and Don'ts

- Do keep the four folder destinations literal and visible near the first
  reading surface.
- Do pin Account and Need help to the desktop rail bottom and make the mobile
  drawer easy to close.
- Do use real current IA and believable draft resource names, dates, access,
  and outcomes.
- Do preserve the supplied pixel folder and the low transparent shelf as
  supporting objects, not decoration.
- Don't number sidebar categories or add a chevron to Explore.
- Don't invent public GitHub links for private repositories.
- Don't turn every region into a rounded card, reintroduce abstract labels, or
  make Resources look like a generic course marketplace.
