# Brand Audit: Quillpine

- **Date:** 2026-11-17
- **Source:** `examples/quillpine/site/`, a static HTML/CSS site with no framework and no build step.

## Sources inspected

| Source | Type | Findings |
|---|---|---|
| `site/styles/tokens.css` | CSS custom properties | 13 colors, 3 font stacks, 10 spacing steps, 3 radii, 1 border, 1 shadow, 3 layout values and 4 motion tokens, all prefixed `--qp-` |
| `site/styles/main.css` | Global CSS | Type scale, components, ruled motif, reveal motion, 2 breakpoints, reduced-motion handling |
| `site/index.html` | Markup and copy | Sections, copy, Google Fonts link, stagger indices |
| `site/scripts/reveal.js` | JS | IntersectionObserver trigger (threshold 0.15) |
| `site/assets/logo.svg` | SVG | Logo mark and wordmark |

**Not present:**
- photography or illustrations;
- icons;
- 3D or WebGL;
- an animation library;
- a dark theme;
- existing brand docs;
- social or marketing assets.

## Rendered audit

The site was rendered with headless Chrome at 1440 and 390px wide; screenshots are in [../screenshots/](../screenshots/). Computed styles matched the declared CSS with one exception, the note-card rotation (see the conflicts table).

## Frequency counts (main.css)

| Value | Count | Notes |
|---|---|---|
| `var(--qp-border)` + `var(--qp-rule)` | 7 + 1 | Hairlines are the main structural device |
| `var(--qp-signal)` | 5 | § marker, margin line (2 gradient stops), list dash, focus ring |
| `var(--qp-radius-card)` | 2 | The `.plan` panel hard-codes 12px instead |
| `var(--qp-shadow-lift)` | 3 | Note card, featured plan, card hover |
| `var(--qp-font-mono)` | 5 | Eyebrow, note meta, tag, card numeral, citation |

## Conflicts and inconsistencies

| # | Issue | Location | Status | Resolution |
|---|---|---|---|---|
| 1 | Note card has `rotate(-1.5deg)` in its CSS, but the rendered card is not rotated | `.note-card` vs `.reveal.is-visible { transform: none }` | Code and render disagree | Followed the rendered page (source priority 1): **no tilt**. The tilt is listed as a possible extension. |
| 2 | Pricing plans use a 12px radius; other panels use 14px | `.plan` | Inconsistent | Token stays 14px. `[Recommended]` normalize. |
| 3 | Footer link hover hard-codes `#E5582F`, which is close to signal and fails AA (3.18:1) | `.footer a:hover` | Inconsistent | Not tokenized. `[Recommended]` use `qp-signal-ink`. |
| 4 | Studio CTA reads "Sign Up Now!"; every other CTA reads "Start writing" | `index.html` #pricing | Voice drift | Documented in BRAND_VOICE.md |
| 5 | `--qp-success` and `--qp-error` are declared but never used | tokens.css | Unused | Tokenized as functional colors, marked unused |
| 6 | `--qp-gutter` (24px) is declared but unused; spacing tokens are used directly | tokens.css:44 | Unused | Left out of layout.json |

## Not established

- Photography and art direction
- Reversed logo, clear space and minimum size
- Dark mode
- Form, modal and tab styles
- Icon set
- Error and support voice
- Positioning statement
- Social voice

## Validation

`validate_brand.py validate brand/` reports 0 errors. Every contrast figure in this package was measured with `validate_brand.py contrast`. The site files were not modified.
