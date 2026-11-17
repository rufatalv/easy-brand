---
name: quillpine-brand-identity
description: Apply the Quillpine brand identity when creating any visual or written asset — social posts, stories, ads, OG images, emails, landing-page sections or UI. Use whenever the user asks for something "on-brand", "in Quillpine style", or for Quillpine marketing or design output. Provides tokens, typography roles, color rules, the ruled-notebook motif, composition, motion and voice extracted from the product.
---

# Quillpine Brand Identity

Quillpine looks like a well-kept research notebook. Warm paper surfaces and warm ink text carry a heavy, tightly set Fraunces display. Uppercase mono labels are marked with a §. A ruled-paper card with an orange margin line stands in for imagery. One forest-green band per page adds depth. The signal orange is used only as small marks, never as a fill.

## Locate the brand system

1. If `brand/` exists in the repo, `brand/tokens/*.json` and `brand/tokens/colors.css` are canonical. Start templates from `brand/templates/`.
2. Otherwise, use the bundled values in [references/design-tokens.md](references/design-tokens.md).

## Core principles

1. **Paper, not screen.** Use `#F4EFE6` and `#FBF8F2` surfaces with `#1C1A17` ink. Never use #FFF or #000.
2. **Notebook motif.** A ruled surface with 32px lines and a 1px orange margin line at 48px. Use it at most once per composition.
3. **Signal in small doses.** `#E4572E` appears only as §, margin lines, dashes, focus rings and the highlighter. Never set text in it.
4. **Three voices of type.** Fraunces speaks, Inter explains, JetBrains Mono labels.
5. **Tight, heavy display.** Fraunces 600, line-height 0.95, tracking -0.03em, a short sentence ending in a period, at most one highlighted word.
6. **One dark band.** Forest `#23332B` is the only dark surface.
7. **Hairlines over shadows.** Use 1px `#D9D1C3` borders. One lift shadow is allowed, on the single picked-up element.
8. **Calm motion.** A 16px fade-rise, 600ms, `cubic-bezier(.2,.7,.2,1)`, 80ms stagger.

## Workflow

1. **Identify the output:** platform, size and medium (HTML/PNG, React, copy only).
2. **Pick a composition** from [references/composition.md](references/composition.md):
   - editorial (type-led on paper);
   - quote (forest band);
   - product (headline plus ruled note, mirroring the hero).
3. **Typography:** apply roles from [references/typography.md](references/typography.md); don't pick sizes ad hoc.
4. **Color:** apply roles from [references/design-tokens.md](references/design-tokens.md).
5. **Graphics:** add one or two signatures (§ eyebrow, ruled note, highlighter).
6. **Imagery:** follow [references/imagery.md](references/imagery.md). There is no photography; use the ruled note or type only.
7. **Motion:** if the asset is animated, follow [references/motion.md](references/motion.md).
8. **Copy:** follow [references/content-generation.md](references/content-generation.md).
9. **Validate** against the checklist below.
10. **Export:** render HTML to PNG with headless Chrome at the exact size.

## Request playbooks

- **"Create a social media post":**
  1. Pick the size: 1080×1350 feed, or 1080×1920 story with the 250/340px safe area.
  2. Use the editorial or quote composition.
  3. Write a headline of 7 words or fewer, ending in a period, with one `<mark>`.
  4. Put the logo bottom-left and the CTA "Start writing →" bottom-right.
- **"Generate a landing-page section":**
  1. Use the section recipe: § eyebrow → h2 → content grid.
  2. Apply the 1200px container, 128px vertical padding and a hairline top border.
  3. Use cards on raised paper with a 14px radius.
  4. Add `.reveal` with a `--i` stagger.
- **"Create an advertisement":**
  1. Identify the one message.
  2. Write a display headline, add the logo and CTA, and add a 1px rule border.
  3. Use no imagery, or a ruled note only if there is room.

## Hard rules

- Fonts: Fraunces, Inter and JetBrains Mono only (all OFL, from Google Fonts).
- No colors outside the token table. Never fill with signal orange.
- No photos, stock imagery, icons, illustrations, gradients, glassmorphism, glows or 3D.
- No centered text blocks. Everything is left-aligned.
- Radii: 14px for panels, pill for buttons, 4px for tags. Nothing else.
- Use only the existing logo file (`brand/assets/logos/quillpine-logo.svg`). Never redraw it. There is no reversed version; on forest, omit the logo or place it on a paper panel.
- Never invent customer names, metrics or claims.

## Validation checklist

- [ ] Only Fraunces, Inter and JetBrains Mono, each in its role
- [ ] Every color matches a token; signal used only as marks
- [ ] Text contrast is at least 4.5:1, or 3:1 for text 24px and up (see the table in design-tokens.md)
- [ ] Radii are 14, 999 or 4; borders are 1px `#D9D1C3`
- [ ] Spacing uses the 8px scale; margins are about 7% of width
- [ ] Left-aligned with one focal headline
- [ ] Headline is sentence case, ends with a period, and has at most one `<mark>`
- [ ] CTA is verb-first, 2–4 words, with no exclamation mark
- [ ] At least 2 signatures: § eyebrow, ruled note, highlighter, tight Fraunces display
- [ ] With the logo covered, it is still recognizably Quillpine
