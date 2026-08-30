---
name: agentic-design-system
description: Route approved, portable visual directions for websites, applications, dashboards, reports, slides, and content surfaces from prior evidence through canonical DESIGN.md, preview, review, cross-owner handoff, ledger proof, and deliberate example promotion.
---

# Agentic Design System primary System skill

This is the one public ADS entry point. It is a filesystem method, not a
service or framework. It works from a clean checkout and keeps the active
design work in `workspace/` until a deliberate curation decision promotes an
example into `examples/`.

## Route

1. Read `workspace/history/runs.jsonl` and inspect records relevant to the
   requested example or brief. Use references and run IDs; never copy a raw
   request or private context into the ledger.
2. Read the active `workspace/BRIEF.md` and `workspace/DESIGN.md`. Confirm that
   the brief makes outcome and receiving owner/reuse scope, audience/job,
   surfaces/states, material constraints, source rights/provenance, and
   review/acceptance owner inspectable. Resume active work when its state says
   it is in progress, or create the smallest surface needed for the intent.
3. Use `$design-solution` for the focused design method when the direction or
   preview needs authoring. `DESIGN.md` is always the canonical portable,
   human-readable visual direction; keep optional preview, assets, tokens,
   exports, and editable sources referenced beside it without letting one
   replace it.
4. ADS owns visual direction, visual hierarchy, brand/style/voice expression,
   composition, typography, color, imagery, interaction/motion direction, and
   selected reusable visual assets. If work reveals a material editorial,
   script, hook, source-media, production-render, packaging, or publication
   decision, return a bounded ACS route suggestion to the current
   caller/coordinator. Never auto-run ACS, invent the decision, recurse, or
   create a deterministic ADS-to-ACS chain. Either sibling may be entered first;
   accepted sibling output returns only as ordinary referenced input.
5. Run the local preview from `workspace/engine/serve.mjs`, inspect desktop
   and mobile widths, and verify landmarks, keyboard-visible focus, reduced
   motion, and relevant loading, empty, error, success, permission, and
   offline states.
6. Use `$review-design` as the review method. Record its result and concrete
   proof references in the run evidence; a review result is not a promotion
   decision by itself.
7. When reviewed work crosses an owner boundary, generate `HANDOFF.md` with the
   existing handoff route. Verify `ADS-HANDOFF/1` identity/revision, receiving
   owner/outcome, source revision, included relative paths and SHA-256 values,
   provenance/licensing, Review state, limitations, and explicit acceptance.
   Generation starts `PENDING`; an accepted snapshot is immutable, and a later
   direction requires a new handoff revision and re-acceptance.
8. When a creative route explicitly selects OpenPencil, verify the pinned
   source decision, open the editable `.op` file through a real supervised
   upstream surface, compare its reviewed PNG/SVG export with `DESIGN.md`,
   and bind paths, hashes, provenance, limitations, review, version/revision,
   and receiving owner in `HANDOFF.md`. If the tool is unavailable, expose
   the fallback and return the required portable handoff plus only any
   independently selected companions unchanged.
9. Write structured input, output, and proof files under
   `workspace/runs/<run-id>/`. A failed route writes failure evidence there;
   an explicit recovery writes a new run and points to its unresolved failed
   predecessor.
10. Append exactly one small JSON object to
    `workspace/history/runs.jsonl`. It records the run ID, timestamps, status,
    input/output/proof references, previous-run relation, and failure/recovery
    references. Use `null` for the first relevant run, `predecessor` for an
    ordinary continuation, and `recovery` only for a recovery route.
11. Promote into `examples/<slug>/` only when the owner explicitly requests
    curation. A promoted example must be standalone, listed in
    `examples/index.html`, understandable without ADS imports, and carry its
    brief, `DESIGN.md`, preview, assets, review proof, and local README.
12. Update `workspace/state/active.json` only as a small current-state pointer;
    do not use it as a second ledger or database. Keep durable learning notes
    intentional and short under `workspace/learning/`.

## Reference commands

From the repository root:

```sh
npm run trace -- --slug clean-clone-proof --preview --review --promote-example
npm run trace -- --slug source-decision-proof --source-decision --preview --review
npm run trace -- --slug recovery-proof --simulate-failure
npm run trace -- --slug recovery-proof --recover --preview --review --promote-example
npm run audit -- --scope repository
```

The tracer accepts `--root` for a fresh temporary checkout, which keeps the
repository's own operational state clean while proving creation/resume,
preview, review, failure, recovery, ledger relations, and gallery promotion.

The ADS-local `audit-design-system` method is a periodic, read-only
accumulated-state route. It is distinct from deterministic checks and
per-design Review, returns only `PASS`, `FAIL`, or `BLOCKED`, and never
creates a run, repair, export, promotion, or issue.

## Boundaries

HeroUI, Origin UI/Originkit, ThreeUI, and DesEngs are source references or
optional adapters selected per brief after source and license review. Never
vendor one as the universal ADS library. Preserve the local design and review
skills as internal repeatable methods; do not create another public route.

ADS can run first, last, or alone. AIOS, APT, ACS, a Project, or another caller
can supply ordinary resolved context, but this skill does not import, start, or
require them. It returns ordinary paths, human-readable handoff, and proof. No
raw prompts, credentials, customer truth, runtime protocol, registry, MCP,
central database, shared state, duplicated ACS truth, or synchronized
cross-System model belongs in ADS-owned evidence.
