# Composition and Layout

Source of truth: [../tokens/layout.json](../tokens/layout.json) and [../tokens/spacing.json](../tokens/spacing.json).

## Grid and rhythm

- **Container:** max-width 1200px. Page margins are 24px on mobile and 48px from 768px.
- **Breakpoints:** two only, 768 and 1024. The layout is mobile-first.
- **Spacing:** 8px base scale (4, 8, 12, 16, 24, 32, 48, 64, 96, 128).
- **Sections:** 64px vertical padding on mobile, 128px on desktop. Each section is separated by a 1px `qp-rule` top border, not by background changes. The forest band is the one exception.
- **Alignment:** everything is left-aligned. No centered headlines or text appear anywhere on the site.

## Section recipe

Every section follows the same order:

```
§ EYEBROW            mono 12px, 16px below
Headline.            Fraunces h2, 24px below (48px to content)
[content grid]       cards / plans / quote
```

## Hero recipe

- Desktop uses a 7:5 asymmetric grid, aligned to the bottom (`align-items: end`).
- **Left column:** eyebrow, then display, then lede (32px above, 48px below), then two buttons: primary ink and ghost.
- **Right column:** a ruled note card showing real-looking user content.
- On mobile the columns stack: copy first, then the note card.

## Hierarchy

1. Display or h2 in ink.
2. Lede in ink-muted.
3. Primary action: pill button in ink.
4. Metadata in mono.

The accent never leads the hierarchy; it only marks.

## Card pattern

Cards use `qp-paper-raised`, a 1px rule border, `qp-radius-card` (14px) and 32px padding. Inside: a mono numeral, a 48px gap, an h3, then muted body text. Three cards sit in a row at 768px and above, with 24px gaps.

## Format layouts

These adapt the site's rules to fixed canvases and are **Inferred**. See [../templates/README.md](../templates/README.md).

- **Square or portrait social:** left-aligned. Margins are 7% of the canvas width. Eyebrow at the top, headline in the upper-middle, logo bottom-left, any CTA bottom-right.
- **Story (9:16):** same layout, with nothing in the top 250px or bottom 340px.
- **OG (1200×630):** headline left, ruled note artifact right (mirrors the hero).
