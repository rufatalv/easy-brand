# Shape and Graphic Language

## Vocabulary

| Element | Spec | Where | Status |
|---|---|---|---|
| Ruled paper | `qp-paper-raised` with horizontal `qp-rule` lines every 32px, plus a 1px `qp-signal` vertical margin line at x=47–48px | Hero note card | Observed |
| § marker | `§ ` in `qp-signal` before mono eyebrows | Every section | Observed |
| Em-dash bullet | `— ` in `qp-signal` before list items | Pricing lists | Observed |
| Highlighter | `qp-highlight` over the lower 45% of the text line | One word per headline or note | Observed |
| Hairline | 1px `qp-rule` | Borders, dividers, list rows | Observed |
| Pill | radius 999px | Buttons only | Observed |
| Card | radius 14px | Panels | Observed |
| Tag chip | radius 4px, `qp-forest` fill, mono 12px `qp-on-forest` | Note tags | Observed |
| Arrow | text `→` | Primary CTA, "linked to" lines | Observed |
| Quill mark | ink tile (radius 7 on 28px) with a paper stroke and an orange curl and dot | Logo | Observed |

## Rules

- There is no illustration, iconography set, pattern fill, blob shape, gradient mesh or 3D on the site. Don't add them.
- Graphic marks are typographic: §, —, →, the highlighter. Prefer a glyph over an icon. `[Inferred]`
- The note card's CSS declares `transform: rotate(-1.5deg)`, but `.reveal.is-visible { transform: none }` cancels it on render. The rendered page shows an **unrotated** card, so treat the tilt as **Not established**. A slight tilt is a possible extension `[Recommended]`, but it is not current brand.
- Scale: rule pitch and margin offset scale together (32px pitch to 48px margin, a 2:3 ratio). On large canvases keep that ratio. `[Inferred]`

## Logo

- **File:** [../assets/logos/quillpine-logo.svg](../assets/logos/quillpine-logo.svg), copied from `site/assets/logo.svg`.
- **Construction:** a 28px tile plus the wordmark "Quillpine" in Fraunces 600, 19px.
- **Notes:**
  - The wordmark is live `<text>`, so it depends on Fraunces being installed. `[Recommended]` Outline it for exports.
  - Only one color version exists (ink on paper). A reversed version for forest backgrounds is **Not established**.
