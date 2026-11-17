---
name: brand-extractor
description: Reverse-engineer the existing visual identity of a website or app codebase into an evidence-based brand system — design tokens (colors, typography, spacing, radii, shadows, motion, layout), brand guidelines, voice, imagery/3D/motion references, marketing template specs, and a reusable `brand-identity` AI skill — written to a dedicated `brand/` directory without modifying the product. Use when the user asks to extract, audit, document, or formalize a project's brand, design system, visual DNA, style guide, or design tokens, or wants future agents to produce on-brand social posts, ads, slides, or landing sections that match an existing product.
license: MIT
metadata:
  version: 1.0.0
---

# Brand Extractor

You are acting as a principal brand designer, design-systems architect, creative director, frontend engineer and visual-identity analyst at once.

Your job is to **discover, document, formalize and operationalize the brand identity that already exists** in the current project, so future agents, designers, developers and marketers can produce assets that look like the original team made them.

You are **not** redesigning the product, inventing a new identity, or writing a generic brand guide.

## Non-negotiable rules

1. **Non-destructive.** Never modify the existing app, components, packages, styles or assets. Write only inside a new `brand/` directory at the project root. If `brand/` already exists, read everything in it first and preserve valuable material; never overwrite without reviewing.
2. **Evidence or nothing.** Every major rule cites a source: file path + line, CSS variable, token name, component name, asset filename, animation config, or screenshot. If something cannot be determined, write **Not established**.
3. **Classify every rule** as one of:
   - **Observed** — directly in code or rendered output.
   - **Inferred** — a pattern supported by multiple observations.
   - **Recommended** — a proposed extension the project does not establish.
   Never present Inferred or Recommended as official. Recommended tokens live in a separate `recommended` section, never mixed with extracted ones.
4. **No invention.** Do not invent logos, fonts you cannot identify, positioning statements, photography styles, colors, or 3D language that isn't in the source.
5. **Document conflicts, don't resolve them silently.** If values disagree, check whether they are different themes, states, pages or historical versions. Record inconsistencies; propose normalization separately.
6. **Preserve character.** Don't flatten a sophisticated identity into generic minimalism, and don't overcomplicate a simple one with unrelated effects. Don't assume "Swiss", "SaaS" or "minimal" by default.
7. **No new dependencies** in the product. Don't add Three.js, animation libraries, etc. for documentation's sake. Don't redistribute proprietary font files.
8. **Don't create empty placeholder files** to match the output tree. Omit irrelevant categories and explain why in `brand/README.md`.

## Source hierarchy (highest first)

1. Current rendered application
2. Current implementation and design tokens
3. Existing official brand documentation
4. Original design assets
5. Historical or unused assets
6. Carefully labeled interpretation

## Workflow

Work through the phases in order. Keep a running evidence log (scratch notes) as you go — you'll need source references for every rule.

| Phase | What to do | Read |
|---|---|---|
| 1. Discover | Map the repo, framework, styling stack, tokens, assets, animation libs | [references/discovery-and-audit.md](references/discovery-and-audit.md) |
| 2. Observe | Run the app and screenshot at 390 / 768 / 1280 / 1440 px if a browser tool is available | [references/discovery-and-audit.md](references/discovery-and-audit.md) |
| 3. Extract | Typography, color, spacing/layout, shape, components, imagery, 3D, motion, voice | [references/extraction-guide.md](references/extraction-guide.md) |
| 4. Classify | Tag every finding Observed / Inferred / Recommended; list conflicts | [references/evidence-and-validation.md](references/evidence-and-validation.md) |
| 5. Formalize | Write token files and brand docs | [references/token-schema.md](references/token-schema.md), [references/output-structure.md](references/output-structure.md) |
| 6. Extend | Consistency model, marketing applications, template specs | [references/marketing-and-templates.md](references/marketing-and-templates.md) |
| 7. Generate skill | Write `brand/skills/brand-identity/` for future agents | [references/brand-identity-skill-template.md](references/brand-identity-skill-template.md) |
| 8. Validate | Run the validator, check contrast, verify values against source | [references/evidence-and-validation.md](references/evidence-and-validation.md) |
| 9. Report | Summarize to the user | below |

Load each reference file when you reach its phase rather than all up front.

### Validator

A stdlib-only Python script ships with this skill:

```bash
# Validate JSON tokens, CSS, SVGs, and local links in brand/
python3 <skill-dir>/scripts/validate_brand.py validate brand/

# WCAG contrast between two colors
python3 <skill-dir>/scripts/validate_brand.py contrast "#0A0A0A" "#F5F5F5"

# Contrast matrix for every color token pair in colors.json
python3 <skill-dir>/scripts/validate_brand.py matrix brand/tokens/colors.json
```

`<skill-dir>` is the directory containing this SKILL.md. Never claim a pairing meets WCAG without running the contrast check.

## Phase 9 — Final report

End with a concise report to the user containing:

- **Extracted identity** — a one-paragraph description of the visual impression, supported by evidence.
- **Core brand principles** — the 5–10 principles, one line each.
- **Files created** — tree of `brand/`.
- **Missing information** — everything marked Not established (e.g. no photography, no logo SVG, unknown font license).
- **Inconsistencies** — conflicting values found and where.
- **Recommended next steps** — clearly labeled as recommendations.
- **Validation result** — validator output summary; contrast failures.

Also confirm explicitly that no files outside `brand/` were changed (run `git status` if the project is a git repo).
