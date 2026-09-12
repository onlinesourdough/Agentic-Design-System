---
name: openpencil-workbench
description: Open and verify an explicitly selected ADS .op companion in the pinned OpenPencil loopback workbench.
metadata:
  version: "1.0.0"
---

# OpenPencil workbench — internal method

Use only through `$agentic-design-system` after the selected brief explicitly
chooses an OpenPencil companion. Read only that selected design and this method.
`DESIGN.md` stays canonical; `.op` sources and reviewed exports stay optional,
ADS-owned, and replaceable.

1. Start the pinned external release bytes; never install or copy OpenPencil
   into ADS:

   ```sh
   npm run openpencil -- start \
     --vsix <verified-openpencil-v0.8.4-platform.vsix> \
     --document workspace/designs/<slug>/openpencil/<name>.op \
     --expected-nodes <reviewed-count>
   ```

2. The workbench copies the selected `.op` into its private task state before
   launching the upstream daemon. Its JSON status identifies both immutable
   `document` source and disposable `working_document`; the daemon is bound
   only to the latter. A source, state, output, or selected-design path that is
   missing, colliding, or outside the selected design is a stop condition, not
   an opportunity to overwrite another design.
3. Parse the single JSON result and give its `url` to the Codex-compatible
   built-in browser owned by the harness. Do not run `op start --web`, `open`, `xdg-open`,
   a Zen command, or any other OS-browser launcher. On a fresh loopback origin
   the proxy writes OpenPencil's upstream anonymous settings key with
   `locale: "en-US"` before UI initialization. A printed URL or chat-rendered
   PNG/SVG alone is not live-surface proof. Record the returned locale proof
   and inspect the actual canvas before claiming rendered English.
4. Author in the browser only after the canvas is visibly present. `File → New`
   and edits affect the disposable workbench document. `File → Save` is a
   supported authoring route when it demonstrably changes that known private
   `working_document`: record its before/after hash and node count, while also
   proving the selected source hash is unchanged. Copy the saved working file
   only to an explicitly selected, absent candidate path (never over a source,
   reviewed artifact, or prior candidate). Reopen that candidate either through
   `File → Open` when that picker is available, or through a fresh, verified
   native `--file` workbench start, and record which interface was used.
   Neither path implies that the other was tested. `File → Save As` is an
   optional alternative only when the browser/harness surfaces its `.op`
   download as a real local file. A changed title, canvas, or hidden browser
   state alone is not saved-output proof.
5. For a verified native PNG, while the workbench is live run `native-export`
   with its `--state-dir` and an explicitly selected, absent `--output-dir`.
   It invokes the verified release's headless `--mcp` `export_frames` tool only
   against the private working copy, validates regular PNGs in a private output
   directory, confirms source and working hashes are unchanged, then copies
   those validated files into the selected empty destination without overwrite
   or symlink traversal. The output scope is the upstream's top-level frames;
   record the returned dimensions rather than inferring browser scale or a
   whole-canvas/platform-upload render.
6. `File → Export image` remains a distinct browser-Blob route. It requires a
   browser/harness-surfaced local download; when unavailable, record
   `unavailable-download` for that browser route only. It does not invalidate
   the native MCP export above or authorize hidden-state extraction.
7. Compare the reopened candidate `.op`, any native PNG, and
   canonical `DESIGN.md`. Run `npm run openpencil -- check --document
<reopened-candidate.op> --expected-nodes <count>` with reviewed hashes; add
   `--export <native-export.png>` only for a validated file. The workbench
   serves both `/canvaskit/*` and the release compatibility path
   `/pkg/canvaskit/*` on strict `127.0.0.1`.
8. Use `status` and bounded `logs --lines <n>` while reviewing. When the
   selected outcome is `waiting-review`, keep the workbench running and return
   its machine-readable URL; cleanup is a later explicit `stop`. Otherwise run
   `stop` after proof; it closes the release daemon and removes the extracted
   temporary runtime. OpenPencil or its browser surface being unavailable must
   leave the portable `DESIGN.md` handoff route valid.
9. The evidence reviewer must match the brief's declared Review owner and
   record `PASS` plus the exact `.op` and native export hashes as reviewed
   source companions before any cross-owner binder may include them. Editing
   either artifact reopens Review. Review mode and any `waiting-owner` decision
   remain owned by the primary ADS route; the receiving owner is a separate
   identity and acceptance decision.
