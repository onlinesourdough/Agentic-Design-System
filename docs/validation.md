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

`npm run check` verifies the visible collection and documentation roots,
required shell and workspace paths, selected-design entries, Design.md lint,
local preview accessibility markers,
stale identity/path/link fragments, canonical DESIGN.md/brief semantics,
versioned handoff/ownership discovery, source/audit discovery, and secret-safe
public text. `npm test` exercises source decisions, genuinely minimal and
explicit optional-companion handoffs, accepted-snapshot immutability, audit
outcomes/read-only behavior, ledger predecessor/recovery rules, and
repeatability in temporary roots.

## Full standalone route

Use a fresh temporary operational root when the checkout's own ledger should
remain empty:

```sh
python3 workspace/engine/tracer.py --root /tmp/ads-proof --slug clean-clone-proof --source-decision --preview --review --curate
python3 workspace/engine/tracer.py --root /tmp/ads-proof --slug recovery-proof --simulate-failure
python3 workspace/engine/tracer.py --root /tmp/ads-proof --slug recovery-proof --recover --preview --review --curate
```

The tracer requires an explicit slug. It creates a previously absent selected
design or resumes a complete one; an incomplete design, output collision, or
symlinked collection path fails before mutation. It writes input/output/proof
evidence only under that selected design, checks the preview and review fixture,
and appends one ledger record per attempt. `--curate` records selected proof in
place; it does not duplicate an example or update a gallery. The failure stays
in the ledger and the recovery points back to it. The test suite uses a managed
temporary directory rather than relying on `/tmp` state.

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
npm run preview -- --design ads-business-freedom-content-e2e-r1
```

Inspect the selected design at desktop and mobile widths. Confirm its brief's
hierarchy and selected static states, the skip link and focus ring, reduced
motion behavior, and local assets. The server binds strict `127.0.0.1`, serves
only canonical regular files beneath that selected design, and rejects malformed
or escaping paths. Record any missing browser automation or visual proof
honestly in the Build handoff.

## Handoff

After the review method returns `PASS`:

```sh
npm run handoff -- --design ads-business-freedom-content-e2e-r1 --output handoffs/example \
  --receiving-owner "Agentic Design System"
```

`--receiving-owner` is explicit and required; an absent or blank owner fails
before any existing output is removed.

`BRIEF.md` must set `**Review mode:** independent` or `owner` and a non-empty
`**Review owner:**` independently of the receiving project. Review evidence
must name a reviewer matching that declared identity, record `PASS`, bind the
current `DESIGN.md` SHA-256, and list every pre-existing selected preview,
asset, `.op`, and native export with its exact source-relative path and SHA-256.
A matching independent PASS is sufficient for independent mode. Owner mode
exits with machine-readable status `waiting-owner` until the exact Review owner
records the PASS, current DESIGN hash, and every selected source-companion hash.
The reviewer is never compared with `--receiving-owner`; receiver acceptance is
separate. Every denial happens before an existing output is replaced.

The minimal output contains only `BRIEF.md`, canonical `DESIGN.md`, copied PASS
`REVIEW.md` or `proof.json` evidence, and generated `HANDOFF.md`. It needs no
preview, asset directory, token export, OpenPencil artifact, or installed token
export tool. The binder follows [`ADS-HANDOFF/1`](HANDOFF_TEMPLATE.md) and
records identity/revision, receiving owner/outcome, source revision, every
included relative path and SHA-256, provenance/licensing, review, limitations,
and explicit acceptance. The receiving project becomes canonical for its
accepted implementation copy; ADS retains its design direction and evidence.

Add only the companions deliberately selected for the receiving outcome:

```sh
npm run handoff -- --design ads-business-freedom-content-e2e-r1 --output handoffs/example \
  --receiving-owner "Agentic Design System" \
  --preview \
  --export tokens \
  --export tailwind
```

`--preview` selects pre-existing source companion `index.html`. Repeatable
`--asset` accepts one pre-existing source-relative file beneath `assets/` (for
example, `--asset assets/approved-mark.svg`); it never copies the directory
implicitly. Both require reviewed path/hash evidence. OpenPencil `.op` and
native PNG/SVG exports are also pre-existing reviewed source companions.
Repeatable `--export` accepts `css`, `tokens`, or `tailwind` and invokes the
pinned Design.md tool only for those selected formats. These outputs are
deterministic derivations of the exact reviewed `DESIGN.md`; emitted JSON and
`HANDOFF.md` record each output hash plus the reviewed DESIGN hash. Review need
not pretend those generated files existed beforehand. Missing or invalid
selected source companions fail before an existing pending output is replaced.

Generation starts `PENDING`. Copying is not acceptance. Once the receiving
owner records `Acceptance state: ACCEPTED`, rerunning the generator against that
output must fail without changing it. A later ADS revision uses a different
output/revision and receives separate acceptance; no live synchronization
exists. A receiving System copies only the accepted snapshot and never sends a
recursive automatic request back to ADS.

### OpenPencil browser workbench

Start the selected v0.8.4 editable source from the verified external VSIX:

```sh
npm run openpencil -- start \
  --vsix <verified-openpencil-v0.8.4-platform.vsix> \
  --document workspace/designs/ads-business-freedom-content-e2e-r1/openpencil/youtube-thumbnails-r1.op \
  --expected-nodes 25 \
  --expected-document-sha256 e6ef1098f55f284972fb0b1a1b6b3d09abeb58dcc03c197f9fc8ffaa5da961cb
```

The single JSON response contains a strict `http://127.0.0.1:<port>/` URL.
Pass that URL to the Codex-compatible built-in browser. The workbench never
invokes `op start --web`, an OS browser, or Zen. It launches the verified
release daemon directly and maps `/pkg/canvaskit/*` to the upstream
`/canvaskit/*` bytes. Each launch copies the selected source into private
workbench state and binds the daemon only to that disposable `working_document`;
the selected design source stays hash-checkable. The fresh loopback page seeds
OpenPencil's upstream browser-settings partition with `en-US` only when no
existing OpenPencil preference exists, then follows a fixed local ready redirect
without reflecting request query data into the bootstrap. The pinned macOS arm64
VSIX SHA-256 is
`7ce6cde22f7e8584de2faca0279f6d74438675291c2547a7d99230fc0e629342`.

For an authoring proof, inspect rendered English in the built-in browser and
make one bounded edit. `File → Save` is sufficient when it demonstrably changes
the named private `working_document`: capture its before/after SHA-256 and node
count, and prove that the selected source SHA-256 is unchanged. Copy that saved
private file only to an explicitly chosen path that does not already exist,
then reopen the copy with `File → Open` and visibly confirm the edit. This is a
reviewable `.op` candidate without a browser download and never overwrites the
selected source, a reviewed artifact, or an earlier candidate. `File → Save
As` is an alternative only when the browser/harness surfaces its `.op` Blob
download as a real local file. For a native PNG, use the bounded workbench
route below while its state is live. It invokes the verified release's
headless `--mcp` `export_frames` tool on the private working copy, first writes
to private state, validates the returned regular PNGs and unchanged source/
working hashes, then copies them to the chosen absent output directory. The
returned dimensions describe upstream top-level-frame output; they do not imply
a browser scale, whole-canvas render, or platform-upload crop.

```sh
npm run openpencil -- native-export \
  --state-dir <live-workbench-state> \
  --output-dir <explicit-absent-output-directory>
```

`File → Export image` is separate: its Save As/PNG results remain browser Blob
downloads and need a real surfaced local file. If that is unavailable, record
`unavailable-download` for the browser route only; do not extract hidden
browser state or infer that the native MCP path was exercised.

After supervised inspection, prove the live surface and reviewed bytes. If the
selected outcome is `waiting-review`, keep the workbench running and return its
machine-readable URL; cleanup is a later explicit `stop`. Otherwise clean it
deterministically:

```sh
npm run openpencil -- check \
  --document <reopened-candidate.op> \
  --expected-nodes <reviewed-count> \
  --expected-document-sha256 <reopened-candidate-sha256>
```

If a validated native MCP output or a real browser-surfaced PNG is selected,
add its separate reviewed evidence:

```sh
npm run openpencil -- check \
  --document <reopened-candidate.op> \
  --expected-nodes <reviewed-count> \
  --expected-document-sha256 <reopened-candidate-sha256> \
  --export <native-download.png> \
  --expected-export-sha256 <native-download-sha256>
```

Then inspect and clean the live session:

```sh
npm run openpencil -- status
npm run openpencil -- logs --lines 80
npm run openpencil -- stop
```

`stop` closes the daemon and removes the temporary extracted runtime and state.
OpenPencil remains optional: failure to start or inspect it leaves the portable
`DESIGN.md` handoff and unavailable-tool fallback valid.

For an explicitly selected OpenPencil route, use the temporary verified CLI
path and bind all native facts:

```sh
npm run handoff -- --design ads-business-freedom-content-e2e-r1 --output handoffs/example \
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
The CLI archive is only a handoff-version probe. The repository-owned
workbench above supplies the supervised web surface from verified VSIX bytes;
no executable, UI, or runtime is installed or committed.

Prove included and tool-unavailable behavior without changing `workspace/`:

```sh
npm run trace:handoff -- --openpencil-tool <verified-op-path>
```

The fallback exits successfully, emits the exact unavailable-tool reason,
copies no native artifact, and still produces the required portable handoff
plus only any independently selected source companions or deterministic derived
exports.

The same existing tracer also proves the public capability boundary in its
temporary root:

- a website/application handoff from the service example;
- a dashboard/report or slide-ready handoff from the executive example;
- an ACS-originated thumbnail/motion-direction brief returned as an accepted
  ADS design snapshot without an ADS runtime dependency;
- a material editorial-promise gap returned as a bounded ACS route suggestion
  with no external invocation or recursive chain; and
- an accepted snapshot left byte-identical while a later design revision uses
  a new pending handoff.

The ordinary Python tracer remains the standalone ADS proof and needs neither
ACS nor AIOS.

## Periodic read-only audit

Deterministic checks, per-design Review, and the periodic System audit have
different scopes. A clean repository can audit its repository contract:

```sh
npm run audit -- --scope repository
```

The aggregate live `workspace` scope examines every valid design-local ledger;
it never selects a fixture or one alphabetically first design. It returns
`BLOCKED` when a managed ledger lacks required accumulated run, failure, or
recovery evidence, while preserved legacy ledgers and curated snapshots retain
their own provenance without manufacturing fresh failure/recovery records. The
isolated tracer proves every outcome and byte-for-byte read-only behavior:

```sh
npm run trace:audit
```

Expected cases are healthy `PASS`, stale-route `FAIL`, contradictory-recovery
`FAIL`, and missing-required-evidence `BLOCKED`. Results include explicit
scope, evidence, gaps, and smallest next action. Audit never repairs, exports,
promotes, appends a run, creates an issue, or calls AIOS.
