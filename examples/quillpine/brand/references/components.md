# Components

These are transferable visual principles, not a component library.

| Component | Appearance | Type | Hover / focus | Responsive | Source |
|---|---|---|---|---|---|
| Nav | 64px sticky bar. Paper at 90% opacity with an 8px blur and a bottom hairline. | Links: Inter 500 15px, muted, turning ink on hover | n/a | Links hidden below 768px; logo and CTA remain | `.nav` |
| Primary button | Ink fill, paper text, 1px ink border, pill, 14×22 padding | Inter 600 15px | Fill → `qp-signal-ink` (180ms); arrow moves 3px right; focus ring 2px `qp-signal`, 3px offset | Wraps in group | `.btn-primary` |
| Ghost button | Transparent with a 1px ink border, pill | same | Inverts to ink fill | same | `.btn-ghost` |
| Card | Raised paper, hairline border, 14px radius, 32px padding | mono numeral → h3 → muted body | 2px lift plus `qp-shadow-lift` | 1 → 3 columns at 768 | `.card` |
| Note card | Ruled paper with margin line, lift shadow, text on 32px lines | mono meta, Inter body, forest tags | none | Stacks below the hero copy | `.note-card` |
| Plan | Raised paper, hairline, **12px** radius (inconsistent), 48×32 padding | Fraunces price, list rows with signal dashes | Featured plan: ink border plus lift shadow | 1 → 2 columns | `.plan` |
| Testimonial | Full-bleed forest band, 128px padding | Fraunces italic quote, mono citation | n/a | Fluid type | `.forest` |
| Footer | Hairline top, 64px padding, muted 14px | Inter | Links hover to hard-coded `#E5582F` (inconsistent) | Wraps | `.footer` |

Form, modal, tab and accordion components are **Not established**: the site doesn't have them.
