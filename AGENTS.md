# Agentic Design System

Agentic Design System (ADS) is a persistent, standalone design System. It
turns resolved intent into inspectable design directions, keeps the useful
history of that work, and deliberately curates examples that other projects
can build from.

## Operating model

- `workspace/` is the active operational truth: the current brief and design,
  browser preview, state, learning notes, run evidence, and append-only run
  history live here.
- `workspace/engine/` is optional technical implementation for preview,
  linting, export, checks, tests, deterministic tracers, and the read-only
  periodic audit. It is not a
  separate System concept.
- `examples/` is the durable gallery. An example is added or promoted only by
  deliberate choice and carries its own brief, design direction, preview,
  assets, and review proof.
- `docs/` is the public contract, source audit, architecture, validation
  recipe, evidence map, and preserved reference material.

The only visible functional roots are `workspace/`, `examples/`, and `docs/`.
The root shell is this file, `README.md`, the primary System skill at
`.agents/skills/agentic-design-system/SKILL.md`, and the package manifest used
by the local toolchain.

## Primary route

Use the primary ADS skill for every design-system run. It first inspects
relevant records in `workspace/history/runs.jsonl`, resumes or creates the
active work in `workspace/`, routes preview and review, records output and
proof references plus failure/recovery relations, and promotes an example
only when that choice is explicit.

The ledger stores small references and structured facts, never raw requests,
credentials, or a second database. A failed run remains evidence; a recovery
is a new run pointing to that predecessor.

An explicitly selected creative route may add an optional OpenPencil `.op`
source and reviewed PNG/SVG exports to a handoff. `DESIGN.md` stays semantic,
`HANDOFF.md` binds provenance and hashes, and ordinary HTML/tokens handoff
must remain green when OpenPencil is unselected or unavailable.

The ADS-local `audit-design-system` route checks accumulated drift without
mutation. It is separate from deterministic checks and per-design Review and
returns exactly `PASS`, `FAIL`, or `BLOCKED`.

## Examples workflow

`main` owns the examples index and the durable gallery. Branches and worktrees
are temporary isolation for review; they are not a permanent home for an
example. A clean checkout can use the standard-library tracer to create or
resume an example, preview and review it, append its run relation, and promote
it into the gallery.

## Source policy

HeroUI, Origin UI/Originkit, ThreeUI, and DesEngs are evaluated sources or
optional adapters. They are not a vendored default library. Each choice is
recorded with a revision, license signal, accessibility and framework fit,
maintenance signal, and visual reason in `docs/SOURCE_AUDIT.md`. The carried
Resources example proves one small, ADS-owned adapter integration without
adding a dependency.

## Boundaries

ADS works from its own checkout with Python 3.9+ and the pinned Node toolchain.
AIOS, APT, and another System may enter ADS with ordinary resolved context and
read its returned example and proof, but no such product is imported, started,
or required by this repository. ADS owns design truth until a receiving
implementation project deliberately takes it on.

Do not add secrets, customer truth, raw prompt dumps, a central database, a
shared cross-System data model, or a copied external skill catalog. Preserve
the local design and review skills as repeatable internal methods.

## Proof commands

From the repository root:

```sh
npm install
npm run check
npm test
npm run trace -- --slug clean-clone-proof --source-decision --preview --review --promote-example
npm run trace:handoff -- --openpencil-tool <verified-op-path>
npm run trace:audit
npm run handoff -- workspace workspace/handoff --receiving-owner "Agentic Design System"
```

Inspect the browser preview at `http://localhost:4173/` and resize it to a
desktop and mobile viewport. Keyboard focus, reduced motion, state changes,
and the gallery links must remain usable. The repository rename and any
commit, push, issue, pull-request, or GitHub setting change belong to a later
authorized Ship after lead review; this Build performs none of those actions.
