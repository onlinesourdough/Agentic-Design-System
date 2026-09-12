# ADS-local skills

ADS owns the direct skills on this shelf. Their standard path is
`.agents/skills/<skill-name>/SKILL.md`.

- [`agentic-design-system`](agentic-design-system/SKILL.md) — primary
  orchestration from prior evidence through canonical portable `DESIGN.md`,
  review, cross-owner handoff, proof, and deliberate promotion across visual
  surface types.
- [`design-solution`](design-solution/SKILL.md) — focused design authoring and
  preview method used by the primary route for websites, apps, dashboards,
  reports, slides, and content visuals.
- [`review-design`](review-design/SKILL.md) — design and handoff review method
  used by the primary route.
- [`openpencil-workbench`](openpencil-workbench/SKILL.md) — internal strict
  loopback launcher and review method for an explicitly selected OpenPencil
  v0.8.4 source/export companion.
- [`audit-design-system`](audit-design-system/SKILL.md) — read-only periodic
  audit of accumulated ADS truth.

Add only ADS- or System-specific repeatable methods and evaluations here.
Cross-project and Global skills remain plugin- or harness-installed outside
ADS. AIOS, project templates, and releases may invoke these local skills, but
they do not overwrite this shelf.

Shared Spec, Build, Review and Ship come from the installed AIOS plugin.
This shelf contains specialist methods only; a domain review or audit adds
local criteria without copying the generic lifecycle. Direct tasks use the
current session; no lead/worker launch is required merely to enter this System.

Each maintained skill declares quoted SemVer under `metadata.version`, initially
`"1.0.0"`. Version a skill independently of the repository/package: patch for
compatible corrections or clarifications, minor for compatible capability or
routing additions, major for incompatible scope, authority, or output changes.
A substantive change to its owned references counts as a skill change. Leave
unaffected skills at their current versions. Local checks require unique names,
non-empty descriptions, quoted SemVer, and a complete linked shelf inventory.
The maintained frontmatter uses one-line scalar strings and a two-space-indented
`metadata` mapping; the zero-dependency validator checks this explicit subset.

The author validator uses a conservative one-line YAML string profile. Unquoted
root values begin with a letter; quote numeric or indicator-leading strings.
Metadata values are quoted strings. Unsupported YAML is rejected, and native
loader validation remains separate.
