# UI source audit

Reviewed 2026-08-27 from public repository metadata, license files, README
signals, and the live source pages. These are inputs to a per-brief choice,
not a component catalog or default design language.

| Source                                                                        | Pinned signal and license                                                                                                                                                                                | Accessibility                                                                                                         | Framework fit                                                                                                                    | Maintenance signal                                                                                     | Visual fit and decision                                                                                                                                                                   |
| ----------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [HeroUI](https://github.com/heroui-inc/heroui)                                | `heroui-inc/heroui` commit `1d2164e7b9a60221e39501081f0fe4f6c564bccf`; Apache-2.0 license file `bf4dfe2e9c9943535853e1e3725e6a38c320792f`                                                                | README describes React Aria and WCAG-oriented keyboard, focus, and screen-reader behavior                             | React 19, Next.js, Tailwind CSS v4; not the static HTML runtime used by ADS                                                      | Default branch `v3`, commit dated 2026-08-22; active signal at review                                  | Useful state model for an accessible disclosure. One original, local `heroui-disclosure` CSS adapter is integrated in the curated Resources example; HeroUI is not installed or vendored. |
| [Origin UI / Originkit](https://www.originkit.dev/)                           | `origin-space/originui` resolves to [cosscom/coss](https://github.com/cosscom/coss), commit `19620ae8cae81e30775f2cde03829326cb4916b2`; AGPL-3.0 license file `29ebfa545f5580919a4e884d7014d7a3eb2df762` | Live catalog exposes an interactive component surface, but ADS did not treat that as a sufficient accessibility audit | Live page signals Next/React/Framer and an animated component catalog; poor fit for dependency-free local previews               | Repository updated 2026-08-24; active but source identity/license transition needs re-checking         | Broad animated visual reference, but license and runtime cost make it a source-only reference for this Build; no adapter selected.                                                        |
| [ThreeUI](https://github.com/MengTo/threeui)                                  | `MengTo/threeui` commit `fbc9b3d61b0ef4b2e93b42e4fffa617ca277429b`; MIT license file `b3a5f823a69b4b010f92930ac09e8a776daf65c6`; bundled fonts retain SIL OFL and Three.js remains MIT per README        | Public README describes a live renderer and controls; no reason to assume every effect meets ADS preview needs        | React package plus Three.js assets; some implementation source is entitled/private, so it does not fit the smallest static route | Community sync merge dated 2026-08-23; active signals, but private Pro boundary increases review cost  | Strong source for selective motion or spatial visual research. Not chosen for the Resources route because 3D runtime would obscure its reading job.                                       |
| [DesEngs](https://desengs.com/) / [source](https://github.com/remvze/desengs) | `remvze/desengs` commit `634ff685dfee02419d48891baf2f79160f7959b6`; MIT license file `8221498bff7ddc727a9ee902daa6593569c8effc`                                                                          | The live resource site is a visual reference, not a component accessibility contract                                  | Live page signals Astro 5.16.2, local fonts, and a resource catalogue; not a drop-in ADS adapter                                 | Repository updated 2026-08-24; active resource curation signal                                         | Useful editorial hierarchy and design-engineering curation reference. No code or assets were copied and no adapter was selected.                                                          |
| [OpenPencil](https://github.com/ZSeven-W/openpencil)                          | release `v0.8.4`, peeled commit `c51d7ed41a96068a09127bbc096fee143fce0b22`; observed main `9c810776dab546076a5d9db791a49d9e8048dbd7`; MIT license blob `0dec8929ada31c1b4a60e64410e283a538ca9dfc`        | Editable canvas/export evidence does not replace semantic HTML accessibility review                                   | Optional standalone editor and CLI; no ADS or receiving-runtime dependency, and ordinary HTML/tokens handoff remains complete    | Signed release assets and checksums were available 2026-08-27; CLI archive needs a desktop or web host | Selected only for the active creative handoff: ADS-owned HTML became editable nodes and one reviewed PNG. No upstream UI, template, code, or asset was copied.                            |

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
- **Maintenance/availability:** The macOS arm64 CLI and DMG plus SHA256 sums were publicly available on 2026-08-27; the CLI archive alone is only a client and needs a desktop or web host.
- **Framework/accessibility fit:** Tool-native editing and export fit an explicitly selected creative route, but accessibility remains owned by semantic `DESIGN.md`, HTML preview, and per-design Review.
- **Visual reason:** It provides an editable composition and reviewed raster boundary for a receiving designer without making every ADS run tool-specific.
- **Learned versus copied:** OpenPencil imported ADS-owned HTML into editable nodes; ADS removed one importer artifact and copied no upstream design content.
- **Active use or rejection:** The active route uses `workspace/openpencil/route-console.op` and its reviewed PNG; ordinary handoffs reject any OpenPencil requirement.
- **DESIGN marker:** §source:openpencil-optional-adapter§

## Selection rule

For a new brief, compare the source signals above with the receiving preview's
framework, interaction needs, license boundary, accessibility evidence,
maintenance cost, and visual job. Record the chosen adapter and proof in the
example README. If those conditions do not justify a source, keep it as
research only.

## Integration proof

`examples/onlinesourdough-resources/` uses the HeroUI state model only as an
original local disclosure adaptation. Its native button, `aria-expanded`,
`aria-controls`, keyboard handler, focus ring, and reduced-motion behavior are
observable in the preview and documented in
[`assets/adapters/README.md`](../examples/onlinesourdough-resources/assets/adapters/README.md).
