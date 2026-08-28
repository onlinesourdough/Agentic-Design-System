# Sources

Reviewed on 2026-08-06. Revisions are pinned so future updates can be compared
deliberately.

| Source                                                                          | Revision                                   | What we reused                                                                                           | What we did not reuse                                                              |
| ------------------------------------------------------------------------------- | ------------------------------------------ | -------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| [Google Design.md](https://github.com/google/design-md)                         | npm `@google/design.md@0.3.0`              | Canonical `DESIGN.md` format, linting, and token exports                                                 | No brand direction or universal visual style                                       |
| [elayadesign/ai-design-skills](https://github.com/elayadesign/ai-design-skills) | `1c1e97cb9878e236552c772092dda7adcdddbcb2` | Focused intake, one desired action, realistic content, responsive and interaction states                 | Its rigid universal font, spacing, radius, motion, and landing-page rules          |
| [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop)               | `d30eddb9e04562234f2070b5ee63ca4649d9a05e` | Minimum effective copy edit, specificity, portability test, and named-pattern review                     | Banned-word lists as an automatic substitute for judgment                          |
| [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md)   | `8147538b4226ae41e2487a9179e3bcc1f68e8554` | Optional research index showing how different brands express `DESIGN.md`                                 | The brand files themselves; they are neither defaults nor templates                |
| [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)                 | `e988add20dab0fa97d7a76781c48961c8184288e` | Composition, hierarchy, density, optical rhythm, complete states, semantic HTML, and anti-generic checks | Its overlapping skill catalog, hard-coded preferences, and high-complexity effects |

All onlinesourdough workflow text and skills in this repository are original
adaptations written for ADS.

## AI Literacy research

Reviewed on 2026-08-18 from the user-supplied AI Hero pages below. These pages
informed only structural principles for a concise reference: overview → what
you’ll understand → content links, grouped active navigation, and practical
progression. The AI Engineer Roadmap was used only as a structural reference for
organizing useful concepts; the Resources preview does not copy its text,
imagery, branding, diagram, CTA, lesson framing, layout, or exact engineering
framing. The five-concept AI Literacy reference is an original business-first
synthesis, not an AI Engineer profession track or second product.

- [LLM fundamentals](https://www.aihero.dev/llm-fundamentals)
- [Messages, system prompts, and reasoning tokens](https://www.aihero.dev/messages-system-prompts-and-reasoning-tokens)
- [What are tokens?](https://www.aihero.dev/what-are-tokens)
- [What is the context window?](https://www.aihero.dev/what-is-the-context-window)
- [What are tools?](https://www.aihero.dev/what-are-tools)
- [What is an agent?](https://www.aihero.dev/what-is-an-agent)
- [AI Engineer roadmap](https://www.aihero.dev/ai-engineer-roadmap)

## Curated migration sources

| Source                                       | Revision                                                                               | Use in this repository                                                                                                                                                                |
| -------------------------------------------- | -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `../design-md-workbench`                     | `30ef68f709f05225e23ac061fcb8da63cca31fba` plus reviewed worktree previews, 2026-08-06 | Curated preserved references for ArcitAI, Online Sourdough, and the historical Resources direction. Exploration labs, caches, generated screenshots, and unused assets were excluded. |
| `../onlinesourdough-resources`               | `01782bf3a46dadfe0de3f4cd9a4073ac2b5ba82f` plus read-only worktree asset, 2026-08-06   | Exact Resources IA/content source and `public/assets/resources-folder-transparent.png`; no application code was copied into the active direction.                                     |
| User-provided AIHero/Matt Pocock screenshots | 2026-08-06                                                                             | Research only for calm documentation hierarchy, sidebar density, and content/right-column rhythm. No brand, copy, asset, or exact layout was reused.                                  |

## UI source audit

HeroUI, Origin UI/Originkit, ThreeUI, and DesEngs were reviewed for a possible
per-brief source or adapter. They are not a vendored default. The pinned
revisions, license signals, accessibility and framework fit, maintenance
signals, visual decisions, and the one local integration proof are recorded in
[`SOURCE_AUDIT.md`](SOURCE_AUDIT.md).
