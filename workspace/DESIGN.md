---
version: alpha
name: Replace with product name
description: Replace with one sentence describing the interface and its audience.
colors:
  primary: "#2f5d50"
  on-primary: "#ffffff"
  background: "#f3efe6"
  surface: "#fffdf8"
  border: "#d8d1c3"
  on-surface: "#25241f"
  on-surface-muted: "#666257"
  accent: "#e4572e"
  on-accent: "#ffffff"
  success: "#39734f"
  on-success: "#ffffff"
  error: "#b53a32"
  focus: "#e4572e"
typography:
  display:
    fontFamily: ui-sans-serif, system-ui, sans-serif
    fontSize: 64px
    fontWeight: 720
    lineHeight: 1
    letterSpacing: -0.04em
  headline:
    fontFamily: ui-sans-serif, system-ui, sans-serif
    fontSize: 32px
    fontWeight: 650
    lineHeight: 1.15
    letterSpacing: -0.02em
  body:
    fontFamily: ui-sans-serif, system-ui, sans-serif
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label:
    fontFamily: ui-monospace, monospace
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.04em
rounded:
  sm: 6px
  md: 12px
  lg: 22px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  xxl: 64px
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
  focus-ring:
    backgroundColor: "{colors.focus}"
    height: 3px
---

## Overview

Replace this section with the job, visual idea, responsive behavior, signature moment, and explicit anti-pattern.

## Colors

Describe semantic use rather than adding decorative colors.

## Typography

Describe hierarchy and content density.

## Layout

Describe grid, max-width, spacing, and responsive collapse.

## Elevation & Depth

Describe surfaces, borders, and shadows.

## Shapes

Describe radius and structural geometry.

## Components

Describe required components and their hover, active, focus, loading, empty, error, and success states.

## Do's and Don'ts

State the few choices that preserve this direction and the generic patterns that would weaken it.
