---
name: agentic-design-system
description: Route a persistent Agentic Design System run from prior evidence through workspace preview, review, ledger proof, and deliberate example promotion.
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
2. Read the active `workspace/BRIEF.md` and `workspace/DESIGN.md`. Resume the
   active example when its state says it is in progress, or create the smallest
   example work surface needed for the resolved intent.
3. Use `$design-solution` for the focused design method when the direction or
   preview needs authoring. Keep the brief, design direction, preview, and
   assets together in the active work surface.
4. Run the local preview from `workspace/engine/serve.mjs`, inspect desktop
   and mobile widths, and verify landmarks, keyboard-visible focus, reduced
   motion, and relevant loading, empty, error, success, permission, and
   offline states.
5. Use `$review-design` as the review method. Record its result and concrete
   proof references in the run evidence; a review result is not a promotion
   decision by itself.
6. When a creative route explicitly selects OpenPencil, verify the pinned
   source decision, open the editable `.op` file through a real supervised
   upstream surface, compare its reviewed PNG/SVG export with `DESIGN.md`,
   and bind paths, hashes, provenance, limitations, review, version/revision,
   and receiving owner in `HANDOFF.md`. If the tool is unavailable, expose
   the fallback and return the ordinary HTML/tokens handoff unchanged.
7. Write structured input, output, and proof files under
   `workspace/runs/<run-id>/`. A failed route writes failure evidence there;
   an explicit recovery writes a new run and points to its unresolved failed
   predecessor.
8. Append exactly one small JSON object to
   `workspace/history/runs.jsonl`. It records the run ID, timestamps, status,
   input/output/proof references, previous-run relation, and failure/recovery
   references. Use `null` for the first relevant run, `predecessor` for an
   ordinary continuation, and `recovery` only for a recovery route.
9. Promote into `examples/<slug>/` only when the owner explicitly requests
   curation. A promoted example must be standalone, listed in
   `examples/index.html`, understandable without ADS imports, and carry its
   brief, `DESIGN.md`, preview, assets, review proof, and local README.
10. Update `workspace/state/active.json` only as a small current-state pointer;
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

AIOS and APT can supply resolved context from outside this checkout, but this
skill does not import, start, or require them. It returns ordinary paths and
proof. No raw prompts, credentials, customer truth, central database, or
shared cross-System model belongs in ADS-owned operational evidence.
