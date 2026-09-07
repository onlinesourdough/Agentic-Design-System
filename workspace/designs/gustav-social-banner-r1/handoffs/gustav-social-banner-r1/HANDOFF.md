# ADS portable design handoff

Contract: `ADS-HANDOFF/1`

Handoff ID: `ads-gustav-online-social-banners-b54dc49df11a`

Handoff revision: `r1+4c0d298a101b`

Source: `workspace`

Source revision: DESIGN.md r1 · SHA-256 4c0d298a101b24bbf3b7a6a53de9c927f02039a8d13a11bfb1efc3feed50b805

Receiving owner: Gustav Anderson

Receiving outcome: Gustav Anderson / Gustav Online social profiles receive one reviewed visual direction, an editable SVG source and exact 1584×396 PNG for LinkedIn, an editable SVG source and exact 1500×500 PNG for X, and direct desktop-profile crop/readability proof. No platform is edited by this Build.

Review state: PASS (evidence: `REVIEW.md`)

Review mode: independent

Review owner: AIOS lead thread 01a066aa-ec32-7c51-a185-178ff44df838

Reviewer: AIOS lead thread 01a066aa-ec32-7c51-a185-178ff44df838

Reviewed DESIGN.md SHA-256: `4c0d298a101b24bbf3b7a6a53de9c927f02039a8d13a11bfb1efc3feed50b805`

Acceptance state: PENDING

Accepted by: _(receiving owner must complete)_

Accepted at: _(receiving owner must complete)_

Acceptance statement: The receiving owner must explicitly replace the pending fields. Generation, copying, or use does not imply acceptance.

## Canonical direction and ownership

`DESIGN.md` is the required, portable, human-readable source of visual truth for this snapshot. It remains usable without ADS, the original caller, OpenPencil, or any sibling System. `BRIEF.md`, the preview, tokens, exports, and assets provide context or implementation help; none replaces `DESIGN.md`.

ADS owns the visual direction, visual hierarchy, brand/style/voice expression, interaction and motion direction, and reusable visual assets represented by this snapshot until acceptance. The receiving owner becomes canonical for its implementation or production copy after explicit acceptance. Later ADS revisions do not update that accepted copy; they require a new handoff revision and re-acceptance.

When Agentic Content System is the receiver, it owns editorial/content production, edit/render execution, packaging, and publication. This handoff creates no ADS-to-ACS runtime dependency or automatic route.

## Included snapshot and integrity

- `BRIEF.md` — SHA-256 `0a3acbcd530181bdfa83fc7f1f799db9bcd21271d620820857be728c0c682cdc`
- `DESIGN.md` — SHA-256 `4c0d298a101b24bbf3b7a6a53de9c927f02039a8d13a11bfb1efc3feed50b805`
- `REVIEW.md` — SHA-256 `e8fdb4f3383672d3a7dd66efeac9c50fec82dc74f684e9f9d5572ebb65bb8b26`
- `assets/arcitai-mark.svg` — SHA-256 `e2e7db4b96105e5b2f7a87d4295adbe788a9af6577faa03aac980c239306cd93`
- `assets/fonts/LICENSE.txt` — SHA-256 `930853ee1daa68554d9e35c8a9175affb74f699fad9a5da6ee5ebe76379d9137`
- `assets/fonts/geist-mono-variable.woff2` — SHA-256 `5f687a5dd4c87da13deaff9f6b9503d5e62249ff501265a96b134565f9aa8c87`
- `assets/fonts/geist-sans-variable.woff2` — SHA-256 `e24cec106619c03f0b3519e31b9bc55e0d5e926b6a95b8d798cd8cef215b1505`
- `assets/gustav-social-banner-r1-background-seed.png` — SHA-256 `055b90690a5db1c545e5608269d0f144ec0b4022c3c27c02d7a8db2e26eedfef`
- `assets/gustav-social-banner-r1-linkedin-crop-proof.png` — SHA-256 `620cb5f443cca57d7db4f3f0b41b6a88806465ba08549337c9d36c7369199693`
- `assets/gustav-social-banner-r1-linkedin-crop-proof.svg` — SHA-256 `1be04d26e4b3ea48fc50d655bd9f152cb2544d81899b2040df8b365cefa50968`
- `assets/gustav-social-banner-r1-linkedin.png` — SHA-256 `d104fc94df2e54c56b50b70cb7d574706183801b42793d910e99e4994fcef5d8`
- `assets/gustav-social-banner-r1-linkedin.svg` — SHA-256 `ef8116294c680583c8a3f72b9e6fcf996e396f2a2a4698c1b19a3b7f53512f80`
- `assets/gustav-social-banner-r1-x-crop-proof.png` — SHA-256 `cd8b973358185031b554e9673a765118719b338ecec7b227c3878ae4ee6bfed0`
- `assets/gustav-social-banner-r1-x-crop-proof.svg` — SHA-256 `09d407212ccdaaa83e29fffe3743aef0d9aca4af9ec393378bd022272ac8ec6a`
- `assets/gustav-social-banner-r1-x.png` — SHA-256 `93f2796d8e08293dd1087aa5fa3136d0729e3f1b86a49b912ac97f6e8885ec08`
- `assets/gustav-social-banner-r1-x.svg` — SHA-256 `3ff18dccc8a741ed54161405c2f1270bf10a3723aa2822e5b432201379be16f2`
- `assets/onlinesourdough-mark.svg` — SHA-256 `64d293422445f3343d3a3367e90425ee19a7127fee18239c56f904bf5c35da35`
- `index.html` — SHA-256 `d56b57cea4dee07c57fd775b0f8bc90037096d7b937af03704116268ae419065`

`HANDOFF.md` is the human-readable binder and is excluded from its own integrity list.

## Review and derivation boundary

The named reviewer matches BRIEF.md Review owner AIOS lead thread 01a066aa-ec32-7c51-a185-178ff44df838. This human Review identity is separate from receiving owner Gustav Anderson and from the receiver's later acceptance decision.

The current `DESIGN.md` hash above is the reviewed canonical direction. Every pre-existing selected preview, asset, editable source, and native export must appear below with its exact reviewed source hash. CSS, design-token, and Tailwind files are instead deterministic derivatives generated from that exact reviewed `DESIGN.md`; they are integrity-hashed here but do not masquerade as pre-existing reviewed files.

Reviewed source companions:

- `index.html` — SHA-256 `d56b57cea4dee07c57fd775b0f8bc90037096d7b937af03704116268ae419065`
- `assets/gustav-social-banner-r1-background-seed.png` — SHA-256 `055b90690a5db1c545e5608269d0f144ec0b4022c3c27c02d7a8db2e26eedfef`
- `assets/gustav-social-banner-r1-linkedin.svg` — SHA-256 `ef8116294c680583c8a3f72b9e6fcf996e396f2a2a4698c1b19a3b7f53512f80`
- `assets/gustav-social-banner-r1-linkedin.png` — SHA-256 `d104fc94df2e54c56b50b70cb7d574706183801b42793d910e99e4994fcef5d8`
- `assets/gustav-social-banner-r1-x.svg` — SHA-256 `3ff18dccc8a741ed54161405c2f1270bf10a3723aa2822e5b432201379be16f2`
- `assets/gustav-social-banner-r1-x.png` — SHA-256 `93f2796d8e08293dd1087aa5fa3136d0729e3f1b86a49b912ac97f6e8885ec08`
- `assets/gustav-social-banner-r1-linkedin-crop-proof.svg` — SHA-256 `1be04d26e4b3ea48fc50d655bd9f152cb2544d81899b2040df8b365cefa50968`
- `assets/gustav-social-banner-r1-linkedin-crop-proof.png` — SHA-256 `620cb5f443cca57d7db4f3f0b41b6a88806465ba08549337c9d36c7369199693`
- `assets/gustav-social-banner-r1-x-crop-proof.svg` — SHA-256 `09d407212ccdaaa83e29fffe3743aef0d9aca4af9ec393378bd022272ac8ec6a`
- `assets/gustav-social-banner-r1-x-crop-proof.png` — SHA-256 `cd8b973358185031b554e9673a765118719b338ecec7b227c3878ae4ee6bfed0`
- `assets/onlinesourdough-mark.svg` — SHA-256 `64d293422445f3343d3a3367e90425ee19a7127fee18239c56f904bf5c35da35`
- `assets/arcitai-mark.svg` — SHA-256 `e2e7db4b96105e5b2f7a87d4295adbe788a9af6577faa03aac980c239306cd93`
- `assets/fonts/geist-sans-variable.woff2` — SHA-256 `e24cec106619c03f0b3519e31b9bc55e0d5e926b6a95b8d798cd8cef215b1505`
- `assets/fonts/geist-mono-variable.woff2` — SHA-256 `5f687a5dd4c87da13deaff9f6b9503d5e62249ff501265a96b134565f9aa8c87`
- `assets/fonts/LICENSE.txt` — SHA-256 `930853ee1daa68554d9e35c8a9175affb74f699fad9a5da6ee5ebe76379d9137`

Deterministic derived exports:

- None selected.

## Provenance and licensing

The owner-supplied Solt Wagner JPEG at '/Users/gustavanderson/Downloads/1500x500.jpg' (SHA-256 '4d0855205e0bef4741640b11ece0437da780a54ee32c1454ac93aa354393c79f') informs only modular rhythm and the unfinished-grid metaphor; none of its logos, app identities, glyphs, badges, characters, or exact layout is copied. The selected textless AI-generated seed is copied unchanged as 'assets/gustav-social-banner-r1-background-seed.png' (SHA-256 '055b90690a5db1c545e5608269d0f144ec0b4022c3c27c02d7a8db2e26eedfef') and is used only as background texture/module material. Its upstream prompt was not supplied or embedded and is not invented. No image-generation call is made for the final exports; exact final image-generation prompt: 'None — deterministic SVG/Chrome raster export from the selected supplied seed.' The owner-approved onlinesourdough and Arc’IT marks are existing ADS companions from their documented project revisions. Geist 1.7.0 is carried under the SIL Open Font License. The listed social URLs and AIOS context files are read-only evidence, not copied content or instructions.

## Known limitations

Platform presentation can change, compress images, or shift avatar geometry. The crop proof uses the observed 2026-09-03 desktop presentation and must be rechecked at upload time. The selected AI-generated seed's upstream generation prompt is unavailable; it is disclosed and used only for noncritical background material. The SVG sources depend on the included Geist fonts and selected seed/marks for faithful rerendering. The exports prove design and legibility, not public performance, owner acceptance, or successful platform upload.

The receiving owner must revalidate behavior, accessibility, content legibility, rights, and tokens against the receiving implementation or production surface.

## Improvement signals

Improvement signals: Handoff fixtures are coupled to the mutable active workspace Review owner and optional OpenPencil selection; failures were reproduced during this banner run, and the implementation workaround was removed for separate issue-based review.

## Optional companions

Preview HTML, assets, token/theme exports, and OpenPencil files are included only when deliberately selected for this outcome. They never replace `DESIGN.md`; no receiving runtime depends on them.

- Preview: `index.html`
- Selected asset: `assets/gustav-social-banner-r1-background-seed.png`
- Selected asset: `assets/gustav-social-banner-r1-linkedin.svg`
- Selected asset: `assets/gustav-social-banner-r1-linkedin.png`
- Selected asset: `assets/gustav-social-banner-r1-x.svg`
- Selected asset: `assets/gustav-social-banner-r1-x.png`
- Selected asset: `assets/gustav-social-banner-r1-linkedin-crop-proof.svg`
- Selected asset: `assets/gustav-social-banner-r1-linkedin-crop-proof.png`
- Selected asset: `assets/gustav-social-banner-r1-x-crop-proof.svg`
- Selected asset: `assets/gustav-social-banner-r1-x-crop-proof.png`
- Selected asset: `assets/onlinesourdough-mark.svg`
- Selected asset: `assets/arcitai-mark.svg`
- Selected asset: `assets/fonts/geist-sans-variable.woff2`
- Selected asset: `assets/fonts/geist-mono-variable.woff2`
- Selected asset: `assets/fonts/LICENSE.txt`

## OpenPencil binding

Status: not selected. This handoff contains no `.op` source or OpenPencil export.
