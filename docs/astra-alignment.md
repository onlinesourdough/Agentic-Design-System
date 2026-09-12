# Instruction alignment — 2026-09-12

The accepted maintenance contract applies the discovery, conditional-reference,
and completion guidance in [OpenAI's Astra article](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra).
This is an instruction cleanup, not evidence of model performance or a change
to any model default. Shared lifecycle and external specialist skills remain
external; local methods retain their domain authority.

ADS root instructions now route task-specific source, handoff, and editor
procedures to their existing owners. Repository maintenance requires no design
selection or production run. The primary skill delegates fragile OpenPencil
mechanics to its workbench method. Named owner review, exact companion hashes,
receiver acceptance, immutable handoffs, and source rights remain required.
The original workbench prose-marker test was replaced by reference/inventory
checks; executable workbench and handoff tests still cover source preservation,
review identity, and immutable snapshots. Lead behavior probes assess routing
and live-surface instruction use; static metadata checks cannot establish that.

Audit scope included the root AGENTS, all five maintained local skills, their
index and the adaptive-reference method. No production artifacts were edited.

Local skill versions start at quoted `metadata.version: "1.0.0"`, independently
of package releases. The [skill index](../.agents/skills/README.md) records bump
criteria and the maintained scalar frontmatter profile. Disposable tests cover
metadata schema, SemVer, duplicate/missing inventory, links and symlinks. Model
behavior probes and final acceptance belong to the lead.

Lead verification installed the lockfile’s author-only dependencies in the isolated
checkout. Final formatting/checks and all 45 tests pass. Skill Creator validates
all five skills; no live editor or production design was launched.
