# Gustav Social Banner R4 — Sources

## Adaptive-reference decision

- Mode: `direct`
- No new source discovery was performed.
- The R4 revision is bounded to the reviewed R3 direction, the exact current first-party brand marks, and the owner's explicit visual correction.
- No Solt, Arc Browser, Zen Browser, or other third-party screenshot, gradient, geometry, or proprietary asset is included.

## Frozen R3 design baseline

| Source                                                                                   | SHA-256                                                            |
| ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| `workspace/handoffs/gustav-social-banner-r3/DESIGN.md`                                   | `a605fa48b0bbea2320335ac48b17b15ba575ee5cfc0b5bfa553c5ac4ec4bfcee` |
| `workspace/handoffs/gustav-social-banner-r3/REVIEW.md`                                   | `d2b7d5c14336c36e936f357d57d7f7dbd37d3d0845565f1f708602014529ee32` |
| `workspace/handoffs/gustav-social-banner-r3/HANDOFF.md`                                  | `3dfb60b4f0395fcdff8d30785411a1c9f3816117920c9ea9652a6bff2eb1acdf` |
| `workspace/handoffs/gustav-social-banner-r3/assets/gustav-social-banner-r3-linkedin.png` | `32a2fa62ffe8451143069aa9bfc9ca3dbea71eea541b551f71da175638c0f1e4` |
| `workspace/handoffs/gustav-social-banner-r3/assets/gustav-social-banner-r3-x.png`        | `0f811152096088d0ec7260d44456885b47420dd5ffb91bbbc337157646089889` |
| `workspace/handoffs/gustav-social-banner-r3/gustav-social-banner-r3.op`                  | `adec19c65163054d8eeb2080731cfe9c803ef0452102264d127438fbcece9645` |

R4 preserves R3's copy, typography, color, grain, grid, cell geometry, brand order, brand names, crop behavior, and all non-G mark sizing. It removes the connector treatment and enlarges only the Gustav Online pixel-G allocation.

## Exact first-party brand marks

| Asset                                            | Role                                                  | SHA-256                                                            |
| ------------------------------------------------ | ----------------------------------------------------- | ------------------------------------------------------------------ |
| `assets/gustav-pixel-g-384.png`                  | Current Gustav Online pixel G; exact aspect preserved | `6019617d64f46c53fec767b25b1282070a4393a3b187db3e4b84c776179ed235` |
| `assets/onlinesourdough-mark-large-pixel-v3.svg` | Current onlinesourdough mark                          | `64d293422445f3343d3a3367e90425ee19a7127fee18239c56f904bf5c35da35` |
| `assets/onlinesourdough-mark-openpencil.png`     | Native raster companion                               | `ef3f6e01977379a9494e06f00f06e531c0f1f89456c2601e040326c65135fcde` |
| `assets/arcitai-mark-final.svg`                  | Current Arc'IT AI mark                                | `e2e7db4b96105e5b2f7a87d4295adbe788a9af6577faa03aac980c239306cd93` |
| `assets/arcitai-mark-openpencil.png`             | Native raster companion                               | `9b74e1cc2ae6f3d58d28469e3080ca7e6be05a4c1a2e80b4ec22ebd6230d017b` |

The deprecated smooth Gustav G is not present.

## Type and texture

| Asset                                    | SHA-256                                                            |
| ---------------------------------------- | ------------------------------------------------------------------ |
| `assets/fonts/geist-sans-variable.woff2` | `e24cec106619c03f0b3519e31b9bc55e0d5e926b6a95b8d798cd8cef215b1505` |
| `assets/fonts/geist-mono-variable.woff2` | `5f687a5dd4c87da13deaff9f6b9503d5e62249ff501265a96b134565f9aa8c87` |
| `assets/fonts/LICENSE.txt`               | `930853ee1daa68554d9e35c8a9175affb74f699fad9a5da6ee5ebe76379d9137` |

The deterministic light material-grain overlays are byte-identical to R3 and use the same fixed platform seeds. They are original generated texture, not copied imagery.

## OpenPencil

- Editor/runtime: verified OpenPencil `v0.8.4`, served on strict `127.0.0.1` by the ADS-local workbench.
- Verified release package SHA-256: `7ce6cde22f7e8584de2faca0279f6d74438675291c2547a7d99230fc0e629342`.
- Editable source: `gustav-social-banner-r4.op`.
- Native export: `gustav-social-banner-r4-native-x.png`, exported from the X board through the verified OpenPencil v0.8.4 CLI/desktop runtime.
- Native export SHA-256: `9a91297542cbef98e86ba7dc63159c67a4a7d1a9997f1f8816454239557d51eb`.

## Licensing and use

- Brand marks are first-party project inputs and remain subject to their owners' brand rights.
- Geist is included under the bundled SIL Open Font License text.
- Generated layout, grid, and grain are ADS-authored companions for this candidate.
