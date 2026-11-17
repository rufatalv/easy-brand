# Phase 3: Extraction Guide

Extract each area below. For each, record value + source + status (Observed / Inferred / Recommended). Skip areas the project doesn't have and say so.

---

## 1. Typography → `tokens/typography.json`, `references/typography.md`

Inspect: font imports, `@font-face`, font files, CSS `font-family`, Tailwind font tokens, weights, variable-font axes (`font-variation-settings`), letter-spacing, line-height, sizes (including `clamp()`), `text-transform`, responsive scales, text-reveal treatments.

Deliverable table (fill every cell or write *Not established*):

| Element | Font | Weight | Size (mobile → desktop) | Line height | Tracking | Transform | Source |
|---|---|---|---|---|---|---|---|
| Display | | | | | | | |
| H1 | | | | | | | |
| H2 | | | | | | | |
| H3 | | | | | | | |
| Body | | | | | | | |
| Caption | | | | | | | |
| Navigation | | | | | | | |
| Button | | | | | | | |

Also document:

- **Fallback stacks** exactly as declared.
- **Personality** — choose only supported descriptors (neo-grotesk, humanist, geometric, editorial serif, condensed, mono/technical, expressive…) and justify from letterforms and usage.
- **Pairing logic** — which face does what, and why it works here.
- **Licensing** — classify each font: Open-source (OFL/Apache, e.g. Google Fonts, Fontsource), Commercial (Adobe Fonts, foundry), Custom, System. Flag uncertainty. **Never copy proprietary font files into `brand/`**; reference them by name and source.

---

## 2. Color → `tokens/colors.json`, `tokens/colors.css`, `references/colors.md`

Sources: CSS variables, theme config, component classes, gradients, SVG fills/strokes, 3D materials, canvas code, UI state styles.

Classify by **role**: primary, secondary, accent, background, foreground, surface, border, muted, overlay, interactive, status.

Classify by **tier**:
- **Core brand** — defines identity.
- **Supporting** — surfaces and structure.
- **Functional** — success / warning / error / info / states.
- **Decorative** — imagery, gradients, illustrations.

Not every hex in the codebase is a brand color. Use usage frequency and placement to decide. A one-off hex in a forgotten component is an inconsistency, not a token.

For each token: name (reuse project naming), HEX, RGB, (OKLCH/HSL if source uses it), role, tier, source, typical usage, contrast notes. Convert source formats accurately — show the original value too.

Color harmony section in `colors.md`:
- Preferred pairings; light/dark combinations
- Accent distribution (e.g. "accent covers <5% of any viewport; used only on CTAs and active states")
- Gradient definitions (stops, angle, where used)
- Combinations to avoid
- **Accessible text/background pairs** — run `validate_brand.py matrix` and report actual ratios. AA: 4.5:1 normal text, 3:1 large text (≥24px, or ≥18.66px bold) and UI components. AAA: 7:1 / 4.5:1.

Dark/light themes: record both sets, keyed by theme, and the mechanism (`.dark`, `[data-theme]`, `prefers-color-scheme`).

---

## 3. Spacing & layout → `tokens/spacing.json`, `tokens/layout.json`, `tokens/radii.json`, `tokens/shadows.json`

Analyze: container widths, grid columns, gutters, section padding (vertical rhythm), component spacing, breakpoints, aspect ratios, alignment, card dimensions, radii, borders, shadows, section framing.

- Identify the **base unit** if one exists (4px, 8px, Tailwind default scale…) — prove it from frequency.
- Record **repeated patterns**, not every declaration.
- List **inconsistent values** (e.g. `rounded-[14px]` once among `rounded-xl` everywhere) with locations.
- Suggest normalization in a separate "Recommended" subsection. Never edit source to normalize.

---

## 4. Shape & graphic language → `references/graphics.md`

Inspect: radii, circles, lines, dividers, masks, `clip-path`, background patterns (SVG/CSS), noise/grain textures, grids, geometric motifs, decorative objects, layering, blur/glass.

Document:
- Shape vocabulary and preferred proportions
- How forms interact (overlap, nesting, bleed off-canvas)
- Where decoration appears and where it never does
- Relationship of graphics to typography
- Scaling behavior

Don't invent motifs that aren't there.

---

## 5. Components → `references/components.md`

Audit major reusable components that exist: navigation, buttons, cards, modals, forms, dropdowns, tabs, accordions, showcases, feature blocks, pricing, footer.

For each: appearance, layout, typography, color, geometry, hover, focus, motion, responsive adaptation, source file.

Purpose is **transferable visual principles** for other media — don't copy the component library.

---

## 6. Imagery & art direction → `references/imagery.md`

From real assets determine: photography style, grading, contrast, lighting, cropping, composition, subject placement, backgrounds, overlays, mockup style, illustration style, texture, depth.

Write rules for: hero imagery, marketing visuals, product screenshots, social graphics, campaign imagery, case-study covers, presentation backgrounds — including subjects, perspectives, aspect ratios, color treatment, cropping, negative space, text-over-image (overlay values, scrim gradients, minimum contrast).

If photographic evidence is thin, write **Not established — requires future art direction** rather than fabricating a style.

---

## 7. 3D / WebGL → `references/3d-language.md` (only if present)

Only if the project contains three.js, R3F, drei, shaders, WebGL canvas, etc.

- **Geometry** — recurring forms, primitives vs. models, detail level.
- **Materials** — type (`MeshStandardMaterial`, `MeshPhysicalMaterial`, custom shader), color, metalness, roughness, transmission, clearcoat, ior, opacity, emissive.
- **Lighting** — light types, intensity, color, position, environment map/preset, shadows.
- **Camera** — perspective/orthographic, fov, position, target, movement.
- **Post-processing** — bloom, noise, chromatic aberration, DOF (with parameters).
- **Animation** — rotation speeds, float/oscillation, scroll sync, pointer interaction, morphing, shader uniforms over time.

Provide reusable scene presets (as JSON or code snippets in the project's own stack) where feasible. If no 3D exists, omit the file and note the omission in `brand/README.md`.

---

## 8. Motion → `tokens/motion.json`, `references/motion.md`

Sources: GSAP/ScrollTrigger, Framer Motion / Motion, CSS transitions/keyframes, WAAPI, Lenis, rAF loops, Lottie.

Extract: durations, delays, easings (exact cubic-bezier or named ease, spring stiffness/damping/mass), stagger, translate distance, scale, rotation, opacity, clip-path reveals, scroll relationships (start/end/scrub/pin), entrance, exit, hover, page transitions, smooth-scroll config, `prefers-reduced-motion` handling.

Motion personality (smooth, energetic, playful, precise, cinematic, spring-based, minimal, expressive) — justify from the numbers.

Provide presets in the project's existing animation stack only. Don't introduce a new library.

---

## 9. Voice → `BRAND_VOICE.md`, `references/content-voice.md`

Analyze headlines, taglines, product/service descriptions, buttons, CTAs, about copy, meta descriptions, marketing copy, social content if available.

Determine: tone, sentence length (measure it), vocabulary, technical depth, formality, emotional character, recurring messages, CTA style (verb-first? length? casing?), punctuation and casing conventions.

Document:
- Voice principles (with quoted examples + source)
- Preferred vocabulary; words to avoid (only if evidenced, otherwise Recommended)
- Headline construction patterns
- CTA patterns
- Examples of consistent copy; examples of inconsistent copy

Never invent a positioning statement or mission and label it as existing.
