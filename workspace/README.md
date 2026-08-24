# ADS workspace

`workspace/` is the active operational truth for Agentic Design System.

- `BRIEF.md`, `DESIGN.md`, and `index.html` are the current working direction
  and technical preview.
- `REVIEW.md` records the latest design-method result and any proof limitation.
- `state/` holds a small current-state pointer, never a history replacement.
- `runs/` holds structured evidence for route attempts.
- `history/runs.jsonl` is append-only and relates predecessors and recoveries.
- `learning/` holds short, intentional notes retained for future routes.
- `engine/` contains optional preview, lint, export, check, test, and tracer
  tooling. It is implementation detail, not another ADS concept.

The primary System skill reads this surface before it starts work. A clean
checkout can use its `--root` tracer option to exercise the route in a fresh
operational directory without importing another System.
