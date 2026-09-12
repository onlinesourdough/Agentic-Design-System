# Agentic Design System

Agentic Design System (ADS) is a persistent, standalone design System. It turns
resolved intent into an approved, portable visual design direction whose
required artifact is `DESIGN.md`, with optional assets and tool-native sources
bound by a reviewed cross-owner handoff. It serves websites, applications,
dashboards, reports, slides, marketing/content surfaces, and other visual
outcomes without owning their receiving implementation or content production.

## Shared lifecycle

Use the installed AIOS plugin (0.4.0 or later) for shared procedures:
`aios-spec-work`, `aios-build-work`, `aios-review-work` and `aios-ship-work`.
Spec owns conditional technology selection; Review owns generic repository
health audits. Resolve these skills through the harness, not copied files or
hardcoded cache paths. This repository owns its requirements, specialist
methods, checks, release facts and recovery. Keep those facts here and load
only the phase and local context needed for the change.

Work in the current task by default, including when opened directly from the
sidebar. Use `aios-orchestrate-workers` only for requested or concretely
beneficial delegation, or existing-worker recovery. Verify each selected root
and preserve one writer for overlapping changes. Repository work does not
preload personal AIOS context. Plugin availability is an authoring capability,
not a dependency of the product at runtime; if unavailable, report the method
gap and perform only work adequately covered by the local contract. Do not
recreate generic skills locally.

## Operating model

- `workspace/designs/<slug>/` is the selected operational truth: one brief,
  canonical portable direction, browser preview, optional companions, state,
  run evidence, history, and handoffs live together under the selected slug.
- `workspace/engine/` is optional technical implementation for preview,
  linting, export, checks, tests, deterministic tracers, and the read-only
  periodic audit. It is not a
  separate System concept.
- `workspace/designs/` is the only persistent design collection. Curated
  directions carry a local proof marker; recovery snapshots retain their
  provenance and are not promoted merely by being copied.
- `docs/` is the public contract, source audit, architecture, validation
  recipe, evidence map, and preserved reference material.

The only visible functional roots are `workspace/` and `docs/`.
The root shell is this file, `README.md`, the primary System skill at
`.agents/skills/agentic-design-system/SKILL.md`, and the package manifest used
by the local toolchain. The [local skill index](.agents/skills/README.md)
documents ADS-owned routes and the boundary with externally installed skills.

## Task routes

- Design authoring, preview, review, or handoff: use the
  [primary ADS skill](.agents/skills/agentic-design-system/SKILL.md) with one
  explicit `workspace/designs/<slug>/`. Its selected brief/history and method
  supply the task context; maintenance does not require a slug or launch it.
- Cross-owner delivery: the [handoff contract](docs/contract.md#cross-owner-and-optional-native-handoff)
  and [binder](docs/HANDOFF_TEMPLATE.md) own review identity, exact hashes,
  provenance/licensing, and immutable snapshots. Preserve the brief-selected
  `independent` or `owner` review mode, named Review owner, and separate
  receiving-owner acceptance. Owner mode waits for that exact owner's bound
  decision; a matching independent PASS needs no extra owner review.
- Source adoption or revision: read [SOURCE_AUDIT.md](docs/SOURCE_AUDIT.md).
  Evaluated libraries remain optional sources/adapters, never a vendored default.
- Explicit OpenPencil companion: use the primary route's
  [workbench method](.agents/skills/openpencil-workbench/SKILL.md).
- Read-only accumulated-state audit: use
  [audit-design-system](.agents/skills/audit-design-system/SKILL.md).
- Repository instruction, documentation, or engine maintenance: use accepted
  inputs, affected sources, and the [change discipline](docs/contract.md#decision-change-and-handback-discipline).
  Do not preload designs or caller/owner context, create design runs, or start
  design production merely to maintain the repository.

`DESIGN.md` remains canonical; previews, assets, tokens and tool sources are
optional companions. The selected design owns its small reference-only ledger;
failed runs remain evidence and recovery appends a related new run. Curated and
recovered material retains provenance. `main` owns the collection index;
branches and worktrees are temporary review isolation.

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

## Completion, validation, and delivery

Complete the accepted local change, relevant checks, in-scope fixes, and final
diff/artifact inspection in the current task. Existing action and destination
authority carries across phases; do not request it again merely to implement,
fix a finding, or enter Review/Ship. A real missing decision, selected owner
review, required unavailable capability, or new action/destination still gates
its dependent work. Continue independent authorized work while that gate waits.
A delegated worker returns its scoped result to the lead for acceptance.

For repository edits, run `npm run check` and `npm test` when applicable with
the existing toolchain. [Validation](docs/validation.md) owns conditional
tracers, source/handoff proof and browser inspection. Use disposable roots for
lifecycle fixtures and preserve active selected-design evidence. Instruction
maintenance needs no live editor, production launch, or network installation.
Repeat checks after changes or failures that invalidate their evidence.

Repository rename, commit, push, issue, pull-request, and GitHub setting changes
require action-specific Ship authority and lead review when delegated. Local
Build authorization alone does not grant delivery. Keep final changes
uncommitted when the caller retains delivery.
