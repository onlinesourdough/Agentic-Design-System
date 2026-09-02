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

2. Parse the single JSON result and give its `url` to the Codex-compatible
   harness's built-in browser. Do not run `op start --web`, `open`, `xdg-open`,
   a Zen command, or any other OS-browser launcher.
3. Inspect the editable canvas and compare it with canonical `DESIGN.md` and
   the selected export. Run `npm run openpencil -- check` with reviewed node
   count and hashes. The workbench serves both `/canvaskit/*` and the release
   compatibility path `/pkg/canvaskit/*` on strict `127.0.0.1`.
4. Use `status` and bounded `logs --lines <n>` while reviewing. Always run
   `stop` after proof; it closes the release daemon and removes the extracted
   temporary runtime. OpenPencil or its browser surface being unavailable must
   leave the portable `DESIGN.md` handoff route valid.
5. The evidence reviewer must match the brief's declared Review owner and
   record `PASS` plus the exact `.op` and native export hashes as reviewed
   source companions before any cross-owner binder may include them. Editing
   either artifact reopens Review. Review mode and any `waiting-owner` decision
   remain owned by the primary ADS route; the receiving owner is a separate
   identity and acceptance decision.
