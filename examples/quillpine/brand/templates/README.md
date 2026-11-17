# Templates

These are **static HTML examples** that show how the extracted tokens compose into marketing formats. They are not an editable template system. To make a new asset, copy an example, replace the `data-slot` content, and render it to PNG with a headless browser at the stated size.

All examples share [template-base.css](template-base.css), which imports [../tokens/colors.css](../tokens/colors.css). Fonts load from Google Fonts; all three families are OFL.

## Index

| ID | File | Format | Size | Category | Status |
|---|---|---|---|---|---|
| social-editorial-01 | [social/editorial-post.html](social/editorial-post.html) | Instagram feed, portrait | 1080×1350 | Editorial | Inferred |
| social-quote-story-01 | [social/quote-story.html](social/quote-story.html) | Instagram Story | 1080×1920 | Editorial (testimonial) | Inferred |
| web-og-01 | [web/og-image.html](web/og-image.html) | Open Graph | 1200×630 | Product | Inferred |
| ad-mrec-01 | [advertising/mrec-300x250.html](advertising/mrec-300x250.html) | IAB medium rectangle | 300×250 | Campaign | Inferred |

Templates are **Inferred**: each one adapts an observed site section to a new canvas.

Categories left out on purpose:
- **Visual (image-led):** the site has no photography.
- **Presentations and Corporate:** there is no evidence of decks or reports.

## Metadata

The machine-readable spec for each template is in [templates.json](templates.json).

## Rules for all formats

- **Margins:** about 7% of canvas width (80px at 1080, 64px at 1200, 20px at 300). `[Inferred]`
- **Alignment:** left, matching the site.
- **Highlights:** at most one `<mark>` per headline.
- **Logo:** bottom-left on social and ads; top-left on OG. Use only [../assets/logos/quillpine-logo.svg](../assets/logos/quillpine-logo.svg).
- **CTA:** an ink pill with `→`. The copy is "Start writing" unless the campaign needs another verb-first phrase of 2–4 words.
- **Story safe area:** nothing in the top 250px or bottom 340px. These are platform figures `[Recommended]`; check them against current Instagram guidance.
- **Export:** PNG in sRGB. For ads, check the network's file-size limit (often 150 KB) and use JPEG if needed.

## Rendering

```bash
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"   # or chromium / google-chrome
"$CHROME" --headless=new --hide-scrollbars --virtual-time-budget=6000 \
  --window-size=1080,1350 --screenshot=post.png "file://$PWD/social/editorial-post.html"
```
