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

The brief selects review mode exactly as `independent` or `owner` and declares
a non-empty `Review owner` distinct from the receiving project or repository.
The evidence reviewer must match that declared identity and record `PASS`, the
current `DESIGN.md` SHA-256, and each selected pre-existing source-companion
path/hash before handoff generation. Independent review is sufficient when
selected; owner mode stops `waiting-owner` until that exact Review owner makes
the bound decision. Deterministic CSS/token/Tailwind exports are derived from
the reviewed `DESIGN.md` and integrity-hashed in the generated binder rather
than represented as pre-existing reviewed files. Receiver acceptance remains
separate. A receiver copies its accepted immutable snapshot, never live-syncs
ADS, and never creates an automatic recursive sibling request.

When OpenPencil is selected, the ADS-local workbench starts verified v0.8.4
release bytes on strict `127.0.0.1`, returns a machine-readable URL for the
Codex-compatible built-in browser, provides the `/pkg/canvaskit/*`
compatibility route, and owns bounded status/log/stop cleanup. It never invokes
an OS browser and does not make OpenPencil a required or vendored runtime.

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

## Validation and delivery

Use [docs/validation.md](docs/validation.md) for checks relevant to the changed
surface. Exercise lifecycle tracers in disposable roots, preserving active
workspace evidence. When a browser preview is selected, inspect its relevant
viewports, keyboard focus, reduced motion, states, and links; desktop and mobile
checks apply to responsive surfaces. Direction-only outcomes require no HTML
preview or browser proof, but cannot establish the adaptive route's rendered
proof for new source adoption.

Repository rename, commit, push, issue, pull-request, and GitHub setting changes
require separately authorized Ship after lead review. Local Build authorization
does not authorize those external or delivery actions.
