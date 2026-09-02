# ADS architecture

Agentic Design System is a persistent System for producing approved, portable
visual directions across websites, applications, dashboards, reports, slides,
and content surfaces. Its shape is intentionally filesystem-first so a clean
checkout and its canonical `DESIGN.md` are inspectable without a service.

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
│   ├── BRIEF.md, DESIGN.md, index.html active input, canonical direction, preview
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

`DESIGN.md` stays the canonical semantic and portable design owner for every
work surface. Optional assets, previews, tokens, exports, and tool-native
sources stay referenced companions.
`docs/SOURCE_AUDIT.md` owns upstream fit and reuse decisions. An explicitly
selected OpenPencil `.op` file is editable tool-native source; its reviewed
PNG/SVG is an export boundary, and generated `HANDOFF.md` binds both to a
receiving owner. For every cross-owner delivery, the same binder also records
identity/revision, receiving outcome, all included paths/hashes,
provenance/licensing, review, limitations, and explicit acceptance. None of
those roles introduces a shared cross-System model.

The brief selects independent or owner review and names a Review owner
separately from the receiver. In both modes the evidence reviewer must match
that declared identity. Its PASS binds the current `DESIGN.md` hash and every
pre-existing selected source-companion hash before generation; owner mode waits
for that exact Review owner, while independent mode proceeds to a separate
pending receiver-acceptance step. Deterministic CSS/token/Tailwind outputs are
generated from the reviewed DESIGN hash and integrity-bound as derived exports,
not pre-existing Review evidence. Receivers copy accepted immutable
snapshots—never a live ADS workspace—and no recursive automatic sibling edge is
created.

ADS owns visual direction, visual hierarchy, brand/style/voice expression,
composition, typography, color, imagery, interaction/motion direction, and
selected reusable visual assets. A receiving Project owns implementation after
acceptance; ACS owns editorial/content production, edit/render execution,
packaging, and publication. Either sibling may be entered first. A boundary
crossing returns a bounded route suggestion to the caller and never creates an
automatic or deterministic ADS-to-ACS edge.

The technical lifecycle has three distinct readers:

| Reader                | Question                                             | Mutation |
| --------------------- | ---------------------------------------------------- | -------- |
| Deterministic checks  | Do known paths, formats, links, and invariants hold? | None     |
| Per-design Review     | Is this direction and selected handoff acceptable?   | None     |
| Periodic System audit | Does accumulated ADS truth still agree with proof?   | None     |

Build owns repairs. Review owns acceptance. The audit only reports `PASS`,
`FAIL`, or `BLOCKED` and routes its smallest next action.
