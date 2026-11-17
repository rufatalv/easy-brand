# Typography

Source of truth: [../tokens/typography.json](../tokens/typography.json). All values are **Observed** unless tagged otherwise.

## Families

| Role | Family | Fallback stack | Loading | License |
|---|---|---|---|---|
| Display | Fraunces (variable: opsz 9–144, wght 400–600, SOFT 50, italic 400) | Georgia, "Times New Roman", serif | Google Fonts `<link>` in `site/index.html` | OFL |
| Sans | Inter 400 / 500 / 600 | system-ui, -apple-system, "Segoe UI", sans-serif | Google Fonts | OFL |
| Mono | JetBrains Mono 500 | ui-monospace, "SF Mono", Menlo, monospace | Google Fonts | OFL |

All three are open-source, so templates may load them from Google Fonts.

## Scale

| Element | Font | Weight | Size (390 → 1440) | Line height | Tracking | Transform | Source |
|---|---|---|---|---|---|---|---|
| Display (h1) | Fraunces, opsz 144, SOFT 50 | 600 | 48 → 96px `clamp(3rem, 7vw, 6rem)` | 0.95 | -0.03em | none | `.display` |
| H2 | Fraunces, opsz 96 | 600 | 32 → 52px `clamp(2rem, 4vw, 3.25rem)` | 1.05 | -0.02em | none | `h2` |
| H3 | Inter | 600 | 22px | 1.25 | -0.01em | none | `h3` |
| Quote | Fraunces italic | 400 | 28 → 44px | 1.2 | -0.01em | none | `.forest blockquote` |
| Price | Fraunces | 600 | 56px | 1 | -0.03em | none | `.plan .price` |
| Lede | Inter | 400 | 20px | 1.5 | 0 | none | `.lede` |
| Body | Inter | 400 | 17px | 1.6 | 0 | none | `body` |
| Eyebrow / Caption | JetBrains Mono | 500 | 12px | 1.6 | 0.08em | uppercase | `.eyebrow`, `.meta`, `cite` |
| Navigation | Inter | 500 | 15px | 1.6 | 0 | none | `.nav-links a` |
| Button | Inter | 600 | 15px | 1 | 0 | none | `.btn` |

## Personality

- **Fraunces:** a soft, "wonky" old-style serif with a high optical size. It is set heavy and tight, so it feels editorial and bookish rather than corporate.
- **Inter:** a neutral neo-grotesk that stays out of the way.
- **JetBrains Mono:** technical and archival. Uppercase and tracked, it reads like labels on index cards.

## Rules

1. Eyebrows always start with `§ ` in `qp-signal`, then uppercase mono in `qp-ink-muted`.
2. Headlines are sentence case and end with a period. Exception: "Two plans. No seat math." uses two short sentences.
3. Use at most one `<mark>` highlight per headline. It is a highlighter stroke covering the lower 45% of the line.
4. Measure: lede at most 34ch, quote at most 24ch.
5. Numerals in cards are mono and zero-padded (`01`, `02`, `03`) in `qp-signal-ink`.
