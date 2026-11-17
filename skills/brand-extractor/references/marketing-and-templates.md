# Phase 6: Consistency Model, Marketing Extensions, Templates

## A. Brand consistency model → `brand/references/consistency-model.md`

A rubric future agents and reviewers use to score output. For each category define **Required**, **Flexible**, **Prohibited**, and **Evaluation criteria** (a concrete check, ideally pass/fail).

Categories:

1. Color consistency
2. Typography
3. Spacing
4. Composition
5. Imagery
6. Shapes
7. Motion
8. Brand voice
9. Accessibility
10. Overall recognition

Write actionable criteria, not adjectives.

- Bad: "Make it beautiful and premium."
- Good: "Uses only `--font-display` for headlines; accent covers < 10% of canvas; corners use `radius-card` (16px); headline ≤ 8 words, sentence case; text/background contrast ≥ 4.5:1 (measured)."

Include a scoring sheet (e.g. each category 0–2, pass threshold) agents can fill out in validation.

## B. Marketing applications → `brand/templates/README.md` + per-format specs

Don't generate every asset. Define **how** to generate each consistently, using the extracted tokens. Only cover formats relevant to the product.

For each format document: dimensions, typography roles (which tokens, min sizes), composition rules, image usage, CTA placement, logo placement, safe areas, export guidance (format, color profile, file size).

Reference dimensions (verify against current platform docs at generation time — platforms change these; mark them **Recommended**, not brand rules):

| Format | Size (px) | Notes |
|---|---|---|
| Instagram feed (portrait) | 1080×1350 (4:5) | Profile grid crops to ~3:4 center; keep key content central |
| Instagram feed (square) | 1080×1080 | |
| Instagram Story / Reel / Reel cover | 1080×1920 (9:16) | Keep text/logo out of top ~250px and bottom ~340px (UI overlays) |
| LinkedIn single image | 1200×627 or 1080×1350 | |
| X / Twitter image | 1600×900 (16:9) | |
| Open Graph | 1200×630 | Center-safe; some clients crop to square |
| Email banner | 600 wide (export 1200 @2x) | Live text preferred for headlines where possible |
| Display ads (IAB) | 300×250, 728×90, 300×600, 160×600, 320×50 | Often < 150 KB; logo + CTA always visible |
| Presentation | 1920×1080 (16:9) | |
| Case-study cover | 1600×900 or project's existing ratio | Prefer the ratio used on the site |
| Landing-page visual | per `layout.json` containers/breakpoints | |

Platform treatment differs: e.g. a Story may lean on full-bleed imagery while an OG image needs legible type at thumbnail size. Don't apply one layout everywhere.

## C. Template architecture → `brand/templates/`

Templates are described by structured metadata. Implement only categories that fit the brand's identity and likely needs:

- **Editorial** — typography-led
- **Visual** — image-led
- **Product** — screenshot-focused
- **Campaign** — advertisements
- **Educational** — structured information
- **Announcement** — releases/updates
- **Corporate** — reports, proposals, presentations

### Template metadata (one JSON per template, or an index in `templates/README.md`)

```json
{
  "id": "social-editorial-01",
  "purpose": "Typography-led announcement for feed posts",
  "category": "editorial",
  "format": "instagram-feed-portrait",
  "dimensions": { "width": 1080, "height": 1350 },
  "layout": "Headline top-left on 12-col grid, 80px margins, logo bottom-left, CTA bottom-right",
  "fonts": { "headline": "typography.display", "body": "typography.body", "cta": "typography.button" },
  "colors": { "background": "color-bg-inverse", "text": "color-fg-inverse", "accent": "color-accent" },
  "image": { "required": false, "treatment": "n/a" },
  "content_limits": { "headline_words": 8, "body_chars": 120, "cta_words": 3 },
  "constraints": ["Accent on CTA only", "No drop shadows", "Corners use radius-card"],
  "source_patterns": ["Hero section src/app/page.tsx:20-48"],
  "status": "inferred",
  "file": "social/editorial-01.html"
}
```

### Example implementations

Where useful, create self-contained **HTML** (with inline CSS using `../../tokens/colors.css` values or copied custom properties) or **SVG** examples. Rules:

- Use only extracted tokens and existing assets; fonts by `font-family` name with the project's fallback stack (load from Google Fonts only if the font is open-source and that is how the project loads it).
- Put content in clearly marked slots (`data-slot="headline"`).
- Label them honestly: a static HTML mockup is an **example**, not a functional editable template system. Say so in `templates/README.md`.
- Keep them few and high-quality (2–6 total is usually plenty) — they demonstrate the system; the metadata is what scales.
