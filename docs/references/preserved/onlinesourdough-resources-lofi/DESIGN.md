---
version: alpha
name: resources.onlinesourdough Course Library
description: A warm, folder-first library for one paid Blueprint, its free companions, and the working kits that turn one business constraint into an owned result.
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
  free: "#3b6f55"
  paid: "#7b4d26"
  dark-background: "#18120e"
  dark-surface: "#221813"
  dark-surface-soft: "#2a1e17"
  dark-border: "#3c2b21"
  dark-border-strong: "#69462d"
  dark-on-surface: "#fff2df"
  dark-on-surface-muted: "#c6ad94"
typography:
  display:
    fontFamily: Geist Pixel, Geist Mono, monospace
    fontSize: 54px
    fontWeight: 400
    lineHeight: 1.02
    letterSpacing: -0.03em
  headline:
    fontFamily: Geist Sans, Arial, Helvetica Neue, ui-sans-serif, system-ui, sans-serif
    fontSize: 22px
    fontWeight: 680
    lineHeight: 1.1
    letterSpacing: -0.025em
  body:
    fontFamily: Geist Sans, Arial, Helvetica Neue, ui-sans-serif, system-ui, sans-serif
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label:
    fontFamily: Geist Mono, SFMono-Regular, Consolas, Liberation Mono, monospace
    fontSize: 10px
    fontWeight: 550
    lineHeight: 1.3
    letterSpacing: 0.05em
  wordmark:
    fontFamily: Geist Pixel, Geist Mono, monospace
    fontSize: 17px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: -0.025em
rounded:
  control: 8px
  folder: 12px
  panel: 12px
  shelf: 26px
  full: 9999px
spacing:
  xs: 4px
  sm: 8px
  md: 14px
  lg: 22px
  xl: 34px
  section: 58px
  container: 1120px
  sidebar: 240px
  topbar: 52px
components:
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
  topbar-control:
    backgroundColor: "{colors.background}"
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
    textColor: "{colors.on-surface}"
    rounded: "{rounded.shelf}"
    padding: "{spacing.sm}"
  resource-row:
    backgroundColor: "{colors.background}"
    textColor: "{colors.on-surface}"
    padding: "{spacing.md}"
  orientation-panel:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    rounded: "{rounded.panel}"
    padding: "{spacing.lg}"
  primary-action:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.control}"
    padding: "{spacing.sm}"
  status-free:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.free}"
    typography: "{typography.label}"
  status-paid:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.paid}"
    typography: "{typography.label}"
  divider:
    backgroundColor: "{colors.border}"
    height: 1px
  divider-strong:
    backgroundColor: "{colors.border-strong}"
    height: 1px
  accent-rule:
    backgroundColor: "{colors.accent}"
    height: 2px
  focus-ring:
    backgroundColor: "{colors.focus}"
    size: 2px
  brand-wordmark:
    backgroundColor: "{colors.background}"
    textColor: "{colors.on-surface}"
    typography: "{typography.wordmark}"
  dark-page:
    backgroundColor: "{colors.dark-background}"
    textColor: "{colors.dark-on-surface}"
  dark-surface:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.dark-on-surface}"
  dark-surface-soft:
    backgroundColor: "{colors.dark-surface-soft}"
    textColor: "{colors.dark-on-surface-muted}"
  dark-divider:
    backgroundColor: "{colors.dark-border}"
    height: 1px
  dark-divider-strong:
    backgroundColor: "{colors.dark-border-strong}"
    height: 1px
---

# resources.onlinesourdough Course Library

## Overview

### Design read

Resources is a paid content and course library, not a marketplace of unrelated templates. The visible promise is practical: take one current business constraint through eight owned steps, with free companions for orientation and Kits for the work itself. The preview keeps the product close to [onlinesourdough.com](https://onlinesourdough.com): warm cream and brown, Geist Pixel/Sans/Mono, quiet rules, compact spacing, pixel-led icons, and restrained paper depth.

### Product brief

- **Product shape:** A folder-first library for a sequential paid Blueprint, free video companions, and paid working Kits.
- **Primary workflow:** Start with a useful free orientation, open a stage folder, read the next step, and turn the result into something the owner can operate and recover.
- **Access model:** Free companions are open. Blueprint lessons and Kits show a safe summary and one paid access action when locked.
- **Audience:** Founders and small teams who need a clearer business result before they add more software or automation.
- **Constraint:** Keep 01–08 understandable at a glance without making Home a dashboard or a sales page.
- **Avoid:** Multicolor marble folders, generic marketing blocks, nested decorative cards, emoji-heavy navigation, and the `resources.online` shorthand.

### Composition fingerprint

- **Page rhythm:** A compact topbar, a short identity line, one four-folder shelf, one VSL-style orientation block, then a flat New & updated list. Stage and reader pages use a narrow editorial header followed by ruled rows.
- **First viewport:** On desktop, Home loads with the sidebar collapsed. The first view shows `resources.onlinesourdough`, a short Pixel heading, four monochrome warm folders, and the beginning of the useful orientation block.
- **Content density:** Quiet working-library density at level 6. Navigation is denser than the reading surface; rows carry real dates, access, durations, and outcomes.
- **Typography contrast:** Geist Pixel carries the full product wordmark and one short page statement. Geist Sans carries titles and explanations. Geist Mono carries numbers, routes, access, dates, and shortcuts.
- **Image role:** A small, warm-monochrome treatment of the existing archive-folder asset sits inside the orientation video's printed frame. It is a product cue, not a hero illustration or a folder-card replacement.
- **Shape language:** Thin warm rules, square-ish controls, flat rows, paper indexes, one shared lower shelf, and warm folder fronts. Cards are used only when they represent a real physical folder or the orientation video.
- **Motion character:** Clicking a folder changes route and opens the rich navigation. Hover or keyboard focus lifts only the paper index by 18 pixels; the folder front and shelf stay still. Sidebar and theme transitions are short and quiet.
- **Signature moment:** Four stages of one Blueprint sit together as a monochrome archive shelf. The index behind each folder exposes its two numbered lessons without adding a second navigation metaphor.
- **Anti-pattern:** Do not build a colorful course dashboard, a Notion clone, a generic hero with feature cards, or a library that hides the eight-step sequence behind an abstract category system.

### Reference translation

- **Live `onlinesourdough` application and `../onlinesourdough` repo:** Learn the warm token family, fine rules, natural spacing, Geist hierarchy, and quiet light/dark theme. Do not copy its public offer-page composition, exact copy, or implementation code.
- **Approved `examples/onlinesourdough-menu-freedom-lofi`:** Learn the open field, warm paper card treatment, pixel icon scale, typography contrast, and restrained hover feedback. Do not reuse its four-offer story, book proportions, hero, footer, or images as a new shell.
- **Current `../onlinesourdough-resources` application:** Learn the real route vocabulary, 01–08 Blueprint structure, search, favorites, tasks, access states, and sidebar collapse behavior. Do not change that application or copy its CSS; this file describes a static design preview only.
- **Committed Resources baseline at `8d81ea2`:** Learn the useful folder paper lift, flat resource rows, and reader states. Do not preserve the later multicolor/marble folder direction, overloaded Home rail, or `resources.online` identity.
- **Existing archive-folder asset in this example:** Learn its immediate file/archive signal and pixel density. It is filtered into a warm monochrome video frame; no new brand mark, logo, screenshot, or proprietary UI is copied.

## Colors

Use the same warm cream, paper, brown, crust, and muted-blue focus family as onlinesourdough.com. The folder front is a single warm brown in both themes; folders are differentiated by labels and the paper index, not by a rainbow palette. Free and Paid are semantic mono text only. The focus blue is reserved for keyboard focus and the orientation guidance.

The dark theme remaps the page onto warm brown-black surfaces while retaining the same line hierarchy. The archive image is filtered rather than inverted so it remains a quiet printed cue in both themes.

## Typography

Self-host Geist Sans, Geist Mono, and Geist Pixel Square from the existing local font bundle. Use the full `resources.onlinesourdough` Pixel wordmark in the sidebar and topbar-adjacent identity. Use Pixel for the short Home statement and one stage/reader heading when needed; keep functional labels, lesson titles, and orientation copy in Sans. Mono is reserved for stage numbers, access, dates, durations, route labels, and keyboard shortcuts.

Use sentence case. Copy names the business constraint, the smallest complete result, ownership, operation, recovery, and business freedom. Sourdough language may add warmth but never replaces the action or outcome.

## Layout

### Application shell

Desktop uses a 240-pixel sticky sidebar, a 52-pixel sticky topbar, and a 1120-pixel content measure with 32-pixel minimum side breathing room. Home starts at `sidebar-collapsed`; clicking a folder or a library route opens the sidebar. The topbar controls sit directly at the left/sidebar boundary: sidebar toggle, browser back, and browser forward. Search, Log in, Favorite, and Theme sit on the right. The topbar does not repeat the current page title.

Below 900 pixels, the sidebar is off-canvas and inert while closed. Folder navigation opens it after a route change so the user can see the Blueprint tree. Returning Home collapses it again. Below 560 pixels, Search becomes an icon-only topbar control, while the full label remains in the sidebar.

### Home folder view

Home follows this order:

1. Full `resources.onlinesourdough` eyebrow, a compact Pixel statement, and one sentence explaining the paid library.
2. Four compact stage folders in one row on wide desktop, two columns below 980 pixels, and one column below 360 pixels.
3. One orientation block with a product-specific video frame, a concrete outcome, a visible `FREE COMPANION` cue, a visible `PAID BLUEPRINT` cue, and one clear `Watch the orientation` action.
4. `New & updated`, with up to four flat rows showing a real date, title, summary, duration, and Free/Paid state.

The Home folders are stages of one Blueprint, not Start, Free, Blueprint, and Kits. Free companions and Kits remain first-class sidebar destinations. Do not add a metrics panel, progress rail, pricing strip, or generic footer pitch to Home.

### Blueprint information architecture

| Stage folder                 | Blueprint steps                                                       | Purpose                                                                     |
| ---------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `01 Understand the business` | `01 Find the current constraint` and `02 Map the business system`     | Name the bottleneck, people, process, and desired freedom.                  |
| `02 Choose the intervention` | `03 Decide what should change` and `04 Place ownership`               | Decide what to eliminate, automate, delegate, or keep, then name the owner. |
| `03 Make the result`         | `05 Specify the smallest complete result` and `06 Build and prove it` | Set boundaries and evidence, then make one complete feedback loop.          |
| `04 Own the system`          | `07 Review and simplify` and `08 Ship, operate, and recover`          | Review correctness, hand over authority, and preserve a recovery path.      |

### Sidebar tree

The rich sidebar contains Search, Home, My tasks, an optional Favorites section, then the Pages tree: Blueprint with the four stage folders and their two lesson links, Free companions, and Kits. Account and Need help? stay at the bottom. Disclosure controls are separate from navigable page links. Stage rows use the same 01–04 numbers as Home; lesson rows use 01–08. No task preview is injected into the narrow sidebar.

### Stage, reader, and access pages

Stage pages show their purpose and two ordered lesson rows. Blueprint shows all eight steps grouped by stage. Free companions and Kits are flat resource lists. Reader pages show breadcrumb, access, duration, title, summary, one content section, and related links. Locked paid lessons show only an approved safe summary and one access panel; the UI is not the security boundary.

My tasks is a focused progress page with a local completion state and one next action. Account shows login and side-by-side Monthly/Annual access choices at larger widths without fabricated prices. Help shows a short support route. All route changes use browser history and preserve direct hash links in the static preview.

### Responsive behavior

Use `minmax(0, 1fr)` for all content grids. Keep two folder columns at 390 pixels, reduce folder copy before switching to one column below 360 pixels, and stack the orientation block below 760 pixels. Reader surfaces remain one column below 760 pixels. Text wraps intentionally, focus states stay visible, and no viewport may overflow horizontally.

## Elevation & Depth

The shell, sidebar, topbar, list rows, and reader surface stay flat. Paper indexes use one short warm shadow and rise 18 pixels on desktop or 12 pixels on compact screens. The shared shelf uses a one-pixel border, a quiet paper mix, and a slight blur; it never rises with the folder. The orientation video frame uses one shallow paper shadow. Avoid black shadows in light mode and glows in either theme.

## Shapes

Use eight-pixel controls, twelve-pixel folder fronts and orientation frames, and 26-pixel lower shelf corners. Full pills are reserved for compact shortcut keys; Login is a quiet text control. Rows are unboxed and divided by one-pixel rules. Folder tabs remain angular enough to read as folders without turning the page into a file-manager imitation.

## Components

### Brand lockup

Render `resources.onlinesourdough` as one complete Pixel wordmark. Pair it with a small code-native archive mark made from warm square modules. Do not shorten the identity to `resources.online`, split it into a slash lockup, or use the folder raster as the logo.

### Blueprint stage folders

Each folder is a real route into its stage page. The front shows stage number, short title, and purpose; the paper index shows both lesson numbers and titles. On hover or `:focus-visible`, only the paper rises. The front remains one monochrome warm tone and the shelf stays still. Reduced motion removes the translation.

### Orientation block

Use the existing archive-folder image as a small warm-monochrome visual inside a printed video frame with a clear play affordance and duration. The copy must state a concrete outcome: name one repeating owner task, trace its handoffs, and choose the next Blueprint step. Show both free orientation and paid Blueprint cues, then provide exactly one primary action.

### Sidebar tree and topbar

Use compact pixel-line icons for Search, Home, My tasks, Blueprint, Account, Help, Back, Forward, Favorite, and Theme. Disclosure buttons have accessible names and `aria-expanded`; parent links still navigate. The full sidebar opens for every non-Home route and collapses when Home is selected.

### Resource rows and readers

Rows carry date, title, summary, duration, and access without decorative cards. Free/Paid remains textual and semantic. Reader pages keep a narrow measure and one content callout at most. Related links use the same ruled row treatment.

### Interaction rules

- Keyboard focus uses a two-pixel muted-blue ring with a three-pixel offset.
- Folder paper rises; folder fronts and shelf stay still.
- Row hover changes only background and small horizontal padding.
- Folder links, sidebar links, orientation action, browser back, and browser forward update history.
- Theme persists in local storage and maps the complete light/dark token system.
- Search opens with `Command-K` or `Control-K`, closes with Escape, and restores focus to its trigger.
- Reduced motion removes translation and nonessential transitions.
- No interaction relies on hover, color, or icon alone.

## Do's and Don'ts

- Do make Home a folder view and let the four folders be the clearest route into 01–08.
- Do load Home with the desktop sidebar collapsed and open the richer sidebar after a folder route.
- Do use the exact full identity `resources.onlinesourdough`.
- Do keep the onlinesourdough warm tokens, Geist family, fine lines, pixel icons, and quiet card treatment visible.
- Do keep the orientation block useful enough to choose the next step, not a vague marketing hero.
- Do use real invented titles, dates, durations, access states, and task progress.
- Do preserve search, favorites, tasks, theme, history, reader, and access states in the preview.
- Do keep the monochrome warm archive/folder treatment coherent across all four stages.
- Don't use multicolor or marble folder fronts.
- Don't shorten the brand to `resources.online`.
- Don't copy the onlinesourdough offer menu's hero, book layout, exact copy, or images.
- Don't build a Notion clone, card-heavy course dashboard, category maze, or generic VSL landing page.
- Don't put a second task list, Blueprint rail, metrics dashboard, or pricing pitch on Home.
- Don't treat the UI as an access-control boundary or expose locked private content.

## Preview Coverage

`index.html` proves the collapsed desktop Home folder view, full brand identity, monochrome warm archive folders, paper-index lift, 01–08 stage routing, richer expanded sidebar, Search, Home, My tasks, optional Favorites, Blueprint tree, Free companions, Kits, Account, Help, one useful orientation video frame with Free/Paid cues, New & updated rows, reader/access states, history controls, theme switching, visible focus, reduced motion, and responsive light/dark layouts.

## Asset Notes

- `assets/resources-folder-transparent.png` is the existing original archive-folder pixel asset in this example. The preview filters it into a warm-monochrome printed frame and does not use it as a logo or as a multicolor folder card.
- `assets/fonts/` contains the existing self-hosted Geist Sans, Geist Mono, Geist Pixel Square, and license from Geist 1.7.0.
- No new assets, external image URLs, third-party screenshots, or proprietary UI fragments are introduced by this reset.

## Implementation Notes

- This artifact is design-only; no files in `../onlinesourdough` or `../onlinesourdough-resources` were changed.
- The static preview uses hash routes and fictional catalog data to demonstrate the product model without changing the Resources application domain or integrations.
- Keep the approved `DESIGN.md` as the portable source of truth. Map its tokens into the application rather than creating a second token system.
