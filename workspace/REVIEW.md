# Active route review

Review: design
Result: PASS
Checks: [job, specificity, voice, composition, states, accessibility, source safety, contract]
Next: create handoff
Findings: []

Scope: the active ADS route console in `workspace/` and the curated
`examples/onlinesourdough-resources/` direction.

The first viewport names the audience, route, current status, and one primary
resume action. Copy is specific to ADS operational truth; route IDs and proof
paths are visible. The composition uses a route spine and field-note rhythm
instead of a generic analytics dashboard. Loading, success, error, empty,
permission, offline, hover, active, focus, reduced-motion, failure, and
recovery states are represented where relevant. Landmarks, skip links, labels,
heading order, local assets, and keyboard-visible focus are present. The
Resources adapter is original local CSS with a documented source decision and
no external component package.

Available proof: Design.md lint, repository checks, clean-copy tracer runs,
HTTP preview responses, local-link/state scans, and an in-app browser pass all
pass. The workspace was inspected at 1440×1000 and 390×844 with screenshots,
no horizontal overflow, semantic landmarks, reduced-motion rules, and a
visible focus ring. The gallery and Resources example were opened at both
widths; the local `heroui-disclosure` adapter expanded with `aria-expanded`,
`aria-controls`, and its focused state. Direct state controls exercised
success, loading, error, empty, permission, and offline fixtures. The in-app
keyboard driver focused controls and exposed the focus ring but did not
capture native Enter/Tab activation events in this session; semantic buttons
and the direct interaction path remain present, so that tool limitation is
explicit rather than claimed as event-level proof.
