---
version: alpha
name: Crypto Club Home
description: Calm dark member dashboard for home.cryptoclub.dk, connecting AI Matthæus, Portfolio, Classroom, Chat, and the wider Crypto Club ecosystem.
colors:
  primary: "#123F84"
  primary-strong: "#0A2F6D"
  primary-soft: "#10223D"
  on-primary: "#FFFFFF"
  background: "#0D0D0D"
  sidebar: "#111111"
  surface: "#171717"
  surface-raised: "#1D1D1D"
  border: "#2A2A2A"
  on-surface: "#F3F3F3"
  on-surface-muted: "#949494"
  success: "#55C69B"
  warning: "#D9AC59"
  error: "#E8757D"
  focus: "#5B91DF"
typography:
  display:
    fontFamily: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif
    fontSize: 35px
    fontWeight: 590
    lineHeight: 1.12
    letterSpacing: -0.035em
  headline:
    fontFamily: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif
    fontSize: 15px
    fontWeight: 590
    lineHeight: 1.3
    letterSpacing: -0.015em
  body:
    fontFamily: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0em
  label:
    fontFamily: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace
    fontSize: 10px
    fontWeight: 650
    lineHeight: 1.25
    letterSpacing: 0.095em
rounded:
  control: 9px
  card: 14px
  full: 9999px
spacing:
  xs: 5px
  sm: 8px
  md: 12px
  lg: 19px
  xl: 26px
  section: 36px
  container: 1240px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    rounded: "{rounded.control}"
    padding: "{spacing.md}"
    height: 34px
  button-primary-hover:
    backgroundColor: "{colors.primary-strong}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    rounded: "{rounded.control}"
  button-secondary:
    backgroundColor: "{colors.primary-soft}"
    textColor: "{colors.on-surface}"
    typography: "{typography.label}"
    rounded: "{rounded.control}"
  field-default:
    backgroundColor: "{colors.surface-raised}"
    textColor: "{colors.on-surface}"
    typography: "{typography.body}"
    rounded: "{rounded.control}"
    padding: "{spacing.md}"
    height: 38px
  card-default:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    rounded: "{rounded.card}"
    padding: "{spacing.lg}"
  sidebar-default:
    backgroundColor: "{colors.sidebar}"
    textColor: "{colors.on-surface-muted}"
    padding: "{spacing.md}"
  status-success:
    backgroundColor: "{colors.success}"
    textColor: "{colors.background}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm}"
  status-warning:
    backgroundColor: "{colors.warning}"
    textColor: "{colors.background}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm}"
  divider:
    backgroundColor: "{colors.border}"
    height: 1px
  focus-ring:
    backgroundColor: "{colors.focus}"
    size: 2px
---

# Crypto Club Home

## Overview

Crypto Club Home is the member's orientation layer at `home.cryptoclub.dk`. It does not replace the specialist products. It gives members a fast read on what matters now and creates a coherent path into AI Matthæus, Portfolio, Classroom, Chat, and future subdomain apps.

### Product brief

- **Audience:** Crypto Club members who move between AI guidance, portfolio context, education, community, and automated market signals.
- **Primary workflow:** Arrive on Home → understand today's state → continue one relevant task → open the specialist software.
- **Core message:** One composed place to continue, without crypto-casino noise.
- **Platform:** Responsive web. Desktop is a dense working overview; mobile preserves priority and stacks the same modules.

### Composition fingerprint

- **Page rhythm:** A narrow persistent sidebar supports orientation. The content canvas moves from greeting, to large software launchers, to an asymmetric intelligence grid, then to community activity.
- **First viewport:** Greeting and three direct ecosystem entry points appear first. Market context begins at the fold; no promotional hero competes with work.
- **Content density:** Compact but breathable. One large market panel is paired with two smaller status panels; the dashboard avoids repeated same-size cards.
- **Typography contrast:** Quiet system sans throughout. Large display type appears only in the personal greeting and primary portfolio value. Uppercase micro-labels identify information layers.
- **Image role:** The approved round Crypto Club logo is the only raster image. Data and product meaning are expressed with code-native charts, icons, and typography.
- **Shape language:** Mostly flat dark planes, 1px neutral borders, 9px controls, and 14px panels. The AI launcher gets a restrained navy field to mark it as the primary external product.
- **Motion character:** Fast 150–180ms hover and drawer transitions. Charts do not animate. Dialog behavior is functional and subdued.
- **Signature moment:** “Fortsæt hvor du slap” treats the ecosystem as three destinations with a clear primary AI launcher, then carries the same destinations into the app switcher.
- **Anti-pattern:** Neon coin decoration, gradient-heavy crypto styling, generic KPI tiles, nested decorative cards, marketing hero stacks, leaderboard gamification, and charts with unexplained numbers.

### Reference translation

- **Provided Tesla Reports screenshot:** Learn compact sidebar proportions, information density, and the asymmetry between smaller summaries and one dominant data panel. Do not copy Tesla branding, page chrome, report labels, chart geometry, section order, or card styling.
- **Existing Crypto Club / LibreChat implementation:** Learn near-black chrome, sparse navigation, round logo treatment, restrained control styling, and the existing navy brand accent. Do not copy the chat transcript layout into Home.
- **Existing workbench example:** Reuse only approved assets, colors, product names, known routes, and fictional Crypto Club-specific content. The previous HTML composition is not a structural reference.

### Product map

| Layer               | Destination                                                     | Home responsibility                                                                                                       |
| ------------------- | --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| Home                | `home.cryptoclub.dk`                                            | Orientation, cross-product summaries, routing                                                                             |
| AI Matthæus         | `app.cryptoclub.dk`                                             | Primary external AI workflow with AI Matthæus and specialist agents                                                       |
| Market Intelligence | `/intelligence`                                                 | Structured access to heatmaps, AI scanner results, algorithm signals, and backtests currently distributed through Discord |
| Portfolio           | `/portfolio` now; later `portfolio.cryptoclub.dk`               | Balance, holdings, allocation, signal context                                                                             |
| Classroom           | `/classroom` and `/lesson` now; later `classroom.cryptoclub.dk` | Course discovery, modules, video lessons, notes, progress, and live sessions                                              |
| Chat                | `/chat` now; later Discord or `chat.cryptoclub.dk`              | Community activity and routing                                                                                            |

## Colors

The interface is intentionally near-black and neutral. Navy is a product accent, not a page wash.

- **Background** `#0D0D0D` creates continuity with the existing LibreChat surface.
- **Sidebar** `#111111`, **surface** `#171717`, and **raised surface** `#1D1D1D` separate layers without shadows.
- **Primary** `#123F84` is a slightly lifted implementation of the existing company navy; `#0A2F6D` remains the pressed/strong state.
- **Success**, **warning**, and **error** appear only with explicit text or semantic context. Color alone never communicates a trading action.
- The approved logo retains its existing `#052B6D` field and is not recolored.

## Typography

- **Display:** Personal greeting and primary total only. Use a moderate 590 weight and tight tracking.
- **Headline:** Section and panel names at 15px. Avoid oversized dashboard headings.
- **Body:** Explanatory copy at 13px with restrained line length.
- **Label:** 10px uppercase sans labels use `typography.label` metrics; mono is reserved for numeric metadata, dates, percentages, and route information in implementation.
- Use system fonts in the static preview so it works offline without external font requests.

## Layout

- Desktop sidebar: 224px fixed/sticky.
- Content canvas: maximum 1240px, centered with 32px side gutters.
- Launch row: one emphasized AI destination plus two equal internal destinations.
- Intelligence grid: approximately 65/35. Market context owns the larger column; portfolio and learning stack in the smaller column.
- Activity aligns below the market panel; the next event aligns below the smaller stack.
- At 1020px the launch row becomes 2 columns with AI full width.
- At 760px the sidebar becomes an off-canvas drawer and all grids stack in priority order.
- At 390px no horizontal scrolling is permitted; tables on secondary pages may scroll within their own region only.

## Elevation & Depth

- Borders and background shifts create hierarchy; regular panels have no drop shadow.
- The primary AI launcher uses a restrained navy tonal field, not glow or glass.
- Only the app-switcher dialog and mobile drawer cast a shadow because they sit above the application plane.

## Shapes

- Controls: 9px radius.
- Panels and launchers: 14px radius.
- Status labels may use full rounding because they communicate compact semantic states.
- The customer logo and profile avatar are circular.
- Avoid nested rounded containers unless the inner boundary represents a real dataset or control group.

## Components

### Sidebar

The sidebar groups Home surfaces separately from external software. The current route uses a neutral lifted field and a blue icon, not a large colored tab. The brand lockup shows only the approved Crypto Club name; no redundant “member portal” subtitle. A compact profile trigger anchors the bottom with a neutral avatar icon, “Test bruger”, and “Inner Circle medlem”. It opens a small menu for profile, settings, support, and logout.

### Ecosystem launchers

Each launcher includes a category, product name, useful current state, icon, and directional arrow. Use “AI Matthæus” consistently as the product name and “AI-assistent & specialister” as supporting context where useful; legacy product naming must not appear in the interface. Specialist destinations use the pattern “AI Matthæus · Portefølje” or “AI Matthæus · Makro”. All launchers use neutral surfaces at rest. The AI launcher receives a navy surface only on hover or keyboard focus rather than remaining permanently blue.

### Market intelligence panel

One panel combines market regime, Fear & Greed context, and a short asset table. It is an orientation surface, not a trading terminal. Signals always include words such as Hold, Follow, or Wait and show a preview-data disclaimer.

### Portfolio summary

Shows one primary total, seven-day change, and a code-native area chart. The complete holdings workflow belongs on the Portfolio surface.

### Learning continuation

Shows one next lesson, duration, and explicit progress. It is designed as a continuation action, not a course catalogue.

### Classroom catalogue and lesson

Classroom follows a two-level learning model. The catalogue uses a restrained course grid with category, duration, lesson count, description, and progress; one larger continuation feature remains the fastest path back into learning. The lesson surface combines a collapsible module rail, a 16:9 video stage, lesson notes, transcript, resources, completion state, and next-lesson navigation. Learn clarity, community, and course discovery from cohort platforms such as Skool, but do not reproduce their card visuals, navigation, branding, or social feed.

### Market Intelligence workspace

Discord is a delivery channel, not the target information architecture. Home shows a compact three-source summary: Heatmaps, AI Market Scanner, and Algo Signals. The dedicated Market Intelligence surface begins with one daily briefing and provides separate tabs for each source. Heatmaps use summary rows with one expandable analysis and chart at a time. The scanner reduces a long bot post into core, approved assets, a collapsed watchlist, conclusion, and model allocation. Algo Signals put the active signal first and keep backtest metrics and charts in expandable reports. Every market surface includes update time, semantic status, and a non-advice disclaimer.

### Activity and next event

Activity uses quiet rows, semantic icons, timestamps, and short descriptions. The next live session uses a single compact date block and calendar action.

### Chat workspace

Chat uses a communication-first split view: searchable channels and direct chats on the left, the active conversation on the right. Channel items combine avatar, type, preview, timestamp, and unread count. The conversation supports a compact header, pinned context, member messages, personal replies, automated signal cards, reactions, and a composer. On mobile the channel list and active conversation become two sliding states with an explicit back action. Learn speed and hierarchy from modern messaging products, but retain Crypto Club colors, typography, icons, and information architecture.

### App switcher

A centered dialog lists Home, AI Matthæus, Market Intelligence, Portfolio, Classroom, Chat, Admin, and Settings. Each destination has its own product-relevant icon and color family; blank icon placeholders are not permitted. It is static in the preview and should become config-driven in production.

### Profile and settings

The profile menu is available from every surface because it is part of the shared shell. The settings page separates profile, preferences, and security. Preview identity is always “Test bruger” with the semantic membership label “Inner Circle medlem”. A neutral person icon is used instead of a generated or real member portrait.

## Do's and Don'ts

- Do prioritize direct links to working software above aggregate metrics.
- Do label fictional or delayed market data clearly.
- Do preserve the near-black LibreChat relationship and existing navy identity.
- Do use original, product-specific Danish copy and realistic member tasks.
- Do keep external destinations visually and semantically distinct from Home routes.
- Don't turn Home into a marketing landing page or a compressed trading terminal.
- Don't use brandless KPI cards, neon gradients, decorative coins, or unexplained financial numbers.
- Don't duplicate portfolio, classroom, or chat workflows that belong in their specialist products.
- Don't infer that a green market value is financial advice; status must remain textual.

## Preview Coverage

| File                | Production route | Coverage                                                                                                                                             |
| ------------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `index.html`        | `/`              | Ecosystem launchers, market intelligence, portfolio trend, learning continuation, activity, next event, app switcher                                 |
| `portfolio.html`    | `/portfolio`     | Holdings, allocation, wallet demo actions, macro and signal context                                                                                  |
| `classroom.html`    | `/classroom`     | Featured continuation, course filters, responsive course grid, progress, weekly learning activity, Inner Circle event                                |
| `lesson.html`       | `/lesson`        | Module navigation, video stage, lesson notes, transcript, resources, completion state, next lesson                                                   |
| `intelligence.html` | `/intelligence`  | Daily briefing, Heatmaps, AI Market Scanner, Algo Signals, expandable charts, scanner watchlist, active signal, backtests                            |
| `chat.html`         | `/chat`          | Searchable channel rail, filters, unread states, pinned context, member threads, signal cards, responsive conversation state, routing to live AI app |
| `settings.html`     | `/settings`      | Profile identity, membership, preferences, notification toggles, security, and shared-shell profile menu                                             |
| `ecosystem.html`    | `/ecosystem`     | Service inventory and technical ownership                                                                                                            |

Mock data in `assets/mock-data.js` is fictional but Crypto Club-specific. It must not be presented as live pricing, portfolio ownership, or financial advice.

## Asset and Implementation Notes

- Approved customer assets: `assets/logo.png` and `assets/favicon-32x32.png`.
- User-provided production research charts are stored under `assets/images/`: five heatmaps and two algorithm backtests. They are resized for the preview and remain visually unchanged beyond optimization.
- Discord screenshots inform content structure and data hierarchy only. Discord chrome, bot avatar, emoji-led formatting, and embeds are not shipped.
- Interface icons and code-native summary charts are original inline SVG; no icon fonts or external requests are used.
- Shared application chrome and interactions live in `assets/app.css` and `assets/app.js`.
- The approved `DESIGN.md` should be copied to the consuming Home repository root.
- The production app switcher belongs in the Home codebase as a config-driven shared feature; it is not a separate service or schema.
