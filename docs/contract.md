# Agentic Design System contract

## Public capability

ADS turns resolved intent into an approved, portable visual design direction
whose required artifact is `DESIGN.md`, with optional assets and tool-native
sources bound by a reviewed cross-owner handoff. It can direct websites,
applications, dashboards, reports, slides, marketing/content surfaces, and
other visual outcomes without taking ownership of their implementation,
content production, render, or publication.

ADS accepts ordinary human-readable context: a conversation, rough visual
request, resolved brief, existing `DESIGN.md`, reference set, content brief,
AIOS task, Project, or another System. Before authoring, `BRIEF.md` makes the
intended outcome and receiving owner/reuse scope, audience/job, surfaces and
states, material brand/content/technical/accessibility/legal/delivery
constraints, source rights/provenance, named Review owner, and separate
receiver-acceptance decision inspectable. This is a semantic boundary, not an
AIOS-only schema or fixed questionnaire. For cross-owner work the brief also
selects review mode exactly as `independent` or `owner`.

## Vocabulary

ADS follows the neutral Agentic System model:

| Concept | Meaning                                                            |
| ------- | ------------------------------------------------------------------ |
| Space   | Persistent business or domain context in which work is situated.   |
| System  | The persistent capability that performs or routes repeatable work. |
| Project | A bounded, self-owning implementation outcome created from intent. |

Template, resource, archive, and skill are supporting constructs. ADS does not
create a new design-handoff type or a shared contract with another System.

## Public filesystem shape

Only these visible functional roots exist:

```text
workspace/                         active operational truth
├── BRIEF.md                        resolved current input
├── DESIGN.md                       canonical portable direction
├── index.html                      technical preview
├── openpencil/                      optional selected native source/exports
├── state/                          small current-state pointer
├── runs/                            one directory per route attempt
├── history/runs.jsonl              append-only run relation
├── learning/                       durable, intentional notes
└── engine/                         optional ADS-owned tooling
examples/                           deliberate standalone gallery
docs/                               contract, audit, validation, references
```

The root shell is `AGENTS.md`, `README.md`, and the primary skill at
`.agents/skills/agentic-design-system/SKILL.md`. The package manifest and
hidden CI are toolchain support, not additional System concepts.

## Operational truth

`workspace/` remains the active work surface. A run directory can contain:

- `input.json`: small references and route facts, not a request transcript;
- `output.json`: result and route status;
- `proof.json`: assertions and references to observable checks;
- `failure.json`: structured failure facts when the route stops; and
- `recovery.json`: evidence for a new route that resolves one failed run.

The append-only ledger has exactly these fields:

```text
run_id
started_at
finished_at
status
input_ref
output_ref
proof_ref
previous_run_id
previous_run_relation
failure
recovery
```

Values are references or small structured facts. `previous_run_relation` is
`null` for the first relevant run, `predecessor` for ordinary continuation,
and `recovery` for an explicit recovery. A failed run is never rewritten and
can be recovered only once.

`workspace/state/active.json` may identify the current active slug and latest
route for quick resume. It is not a second history store. Learning notes are
short and intentional under `workspace/learning/`.

## Source-decision boundary

`docs/SOURCE_AUDIT.md` owns source revision/version, license and reuse
boundary, maintenance/availability, framework/accessibility fit, visual
reason, and learned-versus-copied evidence. The active `DESIGN.md` resolves
those facts into named use/reject decisions. The design/source tracer records
that resolution as run proof; it does not create a catalogue, registry,
`design-list.md`, or second source of truth.

## Canonical portable direction

Every successful ADS outcome includes `DESIGN.md`. It is human-readable and
usable without ADS, OpenPencil, the original caller, or a sibling System. It
contains only relevant sections while making intent, audience/job, scope and
non-goals, visual principles/voice/brand expression, color, typography,
spacing/layout/composition, imagery/iconography/illustration/assets, relevant
motion, surface/responsive/state mappings, accessibility/content legibility,
source use/reject decisions, limitations, revision, review, and the receiving
acceptance boundary inspectable.

Assets, token/theme files, HTML previews, PNG/SVG/PDF exports, implementation
notes, and editable `.op` files are optional referenced companions. They never
replace `DESIGN.md`.

## Ownership and sibling routing

| ADS owns                                                                                                                                                                                   | Receiving or sibling owner                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------- |
| Visual direction, hierarchy, visual voice, brand/style expression, composition, typography, color, imagery, iconography, interaction/motion direction, and selected reusable visual assets | A receiving Project owns implementation after explicit acceptance                                                                       |
| Thumbnail/social composition and motion language after a content brief supplies the editorial promise and selected source media                                                            | ACS owns editorial thesis, script, hook, caption, source-media/content choices, edit/render execution, content package, and publication |
| Reviewed portable direction and selected assets until acceptance                                                                                                                           | The receiver owns its accepted implementation or production copy                                                                        |

Visual format alone does not decide ownership. ADS may design a slide system or
video motion language while a Project or ACS owns narrative, temporal
execution, final render, and publication.

ADS, ACS, or a receiving Project may be entered first; each may run alone. If
ADS discovers a material sibling decision, it names the missing decision and
returns a bounded sibling-route suggestion to the current caller/coordinator.
It never auto-runs ACS, invents content, mutates a sibling repository, recurses,
or creates a deterministic ADS-to-ACS chain. An accepted sibling result returns
as ordinary referenced input, not a runtime dependency.

## Cross-owner and optional native handoff

Same-owner work may remain in `workspace/` or a curated example without a
handoff binder. Every cross-owner delivery contains canonical `DESIGN.md` and
`HANDOFF.md`, with `BRIEF.md` and PASS review evidence bound into the snapshot;
selected HTML/assets/tokens/exports are companions. The
human-readable [`ADS-HANDOFF/1` template](HANDOFF_TEMPLATE.md) binds stable
identity/revision, receiving owner/outcome, source revision, included relative
paths and SHA-256 values, provenance/licensing, review state, known limitations,
and explicit acceptance. The generator requires a non-empty
`--receiving-owner`; receiving outcome and source-rights facts remain in
`BRIEF.md`, not a duplicated cross-System contract.

The receiving owner becomes canonical for its implementation or production
copy only after explicit acceptance. Generation and copying start as `PENDING`.
An `ACCEPTED` snapshot is immutable: a later ADS revision uses a new handoff
revision/output and separate re-acceptance. There is no live synchronization.
The brief declares one non-empty Review owner separately from the receiving
owner. Review evidence names a reviewer matching that declared identity,
records `PASS`, binds the current canonical `DESIGN.md` hash, and lists every
pre-existing selected preview, asset, editable source, and native export with
its reviewed path/hash. Independent mode needs only that matching independent
PASS. Owner mode returns `waiting-owner` until the exact declared Review owner
records the complete bound decision. The reviewer is never compared with
`--receiving-owner`; receiver acceptance remains separate in both modes.

Selected CSS, design-token, and Tailwind outputs are deterministic derivations
of the exact reviewed `DESIGN.md`. The generator records each derived output's
integrity hash and the reviewed DESIGN hash in emitted JSON and `HANDOFF.md`.
They are not required to masquerade as pre-existing files in Review evidence.
An explicitly selected creative route may additionally carry one editable
`<slug>.op` source and reviewed PNG/SVG native exports. Those pre-existing
files are reviewed source companions. `HANDOFF.md` binds the
OpenPencil upstream version/revision, source/export relative paths and SHA-256
hashes, provenance, review result, known limitations, and receiving owner.

OpenPencil remains optional and replaceable. It is not an ADS dependency, a
receiving-runtime dependency, or a shared ADS-to-receiving-System schema.
When it is unselected or unavailable, the visible route falls back to the
required portable handoff plus only any independently selected companions,
without modifying source files. Preview, individual asset paths, token/theme
exports, and OpenPencil files are never copied or generated by default.

A receiving System copies only its accepted immutable snapshot. It never
live-syncs this workspace and never creates a recursive automatic ADS request.

## Deterministic check, Review, and periodic audit

Deterministic checks test known repository invariants. Per-design Review
judges one `DESIGN.md`, any selected preview or companions, and the selected
handoff. The periodic System audit separately reads accumulated current truth, source/license proof,
handoff optionality, run evidence, failure/recovery relations, stale routes,
and unavailable evidence.

The ADS-local audit returns exactly `PASS`, `FAIL`, or `BLOCKED` with scope,
evidence, gaps, and the smallest next action. Missing required evidence is
`BLOCKED`. It never repairs, exports, promotes, creates a run or issue, or
depends on AIOS. Findings return to ADS Build/Review, or to AIOS improvement
triage only when the work originated there.

## Promotion boundary

`examples/` is not scratch space. A promoted example has a local README,
`BRIEF.md`, `DESIGN.md`, an inspectable `index.html`, necessary local assets,
and review/proof evidence. The example is listed in `examples/index.html` and
is understandable without importing ADS. A successful run without explicit
promotion remains operational evidence only.

## Standalone and AIOS entry/return

Standalone operation uses the pinned Node tools and Python standard library.
Any caller may enter this checkout, provide ordinary resolved context, wait for
the primary skill route, and read returned paths and proof. ADS does not import
or auto-run AIOS, APT, ACS, another System, a shared package, runtime protocol,
registry, MCP, central database, shared state, or synchronized cross-System
data model.
