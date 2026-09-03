---
name: agentic-design-system
description: Route approved, portable visual directions for websites, applications, dashboards, reports, slides, and content surfaces from prior evidence through canonical DESIGN.md, preview, review, cross-owner handoff, ledger proof, and deliberate example promotion.
---

# Agentic Design System primary System skill

This is the one public ADS entry point. It is a filesystem method, not a
service or framework. It works from a clean checkout and keeps the active
design work in `workspace/` until a deliberate curation decision promotes an
example into `examples/`.

The Codex conversation is the caller-facing input/output surface. Receive
links, screenshots, prior work, or vague intent there; return the selected
direction and relevant proof there. Create portable `DESIGN.md` and optional
companions only when durable design or cross-owner handoff is needed. Never ask
the caller to browse or configure a separate reference catalogue.

## Route

1. Read `workspace/history/runs.jsonl` and inspect records relevant to the
   requested example or brief. Use references and run IDs; never copy a raw
   request or private context into the ledger.
2. Read the active `workspace/BRIEF.md` and `workspace/DESIGN.md`. Confirm that
   the brief makes outcome and receiving owner/reuse scope, audience/job,
   surfaces/states, material constraints, source rights/provenance, review mode,
   and separate Review owner and receiver-acceptance decision inspectable.
   Review mode is exactly `independent` or `owner`; `Review owner` is a
   non-empty named identity distinct from the receiving project or repository.
   Resume active work when its state says
   it is in progress, or create the smallest surface needed for the intent.
   When the caller supplies visual evidence or the direction remains
   unresolved, read
   [`references/adaptive-references.md`](references/adaptive-references.md).
   Preserve caller media as pointer metadata and extracted signals, apply its
   owner-first precedence, and select exactly one `direct`, `discover`, or
   `explore` mode before authoring. Route evidence remains subordinate to
   canonical `DESIGN.md`.
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
6. Use `$review-design` as the review method. The evidence names its reviewer,
   records `PASS`, binds the reviewed `DESIGN.md` SHA-256, and lists the path and
   SHA-256 of every pre-existing selected preview, asset, or tool-native
   source/native export. Use the `Reviewed source companion` evidence label.
   Deterministic CSS, design-token, and Tailwind exports are generated later
   from the exact reviewed `DESIGN.md`; bind their output hashes and source
   DESIGN hash in the handoff rather than requiring them as pre-existing Review
   evidence. A review result is not a promotion decision by itself.
7. When reviewed work crosses an owner boundary, generate `HANDOFF.md` with the
   existing handoff route. Verify `ADS-HANDOFF/1` identity/revision, receiving
   owner/outcome, source revision, included relative paths and SHA-256 values,
   provenance/licensing, named Review state/mode, limitations, and explicit
   acceptance. In both modes, the evidence reviewer must match the brief's
   declared Review owner; never compare that identity with `--receiving-owner`.
   A matching independent reviewer is sufficient for `independent`. For
   `owner`, stop with `waiting-owner` until that exact Review owner records the
   bound PASS and all selected source-companion hashes. Generation starts
   `PENDING`; receiver acceptance is separate, an accepted snapshot is
   immutable, and a later direction requires a new reviewed revision and
   re-acceptance.
8. When a creative route explicitly selects OpenPencil, use the internal
   `$openpencil-workbench` method to verify the pinned source decision, return
   its strict-loopback URL to the Codex-compatible built-in browser, open the
   editable `.op` file through the real supervised upstream surface, compare
   its reviewed PNG/SVG export with `DESIGN.md`,
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
New source discovery starts only for one concrete unresolved role and may
select no more than one primary source plus one optional adapter after current
first-party and rendered-task evaluation. Dated practitioner posts are
discovery signals, not standalone adoption authority.

ADS can run first, last, or alone. AIOS, APT, ACS, a Project, or another caller
can supply ordinary resolved context, but this skill does not import, start, or
require them. It returns ordinary paths, human-readable handoff, and proof. No
raw prompts, credentials, customer truth, runtime protocol, registry, MCP,
central database, shared state, duplicated ACS truth, or synchronized
cross-System model belongs in ADS-owned evidence.

A receiving System copies only its explicitly accepted immutable snapshot. It
never live-syncs the ADS workspace and never sends an automatic recursive
request back into ADS.
