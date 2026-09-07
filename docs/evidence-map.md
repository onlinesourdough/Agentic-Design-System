# Build requirement to evidence map

| Requirement                                                       | Evidence in this Build                                                                                                |
| ----------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| Persistent standalone System shell                                | `AGENTS.md`, `README.md`, `.agents/skills/agentic-design-system/SKILL.md`, `docs/contract.md`, `docs/ARCHITECTURE.md` |
| One selected design owns active work, history, and state          | `workspace/README.md`, `workspace/designs/<slug>/BRIEF.md`, `DESIGN.md`, `state/`, `history/`, and `runs/`            |
| Optional engine stays under workspace                             | `workspace/engine/`, root `npm` scripts, structural checks in `workspace/engine/checks.mjs`                           |
| One public route with useful local methods                        | primary skill plus internal `design-solution`, `review-design`, and optional `openpencil-workbench` skills            |
| Adaptive `direct`/`discover`/`explore` reference behavior         | primary skill, `references/adaptive-references.md`, and task-specific route evidence                                  |
| Caller reference ownership and owner-first precedence             | adaptive-reference method, contract boundary, and selected `DESIGN.md` decisions                                      |
| Direction-only and selected-surface preview boundaries            | primary/design-solution methods, selected `DESIGN.md`, and `docs/validation.md`                                       |
| Create/resume, preview, review, ledger, and deliberate curation   | `workspace/engine/tracer.py`, its isolation tests, `docs/validation.md`, collection index                             |
| Failure and recovery relations                                    | tracer `--simulate-failure` / `--recover`, `workspace/engine/tests/test_tracer.py`                                    |
| Main-owned design collection index; temporary branches only       | `workspace/designs/README.md`, `workspace/designs/index.html`, primary skill and architecture docs                    |
| Four requested sources audited and one adapter proved             | `docs/SOURCE_AUDIT.md`, Resources adapter README/CSS, carried Resources preview                                       |
| Three source roles resolve into selected design                   | `docs/SOURCE_AUDIT.md` current trace, selected `DESIGN.md` markers, tracer `--source-decision`                        |
| Dirty source preserved                                            | `docs/preservation.md`, matching SHA-256 transfer output, unchanged source status                                     |
| Browser preview states and responsive access                      | selected `DESIGN.md`, `index.html`, `REVIEW.md`, `docs/validation.md`                                                 |
| No external System package or service required                    | package scripts, Python standard-library tracer, checks, contract boundaries                                          |
| CI/checks and stale scans                                         | `workspace/engine/checks.mjs`, `.github/workflows/check.yml`, `npm run check`                                         |
| `DESIGN.md` is canonical across active and curated work           | workspace/example `DESIGN.md` files, author/review skills, deterministic capability checks                            |
| Cross-owner handoff is versioned, hashed, and explicitly accepted | `docs/HANDOFF_TEMPLATE.md`, `workspace/engine/create-handoff.mjs`, handoff tests and tracer                           |
| Named independent/owner Review gates selected immutable bytes     | declared Review owner, exact reviewer match, missing/stale/owner-waiting denial tests, handoff tracer                 |
| Source companions and deterministic derivations stay distinct     | emitted JSON/binder classes, reviewed path/hash tests, derived output/DESIGN integrity assertions                     |
| Minimal handoff and explicit optional companions                  | `create-handoff.mjs`, minimal/selected-companion tests, `handoff_tracer.mjs`, `docs/validation.md`                    |
| Optional editable OpenPencil handoff and portable fallback        | active `.op`/PNG, `create-handoff.mjs`, `handoff_tracer.mjs`, per-design `REVIEW.md`                                  |
| Strict-loopback OpenPencil browser workbench and cleanup          | local skill, `openpencil-workbench.mjs`, focused tests, `docs/validation.md`, built-in-browser proof                  |
| English bootstrap and `waiting-review` keepalive                  | workbench locale bootstrap tests, primary/OpenPencil methods, and selected brief                                      |
| Website/app, dashboard/report, and content-visual portability     | expanded `handoff_tracer.mjs` matrix using curated sources and an isolated ACS-originated content-visual fixture      |
| ADS/ACS ownership and suggestion-only sibling routing             | public contract, primary/author/review skills, tracer bounded-content-gap proof                                       |
| Accepted snapshots remain immutable across later ADS revisions    | generator guard, handoff unit test, accepted/revision handoff tracer case                                             |
| Read-only accumulated-state audit                                 | `audit-design-system` skill, `audit_design_system.py`, `audit_tracer.py`, audit tests                                 |

The Build deliberately does not include a commit, push, repository rename,
GitHub setting change, issue edit, PR, or external-repository mutation.
