---
version: alpha
name: Agentic Design System route console
description: A calm operational surface for resuming design work, reading proof, and curating examples.
colors:
  primary: "#173d45"
  on-primary: "#f5f1e8"
  background: "#f5f1e8"
  surface: "#fffdf7"
  border: "#d7d2c7"
  on-surface: "#1d282b"
  on-surface-muted: "#5c6868"
  accent: "#d06b45"
  on-accent: "#fffaf3"
  success: "#2c765b"
  on-success: "#f5fff9"
  error: "#a84335"
  focus: "#c05437"
typography:
  display:
    fontFamily: ui-sans-serif, system-ui, sans-serif
    fontSize: 68px
    fontWeight: 720
    lineHeight: 0.98
    letterSpacing: -0.055em
  headline:
    fontFamily: ui-sans-serif, system-ui, sans-serif
    fontSize: 32px
    fontWeight: 680
    lineHeight: 1.08
    letterSpacing: -0.03em
  body:
    fontFamily: ui-sans-serif, system-ui, sans-serif
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0em
  label:
    fontFamily: ui-monospace, SFMono-Regular, Consolas, monospace
    fontSize: 12px
    fontWeight: 650
    lineHeight: 1.2
    letterSpacing: 0.055em
rounded:
  sm: 6px
  md: 12px
  lg: 18px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  xxl: 72px
components:
  page:
    backgroundColor: "{colors.background}"
    textColor: "{colors.on-surface}"
  primary-action:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: "{spacing.md}"
  evidence-panel:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
  state-marker:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-success}"
    rounded: "{rounded.sm}"
  focus-ring:
    backgroundColor: "{colors.focus}"
    height: 3px
---

## Overview

The route console makes one operational decision visible: resume the active
design route and decide whether its evidence is ready for gallery promotion.
The visual idea is a **field notebook with a route spine**—warm paper, a dark
teal working rail, and a rust mark for the next action. It fits a persistent
System because history is legible without becoming a dashboard of metrics.

The first viewport names the active route, shows the current status, and gives
one primary action: `Resume active route`. The gallery, source decision, and
proof relation remain visible below it. A quiet state lab makes loading,
success, error, empty, permission, and offline behavior inspectable.

## Colors

Warm paper is the page field; white paper marks durable evidence surfaces.
Deep teal is reserved for the working rail and the primary action. Rust marks
the next decision and visible focus. Green means a checked proof, not a generic
positive decoration. Red is reserved for a blocked route or failed review.

## Typography

The display face is tight and editorial for the route name. Body text stays
plain and readable. Monospace labels identify route IDs, timestamps, and
evidence paths so operational facts do not masquerade as prose.

## Layout

The page uses a 1200px maximum frame. The first viewport is a two-part route
header: an open text field on the left and a compact status ledger on the
right. Below it, the active brief gets the widest column while proof and the
source decision form a narrow reading rail. The gallery uses a four-column
index that collapses to two columns and then one. At mobile widths the status
rail follows the action, and every important link remains in document flow.

## Elevation & Depth

Evidence surfaces use a 1px warm border and a short, soft shadow only where a
surface needs separation from the paper field. The working rail is flat. The
route spine is a 1px rule with a small rust marker; depth comes from alignment
and rhythm rather than floating cards.

## Shapes

Panels use a restrained 18px radius; controls use 6–12px radii. The active
marker is circular, while route cards stay rectangular. Avoid pills except for
short state labels whose color and text both carry meaning.

## Components

- **Route header:** H1, concise job statement, `Resume active route`, and a
  status panel. The button has hover, pressed, visible focus, loading, and
  success behavior.
- **Brief and evidence panels:** Real route IDs, dates, paths, and decisions;
  no invented customer metrics. Empty, failed, and recovered relations are
  shown as useful copy rather than hidden states.
- **Gallery index:** Four durable examples with a clear `Open preview` action.
  Cards have hover, active, and keyboard-visible focus states.
- **State lab:** A keyboard-operable set of success, error, empty, permission,
  and offline fixtures. The message is announced in a polite live region and
  does not pretend a fixture is live customer truth.
- **Responsive navigation:** Skip link, semantic header/nav/main/section
  landmarks, labels, strong focus ring, and a reduced-motion media query.

## Do's and Don'ts

- Do lead with the current route and the next decision.
- Do show evidence paths and honest state language.
- Do use spacing to distinguish active work, history, and curation.
- Do keep source adapters local, optional, and traceable.
- Don't turn the workspace into a generic analytics dashboard.
- Don't hide the failed or offline state behind a spinner.
- Don't make the gallery a second ledger or the external sources a default UI
  kit.
