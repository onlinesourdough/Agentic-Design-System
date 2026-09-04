---
name: openpencil-workbench
description: Internal ADS method for opening a selected editable .op source in the verified OpenPencil v0.8.4 web canvas through a strict loopback URL owned by the calling harness.
---

# OpenPencil workbench — internal method

Use only through `$agentic-design-system` after the brief explicitly selects an
OpenPencil companion. `DESIGN.md` stays canonical; `.op` sources and reviewed
exports stay optional, ADS-owned, and replaceable.

1. Start the pinned external release bytes; never install or copy OpenPencil
   into ADS:

   ```sh
   npm run openpencil -- start \
     --vsix <verified-openpencil-v0.8.4-platform.vsix> \
     --document workspace/openpencil/<name>.op \
     --expected-nodes <reviewed-count>
   ```

2. Parse the single JSON result and give its `url` to the caller/harness. Open
   that URL with the Codex-compatible built-in browser; do not run `op start
--web`, `open`, `xdg-open`, a Zen command, or any other OS-browser launcher.
   A fresh ADS origin seeds OpenPencil v0.8.4's supported
   `openpencil-rust-web-settings::<profile>` record with the minimal
   `{"version":1,"locale":"en-US"}` anonymous preference before the real
   canvas loads. Seed only when no OpenPencil settings record exists; an
   explicit user locale remains authoritative. The bootstrap redirects only to
   the fixed ADS-owned ready path and never reflects request query data into
   its inline script. A printed URL or chat-rendered PNG/SVG alone is not
   proof.
3. Verify the actual `.op` document is visible in the editable canvas, inspect
   its document/layer state, and compare it with canonical `DESIGN.md` and the
   selected export. Run `npm run openpencil -- check` with reviewed node count
   and hashes. The workbench serves both `/canvaskit/*` and the release
   compatibility path `/pkg/canvaskit/*` on strict `127.0.0.1`.
4. Use `status` and bounded `logs --lines <n>` while reviewing. For a selected
   outcome that stops at `waiting-review` for receiver or owner inspection,
   keep the workbench running and return its machine-readable URL; cleanup is a
   later explicit `stop`. Otherwise run `stop` after proof. `stop` closes the
   release daemon and removes the extracted temporary runtime. OpenPencil or
   its browser surface being unavailable must leave the portable `DESIGN.md`
   handoff route valid.
5. The evidence reviewer must match the brief's declared Review owner and
   record `PASS` plus the exact `.op` and native export hashes as reviewed
   source companions before any cross-owner binder may include them. Editing
   either artifact reopens Review. Review mode and any `waiting-owner` decision
   remain owned by the primary ADS route; the receiving owner is a separate
   identity and acceptance decision.
