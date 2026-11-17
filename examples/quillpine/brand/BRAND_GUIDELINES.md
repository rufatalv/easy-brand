# Quillpine Brand Guidelines

Extracted from `site/` by the brand-extractor skill. Untagged rules are **Observed**; other rules are tagged `[Inferred]` or `[Recommended]`. Details are in [references/](references/).

## 1. Identity in one paragraph

Quillpine looks like a well-kept research notebook. Warm paper surfaces and warm ink text carry a heavy, tightly set Fraunces display. Uppercase mono labels are marked with a §. A ruled-paper card with an orange margin line stands in for imagery. One forest-green band per page adds depth. The signal orange is used only as small marks.

## 2. Principles

1. **Paper, not screen.** Warm off-whites and warm near-black; never #FFF or #000.
2. **The notebook motif.** A ruled surface with a 32px pitch and a 48px orange margin line, used once per composition.
3. **Signal in small doses.** Orange appears only as marks: §, margin line, dashes, focus ring and highlighter.
4. **Three voices of type.** Serif speaks, sans explains, mono labels.
5. **Tight, heavy display.** Fraunces 600, line-height 0.95, tracking -0.03em, short headlines ending with a period.
6. **One dark band.** Forest green appears once per page, for quotes or emphasis.
7. **Hairlines over shadows.** Use 1px rule borders; the single lift shadow marks the one picked-up element.
8. **Calm motion.** A 16px fade-rise over 600ms with an 80ms stagger. Reduced motion is honored.

Full evidence and constraints are in [references/visual-dna.md](references/visual-dna.md).

## 3. Logo

- **File:** [assets/logos/quillpine-logo.svg](assets/logos/quillpine-logo.svg): an ink tile with a quill stroke, plus the Fraunces wordmark.
- **Placement:** top-left in navigation, 28px high. `[Inferred]` On marketing canvases, use bottom-left or top-left at about 4% of canvas height.
- **Not established:**
  - a reversed version for forest backgrounds;
  - clear-space rules;
  - a minimum size.

## 4. Color

| Use | Token |
|---|---|
| Canvas | `qp-paper` #F4EFE6 |
| Panels | `qp-paper-raised` #FBF8F2 |
| Text | `qp-ink` #1C1A17 / `qp-ink-muted` #5F5950 |
| Lines | `qp-rule` #D9D1C3 |
| Accent marks | `qp-signal` #E4572E |
| Accent text and hover | `qp-signal-ink` #B83A16 |
| Dark band | `qp-forest` #23332B with `qp-on-forest` #EDE6D8 |

Never use `qp-signal` for text: it measures 3.22:1 on paper. Contrast tables are in [references/colors.md](references/colors.md).

## 5. Typography

| Face | Used for |
|---|---|
| Fraunces 600 | Display (48–96px) and h2 (32–52px) |
| Fraunces 400 italic | Quotes |
| Inter | Body (17px / 1.6), h3, buttons and nav |
| JetBrains Mono 500 | Eyebrows and labels (12px, uppercase, 0.08em tracking) |

Details are in [references/typography.md](references/typography.md).

## 6. Layout

- 1200px container.
- Page margins of 24px, or 48px from 768px.
- 8px spacing scale.
- 128px section padding on desktop, with sections divided by hairlines.
- Everything left-aligned.
- Asymmetric 7:5 hero.

Details are in [references/composition.md](references/composition.md).

## 7. Shapes and graphics

Shapes:
- 14px radius on panels;
- pill radius on buttons;
- 4px radius on tags;
- 1px hairlines.

Graphic marks are typographic: §, —, → and the highlighter. There are no icons, illustrations or photographs. Details are in [references/graphics.md](references/graphics.md).

## 8. Imagery

Photography is **Not established**. Use the ruled note artifact or type-only layouts. Details are in [references/imagery.md](references/imagery.md).

## 9. Motion

The reveal is 600ms with `cubic-bezier(0.2, 0.7, 0.2, 1)`, a 16px rise and an 80ms stagger. Hovers take 180ms. Details are in [references/motion.md](references/motion.md).

## 10. Voice

Short, concrete, calm sentences in sentence case. Headlines end with a period. The CTA is "Start writing". Details are in [BRAND_VOICE.md](BRAND_VOICE.md).

## Do / Don't

| Do | Don't |
|---|---|
| Paper canvas with ink type | White canvas, gray UI |
| One highlighted word | Highlight whole sentences |
| § before section labels | Icons for section labels |
| Ruled note with real-sounding content | Stock photos or device mockups |
| Signal as a 1px line or glyph | Signal buttons or backgrounds |
| "Start writing →" | "Sign Up Now!" |
