# Brief — Harborlight operations workspace

- **Need:** A repair cooperative needs one daily surface for scheduling work,
  resolving blockers, and handing jobs between dispatch and technicians.
- **Audience:** Five dispatchers and 24 mobile repair technicians.
- **Desired decision:** Decide what needs attention before the next dispatch
  window and assign one owner.
- **Current constraint:** Status is split across calls, a calendar, and a shared
  spreadsheet, so blockers are discovered late.
- **Required data:** Dispatch window, job, customer area, technician, parts,
  status, due time, and blocker reason.
- **States:** Loading, no jobs, no matching jobs, permission denied, stale data,
  inline error, saved, and offline draft.
- **Constraints:** Keyboard-usable, dense but calm, mobile view prioritizes the
  next action rather than reproducing the full table.
- **Proof:** A dispatcher identifies overdue or blocked work and records an
  owner without leaving the workspace.
- **Receiving repository:** Solution-template.
