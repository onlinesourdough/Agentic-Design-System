![Agentic Design System route](docs/assets/agentic-design-system-overview.svg)

# Agentic Design System

Agentic Design System (ADS) is a standalone design System for turning resolved
intent into an inspectable, reviewable design direction and a durable example.
It is a repeatable work surface, not a project template or a library that a
receiving product installs.

```text
prior runs → workspace brief/design → preview → review → evidence → curated gallery
                                      ↘ optional native handoff
accumulated truth ─────────────────────→ read-only periodic audit
```

The durable model is small:

```text
workspace/   active work, state, history, learning, and optional engine
examples/    deliberately promoted, self-contained design proof
docs/        contract, source audit, architecture, validation, references
```

## Start locally

```sh
npm install
npm run preview
```

The server opens the examples gallery at `http://localhost:4173/`. Pass a
directory after `--` to preview a specific surface, for example:

```sh
npm run preview -- workspace
npm run preview -- examples/onlinesourdough-resources
```

The primary agent entry is
[`agentic-design-system`](.agents/skills/agentic-design-system/SKILL.md). It
inspects prior runs, works in `workspace/`, and routes the internal
[`design-solution`](.agents/skills/design-solution/SKILL.md) and
[`review-design`](.agents/skills/review-design/SKILL.md) methods. Those methods
remain separate so a design can be authored and reviewed without duplicating
the System route. The ADS-local
[`audit-design-system`](.agents/skills/audit-design-system/SKILL.md) method
checks accumulated drift without repairing or creating anything.

## Verify a route

```sh
npm run check
npm test
npm run trace -- --slug clean-clone-proof --source-decision --preview --review --promote-example
npm run trace:audit
npm run handoff -- workspace workspace/handoff --receiving-owner "Agentic Design System"
```

The tracer uses only the standard library. It can also prove a recoverable
failure relation:

```sh
npm run trace -- --slug recovery-proof --simulate-failure
npm run trace -- --slug recovery-proof --recover --preview --review --promote-example
```

Use a temporary checkout for those demonstrations when the operational ledger
should remain empty in the working tree. See [`docs/validation.md`](docs/validation.md)
for the clean-clone recipe.

## Portable and optional native handoff

Every reviewed route can return semantic `DESIGN.md`, HTML/assets, and token
exports without OpenPencil. A creative route adds `.op` and reviewed PNG/SVG
files only when explicitly selected. The generated `HANDOFF.md` binds the
receiving owner, upstream version/revision, source/export paths and SHA-256
hashes, provenance, review, and limitations. The tool-unavailable route is
visible and falls back to the ordinary handoff without changing its source.
Every handoff command requires a non-empty explicit `--receiving-owner`.

Run the native success/fallback tracer with a temporary verified v0.8.4 CLI:

```sh
npm run trace:handoff -- --openpencil-tool <verified-op-path>
```

## Periodic read-only audit

`npm run check` is deterministic validation and `review-design` evaluates
one design. The periodic audit instead reads accumulated ADS truth, source and
license proof, handoff optionality, run evidence, failures/recovery, stale
routes, and unavailable evidence:

```sh
npm run audit -- --scope repository
npm run trace:audit
```

It returns exactly `PASS`, `FAIL`, or `BLOCKED` and never repairs,
exports, promotes, creates an issue, or appends a run.

## Gallery

The [examples index](examples/index.html) is owned by the main line and is the
single durable entry point for curated work. Branches and worktrees are review
isolation only. Current examples include service, operations, executive
reporting, and the carried `resources.onlinesourdough` direction.

Every curated example carries a brief, a portable `DESIGN.md`, a local
browser preview, relevant assets, and a readable proof/review note. The
Resources example also proves the selected dependency-free disclosure adapter
in `examples/onlinesourdough-resources/assets/adapters/`.

## References and ownership

Google Design.md remains the pinned format and export tool. The source audit
records what was learned from external design repositories and why no one
external UI library becomes the ADS default. Preserved historical references
are under [`docs/references/preserved`](docs/references/preserved/), clearly
separate from the active gallery.

ADS can be used entirely on its own. Another System may pass ordinary resolved
context and read the returned path and proof, but no AIOS or APT package,
service, database, or shared data contract is needed to run this repository.
