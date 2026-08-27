# ADS architecture

Agentic Design System is a persistent System for repeated design work. Its
shape is intentionally filesystem-first so a clean checkout is inspectable by
a person or an agent without a service.

```text
root shell
├── AGENTS.md                         operating contract
├── README.md                         standalone entry
├── .agents/skills/
│   ├── agentic-design-system/        one public System route
│   ├── design-solution/              internal authoring method
│   ├── review-design/                internal per-design review method
│   └── audit-design-system/          internal periodic read-only audit
├── workspace/
│   ├── BRIEF.md, DESIGN.md, index.html active work and preview
│   ├── state/                         current resume pointer
│   ├── runs/                          route evidence
│   ├── history/runs.jsonl             append-only relations
│   ├── learning/                      durable learning
│   ├── openpencil/                    optional native source/export boundary
│   └── engine/                        optional preview/lint/export/tracer
├── examples/                          curated gallery, index owned by main
└── docs/                              contract, audits, validation, references
```

The primary skill is the only owner-facing route. It delegates focused
authoring and review methods, but keeps routing, state, ledger, failure and
promotion decisions in ADS. The technical engine is nested under workspace so
it cannot be mistaken for a new top-level System concept.

The active workspace and durable examples have different ownership rules:

| Surface              | Owner                   | Lifecycle                                 |
| -------------------- | ----------------------- | ----------------------------------------- |
| `workspace/`         | current ADS route       | resumed and replaced as work evolves      |
| `workspace/history/` | ADS operational history | append-only relations                     |
| `examples/`          | main gallery            | deliberate curated promotion              |
| branches/worktrees   | temporary isolation     | removed or merged after review            |
| receiving project    | receiving project       | canonical implementation after acceptance |

External UI sources remain a reviewed source boundary. An adapter can be
selected for a brief when its license, accessibility, framework fit,
maintenance signal, and visual value justify it. The adapter is implemented in
the receiving preview or curated example; a source repository is never copied
into ADS as a universal catalog.

`DESIGN.md` stays the semantic and portable design owner.
`docs/SOURCE_AUDIT.md` owns upstream fit and reuse decisions. An explicitly
selected OpenPencil `.op` file is editable tool-native source; its reviewed
PNG/SVG is an export boundary, and generated `HANDOFF.md` binds both to a
receiving owner. None of those roles introduces a shared cross-System model.

The technical lifecycle has three distinct readers:

| Reader                | Question                                             | Mutation |
| --------------------- | ---------------------------------------------------- | -------- |
| Deterministic checks  | Do known paths, formats, links, and invariants hold? | None     |
| Per-design Review     | Is this direction and selected handoff acceptable?   | None     |
| Periodic System audit | Does accumulated ADS truth still agree with proof?   | None     |

Build owns repairs. Review owns acceptance. The audit only reports `PASS`,
`FAIL`, or `BLOCKED` and routes its smallest next action.
