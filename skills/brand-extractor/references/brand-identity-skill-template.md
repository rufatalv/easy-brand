# Phase 7: Generating `brand/skills/brand-identity/`

This is one of the most important deliverables: a skill future coding/design agents load to produce on-brand work **without re-auditing the codebase**.

It must be **self-contained**: the references inside `brand/skills/brand-identity/references/` carry the essential values (not just links), so the skill still works if copied into another repo or installed globally. Keep paths to `brand/tokens/*` as the canonical source when available.

Fill in every `{{…}}` from your extraction. Remove sections that don't apply (e.g. 3D). Keep `SKILL.md` under ~300 lines; push detail into references.

---

## Template: `brand/skills/brand-identity/SKILL.md`

````markdown
---
name: {{project-slug}}-brand-identity
description: Apply the {{Project Name}} brand identity when creating any visual or written asset — social posts, ads, banners, presentations, OG images, emails, landing-page sections or UI. Use whenever the user asks for something "on-brand", "in our style", or for {{Project Name}} marketing/design output. Provides tokens, typography, color roles, composition, imagery, motion and voice rules extracted from the product.
---

# {{Project Name}} Brand Identity

{{One-paragraph visual impression, evidence-based.}}

## Locate the brand system

1. If `brand/` exists in the repo, treat `brand/tokens/*.json` and `brand/tokens/colors.css` as canonical.
2. Otherwise use the values in `references/design-tokens.md` (bundled copy).

## Core principles

{{5–10 principles: name — one-line rule — constraint}}

## Workflow for any request

1. **Identify the output**: format, platform, dimensions, medium (HTML, SVG, React, slides, copy only).
2. **Pick a composition** from `references/composition.md` (and a template from `brand/templates/` if present).
3. **Apply typography** exactly per `references/typography.md` — roles, not ad-hoc sizes.
4. **Apply color** by role per `references/design-tokens.md` — respect accent budget and approved pairings.
5. **Apply graphic elements** — only the documented shape vocabulary.
6. **Handle imagery** per `references/imagery.md`; if no art direction is established, prefer type-led layouts or product screenshots over stock photos.
7. **Apply motion** (if animated) per `references/motion.md`.
8. **Write copy** per `references/content-generation.md`.
9. **Validate** against the checklist below.
10. **Export** in the requested format at the specified dimensions.

## Request playbooks

- **"Create a social media post"** → determine platform & size → choose editorial / visual / product template → apply tokens → write headline + CTA in brand voice → validate → export.
- **"Generate a landing-page section"** → read existing layout rules and component styles → reuse grid, spacing rhythm, type scale and motion presets → use the project's existing stack and components where in-repo → no new styles.
- **"Create an advertisement"** → identify campaign goal & audience → apply visual hierarchy (headline → proof → CTA) → one CTA per the CTA pattern → validate contrast and safe areas.

## Hard rules

- Do not invent a new identity per request.
- Do not change fonts: {{fonts}} only.
- Do not replace the palette or add colors outside the tokens.
- Do not introduce visual trends unrelated to the brand ({{list unrelated trends, e.g. glassmorphism, neon gradients — only if evidenced as absent}}).
- Do not use generic templates when project patterns exist.
- Do not invent logos — use files in `brand/assets/logos/` or {{logo note}}.

## Validation checklist

{{Condensed pass/fail list from consistency-model.md, e.g.:}}
- [ ] Only brand fonts, correct roles
- [ ] Colors only from tokens; accent within budget
- [ ] Text contrast ≥ 4.5:1 (≥ 3:1 for large text) — measured
- [ ] Radii/borders/shadows from tokens
- [ ] Spacing on the {{base}}px scale
- [ ] Copy matches voice: {{key voice traits}}
- [ ] Logo placement and safe areas respected
- [ ] Would be recognizable as {{Project Name}} with the logo removed
````

---

## Required reference files

Each should be compact (≤ ~200 lines), value-dense, and carry status tags only where something is Inferred/Recommended (Observed can be the default, stated once at the top).

| File | Contents |
|---|---|
| `brand-foundations.md` | Visual impression, principles with do/don't, what to preserve, logo usage, known gaps |
| `design-tokens.md` | Full color table (token, hex, role, approved pairs + measured ratios), spacing scale, radii, shadows, breakpoints/containers, CSS custom-property snippet ready to paste |
| `typography.md` | Families + fallbacks + loading method + license, role table, responsive scale, tracking/case rules |
| `imagery.md` | Image rules, text-over-image rules, screenshot/mockup treatment, or "Not established — prefer X" |
| `composition.md` | Grid, margins, hierarchy patterns, section recipes, per-format layouts and safe areas |
| `motion.md` | Durations, easings, springs, stagger, entrance/hover patterns, reduced-motion rule, code presets in the project's stack |
| `content-generation.md` | Voice principles, vocabulary, headline formulas, CTA patterns, length limits, good/bad examples from the real site |

Make the generated skill installable on its own: valid frontmatter (`name` lowercase-hyphenated, `description` explains what + when), and no references outside its folder that are *required* (links to `brand/` are fine as "if present").
