# ADS portable design handoff

Contract: `ADS-HANDOFF/1`

Handoff ID: `ads-business-freedom-content-system-story-e0cfce24fd44`

Handoff revision: `r1+958ac18a0448`

Source: `workspace`

Source revision: DESIGN.md r1 · SHA-256 958ac18a044822e4c39116db36992887ddd2b99589ddd4b5d1721a2f0ad68905

Receiving owner: Agentic Content System

Receiving outcome: Agentic Content System receives one reviewed portable visual direction, three keyframe/thumbnail concepts, selected brand assets, a local storyboard preview, and an optional editable native composition. ACS may use the accepted snapshot to decide the final thesis, hook, script, source media, edit, render, package, supervised handoff, and publication.

Review state: PASS (evidence: `REVIEW.md`)

Acceptance state: PENDING

Accepted by: _(receiving owner must complete)_

Accepted at: _(receiving owner must complete)_

Acceptance statement: The receiving owner must explicitly replace the pending fields. Generation, copying, or use does not imply acceptance.

## Canonical direction and ownership

`DESIGN.md` is the required, portable, human-readable source of visual truth for this snapshot. It remains usable without ADS, the original caller, OpenPencil, or any sibling System. `BRIEF.md`, the preview, tokens, exports, and assets provide context or implementation help; none replaces `DESIGN.md`.

ADS owns the visual direction, visual hierarchy, brand/style/voice expression, interaction and motion direction, and reusable visual assets represented by this snapshot until acceptance. The receiving owner becomes canonical for its implementation or production copy after explicit acceptance. Later ADS revisions do not update that accepted copy; they require a new handoff revision and re-acceptance.

When Agentic Content System is the receiver, it owns editorial/content production, edit/render execution, packaging, and publication. This handoff creates no ADS-to-ACS runtime dependency or automatic route.

## Included snapshot and integrity

- `BRIEF.md` — SHA-256 `9fb0222efcc2fbc8388fd7d11d681a99ec14b11aa13afd0d99a8e51863b4eee8`
- `DESIGN.md` — SHA-256 `958ac18a044822e4c39116db36992887ddd2b99589ddd4b5d1721a2f0ad68905`
- `REVIEW.md` — SHA-256 `fa6cbb5cf93ac7a7a8acafdd55cb1f3cefd3809e84f67c36138b4f679c57929d`
- `assets/arcitai-mark.svg` — SHA-256 `e2e7db4b96105e5b2f7a87d4295adbe788a9af6577faa03aac980c239306cd93`
- `assets/arcitai-panorama-day.jpg` — SHA-256 `b9760c08b8bcdcbd9a350e380aabff5e4a50ec6da7c83acba7887cb6c2df1bb4`
- `assets/complete-bake-dfy.png` — SHA-256 `01a150ff1c5851eebc139b0517b0a1b57b1b29bd26ae5c3715cf0f6c28efd126`
- `assets/content-publishing-desk.png` — SHA-256 `88a20834e07c5221fd4f629a846b2b636901a4ebd232c55409f14da670963cc9`
- `assets/fermentary-dwy.png` — SHA-256 `de8dd5e79ed5984969e4111716e2dbe4c02d87b7a655f600b3604d791dfba68f`
- `assets/fonts/LICENSE.txt` — SHA-256 `930853ee1daa68554d9e35c8a9175affb74f699fad9a5da6ee5ebe76379d9137`
- `assets/fonts/geist-mono-variable.woff2` — SHA-256 `5f687a5dd4c87da13deaff9f6b9503d5e62249ff501265a96b134565f9aa8c87`
- `assets/fonts/geist-pixel-square.woff2` — SHA-256 `04f9cf917a824370c77fecbd743c99d0b3dfd2c6c906de959996ac6f7fb343b3`
- `assets/fonts/geist-sans-variable.woff2` — SHA-256 `e24cec106619c03f0b3519e31b9bc55e0d5e926b6a95b8d798cd8cef215b1505`
- `assets/gustav-portrait.jpg` — SHA-256 `4b1001c1b9ef3ec23c46e0d745210671609488b608fdb6b31c0bad9307644ebd`
- `assets/keyframe-01-founder-constraint.png` — SHA-256 `8c8d07eda1fce269a5b527f960007db556eed115ce460e22f8c3c9c16666b9ee`
- `assets/keyframe-01-founder-constraint.svg` — SHA-256 `fffc13295787ce4e9684a39afe2401f68ff5c9b4a40d9fed4d87b558884dbf43`
- `assets/keyframe-02-smallest-complete-change.png` — SHA-256 `47dff749c8140468229dba75cfc8fb94657c2b359018dc770244123b530fedbb`
- `assets/keyframe-02-smallest-complete-change.svg` — SHA-256 `3696d42d827180e314fea4e3ca4107eff8400ec29fc93ce0743b20b2cd7ffb88`
- `assets/keyframe-03-reviewed-handoff.png` — SHA-256 `bff62e7fe4306a672c6c87fd69050949b4049765cf7fe6a4b64ea0b956174b5a`
- `assets/keyframe-03-reviewed-handoff.svg` — SHA-256 `3453028a0b054e5fd3a302b920926b75c1646b68650c3e0712a85d486d68ab89`
- `assets/onlinesourdough-mark.svg` — SHA-256 `64d293422445f3343d3a3367e90425ee19a7127fee18239c56f904bf5c35da35`
- `assets/resources-diy.png` — SHA-256 `81bd451b2bab0d9c928726afcc1cd583b414077f29f63e30c54f43c8df7ac823`
- `index.html` — SHA-256 `9f4cf64bd7b158e0d64cb50509f7514af187f7d3a731c3dae70b85d40e18767c`
- `openpencil/exports/route-console.png` — SHA-256 `734c32836a61c42088141d84308392a198403d6e4a80991f65d3d2f9a8b5e92d`
- `openpencil/route-console.op` — SHA-256 `33ab74b5315b89f68eefe8b6a3d3da193e968afab6f851de3c9f3b2f97b9b0e0`

`HANDOFF.md` is the human-readable binder and is excluded from its own integrity list.

## Provenance and licensing

Owner-listed AIOS context and preserved ADS directions are ordinary read-only references. Selected visual assets are copied unchanged from the clean local Gustav Online, onlinesourdough, and Arc’IT project repositories. Geist 1.7.0 is carried under the SIL Open Font License. OpenPencil is an optional MIT-licensed v0.8.4 tool adapter; no upstream template, UI, or design asset is copied.

## Known limitations

The 39-second words are draft visual-size cues, not a final script or public claim. The preview and native export prove visual direction, not final video timing, audio, captions, production rendering, browser-companion implementation, content performance, or receiver acceptance. Any importer approximation is recorded in the handoff.

The receiving owner must revalidate behavior, accessibility, content legibility, rights, and tokens against the receiving implementation or production surface.

## Optional companions

Preview HTML, assets, token/theme exports, and OpenPencil files are included only when deliberately selected for this outcome. They never replace `DESIGN.md`; no receiving runtime depends on them.

- Preview: `index.html`
- Selected asset: `assets/gustav-portrait.jpg`
- Selected asset: `assets/content-publishing-desk.png`
- Selected asset: `assets/onlinesourdough-mark.svg`
- Selected asset: `assets/resources-diy.png`
- Selected asset: `assets/fermentary-dwy.png`
- Selected asset: `assets/complete-bake-dfy.png`
- Selected asset: `assets/arcitai-panorama-day.jpg`
- Selected asset: `assets/arcitai-mark.svg`
- Selected asset: `assets/fonts/LICENSE.txt`
- Selected asset: `assets/fonts/geist-mono-variable.woff2`
- Selected asset: `assets/fonts/geist-pixel-square.woff2`
- Selected asset: `assets/fonts/geist-sans-variable.woff2`
- Selected asset: `assets/keyframe-01-founder-constraint.svg`
- Selected asset: `assets/keyframe-01-founder-constraint.png`
- Selected asset: `assets/keyframe-02-smallest-complete-change.svg`
- Selected asset: `assets/keyframe-02-smallest-complete-change.png`
- Selected asset: `assets/keyframe-03-reviewed-handoff.svg`
- Selected asset: `assets/keyframe-03-reviewed-handoff.png`

## OpenPencil binding

Status: included after supervised tool and visual review.

Upstream version: `v0.8.4` (release commit `c51d7ed41a96068a09127bbc096fee143fce0b22`)

Observed upstream main revision: `9c810776dab546076a5d9db791a49d9e8048dbd7`

Verified CLI response: `0.8.4`

Editable source: `openpencil/route-console.op` — SHA-256 `33ab74b5315b89f68eefe8b6a3d3da193e968afab6f851de3c9f3b2f97b9b0e0`

Reviewed export boundary:

- `openpencil/exports/route-console.png` — SHA-256 `734c32836a61c42088141d84308392a198403d6e4a80991f65d3d2f9a8b5e92d`

Provenance: ADS-owned HTML and original ADS-owned keyframe compositions were imported, saved, and exported through the genuine supervised OpenPencil v0.8.4 web surface; no upstream template, UI, or design asset was copied.

Review result: PASS

Known limitations: The v0.8.4 HTML importer approximates webfonts, grids, transforms, overflow, filters, margins, flex wrapping, radii, and shadows, with visible non-keyframe collisions; it ignores reduced-motion media behavior. Native export supports PNG but not SVG. The semantic browser preview and independently selected ADS-owned keyframe SVGs remain authoritative.

Only the listed exports were reviewed. Editing the `.op` source or regenerating an export reopens visual Review. `DESIGN.md` remains the portable semantic direction; the `.op` file is an optional tool-native working source.
