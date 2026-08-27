# Validation recipe

ADS uses a pinned Node toolchain for Design.md lint/export and a Python 3.9+
standard-library tracer for operational proof. No external service is needed.

## Repository checks

From the repository root:

```sh
npm install
npm run check
npm test
```

`npm run check` verifies the three visible roots, required shell and workspace
paths, gallery entries, Design.md lint, local preview accessibility markers,
stale identity/path/link fragments, source/handoff/audit discovery, and
secret-safe public text. `npm test` exercises source decisions, ordinary and
optional handoffs, audit outcomes/read-only behavior, ledger
predecessor/recovery rules, and repeatability in temporary roots.

## Full standalone route

Use a fresh temporary operational root when the checkout's own ledger should
remain empty:

```sh
python3 workspace/engine/tracer.py --root /tmp/ads-proof --slug clean-clone-proof --source-decision --preview --review --promote-example
python3 workspace/engine/tracer.py --root /tmp/ads-proof --slug recovery-proof --simulate-failure
python3 workspace/engine/tracer.py --root /tmp/ads-proof --slug recovery-proof --recover --preview --review --promote-example
```

The tracer creates or resumes an example, writes input/output/proof evidence,
checks the preview and review fixture, appends one ledger record per attempt,
and updates the temporary gallery index only when promotion is requested. The
failure stays in the ledger and the recovery points back to it. The test suite
uses a managed temporary directory rather than relying on `/tmp` state.

For a clean-clone equivalent of an uncommitted Build, make a fresh directory
from the final worktree while excluding `.git`, `node_modules`, ignored output,
and active operational artifacts; install from `package-lock.json`, then run
the commands above from that directory. This verifies the delivered tree,
not a developer's existing module cache or ledger.

The `--source-decision` proof reads at least the UI/library,
inspiration/reference, and optional tool-adapter records from
`docs/SOURCE_AUDIT.md` and verifies that the active `DESIGN.md` uses or
rejects each one. The run proof records the resolved fields but does not become
a second source database.

## Browser proof

Run:

```sh
npm run preview -- workspace
```

Inspect the route console at desktop width around 1440×1000 and mobile width
around 390×844. Confirm the first viewport names the route and action, the
resume button moves through loading to success, every state fixture is
keyboard-operable, the skip link and focus ring are visible, reduced motion is
honored, and the gallery links remain reachable without horizontal scrolling.
Then run the gallery preview and the carried Resources preview. Record any
missing browser automation or visual tool proof honestly in the Build handoff.

## Handoff

After the review method returns `PASS`:

```sh
npm run handoff -- workspace workspace/handoff \
  --receiving-owner "Agentic Design System"
```

`--receiving-owner` is explicit and required; an absent or blank owner fails
before any existing output is removed.

The output must contain `DESIGN.md`, `index.html`, local assets, `theme.css`,
`tokens.json`, `tailwind.theme.json`, and `HANDOFF.md`. The receiving project
becomes canonical for its copied implementation; ADS remains the owner of its
curated example and evidence.

For an explicitly selected OpenPencil route, use the temporary verified CLI
path and bind all native facts:

```sh
npm run handoff -- workspace workspace/handoff \
  --receiving-owner "Agentic Design System" \
  --openpencil \
  --openpencil-tool <verified-op-path> \
  --openpencil-source openpencil/route-console.op \
  --openpencil-export openpencil/exports/route-console.png \
  --openpencil-version v0.8.4 \
  --openpencil-release-revision c51d7ed41a96068a09127bbc096fee143fce0b22 \
  --openpencil-revision 9c810776dab546076a5d9db791a49d9e8048dbd7 \
  --openpencil-provenance "ADS-owned HTML imported and edited through the verified OpenPencil release surface; no upstream design asset copied." \
  --openpencil-review PASS \
  --openpencil-limitations "The importer approximates some CSS; v0.8.4 CLI needs a separately available desktop or web host for live file operations."
```

The supervised proof uses OpenPencil release `v0.8.4`. The macOS arm64 CLI
archive SHA-256 is
`2784d041bed961af2efa21fc68e494eb1915e90445e3ac16caf5d9cd21966b99`;
the signed arm64 DMG SHA-256 is
`576af5beb22bb0e6df5b82fbedae757c6b10e9f2e5d635f99f96d1d184319180`.
The CLI archive is only a client, so the separate desktop or web surface is a
known availability boundary. No executable is installed or committed.

Prove included and tool-unavailable behavior without changing `workspace/`:

```sh
npm run trace:handoff -- --openpencil-tool <verified-op-path>
```

The fallback exits successfully, emits the exact unavailable-tool reason,
copies no native artifact, and still produces the complete ordinary handoff.

## Periodic read-only audit

Deterministic checks, per-design Review, and the periodic System audit have
different scopes. A clean repository can audit its repository contract:

```sh
npm run audit -- --scope repository
```

The live `workspace` scope returns `BLOCKED` when required accumulated run,
failure, or recovery evidence has not yet been created; it never infers a
pass. The isolated tracer proves every outcome and byte-for-byte read-only
behavior:

```sh
npm run trace:audit
```

Expected cases are healthy `PASS`, stale-route `FAIL`, contradictory-recovery
`FAIL`, and missing-required-evidence `BLOCKED`. Results include explicit
scope, evidence, gaps, and smallest next action. Audit never repairs, exports,
promotes, appends a run, creates an issue, or calls AIOS.
