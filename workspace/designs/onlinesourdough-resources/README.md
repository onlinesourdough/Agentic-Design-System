# resources.onlinesourdough — Resources design direction

This is a self-contained design direction for the Resources product. It keeps
the warm Online Sourdough material language, local Geist fonts, supplied
pixel-folder cue, and active v2 computer scene inside a quiet documentation-like
shell.

`DESIGN.md` is the canonical portable visual direction. The HTML preview,
fonts, imagery, motion preview, adapter, tokens, exports, and any editable
source are optional referenced companions. A cross-owner delivery adds the
versioned `HANDOFF.md` binder and remains pending until explicitly accepted;
the receiving Project owns implementation, while ACS owns editorial/content
production and edit/render/package/publish execution when selected.

The sidebar has four static group headings—Explore, Business Freedom Ecosystem,
Open Source, and In Practice—with only their listed children navigable. Explore
contains a quiet keyboard-accessible AI Literacy disclosure before Newsletter;
the homepage folders use the same four names and open the first child in each
group.
The Business Freedom Ecosystem is the business-first method; AI, agents, and
software are the primary solution mechanism; AI Workspace is the configured
technical base inside it; AIOS Template is the open-source foundation.

Positioning: Business Freedom Ecosystem for solo business owners who want to
become more techy and build more of their business with AI and software.

The locked children are:

- Explore: Start Here, What’s New, AI Literacy, Newsletter
- Business Freedom Ecosystem: Understand your business, Choose what to change,
  Build the solution, Launch and run it
- Open Source: AIOS Template, Solution Template, Skills
- In Practice: Arc’IT AI, AIOS Desktop, Power BI Template

The delivery routes are Resources · do it yourself, The Fermentary · done with
you, and Complete Bake · done for you. Arc’IT AI remains a separate In Practice
external destination. These names appear as concise orientation copy without
turning the preview into a pricing page or claiming published proof.

The overview keeps three compact layers: business architecture finds the right
constraint through a fixed, individually applied journey; AI, agents, and
software are the primary solution mechanism, with AI Workspace as the concrete
configured base inside the ecosystem; business bandwidth/freedom is the outcome
through keep, remove, automate, or delegate. Resources, The Fermentary, and
Complete Bake are delivery modes for the same layers. The preview does not
imply meeting cadence, capacity, or guaranteed outcomes.

## ADS adapter proof

This curated example includes one local `heroui-disclosure` adapter under
`assets/adapters/`. It adapts the accessible disclosure state model to the
existing static HTML route—native button semantics, `aria-expanded`, keyboard
activation, hover, focus, and reduced motion—without vendoring HeroUI or
adding a React/Tailwind runtime. The source decision and license review are in
`../../docs/SOURCE_AUDIT.md`; the adapter README records the exact proof
surface.

Explore also contains the quiet `AI Literacy` disclosure immediately before
`Newsletter`. It contains `Overview`, `Context`, `How AI works`, `Tools`,
`Agents`, and `Skills`; the five concept routes are nested links rather than a
new top-level group. The parent is a neutral text-and-chevron label, while only
the nested links receive hover and active surfaces. Only the exact selected
nested link owns `aria-current="page"`; the parent exposes disclosure state
through `aria-expanded`. Expanding it from the collapsed state opens
`/explore/ai-literacy` with `Overview` selected;
collapsing keeps the current route. AI Literacy makes technical concepts clear
enough to choose and build responsibly, then connects that language to Business
Freedom Ecosystem, AIOS, and AI Workspace without making AI Workspace a
mandatory first step.

## Files

- `BRIEF.md`: resolved need, locked IA, underlying 00–08 sequence, states,
  constraints, and proof.
- `DESIGN.md`: portable tokens, composition fingerprint, exact shelf behavior,
  component rules, page contract, and receiving-project guidance.
- `index.html`: static hash-routed preview with the responsive shell, local v2
  video player, data-driven ecosystem pages, contextual toolkit examples,
  the AI Literacy disclosure/reference and concept routes, minimal reading
  pages, search, themes, forms, external-link safety, and explicit states.
- `assets/resources-folder-transparent.png`: exact 640×640 folder cue used in
  the compact sidebar identity treatment.
- `assets/resources-hero-agentic-v2.png`: active 1672×940 computer-centered
  poster with two small in-world pixel companions and one unbranded cabled
  local-AI node.
- `assets/resources-vsl-motion-preview-v2.mp4`: active six-second silent local
  motion preview derived from the v2 poster. It is replaceable design-preview
  media, not a final VSL source.
- `assets/resources-hero-agentic-v1.png` and
  `assets/resources-vsl-motion-preview.mp4`: retained reviewed predecessors;
  they are not active Home sources.
- `assets/fonts/`: local Geist Sans, Geist Mono, Geist Pixel, and license.

No remote assets or external icon libraries are needed by this preview. The
only verified external destinations are Newsletter
(`https://gustavonline.com/newsletter`) and Arc’IT AI (`https://arcitai.com/`),
and both use `target="_blank" rel="noopener noreferrer"`.

## Underlying content contract

The visible Business Freedom Ecosystem children are four working stages, not a
new category for the existing curriculum. Their child resources preserve the
sequence: 00–02 under `Understand your business`, 03–04 under `Choose what to
change`, 05–06 under `Build the solution`, and 07–08 under `Launch and run it`.
00 is the orientation resource `Start Here`; 01–08 keep their existing
semantic titles and intent. Each stage also shows contextual toolkit examples
as plain child links; their draft/internal truth stays in the data contract.

Start Here, What’s New, AI Literacy, and the four ecosystem stages use the same
quiet reading pattern: one H1 and summary, short headings, plain links or
bullets, and generous whitespace. The visible stage pages do not repeat the
curriculum prefixes, numbered labels, dense cards, repeated rules, or
status/meta scaffolding; the existing content and routes remain in the data
contract. Ordinary pages have no generic resource/status panels, and an
explainer block appears only when a playable source exists.

The receiving project should implement one route shell, such as
`app/(resources)/template.tsx` or its framework equivalent. That shell owns page
padding, the shared 720px reading track, and rhythm. The topbar breadcrumb,
page header, route layout, and ordinary page actions all use that same centered
track inside the main surface. Shared `ResourcePage` and `ResourceSubpage`
components own the semantic H1, summary, ordered body, and child presentation;
route files choose data rather than bespoke widths or margins. The locked
contract is one calm reading column; H2 for meaningful
sections; H3 only for real nested content; plain paragraphs, compact bullets,
and text links; at most one divider between genuinely separate long sections;
and no card/panel surface for normal prose. Draft/access truth stays in the
data contract rather than repeated in the UI.

## AI Literacy content contract

The AI Literacy page is a small Explore reference, not a course, module
sequence, or separate product. Its disclosure contains `Overview` and five
unnumbered concepts:

`Context`; `How AI works`; `Tools`; `Agents`; `Skills`.

The canonical concept routes are `/explore/ai-literacy/context`,
`/explore/ai-literacy/how-ai-works`, `/explore/ai-literacy/tools`,
`/explore/ai-literacy/agents`, and `/explore/ai-literacy/skills`. The overview
has one short intro, at most three concise “What you’ll understand” bullets,
and a `Concepts` link list. Concept pages keep their summary and concise key
points as ordinary reading content; they do not show an unloaded video or
explainer placeholder. No commercial proof, published inventory, or
professional AI Engineer pathway is implied. Old Models, Workflows, numbered,
and Open Source AI Literacy routes are not canonical.

The minimal relation-shaped data interface is record kind (`page`, `subpage`,
or contextual `toolkit`), parent relation, slug, title, summary, ordered
body/children, access/status, and sort order. Breadcrumbs derive from parent
relations. No public URL, commercial proof, published inventory, or technical
status is implied by this static preview.
