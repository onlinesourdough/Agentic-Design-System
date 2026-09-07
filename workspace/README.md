# ADS workspace

`workspace/` contains the ADS design collection and its shared implementation
helpers. Select exactly one direction beneath `designs/<slug>/` before reading,
editing, previewing, reviewing, or handing off a design.

- Each selected design owns `BRIEF.md`, canonical portable `DESIGN.md`, and its
  supporting `index.html` preview.
- Optional `openpencil/` content belongs only to the selected creative route;
  it never replaces `DESIGN.md`.
- Selected designs own their own `state/`, `runs/`, and append-only
  `history/runs.jsonl`; these never form a cross-design database.
- Selected designs own versioned `handoffs/` snapshots when delivery crosses an
  owner boundary.
- `learning/` holds short, intentional notes retained for future routes.
- `engine/` contains optional preview, lint, export, check, test, tracer, and
  read-only audit tooling. It is implementation detail, not another ADS
  concept.

The primary System skill first lists the collection and requires an explicit
slug. A clean checkout can use its `--root` tracer option to exercise a fresh
selected direction without importing another System.

When delivery crosses to another owner, the existing handoff generator creates
the `ADS-HANDOFF/1` `HANDOFF.md` snapshot with receiver/outcome, revision,
paths/hashes, provenance/licensing, Review, limitations, and explicit
acceptance. Same-owner active work needs no binder. Sibling capability gaps are
returned to the caller as bounded suggestions and are never auto-run.
The minimal cross-owner snapshot needs no preview, asset, token export, or
OpenPencil file; each companion is added only with its explicit handoff option.
For cross-owner work, `BRIEF.md` selects `independent` or `owner` review and
declares a named `Review owner` separately from the receiver. The evidence
reviewer must match that identity and bind the current `DESIGN.md` plus each
selected pre-existing source-companion hash. Owner mode stops `waiting-owner`
until that exact Review owner decides; independent mode proceeds to separate
receiver acceptance. Deterministic CSS/token/Tailwind outputs are generated
from and bound to the reviewed DESIGN hash rather than entered as pre-existing
review evidence. Accepted receivers copy the snapshot and never live-sync or
recursively invoke ADS.
