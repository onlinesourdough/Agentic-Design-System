# Gustav Online constraint thumbnails — design review

Review: design
Reviewer: ADS Review
Result: PASS
Reviewed DESIGN.md SHA-256: `f1b7c554a96c06bc17eb9e6cb91afd916721251bbff3332606a3e89728a04a49`
Checks: [job, specificity, voice, composition, states, accessibility, source safety, contract, optional native source, ownership and sibling route]
Next: create handoff
Findings: []

## Scope

This independent, read-only `review-design` gate covers canonical
`workspace/DESIGN.md`, `workspace/index.html`, the selected portrait and Geist
font/license bytes, the two editable SVG masters, their exact PNG exports, the
contact sheet, and the selected Topic 02 OpenPencil source and comparison
export. It does not approve a video thesis, title, script, source footage,
performance claim, upload package, publication, or receiver acceptance.

## Required checks

1. **Job — PASS.** Topic 01 makes the founder-owned queue legible through a
   real portrait, the line `THE WORK WAITED FOR ME`, and a converging queue.
   Topic 02 makes diagnosis the first decision through `THE REAL CONSTRAINT`
   and the distinct `OFFER / OPS / DEMAND` structure. Both remain plausible
   future-content directions rather than claims that the videos exist.
2. **Specificity — PASS.** The approved portrait, named queue slips, three
   diagnosis lanes, `CURRENT` marker, and smallest-complete-change note trace
   directly to the brief. There is no placeholder company, invented metric,
   fake customer proof, or vague automation promise.
3. **Voice — PASS.** Copy is short, direct, calm, and specific to Gustav's
   founder-dependency and constraint-diagnosis stories. It avoids clickbait
   shock language, generic AI framing, maximum-automation language, and
   replace-humans claims.
4. **Composition — PASS.** The portrait-led dark founder queue and diagram-led
   light diagnosis board are intentionally distinct while sharing cream,
   walnut, terracotta, orange, Geist typography, paper-rule detail, safe-area
   treatment, and editorial rhythm. Full-size and 320x180 inspections found
   the primary copy legible, hierarchy clear, all essential meaning inside the
   48px inset, and the lower-right duration reserve free of essential meaning.
5. **States — PASS.** The thumbnail surfaces are static; product hover,
   loading, success, error, empty, permission, and offline states are not
   applicable. The supporting preview labels those fixtures explicitly and
   does not present them as thumbnail interactions.
6. **Accessibility — PASS.** The preview provides header, main, section, and
   footer landmarks; ordered headings; descriptive alt text; local assets; a
   skip link; a visible 3px keyboard focus indicator; and reduced-motion
   handling. Browser inspection at 1440x1000 and emulated 390x844 confirmed no
   horizontal overflow. At 390px, `innerWidth`, `clientWidth`, and
   `scrollWidth` were all 390px and the first thumbnail rendered 360x202.5px.
   Under `prefers-reduced-motion: reduce`, the query matched, scroll behavior
   became `auto`, and transition duration was reduced to `0.00001s`.
7. **Originality and source safety — PASS.** Mode `explore` applied owner-first
   precedence. The tracked owner-supplied portrait is unchanged at its declared
   SHA-256. Creator URLs and the local screenshot kit remained research-only
   pointers; no screenshot byte, layout, logo, metric, claim, or portrait
   treatment was copied. The SVG and OpenPencil compositions are original
   ADS-owned work. The carried Geist files retain their SIL Open Font License.
8. **Contract — PASS.** `BRIEF.md`, canonical `DESIGN.md`, preview, assets, and
   receiver boundary agree. Both PNGs are exactly 1280x720; the contact sheet
   is 1440x1200; card proofs are 320x180. `npm run check`, the focused skill
   regression, and the full 30-test suite passed before this gate. The handoff
   generator will bind contract `ADS-HANDOFF/1`, revision, receiver, outcome,
   exact paths and hashes, provenance, this Review, limitations, and separate
   `PENDING` acceptance without making any companion canonical over
   `DESIGN.md`.
9. **Optional native source — PASS with named limitation.** The verified
   OpenPencil v0.8.4 workbench opened the actual 25-node `.op` document on
   strict loopback in Codex's built-in browser. The whole 1280x720 composition,
   expanded layer tree, root dimensions, and editable properties were visible.
   The selected comparison PNG agrees with `DESIGN.md` and is byte-identical to
   the reviewed Topic 02 SVG-rendered PNG. OpenPencil's top-bar export did not
   yield a downloadable artifact in the built-in browser, so the comparison
   file is not represented as a native UI export. The live canvas proves
   rendering and editability; the exact SVG/PNG pair remains the reviewed
   rendering boundary. The workbench remains running for receiver inspection
   at `waiting-review`; cleanup requires a later explicit stop.
10. **Ownership and sibling route — PASS.** ADS stops at visual direction,
    selected assets, proof, and a pending portable handoff. Gustav Anderson /
    Gustav Online owns receiver acceptance and later content-planning use. ACS
    would own any separately requested thesis, script, source-media, render,
    package, or publication work. No sibling was invoked and no receiving
    repository, runtime dependency, recursive route, or live synchronization
    was created.

## Reviewed source companions

Only the source companions below are eligible for this handoff revision.

Reviewed source companion: `index.html` — SHA-256 `e8cba56ecd8e37abcdabbb2f2d10687cd7d1c1daec86bff19372b7644e9c67b4`
Reviewed source companion: `assets/gustav-portrait.jpg` — SHA-256 `4b1001c1b9ef3ec23c46e0d745210671609488b608fdb6b31c0bad9307644ebd`
Reviewed source companion: `assets/fonts/LICENSE.txt` — SHA-256 `930853ee1daa68554d9e35c8a9175affb74f699fad9a5da6ee5ebe76379d9137`
Reviewed source companion: `assets/fonts/geist-sans-variable.woff2` — SHA-256 `e24cec106619c03f0b3519e31b9bc55e0d5e926b6a95b8d798cd8cef215b1505`
Reviewed source companion: `assets/fonts/geist-mono-variable.woff2` — SHA-256 `5f687a5dd4c87da13deaff9f6b9503d5e62249ff501265a96b134565f9aa8c87`
Reviewed source companion: `assets/fonts/geist-pixel-square.woff2` — SHA-256 `04f9cf917a824370c77fecbd743c99d0b3dfd2c6c906de959996ac6f7fb343b3`
Reviewed source companion: `assets/thumbnail-01-founder-queue.svg` — SHA-256 `02fcea77d8317e1b11adfcdb036456d011244016f62b0eff502e07ccb1b7e137`
Reviewed source companion: `assets/thumbnail-01-founder-queue.png` — SHA-256 `2b9ad33186918547c90d68cd89be392096866eba6e2724a5f1047dd10064613c`
Reviewed source companion: `assets/thumbnail-02-real-constraint.svg` — SHA-256 `fedcb893f1220dcfe0389d8726ad9c773f67c5c0a5fb59e3f42fb815ede020f4`
Reviewed source companion: `assets/thumbnail-02-real-constraint.png` — SHA-256 `6107bed3c6c5c88b91718e4ce4d624fa66782d92b36957a498e7268322ed3004`
Reviewed source companion: `assets/youtube-thumbnails-contact-sheet.png` — SHA-256 `3c45ba90db6c5f3bf1e8236ee4fe2ddd1d1914cced1ac8ff53baddbfa2f696cf`
Reviewed source companion: `openpencil/youtube-thumbnails-r1.op` — SHA-256 `e6ef1098f55f284972fb0b1a1b6b3d09abeb58dcc03c197f9fc8ffaa5da961cb`
Reviewed source companion: `openpencil/exports/topic-02-real-constraint.png` — SHA-256 `6107bed3c6c5c88b91718e4ce4d624fa66782d92b36957a498e7268322ed3004`

## Direct evidence

- Exact exports: both selected thumbnail PNGs are 1280x720.
- Card proofs: `runs/ads-youtube-thumbnails-r1/card-01-320x180.png` SHA-256
  `c05a2eb40e57b2d4c66f513442ce88e9ece5f4ae65960751cb4e8d1512b09e3c`;
  `card-02-320x180.png` SHA-256
  `d211dcadc9105f517c8bfc7db54ab5066481776d47013a3068e1d645ab2368d1`.
- Browser captures: desktop 1440x1000 SHA-256
  `0701f6adfa9f21c4ce88957d57b82bf48a047cc4994f9012b591e7bec1fdb796`;
  mobile 390x844 SHA-256
  `e36ac715af2ce6bdb49f3e1b8e42f912b52608cc615abdd93499fe0cc0d78a21`.
- OpenPencil workbench: v0.8.4, 25 nodes, document SHA-256
  `e6ef1098f55f284972fb0b1a1b6b3d09abeb58dcc03c197f9fc8ffaa5da961cb`,
  verified VSIX SHA-256
  `7ce6cde22f7e8584de2faca0279f6d74438675291c2547a7d99230fc0e629342`,
  live URL `http://127.0.0.1:51712/`.

The independent design gate is PASS. The next bounded action is to generate a
pending receiver handoff and stop at `waiting-review`.
