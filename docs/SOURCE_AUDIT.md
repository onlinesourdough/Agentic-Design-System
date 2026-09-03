# UI source audit

Reviewed 2026-08-27 from public repository metadata, license files, README
signals, and the live source pages, with the bounded adaptive-reference and UI
playbook audit added 2026-09-03. These are inputs to a per-brief choice, not a
component catalog or default design language.

| Source                                                                        | Pinned signal and license                                                                                                                                                                                | Accessibility                                                                                                         | Framework fit                                                                                                                    | Maintenance signal                                                                                     | Visual fit and decision                                                                                                                                                                   |
| ----------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [HeroUI](https://github.com/heroui-inc/heroui)                                | `heroui-inc/heroui` commit `1d2164e7b9a60221e39501081f0fe4f6c564bccf`; Apache-2.0 license file `bf4dfe2e9c9943535853e1e3725e6a38c320792f`                                                                | README describes React Aria and WCAG-oriented keyboard, focus, and screen-reader behavior                             | React 19, Next.js, Tailwind CSS v4; not the static HTML runtime used by ADS                                                      | Default branch `v3`, commit dated 2026-08-22; active signal at review                                  | Useful state model for an accessible disclosure. One original, local `heroui-disclosure` CSS adapter is integrated in the curated Resources example; HeroUI is not installed or vendored. |
| [Origin UI / Originkit](https://www.originkit.dev/)                           | `origin-space/originui` resolves to [cosscom/coss](https://github.com/cosscom/coss), commit `19620ae8cae81e30775f2cde03829326cb4916b2`; AGPL-3.0 license file `29ebfa545f5580919a4e884d7014d7a3eb2df762` | Live catalog exposes an interactive component surface, but ADS did not treat that as a sufficient accessibility audit | Live page signals Next/React/Framer and an animated component catalog; poor fit for dependency-free local previews               | Repository updated 2026-08-24; active but source identity/license transition needs re-checking         | Broad animated visual reference, but license and runtime cost make it a source-only reference for this Build; no adapter selected.                                                        |
| [ThreeUI](https://github.com/MengTo/threeui)                                  | `MengTo/threeui` commit `fbc9b3d61b0ef4b2e93b42e4fffa617ca277429b`; MIT license file `b3a5f823a69b4b010f92930ac09e8a776daf65c6`; bundled fonts retain SIL OFL and Three.js remains MIT per README        | Public README describes a live renderer and controls; no reason to assume every effect meets ADS preview needs        | React package plus Three.js assets; some implementation source is entitled/private, so it does not fit the smallest static route | Community sync merge dated 2026-08-23; active signals, but private Pro boundary increases review cost  | Strong source for selective motion or spatial visual research. Not chosen for the Resources route because 3D runtime would obscure its reading job.                                       |
| [DesEngs](https://desengs.com/) / [source](https://github.com/remvze/desengs) | `remvze/desengs` commit `634ff685dfee02419d48891baf2f79160f7959b6`; MIT license file `8221498bff7ddc727a9ee902daa6593569c8effc`                                                                          | The live resource site is a visual reference, not a component accessibility contract                                  | Live page signals Astro 5.16.2, local fonts, and a resource catalogue; not a drop-in ADS adapter                                 | Repository updated 2026-08-24; active resource curation signal                                         | Useful editorial hierarchy and design-engineering curation reference. No code or assets were copied and no adapter was selected.                                                          |
| [OpenPencil](https://github.com/ZSeven-W/openpencil)                          | release `v0.8.4`, peeled commit `c51d7ed41a96068a09127bbc096fee143fce0b22`; observed main `9c810776dab546076a5d9db791a49d9e8048dbd7`; MIT license blob `0dec8929ada31c1b4a60e64410e283a538ca9dfc`        | Editable canvas/export evidence does not replace semantic HTML accessibility review                                   | Optional standalone editor and CLI; no ADS or receiving-runtime dependency, and the minimal portable handoff needs neither       | Signed release assets and checksums were available 2026-08-27; CLI archive needs a desktop or web host | Selected only for the active creative handoff: ADS-owned HTML became editable nodes and one reviewed PNG. No upstream UI, template, code, or asset was copied.                            |

## Adaptive-reference research boundary — 2026-09-03

| Source                                                                                                                                                                                                                                                                                                                                | Revision/date and authority                                                                                                                                | Concrete implication for ADS                                                                                                                                                                           | Adoption boundary                                                                                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Nielsen Norman Group: Mood Boards in UX](https://www.nngroup.com/articles/mood-boards/)                                                                                                                                                                                                                                              | Lillian Yang, 2023-02-26; established UX guidance                                                                                                          | Review existing identity first, separate materially different concepts, and avoid collecting screenshots when the direction is already resolved.                                                       | Supports adaptive routing and bounded exploration; supplies no visual template or asset.                                                                                                                                              |
| [W3C WCAG 2.2: Use of Color](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html), [Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html), [Animation from Interactions](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html)                                                           | Current W3C WAI understanding documents inspected 2026-09-03; primary accessibility guidance                                                               | Status must not rely on color alone; content/action reflow is checked at equivalent 320px with documented surface exceptions; interaction motion needs suppression/control or reduced-motion behavior. | Adopted as observable mechanics, not aesthetic rules. Presentation, video, diagram, data-table, and manipulation-interface exceptions remain explicit.                                                                                |
| [U.S. Copyright Office: What Does Copyright Protect?](https://www.copyright.gov/help/faq/faq-protect.html)                                                                                                                                                                                                                            | Current page inspected 2026-09-03; U.S. primary guidance, not universal legal advice                                                                       | Learn from ideas and methods while preserving rights/provenance and avoiding copied expression or redistributed screenshots.                                                                           | Caller and third-party media remains pointer-only; the compact ADS baseline guidance is original.                                                                                                                                     |
| [Vercel: How our agents build on-brand pages with design.md](https://vercel.com/blog/how-our-agents-build-on-brand-pages-with-design-md) and [Teaching agents product design](https://vercel.com/blog/teaching-agents-product-design-at-vercel)                                                                                       | John Phamous/Vercel, 2026-08-31 and 2026-06-25; current first-party production accounts inspected 2026-09-03                                               | Keep one canonical design file, route by task/surface, use fixed realistic evaluations, separate deterministic mechanics from visual judgment, and treat rendered output plus human feedback as proof. | Supports canonical `DESIGN.md`, multiple surface fixtures, and rendered review; no Vercel prompt, component, style, or stack is copied.                                                                                               |
| Current practitioner posts from [Dianne Alter](https://x.com/dianne_alter/status/2094776531222405527), [Levi](https://x.com/levithefirst/status/2092975925306507619), [Elaya](https://x.com/elayadesigns/status/2093236801079279978), [Tran Mau Tri Tam](https://x.com/tranmautritam/status/2095078647652917329), and issue #10 links | Dated 2026-08-27 through 2026-09-02; primary discovery material for contemporary design-with-agents practice, but practitioner signal rather than standard | Concrete references, positive/avoid context, and progressive instructions can improve agent judgment; catalog posts can reveal a source worth checking.                                                | Preserve author/date/locator/claim. Follow consequential claims to first-party evidence and real rendered proof; do not treat popularity, a list, or an X claim as license, accessibility, maintenance, framework, or reuse approval. |
| [VisualWebBench](https://arxiv.org/abs/2404.05955)                                                                                                                                                                                                                                                                                    | Liu et al., submitted 2024-04-09; older academic corroboration                                                                                             | Screenshot interpretation has historically had OCR/grounding limitations, so extracted signals need confidence and rendered review.                                                                    | Historical corroboration only; not represented as evidence of current frontier-model performance.                                                                                                                                     |

Discovery starts only when a real brief exposes one concrete unresolved role.
The route may select one primary source and one optional adapter after current
first-party license/revision/maintenance/accessibility/framework/reuse
evaluation. A failed or unclear check produces rejection or `blocked`. A
`direct` or `explore` route evaluates no unrelated source entries.

## Issue #10 current brief/source gap

The current `workspace/BRIEF.md` asks for an optional editable native
composition when one is genuinely available. That was one concrete unresolved
role, so the task used `discover` for that role only. The existing OpenPencil
record supplied first-party release, revision, license, availability,
framework, reuse, and accessibility-boundary evidence; no practitioner post
was treated as adoption authority. `workspace/DESIGN.md` selected the optional
adapter, and `workspace/REVIEW.md` records the supervised editable source,
rendered export, limitations, hashes, and PASS. This real task decision does
not make OpenPencil a default or turn the source audit into a catalogue.

## Issue #14 bounded external-playbook overlap audit

Audit target: the current `design-solution`, `review-design`, design contract,
source-decision boundary, and the shipped Resources example. The one material
gap was observable in `examples/onlinesourdough-resources/index.html`: a blank
Account submission created adjacent error text and `aria-invalid="true"`, but
the field had no `aria-describedby` and the error had no ID. The correction
uses one shared helper for the Account and Need help forms; each dynamic error
now receives a stable field-derived ID and each invalid field references it.
The existing repository checker guards that relation, and real browser
interaction supplies the before/after evidence.

| External claim                                                                                                                                           | Existing ADS coverage                                                                                                                                                                                                                | Decision and observable proof                                                                                                                                                                                                             |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Accessible names, native controls, keyboard access, visible focus, and skip navigation                                                                   | Already covered by both internal skills, preview checks, and existing surface fixtures.                                                                                                                                              | **Covered; rejected as duplicate.** No new rule or package.                                                                                                                                                                               |
| Show an error where the action happens and associate it with the invalid field                                                                           | [ibelick/ui-skills `9f140de`](https://github.com/ibelick/ui-skills/tree/9f140de767e6e2d4adc3970eb68d24b3ec896f99), `baseline-ui` and `fixing-accessibility`; repository MIT license blob `cac7c466df604fc44527fd89d9662626bab57354`. | **One material gap; adopted narrowly.** The real Resources form failed before correction and passes after it. Review now requires adjacent, programmatically associated error evidence. Wording and implementation are original ADS work. |
| Do not convey disabled/status state by color alone                                                                                                       | Same pinned `ui-skills` source, corroborated by WCAG 2.2 Use of Color; the active preview already gives all six proof states persistent text labels.                                                                                 | **Already covered; primary-standard reinforcement only.** Forced-color browser inspection kept every state label visible, so no failure or new material-gap claim is manufactured.                                                        |
| Prove narrow-screen reflow and preserve access to content/actions                                                                                        | WCAG 2.2 Reflow and the existing Review requirement that mobile retain content/action access.                                                                                                                                        | **Already covered; primary-standard reinforcement only.** Actual 390px and 320px renders had zero horizontal overflow; surface exceptions remain a standards consideration, not a newly demonstrated ADS failure.                         |
| Suppress or control interaction-triggered motion                                                                                                         | WCAG 2.2 Animation from Interactions; authoring and Review already require reduced-motion behavior, and the active preview already implements it.                                                                                    | **Already covered; primary-standard reinforcement only.** The real reduced-motion browser query was active and collapsed transition duration; no new material-gap claim is made.                                                          |
| Tailwind defaults, Base UI/React Aria/Radix preference, `motion/react`, fixed durations, one accent, no gradients, fixed typography/spacing/radius rules | `ui-skills` `baseline-ui` and [elayadesign/ai-design-skills `1c1e97c`](https://github.com/elayadesign/ai-design-skills/tree/1c1e97cb9878e236552c772092dda7adcdddbcb2), both MIT-licensed repositories.                               | **Rejected: vendor-specific or stylistic-only.** Conflicts with adaptive surfaces and optional runtime boundaries; not an observable universal quality condition.                                                                         |
| Broad _Refactoring UI_-derived rule set                                                                                                                  | [s0xDk/refactoring-ui-skill `4887214`](https://github.com/s0xDk/refactoring-ui-skill/tree/48872143abb0a8feb6d9bf58e222afbd800210b0); repository MIT license, README says that license does not extend to the copyrighted book.       | **Rejected: license/copy boundary plus duplicate/style overlap.** No passage, package, or taxonomy is copied.                                                                                                                             |
| “Improve,” “deslop,” or banned-pattern prompts without a rendered pass/fail condition                                                                    | Current playbook/package framing.                                                                                                                                                                                                    | **Rejected: prompt-only and unverifiable.** Existing Review retains visual judgment; deterministic checks cover only stable observable mechanics.                                                                                         |

No third-party skill, package, component library, MCP server, generator, media,
or runtime was installed or copied for this audit.

## Current design/source trace

This is the smallest source-decision record for the active route. The table
above remains the source/fit owner; this trace resolves three materially
different roles into the current semantic direction and one named example.

### HeroUI

- **Role:** UI/library source
- **Revision/version:** `heroui-inc/heroui` commit `1d2164e7b9a60221e39501081f0fe4f6c564bccf`.
- **License/reuse boundary:** Apache-2.0 license file `bf4dfe2e9c9943535853e1e3725e6a38c320792f`; ADS copied no package or component source.
- **Maintenance/availability:** Default branch `v3`, active commit dated 2026-08-22, publicly available at review.
- **Framework/accessibility fit:** React 19/Next/Tailwind v4 does not fit the static ADS runtime; its React Aria and WCAG-oriented state model is useful accessibility research.
- **Visual reason:** The disclosure state model supports the Resources reading job without imposing HeroUI's visual language.
- **Learned versus copied:** ADS learned interaction states; the local disclosure CSS and behavior are original ADS-owned work.
- **Active use or rejection:** `examples/onlinesourdough-resources/` uses the local disclosure adaptation; the active route console rejects HeroUI as a runtime or default library.
- **DESIGN marker:** §source:heroui-ui-library§

### DesEngs

- **Role:** inspiration/reference source
- **Revision/version:** `remvze/desengs` commit `634ff685dfee02419d48891baf2f79160f7959b6`.
- **License/reuse boundary:** MIT license file `8221498bff7ddc727a9ee902daa6593569c8effc`; no code, copy, layout, or asset was reused.
- **Maintenance/availability:** Public repository updated 2026-08-24 with an active curation signal.
- **Framework/accessibility fit:** Astro resource site is reference-only and supplies no component or accessibility contract to the dependency-free preview.
- **Visual reason:** Its editorial hierarchy is relevant research for making source choices readable without turning ADS into a catalogue.
- **Learned versus copied:** ADS learned the value of concise editorial grouping; the route-spine composition, content, and styling remain original.
- **Active use or rejection:** `workspace/DESIGN.md` uses the editorial principle and rejects DesEngs as an adapter, dependency, or visual template.
- **DESIGN marker:** §source:desengs-inspiration§

### OpenPencil

- **Role:** optional tool adapter
- **Revision/version:** Release `v0.8.4` at peeled commit `c51d7ed41a96068a09127bbc096fee143fce0b22`; upstream main observed at `9c810776dab546076a5d9db791a49d9e8048dbd7`.
- **License/reuse boundary:** MIT license blob `0dec8929ada31c1b4a60e64410e283a538ca9dfc`; temporary verified binaries were not vendored, and no OpenPencil UI/template/asset enters ADS.
- **Maintenance/availability:** The macOS arm64 CLI, DMG, and VSIX plus SHA256
  sums were publicly available on 2026-08-27. The verified VSIX SHA-256 is
  `7ce6cde22f7e8584de2faca0279f6d74438675291c2547a7d99230fc0e629342`;
  its release daemon and web bundle run through the optional ADS-local
  strict-loopback workbench without installing or vendoring them. The CLI
  archive alone remains only a client/version probe.
- **Framework/accessibility fit:** Tool-native editing and export fit an explicitly selected creative route, but accessibility remains owned by semantic `DESIGN.md`, HTML preview, and per-design Review.
- **Visual reason:** It provides an editable composition and reviewed raster boundary for a receiving designer without making every ADS run tool-specific.
- **Learned versus copied:** OpenPencil imported ADS-owned HTML into editable nodes; ADS removed one importer artifact and copied no upstream design content.
- **Active use or rejection:** The active route uses `workspace/openpencil/route-console.op` and its reviewed PNG; minimal handoffs reject any OpenPencil requirement.
- **DESIGN marker:** §source:openpencil-optional-adapter§

## Selection rule

For a new brief, compare the source signals above with the receiving preview's
framework, interaction needs, license boundary, accessibility evidence,
maintenance cost, and visual job. Record the chosen adapter and proof in the
example README and canonical `DESIGN.md`. If those conditions do not justify a
source, keep it as research only. A selected asset, adapter, export, or `.op`
file remains an optional companion and receives a path/hash plus provenance and
licensing entry in a cross-owner `HANDOFF.md`; it never replaces `DESIGN.md`.

Source selection does not change the ADS/ACS boundary. ADS owns visual
direction and reusable visual assets; ACS owns editorial/content production,
edit/render execution, packaging, and publication. A missing sibling decision
is suggested to the caller as a bounded route and is never auto-run from this
audit or source record.

## Integration proof

`examples/onlinesourdough-resources/` uses the HeroUI state model only as an
original local disclosure adaptation. Its native button, `aria-expanded`,
`aria-controls`, keyboard handler, focus ring, and reduced-motion behavior are
observable in the preview and documented in
[`assets/adapters/README.md`](../examples/onlinesourdough-resources/assets/adapters/README.md).
