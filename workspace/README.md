# ADS workspace

`workspace/` is the active operational truth for Agentic Design System.

- `BRIEF.md` is the resolved input, `DESIGN.md` is always the canonical portable
  human-readable visual direction, and `index.html` is a supporting technical
  preview.
- `REVIEW.md` records the latest design-method result and any proof limitation.
- `openpencil/` exists only for the active explicitly selected creative route:
  one editable source and its reviewed export boundary. It is not required for
  ordinary work and never replaces `DESIGN.md`.
- `state/` holds a small current-state pointer, never a history replacement.
- `runs/` holds structured evidence for route attempts.
- `history/runs.jsonl` is append-only and relates predecessors and recoveries.
- `learning/` holds short, intentional notes retained for future routes.
- `engine/` contains optional preview, lint, export, check, test, tracer, and
  read-only audit tooling. It is implementation detail, not another ADS
  concept.

The primary System skill reads this surface before it starts work. A clean
checkout can use its `--root` tracer option to exercise the route in a fresh
operational directory without importing another System.

When delivery crosses to another owner, the existing handoff generator creates
the `ADS-HANDOFF/1` `HANDOFF.md` snapshot with receiver/outcome, revision,
paths/hashes, provenance/licensing, Review, limitations, and explicit
acceptance. Same-owner active work needs no binder. Sibling capability gaps are
returned to the caller as bounded suggestions and are never auto-run.
The minimal cross-owner snapshot needs no preview, asset, token export, or
OpenPencil file; each companion is added only with its explicit handoff option.
