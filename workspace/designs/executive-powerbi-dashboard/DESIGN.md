---
version: alpha
name: Common Table margin pulse
description: A weekly executive Power BI dashboard organized around one margin-recovery decision.
colors:
  primary: "#273f32"
  on-primary: "#ffffff"
  background: "#f1eee5"
  surface: "#fffdf8"
  border: "#d3cdbf"
  on-surface: "#232720"
  on-surface-muted: "#687066"
  accent: "#d5673f"
  on-accent: "#ffffff"
  success: "#417452"
  on-success: "#ffffff"
  error: "#aa3f36"
  focus: "#d5673f"
typography:
  display:
    fontFamily: ui-sans-serif, system-ui, sans-serif
    fontSize: 44px
    fontWeight: 760
    lineHeight: 1
    letterSpacing: -0.04em
  headline:
    fontFamily: ui-sans-serif, system-ui, sans-serif
    fontSize: 24px
    fontWeight: 720
    lineHeight: 1.15
    letterSpacing: -0.02em
  body:
    fontFamily: ui-sans-serif, system-ui, sans-serif
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0em
  label:
    fontFamily: ui-monospace, monospace
    fontSize: 11px
    fontWeight: 650
    lineHeight: 1.2
    letterSpacing: 0.05em
rounded:
  sm: 4px
  md: 8px
  lg: 16px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 36px
  xxl: 52px
components:
  page:
    backgroundColor: "{colors.background}"
    textColor: "{colors.on-surface}"
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
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

A 16:9 executive view that starts with the decision, then shows one margin
story and the account/product evidence beneath it. The signature element is a
plain-language decision strip that combines gap, cause, and owner. Avoid a
gallery of unrelated charts, traffic-light decoration, and context-free KPIs.

## Portable direction and ownership

This `DESIGN.md` is the canonical, portable visual direction for the fictional
Common Table dashboard and its slide-ready 16:9 composition. The HTML preview,
token exports, and any report assets are optional companions and never replace
this file.

- **Scope and non-goals:** ADS owns report hierarchy, composition, typography,
  color, visual voice, and reusable visual assets. The receiving analytics
  Project owns data modeling, calculations, row-level security, refresh, report
  implementation, and distribution after acceptance.
- **Review, revision, and acceptance:** Revision `alpha` has ADS Review `PASS`.
  A cross-owner dashboard or slide snapshot requires explicit acceptance in
  `HANDOFF.md`; later directions require a new revision and re-acceptance.
- **Known limitations:** The business and measures are fictional. The preview
  is neither a Power BI file nor a live or production-ready data model, and it
  does not prove projection hardware or tenant accessibility.

## Colors

Warm neutral pages reduce projection glare. Deep green structures the report,
orange marks an actionable negative variance, green confirms on-target values,
and red is reserved for failed refresh or genuine critical variance.

## Typography

Use compact sans-serif hierarchy and tabular figures. KPI values are large but
never compete with the decision statement.

## Layout

Use a 16:9 canvas with a header/filter rail, four compact KPIs, one dominant
variance chart, one account table, and a right-side decision panel. At narrow
widths, place the decision panel first and allow the table to scroll.

## Elevation & Depth

Surface contrast and one-pixel dividers define regions. Avoid shadows inside
the report canvas.

## Shapes

Rectangular report regions with 4–16px radii. Data bars have square ends so
length remains easy to compare.

## Components

Filters show selection and clear actions. Visuals expose titles and summaries
in reading order. Required states cover loading, no selection, no data, stale
data, refresh failure, and row-level-security denial.

## Do's and Don'ts

Lead with the decision, compare against a named target, show units and freshness,
and put an owner next to the action. Do not use gauges, unexplained red/green,
decorative donuts, truncated account labels, or more precision than the decision
needs.
