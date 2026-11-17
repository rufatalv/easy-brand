# Color

Source of truth: [../tokens/colors.json](../tokens/colors.json) and [../tokens/colors.css](../tokens/colors.css). There is a single light theme; dark mode is **Not established**.

## Palette

| Token | HEX | Tier | Role | Use |
|---|---|---|---|---|
| `qp-paper` | #F4EFE6 | core | background | Page canvas |
| `qp-paper-raised` | #FBF8F2 | supporting | surface | Cards, plans, ruled note |
| `qp-ink` | #1C1A17 | core | foreground | Text, primary button, logo tile |
| `qp-ink-muted` | #5F5950 | supporting | muted | Secondary text |
| `qp-rule` | #D9D1C3 | supporting | border | Hairlines and rule lines (never text) |
| `qp-signal` | #E4572E | core | accent | Marks only: §, margin line, dashes, focus ring |
| `qp-signal-ink` | #B83A16 | core | interactive | Accent text, primary-button hover |
| `qp-forest` | #23332B | core | background | One dark band per page, tags |
| `qp-on-forest` | #EDE6D8 | supporting | foreground | Text on forest |
| `qp-on-forest-muted` | #A9B3A6 | supporting | muted | Secondary text on forest |
| `qp-highlight` | rgba(228,87,46,.22) | decorative | overlay | `<mark>` highlighter |
| `qp-success` | #3B7A57 | functional | status | Declared, unused on site |
| `qp-error` | #B3261E | functional | status | Declared, unused on site |

## Measured contrast

Measured with `validate_brand.py contrast`.

| Text | Background | Ratio | Normal text | Large text / UI |
|---|---|---|---|---|
| ink | paper | 15.16 | AAA | AAA |
| ink-muted | paper | 6.05 | AA | AAA |
| ink-muted | paper-raised | 6.54 | AA | AAA |
| signal-ink | paper | 5.02 | AA | AAA |
| signal-ink | paper-raised | 5.42 | AA | AAA |
| paper | ink (primary button) | 15.16 | AAA | AAA |
| paper | signal-ink (button hover) | 5.02 | AA | AAA |
| on-forest | forest | 10.70 | AAA | AAA |
| on-forest-muted | forest | 6.13 | AA | AAA |
| **signal** | paper | **3.22** | **Fail** | AA |
| **signal** | forest | **3.61** | **Fail** | AA |
| rule | paper | 1.32 | Fail | Fail (decorative only) |

## Harmony

- **Distribution** `[Inferred, from screenshots]`: about 85% paper tones, 10% ink, one forest band, and less than 2% signal.
- **Preferred pairs:** ink on paper; ink-muted on paper-raised; on-forest on forest; signal marks beside ink text.
- **Gradients:** none. The only gradient is the hard-stop highlighter (`linear-gradient(transparent 55%, qp-highlight 55%)`).
- **Avoid:**
  - signal as a fill;
  - signal text at body size;
  - forest and signal at equal weight;
  - pure white or black;
  - any color not listed above.

## Inconsistency

`site/styles/main.css` `.footer a:hover` hard-codes `#E5582F`. It is a near-duplicate of `qp-signal`, and at 3.18:1 on paper it fails AA for link text. `[Recommended]` Use `var(--qp-signal-ink)` there instead. The site has not been changed.
