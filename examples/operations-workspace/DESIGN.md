---
version: alpha
name: Harborlight dispatch
description: A decision-first operations workspace for dispatchers coordinating repair jobs and blockers.
colors:
  primary: "#123e4a"
  on-primary: "#f6fbfc"
  background: "#e8eeef"
  surface: "#f8fbfb"
  border: "#c5d0d2"
  on-surface: "#17272b"
  on-surface-muted: "#5d6e72"
  accent: "#dd6b3d"
  on-accent: "#ffffff"
  success: "#2f7658"
  on-success: "#ffffff"
  error: "#b33f38"
  focus: "#dd6b3d"
typography:
  display:
    fontFamily: ui-sans-serif, system-ui, sans-serif
    fontSize: 48px
    fontWeight: 750
    lineHeight: 1.02
    letterSpacing: -0.04em
  headline:
    fontFamily: ui-sans-serif, system-ui, sans-serif
    fontSize: 28px
    fontWeight: 720
    lineHeight: 1.15
    letterSpacing: -0.025em
  body:
    fontFamily: ui-sans-serif, system-ui, sans-serif
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0em
  label:
    fontFamily: ui-monospace, monospace
    fontSize: 12px
    fontWeight: 650
    lineHeight: 1.2
    letterSpacing: 0.04em
rounded:
  sm: 6px
  md: 12px
  lg: 18px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 36px
  xxl: 56px
components:
  page:
    backgroundColor: "{colors.background}"
    textColor: "{colors.on-surface}"
  button-primary:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: "{spacing.md}"
  panel:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
  status-success:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-success}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
  focus-ring:
    backgroundColor: "{colors.focus}"
    height: 3px
---

## Overview

A calm daily control surface organized around attention, not navigation. The
signature is a narrow dispatch rail above a work table and a dedicated blocker
panel that keeps ownership visible. Avoid a permanent left sidebar, a wall of
equal KPI cards, and status conveyed by color alone.

## Colors

Cool harbor neutrals reduce glare during long shifts. Deep teal owns primary
structure, orange means attention or action, green means confirmed, and red is
reserved for actual failure or overdue work.

## Typography

Compact sans-serif labels support scanning. Tabular figures align times and
counts. Large type appears only in the attention summary.

## Layout

Desktop uses a full-width top bar, a three-part dispatch rail, and a 9/3 split
between work table and blockers. Below 820px, the table becomes prioritized job
cards and blockers appear immediately after the attention summary.

## Elevation & Depth

Use surface contrast and hairline borders. Only the active blocker drawer lifts
with a shadow.

## Shapes

Restrained 6–18px radii. Status lozenges are compact labels with text and an
icon, not decorative pills.

## Components

Rows expose a clear action on focus and hover. Filters announce result counts.
The workspace includes shaped skeletons, empty and no-match messages,
permission denial, stale-data warning, inline save error, saved confirmation,
and an offline draft state.

## Do's and Don'ts

Prioritize overdue and blocked work, show owners next to problems, and keep
actions reversible. Do not use unexplained color dots, hidden row menus for the
main action, a generic sidebar, or a dashboard full of vanity metrics.
