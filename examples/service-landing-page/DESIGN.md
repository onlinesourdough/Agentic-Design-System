---
version: alpha
name: Plainwork Studio
description: A specific, editorial landing page for an operations-mapping service aimed at small service-business owners.
colors:
  primary: "#244b3f"
  on-primary: "#fffdf7"
  background: "#f3eee4"
  surface: "#fffdf7"
  border: "#cfc7b8"
  on-surface: "#25231e"
  on-surface-muted: "#6c665b"
  accent: "#e2542d"
  on-accent: "#ffffff"
  success: "#39734f"
  on-success: "#ffffff"
  error: "#ad3b32"
  focus: "#e2542d"
typography:
  display:
    fontFamily: ui-serif, Georgia, serif
    fontSize: 72px
    fontWeight: 600
    lineHeight: 0.98
    letterSpacing: -0.04em
  headline:
    fontFamily: ui-sans-serif, system-ui, sans-serif
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.12
    letterSpacing: -0.02em
  body:
    fontFamily: ui-sans-serif, system-ui, sans-serif
    fontSize: 17px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0em
  label:
    fontFamily: ui-monospace, monospace
    fontSize: 12px
    fontWeight: 650
    lineHeight: 1.2
    letterSpacing: 0.06em
rounded:
  sm: 4px
  md: 10px
  lg: 20px
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

An editorial service page built around one argument: map the work before adding
automation. A cream paper field, dark-green annotations, and a single orange
action feel practical rather than technological. The signature moment is the
annotated operating map beside the hero. Avoid generic feature cards, fake
logos, stock team photos, and claims without evidence.

## Portable direction and ownership

This `DESIGN.md` is the canonical, portable visual direction for the fictional
Plainwork Studio landing page. Its preview, exported tokens, and any future
assets are optional companions; none replaces this human-readable file.

- **Scope and non-goals:** ADS owns visual direction, visual voice, brand
  expression, composition, and interaction direction. The receiving Project
  owns implementation, while the offer owner owns editorial claims and
  publication; this direction does not supply testimonials or operating code.
- **Review, revision, and acceptance:** Revision `alpha` has ADS Review `PASS`.
  A cross-owner copy remains pending until the implementation owner explicitly
  accepts its `HANDOFF.md`; later revisions require a new snapshot.
- **Known limitations:** The company, offer, and booking flow are fictional.
  The preview proves responsive and state direction, not a connected booking
  service, conversion claim, or production accessibility audit.

## Colors

Cream carries the page, paper-white lifts working artifacts, green marks
structure, and orange is reserved for the booking action and keyboard focus.

## Typography

Serif display type gives the promise a human editorial voice. Sans-serif body
copy stays plain and readable. Monospace labels make working notes feel like
real annotations rather than decorative badges.

## Layout

Use a 12-column, 1180px desktop grid with an asymmetric seven/five hero. Below
760px, everything becomes one column and the annotated map follows the CTA.
Sections use generous but optically varied spacing instead of identical cards.

## Elevation & Depth

Use borders, paper overlap, and one tinted shadow on the map. Do not place a
shadow on every section.

## Shapes

Mostly square editorial blocks with restrained 10–20px curves. Annotation
lines and numbered circles provide the recognizable shape language.

## Components

The CTA darkens on hover, depresses on active, and has an orange offset focus
ring. The booking form shows inline validation, a text-based progress state,
specific success confirmation, and a recoverable service-error message.

## Do's and Don'ts

Use one action, specific deliverables, working artifacts, and honest fit
guidance. Do not use competing hero CTAs, a three-card feature row, AI-gradient
decoration, fabricated proof, or vague transformation language.
