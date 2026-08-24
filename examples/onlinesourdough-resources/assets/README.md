# Preview assets

| Asset                                 | Provenance                                                                                                                                         | Use                                                                                            |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `resources-folder-transparent.png`    | Copied byte-for-byte from `/Users/gustavanderson/Downloads/AIOS/projects/onlinesourdough-resources/public/assets/resources-folder-transparent.png` | The compact Resources identity cue in the sidebar.                                             |
| `resources-hero-agentic-v1.png`       | Prior reviewed poster generated with the built-in `image_gen` tool; retained at 1672×941.                                                          | Retained predecessor; not the active Home poster.                                              |
| `resources-vsl-motion-preview.mp4`    | Prior silent H.264 preview derived with `ffmpeg` from the v1 poster; six seconds, 1280×720.                                                        | Retained predecessor; not the active Home video source.                                        |
| `resources-hero-agentic-v2.png`       | Active built-in `image_gen` compositing edit from the v1 base plus two supplied pet references; cropped to 1672×940.                               | Active Resources poster with two small in-world pixel companions and one cabled local-AI node. |
| `resources-vsl-motion-preview-v2.mp4` | Active silent H.264 preview derived with `ffmpeg` from the v2 poster; six seconds, 1280×720, web-optimized.                                        | Replaceable active motion-preview asset; it is not the final VSL source.                       |
| `fonts/geist-sans-variable.woff2`     | Existing local Online Sourdough font from the read-only Resources source                                                                           | Reading text and controls.                                                                     |
| `fonts/geist-mono-variable.woff2`     | Existing local Online Sourdough font from the read-only Resources source                                                                           | Routes, labels, metadata, and ordered steps.                                                   |
| `fonts/geist-pixel-square.woff2`      | Existing local Online Sourdough font from the read-only Resources source                                                                           | Product name and display heading.                                                              |
| `fonts/LICENSE.txt`                   | Preserved font license bundled with the reviewed Workbench Resources reference                                                                     | Asset provenance.                                                                              |

No remote assets or external icon libraries are needed by this preview.

## Adapter

`adapters/heroui-disclosure.css` is the one ADS-owned integration proof. It is
original CSS that maps the existing AI Literacy disclosure to an accessible,
stateful interaction model studied from pinned HeroUI/React Aria sources. It
is not a copied component or a package dependency. See
[`adapters/README.md`](adapters/README.md).

## Prior v1 hero provenance

- **Mode:** Built-in `image_gen` generation mode, not CLI fallback. The source
  remains at `/Users/gustavanderson/.codex/generated_images/019ffab5-fbe6-7c30-b1c9-ca8cc19f0b28/exec-2114ce0a-7a10-4b0d-958e-3fbb44c1b56f.png`; this project owns the copied,
  versioned artifact above.
- **Reference role:** The two supplied screenshots were used only as mood and
  broad composition references. They were not edit targets, and the generated
  scene does not copy their branding, scenery, UI, text, or exact composition.
- **Final prompt:** `Use case: stylized-concept. Asset type: wide website hero
raster for resources.onlinesourdough Resources. Create an original wide
pixel-art hero scene for a calm business resources library with a practical
local-AI working context. Make a
clearly recognizable laptop/computer the primary visual anchor, centered
slightly right, with believable screen, keyboard, base, and abstract
connected workflow nodes. Keep the left 42% comparatively open and lower
contrast for live HTML copy. Use a warm quiet studio-workbench environment
with walnut, cream, terracotta, muted sage, and restrained desaturated blue
operational accents. Use crisp deliberate chunky pixels and a calm focused
mood. No text in the image. No logos, brand marks, watermark, letters,
numbers, readable UI text, buttons, copied third-party assets, exact
  reference recreation, malformed computer geometry, extra screens, neon
  cyberpunk gradients, purple AI glow, stock-photo realism, or clutter in the
  left copy area.`

## Active v2 hero provenance

- **Mode:** Built-in `image_gen` compositing edit, not CLI fallback. The
  generated source was copied into the project as
  `resources-hero-agentic-v2.png`; the active poster is cropped to the exact
  1672×940 production dimensions.
- **Input roles:** Image 1 was the v1 poster edit target. Image 2 was a
  supporting reference for the blue rounded terminal pet. Image 3 was a
  supporting reference for the orange blocky pet. The two supporting images
  informed silhouette and palette only; their screenshot backgrounds and
  presentation were not copied.
- **Final prompt:** `Use case: compositing. Asset type: wide website VSL hero
artwork for Resources.onlinesourdough. Edit Image 1 into one new original
warm lo-fi pixel-art Resources hero scene. Preserve the existing base
composition and recognizable scene: sunlit tactile wooden desk, laptop as
the dominant subject on the right half, abstract agent/system workspace on
the screen, plants, books, notebook, pen, mug, perspective, calm mood, warm
light, and the wide landscape crop. Integrate two small in-world pixel
companions derived from the supplied references: a compact blue rounded
terminal pet with a tiny cyan terminal face, and a compact orange blocky pet
with a simple expressive face. They must feel physically present on the
desk/near the laptop with matched pixel scale, lighting, contact shadows,
and perspective; they are secondary accents, never larger than the laptop or
visually dominant. Add one small generic unbranded local-AI mini computer
beside the laptop: a compact rounded-square brushed warm-gray box with one
restrained status light and a clearly visible cable running to the laptop.
Keep the upper-left and left-middle relatively quiet for live HTML cover
copy. No text, logos, brand marks, watermarks, extra mascots, extra screens,
photorealism, neon cyberpunk, or clutter.`
