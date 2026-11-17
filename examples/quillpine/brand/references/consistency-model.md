# Consistency Model

Score each category 0, 1 or 2 (0 = violates a required rule, 1 = minor drift, 2 = on-brand). An asset **passes at 17/20 or higher with no zeros**.

| # | Category | Required | Flexible | Prohibited | Check |
|---|---|---|---|---|---|
| 1 | Color | Only tokens from colors.json; paper or forest canvas | Choice of paper vs. forest | Signal as a fill; #FFF or #000; new hues; gradients other than the highlighter | Eyedrop every color and match it to a token |
| 2 | Typography | Fraunces for headline, Inter for body, JetBrains Mono for labels | Exact px sizes per canvas | Serif or mono body text; Inter headlines; all-caps display; loose display tracking | Display line-height ≤ 1.0 and tracking ≤ -0.02em |
| 3 | Spacing | Values from the 8px scale; about 7% margins | Scaling for large canvases | Arbitrary odd values | Measure margins and gaps |
| 4 | Composition | Left-aligned; eyebrow → headline → body → action | Artifact placement | Centered text blocks; more than one focal point | Squint test: one focal headline |
| 5 | Imagery | Ruled note artifact or type only | Artifact content | Stock photos, device mockups, illustrations | Any raster image must be justified |
| 6 | Shapes | 14px panels, pill buttons, 4px tags, 1px hairlines | Whether to show the artifact | Other radii; icons where a glyph works; blobs | Inspect border-radius values |
| 7 | Motion | 16px fade-rise, 600ms, ease (0.2, 0.7, 0.2, 1), 80ms stagger | Order of reveals | Scale, spin, bounce, parallax | Read the CSS/JS values |
| 8 | Voice | Sentence case; headline ends with a period; verb-first CTA of 2–4 words | Headline wording | Exclamation marks; "unlock", "seamless" etc.; title-case CTAs | Read aloud and count words |
| 9 | Accessibility | Text ≥ 4.5:1 (large ≥ 3:1), measured | — | Signal text at body size (3.22:1) | `validate_brand.py contrast` |
| 10 | Recognition | Shows at least 2 of: § eyebrow, ruled artifact, highlighter, tight Fraunces display | Which signatures | None of the signatures | Cover the logo: is it still Quillpine? |
