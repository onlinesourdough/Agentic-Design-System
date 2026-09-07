# Packaging revision — existing CLI route

Status: prepared for lead review; NOT generator-compatible yet.

The previous handoff-r1-fd221d5478b4 snapshot remains unchanged and unaccepted
evidence. The lead rejected its manual packaging route only.
Same worker/session: 01a072d2-1699-7bf0-97fa-612e363bef33.
No previous artifact or image is superseded or deleted.

## Source

`handoff-source-r1-cli/` contains the exact approved DESIGN.md and all 77
approved PNGs at their original relative paths, plus the new minimal BRIEF.md.
No gallery, manifest or root provenance companion is selected.

## Actual parser result and remaining decision

The existing parser accepts the four required fields in the new BRIEF.md.
However, create-handoff.mjs also calls requiredStrongField on DESIGN.md for
`Known limitations`. The exact approved DESIGN.md lacks this required field.
Observed parser failure: `DESIGN.md lacks a non-empty **Known limitations:** field.`

Thus exact approved DESIGN bytes and successful execution of the unmodified
generator are incompatible with the current source. The CLI has no limitations
override. Adding the field to BRIEF.md would not satisfy it.
No source DESIGN change, new generator, manual binder or generation was performed.

Smallest proposed follow-up for lead decision: authorize a packaging-only addition
of `- **Known limitations:**` to the sibling source DESIGN, retaining all existing
text, then review its new hash together with this BRIEF and the unchanged PNG
hashes. This has NOT been applied. If exact DESIGN bytes must remain mandatory,
the existing generator cannot deliver this package.

After the lead accepts the compatible source, record its exact bound REVIEW.md.
Do not reuse the old brief PASS as approval for the new brief.

## Exact intended CLI (not executed)

From the ADS repository root, after compatibility and review are resolved:

```sh
npm run handoff -- workspace/runs/onlinesourdough-stack-r1/handoff-source-r1-cli workspace/runs/onlinesourdough-stack-r1/handoff-r1-cli --receiving-owner 'Gustav Anderson / onlinesourdough' \
  --asset 'assets/exports/acs-banner-1536x512.png' \
  --asset 'assets/exports/acs-icon-1024.png' \
  --asset 'assets/exports/acs-icon-128.png' \
  --asset 'assets/exports/acs-icon-512.png' \
  --asset 'assets/exports/acs-icon-64.png' \
  --asset 'assets/exports/ads-banner-1536x512.png' \
  --asset 'assets/exports/ads-icon-1024.png' \
  --asset 'assets/exports/ads-icon-128.png' \
  --asset 'assets/exports/ads-icon-512.png' \
  --asset 'assets/exports/ads-icon-64.png' \
  --asset 'assets/exports/aios-banner-1536x512.png' \
  --asset 'assets/exports/aios-icon-1024.png' \
  --asset 'assets/exports/aios-icon-128.png' \
  --asset 'assets/exports/aios-icon-512.png' \
  --asset 'assets/exports/aios-icon-64.png' \
  --asset 'assets/exports/atlas-banner-1536x512.png' \
  --asset 'assets/exports/atlas-icon-1024.png' \
  --asset 'assets/exports/atlas-icon-128.png' \
  --asset 'assets/exports/atlas-icon-512.png' \
  --asset 'assets/exports/atlas-icon-64.png' \
  --asset 'assets/exports/org-banner-1536x512.png' \
  --asset 'assets/exports/org-icon-1024.png' \
  --asset 'assets/exports/org-icon-128.png' \
  --asset 'assets/exports/org-icon-512.png' \
  --asset 'assets/exports/org-icon-64.png' \
  --asset 'assets/exports/powerbi-banner-1536x512.png' \
  --asset 'assets/exports/powerbi-icon-1024.png' \
  --asset 'assets/exports/powerbi-icon-128.png' \
  --asset 'assets/exports/powerbi-icon-512.png' \
  --asset 'assets/exports/powerbi-icon-64.png' \
  --asset 'assets/exports/project-banner-1536x512.png' \
  --asset 'assets/exports/project-icon-1024.png' \
  --asset 'assets/exports/project-icon-128.png' \
  --asset 'assets/exports/project-icon-512.png' \
  --asset 'assets/exports/project-icon-64.png' \
  --asset 'assets/exports/resources-banner-1536x512.png' \
  --asset 'assets/exports/resources-icon-1024.png' \
  --asset 'assets/exports/resources-icon-128.png' \
  --asset 'assets/exports/resources-icon-512.png' \
  --asset 'assets/exports/resources-icon-64.png' \
  --asset 'assets/exports/review-banner-1536x512.png' \
  --asset 'assets/exports/review-icon-1024.png' \
  --asset 'assets/exports/review-icon-128.png' \
  --asset 'assets/exports/review-icon-512.png' \
  --asset 'assets/exports/review-icon-64.png' \
  --asset 'assets/exports/skills-banner-1536x512.png' \
  --asset 'assets/exports/skills-icon-1024.png' \
  --asset 'assets/exports/skills-icon-128.png' \
  --asset 'assets/exports/skills-icon-512.png' \
  --asset 'assets/exports/skills-icon-64.png' \
  --asset 'assets/exports/system-banner-1536x512.png' \
  --asset 'assets/exports/system-icon-1024.png' \
  --asset 'assets/exports/system-icon-128.png' \
  --asset 'assets/exports/system-icon-512.png' \
  --asset 'assets/exports/system-icon-64.png' \
  --asset 'assets/masters/acs-banner.png' \
  --asset 'assets/masters/acs-icon.png' \
  --asset 'assets/masters/ads-banner.png' \
  --asset 'assets/masters/ads-icon.png' \
  --asset 'assets/masters/aios-banner.png' \
  --asset 'assets/masters/aios-icon.png' \
  --asset 'assets/masters/atlas-banner.png' \
  --asset 'assets/masters/atlas-icon.png' \
  --asset 'assets/masters/org-banner.png' \
  --asset 'assets/masters/org-icon.png' \
  --asset 'assets/masters/powerbi-banner.png' \
  --asset 'assets/masters/powerbi-icon.png' \
  --asset 'assets/masters/project-banner.png' \
  --asset 'assets/masters/project-icon.png' \
  --asset 'assets/masters/resources-banner.png' \
  --asset 'assets/masters/resources-icon.png' \
  --asset 'assets/masters/review-banner.png' \
  --asset 'assets/masters/review-icon.png' \
  --asset 'assets/masters/skills-banner.png' \
  --asset 'assets/masters/skills-icon.png' \
  --asset 'assets/masters/system-banner.png' \
  --asset 'assets/masters/system-icon.png'
```

The command uses the existing generator unchanged, selects each of the 77 assets
explicitly, and does not select preview, token exports or unsupported root files.
The destination does not yet exist. No handoff generation occurs before lead
acceptance. Receiver acceptance, shared-ledger append and receiving placement
remain separate later steps.
