# Visual DNA: Quillpine

Untagged statements are **Observed**. Others are tagged `[Inferred]` or `[Recommended]`.

## Visual impression

A warm, paper-toned editorial interface. A large soft-serif display (Fraunces) sits over quiet Inter body text. Monospaced, section-marked metadata gives it the feel of a field notebook. One dark forest-green band breaks the paper. A single signal-orange accent appears only as small marks: margin lines, § markers, dashes and highlighter strokes.

Evidence: screenshots `home@1440` and `home@390` ([../../screenshots](../../screenshots)), `site/styles/tokens.css`, `site/styles/main.css`.

## Core principles

### 1. Paper, not screen
- **Description:** Surfaces are warm off-whites (`qp-paper`, `qp-paper-raised`) and text is warm near-black (`qp-ink`). No pure white or pure black appears anywhere.
- **Evidence:** tokens.css:4–7; body background; logo tile fill `#1C1A17`.
- **Apply:** Default every canvas to `qp-paper`. Raised panels use `qp-paper-raised` with a 1px `qp-rule` border.
- **Constraint:** Never use `#FFFFFF` or `#000000`. Never use cool grays.

### 2. The notebook motif
- **Description:** Ruled lines on a 32px pitch with a signal-orange margin line 48px from the left edge. This is the brand's one signature graphic.
- **Evidence:** `.ruled` in main.css; `--qp-ruled: 32px`; hero note card.
- **Apply:** Use it for "artifact" panels that show user content: notes, quotes, snippets. Set text line-height to 32px so it sits on the lines.
- **Constraint:** Only one ruled surface per composition. Never use it as a full-page background. `[Inferred]` from single use per page.

### 3. Signal in small doses
- **Description:** `qp-signal` (#E4572E) appears only as thin or small marks: the § prefix, the margin line, list dashes, the focus ring, the logo quill and the highlighter wash. Large accent areas never appear.
- **Evidence:** every `var(--qp-signal)` use in main.css; screenshot color distribution (accent is well under 2% of the 1440 viewport).
- **Apply:** Use at most one or two accent marks per view. For accent-colored *text*, use `qp-signal-ink` (5.02:1 on paper).
- **Constraint:** Never fill a button, card or background with signal. Never set body text in `qp-signal` (3.22:1 fails AA).

### 4. Three voices of type
- **Description:** Serif (Fraunces) speaks, sans (Inter) explains, mono (JetBrains Mono) labels. Each has a fixed job.
- **Evidence:** `.display`/`h2`/`blockquote`/`.price` use the display face; body/h3/buttons use sans; `.eyebrow`/`.meta`/`cite`/`.num`/`.tag` use mono.
- **Apply:** Headlines, quotes and big numbers in Fraunces. Explanations and UI in Inter. Metadata in uppercase mono with 0.08em tracking.
- **Constraint:** Never set body copy in serif or mono. Never set headlines in Inter (h3 is the only sans heading).

### 5. Tight, heavy display
- **Description:** The display is set tight (line-height 0.95, tracking -0.03em) at weight 600 with optical size 144. Headlines are short, end with a period, and often highlight one word with `<mark>`.
- **Evidence:** `.display`; "Research that remembers itself."; "Notes that find each other."; "Two plans. No seat math."
- **Apply:** Keep headlines to 2–5 words per line and 1–2 sentences.
- **Constraint:** Never use all caps for display. Never loosen the tracking.

### 6. One dark band
- **Description:** Forest green (`qp-forest`) is the only dark surface. It appears once per page as a full-bleed band carrying a testimonial in italic serif.
- **Evidence:** `.forest` section; `.tag` chips reuse forest at small scale.
- **Apply:** Use forest for a single emphasis moment: a quote, a stat or a closing statement.
- **Constraint:** There is no dark mode. Don't invert whole layouts to forest. `[Inferred]`

### 7. Hairlines over shadows
- **Description:** Structure comes from 1px `qp-rule` borders and section dividers. There is a single shadow (`qp-shadow-lift`), used only for "lifted" items: the hero note, the featured plan and card hover.
- **Evidence:** `--qp-border` used on nav, sections, cards, plans and list items; `--qp-shadow-lift` used in 3 places.
- **Apply:** Use a border first. Add the lift shadow only to the one element that should feel picked up.
- **Constraint:** No other shadows, no glows, no gradients except the highlighter.

### 8. Calm motion
- **Description:** Motion is limited to a 16px fade-rise on scroll, 600ms with `cubic-bezier(0.2, 0.7, 0.2, 1)` and an 80ms stagger, plus 180ms hovers (2px lift, 3px arrow nudge). The site honors reduced-motion.
- **Evidence:** motion tokens; `reveal.js`.
- **Apply:** See [motion.md](motion.md).
- **Constraint:** No bounce, spin, parallax or scale-up entrances.

## What must be preserved

Paper palette · Fraunces display set tight · § mono eyebrows · ruled-paper artifact with orange margin line · signal used only as marks · one forest band · pill buttons in ink.
