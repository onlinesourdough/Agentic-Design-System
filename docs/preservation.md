# Dirty source carry proof

The user-owned source checkout was read-only during this Build:

`Owner project source: projects/Design-template`

At ingest it reported six modified files and four untracked media assets. The
following SHA-256 values were recorded before any restructuring and matched in
the isolated Build immediately after explicit-path transfer:

| Relative path                                                                   | SHA-256 at ingest                                                  |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| `docs/SOURCES.md`                                                               | `edc6d5666f0b323277ae51b3731797b710e14972c56dba8c7fd57077a20dca64` |
| `examples/onlinesourdough-resources/BRIEF.md`                                   | `b286395b116f7fac2d699486c5f5ad6e24cdc47b424502e4a10600b9978724e3` |
| `examples/onlinesourdough-resources/DESIGN.md`                                  | `ec9fccfd39476d0d13a54452270a381bb460bf105591961519a1fee7c916f7b9` |
| `examples/onlinesourdough-resources/README.md`                                  | `650b75437a7e60243150ae92464ea27bf5ef67e1ce8308600a39d68286a60134` |
| `examples/onlinesourdough-resources/assets/README.md`                           | `4f3fae0e3a1628a7dfb47b9cff0721c832e486186d386c9ee27acfaf5455b24e` |
| `examples/onlinesourdough-resources/index.html`                                 | `69c678e3561d56a6f45ff17bca40bcc4d39115064cc45c88843148b755b83060` |
| `examples/onlinesourdough-resources/assets/resources-hero-agentic-v1.png`       | `335478aa5c50516f3c431ff6d08882cc59b30c8098960bfbac8b3280887d7525` |
| `examples/onlinesourdough-resources/assets/resources-hero-agentic-v2.png`       | `4f0b4a20ae415cdef46b7e9d9c15dabc0b1f7f044bd7ec0bb307669b2407645b` |
| `examples/onlinesourdough-resources/assets/resources-vsl-motion-preview-v2.mp4` | `69698aa95781d2aeb2c9759206209738c2bb83263d1dbbe9d118d8dfe09cf761` |
| `examples/onlinesourdough-resources/assets/resources-vsl-motion-preview.mp4`    | `60bf87b1da6c808e5661053930a2a96b38eed29cb33b30f413c96eec7784c245` |

The copied textual example files were then extended only where the ADS
architecture and the one selected adapter needed an explicit integration.
The four media files remain byte-for-byte identical. The source checkout's
status and these hashes were re-read after the transfer; no source mutation or
external repository mutation was performed.

## 2026-09-07 selected-collection integration

The five commits at fresh `origin/main` revision
`8950a98b44aab9ed380e1c9b424d3c8f96e24e49` were integrated through a normal
merge after the local selected-design migration commit. Their behavior is kept,
not reintroduced as the obsolete singleton runtime:

- adaptive `direct`, `discover`, and `explore` remain one owner-first route in
  the primary skill, with pointer-only caller media and canonical decisions in
  `DESIGN.md`;
- HTML is optional: direction-only work has no invented preview requirement,
  while selected responsive surfaces retain their relevant viewport and
  accessibility checks;
- handoff instructions retain canonical contract, binder, and validation links;
  `waiting-review` keeps the OpenPencil workbench alive until explicit cleanup;
  and
- the remote Gustav Online thumbnail brief, direction, review, PNG/SVG assets,
  contact sheet, and editable `.op` source live under
  `workspace/designs/ads-business-freedom-content-e2e-r1/`.

The old singleton ledger is retained byte-for-byte at that design's
`history/original-workspace-runs.jsonl`; `history/MIGRATION.json` maps evidence
that exists locally and pins the three historical records whose output/proof
files were never present in the imported tree. The audit accepts only a record
whose contents still match that hash-verified original ledger and its declared
missing field; a new or altered missing reference remains `BLOCKED`. It reports
the pinned facts as provenance rather than fabricating evidence or restoring a
singleton path.

For review, compare the final tree with the fetched remote using
`git diff --stat 8950a98b44aab9ed380e1c9b424d3c8f96e24e49..HEAD`. The expected
delta is the selected-design migration, preserved local social-banner work,
and the scoped compatibility bindings above; remote commits and their assets
remain reachable from the merge history.

This carry proof records historical ingest provenance only. It is not a live
receiving link or shared state: the migrated
`workspace/designs/onlinesourdough-resources/DESIGN.md` is the canonical
portable visual direction in ADS, and any later cross-owner copy receives its
own versioned `HANDOFF.md`, integrity list, rights boundary, and explicit
acceptance.
