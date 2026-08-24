# Agentic Design System contract

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
├── DESIGN.md                       current direction
├── index.html                      technical preview
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

## Promotion boundary

`examples/` is not scratch space. A promoted example has a local README,
`BRIEF.md`, `DESIGN.md`, an inspectable `index.html`, necessary local assets,
and review/proof evidence. The example is listed in `examples/index.html` and
is understandable without importing ADS. A successful run without explicit
promotion remains operational evidence only.

## Standalone and AIOS entry/return

Standalone operation uses the pinned Node tools and Python standard library.
An AIOS-root caller may enter this checkout, provide resolved Space context as
ordinary input, wait for the primary skill route, and read the returned example
path and proof. ADS does not import AIOS, APT, another System, a shared
package, a central database, or a synchronized cross-System data model.
