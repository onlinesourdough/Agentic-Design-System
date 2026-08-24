# Brief — Agentic Design System route console

- **Need:** Keep repeated design work visible as an operational route: inspect
  what ran before, resume the active brief, preview and review the direction,
  and decide what deserves a durable gallery place.
- **Audience:** The owner and the agent operating ADS, plus a reviewer who
  needs to verify the design evidence without knowing the repository history.
- **Desired action or decision:** Resume the active route, inspect its brief,
  design, preview, review result, and source choices, then deliberately
  promote the result when the proof is sufficient.
- **Current constraint:** The old workbench was a singleton preview with no
  durable operational state or relation between successful, failed, and
  recovered runs. Examples must remain readable and owned by the main gallery.
- **Required content and data:** Active brief and design, route status,
  previous-run relation, review result, source/adaptor decision, curated
  examples, and honest proof references. No customer data, credential, raw
  request, or external service is needed.
- **States:** Loading while resuming a route; success when the active preview
  is ready; error when a review or preview cannot be read; empty when no prior
  run exists; permission when promotion is intentionally not selected; and
  offline guidance when a local preview is unavailable.
- **Constraints:** Three visible roots (`workspace/`, `examples/`, `docs/`);
  `workspace/engine/` is optional tooling; local assets only; keyboard-visible
  focus; reduced motion; mobile and desktop widths; standalone operation with
  the pinned Node/Python toolchain; no AIOS/APT package or service coupling.
- **Proof:** A reviewer can identify the active decision in the first viewport,
  resume the route, switch state fixtures, open the gallery, inspect evidence,
  and understand the create/preview/review/ledger/promotion flow at roughly
  1440×1000 and 390×844 without horizontal overflow.
- **Receiving project or repository:** Agentic Design System, this repository
  as the canonical design-workbench owner until a later implementation project
  deliberately accepts a copied direction.
