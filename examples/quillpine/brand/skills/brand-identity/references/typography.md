# Typography

## Loading

All three families are OFL and load from Google Fonts:

```html
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght,SOFT@0,9..144,400..600,50;1,9..144,400,50&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
```

## Roles

| Role | Font | Wt | Web size | Line height | Tracking | Notes |
|---|---|---|---|---|---|---|
| Display | Fraunces, `"opsz" 144, "SOFT" 50` | 600 | clamp(48px, 7vw, 96px) | 0.95 | -0.03em | One `<mark>` max |
| H2 | Fraunces, `"opsz" 96` | 600 | clamp(32px, 4vw, 52px) | 1.05 | -0.02em | |
| H3 | Inter | 600 | 22px | 1.25 | -0.01em | The only sans heading |
| Quote | Fraunces italic | 400 | 28–44px | 1.2 | -0.01em | Max 24ch, on forest |
| Price / big number | Fraunces | 600 | 56px | 1 | -0.03em | |
| Lede | Inter | 400 | 20px | 1.5 | 0 | Max 34ch, muted |
| Body | Inter | 400 | 17px | 1.6 | 0 | |
| Eyebrow | JetBrains Mono | 500 | 12px | — | 0.08em | Uppercase; `§ ` in signal |
| Caption / meta | JetBrains Mono | 500 | 12px | — | 0.08em | Uppercase |
| Button | Inter | 600 | 15px | 1 | 0 | |
| Nav | Inter | 500 | 15px | — | 0 | Muted, ink on hover |

## Fixed canvases `[Inferred]`

These sizes come from the templates.

| Canvas | Display | Eyebrow | Body | CTA |
|---|---|---|---|---|
| 1080 wide | 132px | 22px | 34px | 26px |
| 1200×630 OG | 84px | 15px | 18px | — |
| 300×250 | 38px | 10px | — | 13px |

Rule of thumb: the display is about 12% of canvas width on social formats and about 7% on OG.
