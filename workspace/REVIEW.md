# Active route review

Review: design
Result: PASS
Checks: [job, specificity, voice, composition, states, accessibility, source safety, contract, optional native source]
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

## Optional OpenPencil route

Review: native source and export
Result: PASS

OpenPencil release `v0.8.4` reopened the final ADS-owned route console as 191 editable
nodes, returned its document summary and layout tree, saved
`openpencil/route-console.op`, and exported the selected root frame to
`openpencil/exports/route-console.png` at 1440×2129. The reviewed raster was
visually inspected at original resolution. Its warm paper field, deep-teal
header and action, rust route marker, asymmetric proof rail, gallery rhythm,
state lab, content, and hierarchy agree with this `DESIGN.md`.

The importer initially rendered the HTML skip link as a visible top strip
because percentage transform translation had no definite imported size. That
single importer artifact was removed in the editable source before the final
export; the semantic HTML preview still owns the real accessible skip link.
The final source SHA-256 is
`cdd323e1fcf0b055d226ad0d8078eddebb9d95fc891913f0296efe4bee73ec92`
and the reviewed PNG SHA-256 is
`270623d4f40c9740254a343059c358e96fe7f50beaae280536923272bd957165`.

Known limitations: v0.8.4 reported seven non-blocking design-lint warnings
from HTML/CSS approximation (container contrast, sibling sizing/radii/padding,
and three 50px shadows); it does not preserve reduced-motion media behavior or
browser interaction in a raster. The CLI archive is a client and required the
separately verified v0.8.4 desktop binary for the supervised file-backed
surface. The release export command supports PNG but not SVG. The PNG is
reviewed visual evidence, not proof of browser accessibility or pixel-level
equivalence; the semantic HTML preview remains authoritative for those checks.
