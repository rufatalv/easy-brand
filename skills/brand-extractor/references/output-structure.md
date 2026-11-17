# Phase 5: Output Structure

Create everything inside `brand/` at the project root. **Only create files you have real content for.** Omit irrelevant ones and explain the omission in `brand/README.md`.

```text
brand/
├── README.md                 # Entry point: what this is, how to use, file map, omissions, how to regenerate
├── BRAND_GUIDELINES.md       # Human-readable guidelines: principles, logo, color, type, layout, imagery, motion, do/don't
├── BRAND_AUDIT.md            # Evidence log: sources inspected, screenshots, findings by status, conflicts, gaps
├── BRAND_VOICE.md            # Voice principles, vocabulary, headline & CTA patterns, examples
│
├── tokens/
│   ├── colors.json
│   ├── colors.css
│   ├── typography.json
│   ├── spacing.json
│   ├── radii.json
│   ├── shadows.json
│   ├── motion.json
│   └── layout.json
│
├── references/
│   ├── visual-dna.md         # Visual impression + 5–10 core principles
│   ├── typography.md
│   ├── colors.md             # incl. harmony + measured contrast table
│   ├── composition.md        # grid, spacing rhythm, hierarchy, section patterns
│   ├── imagery.md
│   ├── graphics.md           # shape & graphic language
│   ├── components.md
│   ├── motion.md
│   ├── 3d-language.md        # only if 3D/WebGL exists
│   ├── content-voice.md
│   └── consistency-model.md  # scoring rubric for future output
│
├── templates/
│   ├── README.md             # Template index + metadata schema
│   ├── social/
│   ├── advertising/
│   ├── presentations/
│   └── web/
│
├── assets/
│   ├── logos/                # COPIES of existing logo files only — never invented
│   ├── icons/                # only if the project has a distinct icon set worth reusing
│   └── graphics/             # existing reusable motifs/patterns
│
└── skills/
    └── brand-identity/
        ├── SKILL.md
        └── references/
            ├── brand-foundations.md
            ├── design-tokens.md
            ├── typography.md
            ├── imagery.md
            ├── composition.md
            ├── motion.md
            └── content-generation.md
```

## File guidance

**README.md** — Start with a 3-line summary of the brand. Then: how humans use this, how agents use it (point to `skills/brand-identity/SKILL.md`), file map, legend for Observed/Inferred/Recommended, omitted categories with reasons, date generated and source commit (`git rev-parse --short HEAD`).

**BRAND_GUIDELINES.md** — The readable guide. Each section: rule → why → example → source → status. Include do/don't lists derived from evidence.

**BRAND_AUDIT.md** — Everything an auditor would need: files inspected, tools used, whether the app was rendered (and at which viewports), raw frequency counts (top colors, radii, font sizes), conflicts, open questions, gaps (Not established).

**assets/** — Copy existing logos/marks/icons (don't move them; originals stay). Prefer SVG. Record original path in `assets/README.md` or in BRAND_GUIDELINES. If there is no logo file, write "Logo: Not established — no logo asset found" rather than drawing one. Never copy proprietary font files.

**Markdown style** — Tables for values, short paragraphs for principles. Every rule line ends with a status tag like `[Observed: src/styles/globals.css:8]`.
