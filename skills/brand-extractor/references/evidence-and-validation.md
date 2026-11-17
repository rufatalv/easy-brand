# Phases 4 & 8: Evidence, Classification and Validation

## Evidence

Every major rule needs at least one source:

- File path with line: `src/app/globals.css:14`
- CSS variable / token: `--radius-lg`, `theme.colors.brand.600`
- Component: `components/ui/button.tsx (variant="primary")`
- Asset: `public/logo-mark.svg`
- Animation config: `components/Hero.tsx:42 gsap.from(..., { duration: 1.2, ease: "expo.out" })`
- Screenshot: `home@1440 — hero` (describe if images aren't saved)

## Classification

| Status | Meaning | Allowed in `tokens` | Tag |
|---|---|---|---|
| Observed | Directly in code or rendered output | Yes | `[Observed: <source>]` |
| Inferred | Plausible pattern from ≥ 2 observations | Yes, with `status: "inferred"` | `[Inferred: <sources>]` |
| Recommended | Proposed extension, not in the project | Only under `recommended` | `[Recommended]` |
| Not established | Cannot be determined | No | `Not established` |

Conflicts: when two sources disagree, record both, investigate (theme? state? page? legacy?), and state which is current and why. If you can't tell, say so.

## Validation checklist (Phase 8)

### Accuracy — re-open the source and compare

- [ ] Every core color hex matches source (spot-check all core + supporting tokens; convert HSL/OKLCH carefully)
- [ ] Font family names, weights and loading method match
- [ ] Type sizes / line-heights / tracking match (computed styles if rendered)
- [ ] Spacing, container, breakpoint values match config
- [ ] Animation durations, easings, springs match code
- [ ] Component descriptions match their implementations

### Visual consistency (if rendering is available)

Render any generated template examples and compare side-by-side with the site:
mismatched fonts, wrong color balance, incorrect radii, unrelated imagery, inconsistent hierarchy, wrong motion personality. Fix the template, not the site.

### Code validation

Run:

```bash
python3 <skill-dir>/scripts/validate_brand.py validate brand/
python3 <skill-dir>/scripts/validate_brand.py matrix brand/tokens/colors.json
```

`validate` checks:
- JSON syntax for every `*.json`
- Token envelope + required token fields (`$value`, `$type`, `$description`, `status`, `source`); `recommended` tokens kept out of `tokens`
- CSS brace balance and custom-property syntax
- SVG files parse as XML with an `<svg>` root
- Relative links/`src`/`href` in `.md`, `.html`, `.css` resolve to existing files
- Generated `SKILL.md` files have `name` + `description` frontmatter

Fix every error. Warnings should be reviewed and either fixed or explained in `BRAND_AUDIT.md`.

### Non-destructive check

```bash
git status --porcelain | grep -v '^?? brand/' | grep -v '^.. brand/'
```

Should print nothing that you caused. If you changed anything outside `brand/`, revert it.

### Documentation usability

Ask: could another agent produce an on-brand Instagram post and a landing section using only `brand/skills/brand-identity/` without opening the app source? If not, add the missing values to the skill's references.
