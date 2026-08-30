# Brief — Harborlight operations workspace

- **Need:** A repair cooperative needs one daily surface for scheduling work,
  resolving blockers, and handing jobs between dispatch and technicians.
- **Audience:** Five dispatchers and 24 mobile repair technicians.
- **Desired decision:** Decide what needs attention before the next dispatch
  window and assign one owner.
- **Receiving outcome:** Implement the approved workspace hierarchy, responsive
  behavior, and operational states in the receiving application without ADS as
  a runtime dependency.
- **Current constraint:** Status is split across calls, a calendar, and a shared
  spreadsheet, so blockers are discovered late.
- **Required data:** Dispatch window, job, customer area, technician, parts,
  status, due time, and blocker reason.
- **States:** Loading, no jobs, no matching jobs, permission denied, stale data,
  inline error, saved, and offline draft.
- **Constraints:** Keyboard-usable, dense but calm, mobile view prioritizes the
  next action rather than reproducing the full table.
- **Source/reference rights, provenance, and licensing:** The cooperative,
  data, direction, and preview are fictional ADS-owned proof; they contain no
  customer truth, external brand asset, or copied component.
- **Ownership boundary:** ADS owns visual hierarchy, style/voice expression,
  interaction direction, and reusable visual assets. The receiving Project
  owns data behavior and implementation after acceptance.
- **Proof:** A dispatcher identifies overdue or blocked work and records an
  owner without leaving the workspace.
- **Receiving project or repository:** The implementation project selected by its owner.
- **Review and acceptance owner:** ADS Review approves the portable direction;
  the selected application owner explicitly accepts any cross-owner snapshot.
