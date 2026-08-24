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
stale identity/path/link fragments, and secret-safe public text. `npm test`
exercises ledger predecessor/recovery rules and repeatability in temporary
roots.

## Full standalone route

Use a fresh temporary operational root when the checkout's own ledger should
remain empty:

```sh
python3 workspace/engine/tracer.py --root /tmp/ads-proof --slug clean-clone-proof --preview --review --promote-example
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
npm run handoff -- workspace
```

The output must contain `DESIGN.md`, `index.html`, local assets, `theme.css`,
`tokens.json`, `tailwind.theme.json`, and `HANDOFF.md`. The receiving project
becomes canonical for its copied implementation; ADS remains the owner of its
curated example and evidence.
