# Agentic Design System

Agentic Design System (ADS) is a persistent, standalone design System. It turns
resolved intent into an approved, portable visual design direction whose
required artifact is `DESIGN.md`, with optional assets and tool-native sources
bound by a reviewed cross-owner handoff. It serves websites, applications,
dashboards, reports, slides, marketing/content surfaces, and other visual
outcomes without owning their receiving implementation or content production.

## Operating model

- `workspace/` is the active operational truth: the current brief and canonical
  portable design direction,
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
by the local toolchain. The [local skill index](.agents/skills/README.md)
documents ADS-owned routes and the boundary with externally installed skills.

## Primary route

Use the primary ADS skill for every design-system run. It first inspects
relevant records in `workspace/history/runs.jsonl`, resumes or creates the
active work in `workspace/`, routes preview and review, records output and
proof references plus failure/recovery relations, and promotes an example
only when that choice is explicit.

`DESIGN.md` is always the canonical human-readable visual direction. Optional
assets, previews, tokens, exports, and editable sources remain referenced
companions. The ledger stores small references and structured facts, never raw requests,
credentials, or a second database. A failed run remains evidence; a recovery
is a new run pointing to that predecessor.

Every cross-owner delivery adds the versioned `HANDOFF.md` Markdown binder. It
records stable identity/revision, receiving owner/outcome, source revision,
included relative paths and integrity hashes, provenance/licensing, review,
limitations, and explicit acceptance. An explicitly selected creative route
may add an optional OpenPencil `.op` source and reviewed PNG/SVG exports;
minimal handoff requires only `BRIEF.md`, canonical `DESIGN.md`, PASS review
evidence, the binder, and an explicit receiving owner. Preview, individual
assets, token/theme exports, and OpenPencil files are included only when
deliberately selected; the route remains green without their tools.

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

## Capability and sibling boundaries

ADS works from its own checkout with Python 3.9+ and the pinned Node toolchain.
It owns visual direction, visual hierarchy, brand/style/voice expression,
graphic composition, typography, color, imagery, interaction/motion direction,
and selected reusable visual assets. A receiving Project owns implementation
after explicit acceptance. ACS owns editorial/content production, edit/render
execution, packaging, and publication; visual format alone does not transfer
that ownership to ADS.

Either ADS or a sibling such as ACS may be entered first and either may run
alone. When work reaches a material sibling boundary, return a bounded route
suggestion to the current caller/coordinator. Never auto-run the sibling,
invent its missing decisions, recurse, or create a deterministic ADS-to-ACS
chain. Accepted sibling output returns only as ordinary referenced input.

AIOS, APT, and another System may enter ADS with ordinary resolved context and
read its returned paths and proof, but no such product is imported, started,
or required by this repository.

Do not add secrets, customer truth, raw prompt dumps, a central database,
runtime protocol, registry, shared cross-System data model, duplicated ACS
truth, or copied external skill catalog. Preserve the local design and review
skills as repeatable internal methods.

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
