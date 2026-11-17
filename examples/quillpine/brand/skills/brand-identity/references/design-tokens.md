# Design Tokens

This is a bundled copy. If `brand/tokens/` exists, it is canonical.

## Color

| Token | HEX | Role | Use |
|---|---|---|---|
| `--qp-paper` | #F4EFE6 | background | Canvas |
| `--qp-paper-raised` | #FBF8F2 | surface | Panels, ruled note |
| `--qp-ink` | #1C1A17 | foreground | Text, primary button, logo tile |
| `--qp-ink-muted` | #5F5950 | muted | Secondary text, eyebrows |
| `--qp-rule` | #D9D1C3 | border | Hairlines, rule lines (never text) |
| `--qp-signal` | #E4572E | accent | Marks only |
| `--qp-signal-ink` | #B83A16 | interactive | Accent text, button hover |
| `--qp-forest` | #23332B | background | Dark band, tags |
| `--qp-on-forest` | #EDE6D8 | foreground | Text on forest |
| `--qp-on-forest-muted` | #A9B3A6 | muted | Labels on forest |
| `--qp-highlight` | rgba(228,87,46,.22) | overlay | `<mark>` |
| `--qp-success` / `--qp-error` | #3B7A57 / #B3261E | status | UI states only |

### Measured contrast

| Pair | Ratio | Result |
|---|---|---|
| ink on paper | 15.16 | AAA |
| ink-muted on paper | 6.05 | AA |
| signal-ink on paper | 5.02 | AA |
| paper on ink | 15.16 | AAA |
| on-forest on forest | 10.70 | AAA |
| on-forest-muted on forest | 6.13 | AA |
| signal on paper | 3.22 | Large text and UI only |
| signal on forest | 3.61 | Large text and UI only |

## Spacing (8px base)

4 · 8 · 12 · 16 · 24 · 32 · 48 · 64 · 96 · 128. Button padding is a fixed 14px × 22px.

## Shape

| Use | Value |
|---|---|
| Panels and cards | 14px radius |
| Buttons | 999px (pill) |
| Tags | 4px |
| Border | `1px solid #D9D1C3` |
| Shadow (single use) | `0 1px 0 #D9D1C3, 0 12px 24px -12px rgba(28,26,23,.25)` |

## Layout

| Item | Value |
|---|---|
| Container | 1200px |
| Page margins | 24px, or 48px from 768px |
| Breakpoints | 768, 1024 |
| Section padding | 64px, or 128px from 768px |
| Hero grid | 7fr / 5fr, aligned to the bottom |
| Ruled lines | 32px pitch; margin line at 48px |

## Paste-ready CSS

```css
:root {
  --qp-paper:#F4EFE6; --qp-paper-raised:#FBF8F2; --qp-ink:#1C1A17; --qp-ink-muted:#5F5950;
  --qp-rule:#D9D1C3; --qp-signal:#E4572E; --qp-signal-ink:#B83A16; --qp-forest:#23332B;
  --qp-on-forest:#EDE6D8; --qp-on-forest-muted:#A9B3A6; --qp-highlight:rgba(228,87,46,.22);
  --qp-font-display:"Fraunces",Georgia,"Times New Roman",serif;
  --qp-font-sans:"Inter",system-ui,-apple-system,"Segoe UI",sans-serif;
  --qp-font-mono:"JetBrains Mono",ui-monospace,"SF Mono",Menlo,monospace;
  --qp-radius-sm:4px; --qp-radius-card:14px; --qp-radius-pill:999px; --qp-ruled:32px;
  --qp-shadow-lift:0 1px 0 var(--qp-rule),0 12px 24px -12px rgba(28,26,23,.25);
}
.ruled {
  background-color: var(--qp-paper-raised);
  background-image:
    linear-gradient(90deg, transparent 47px, var(--qp-signal) 47px, var(--qp-signal) 48px, transparent 48px),
    repeating-linear-gradient(transparent 0 calc(var(--qp-ruled) - 1px), var(--qp-rule) calc(var(--qp-ruled) - 1px) var(--qp-ruled));
  border: 1px solid var(--qp-rule); border-radius: var(--qp-radius-card); line-height: var(--qp-ruled);
}
mark { background: linear-gradient(transparent 55%, var(--qp-highlight) 55%); color: inherit; }
```
