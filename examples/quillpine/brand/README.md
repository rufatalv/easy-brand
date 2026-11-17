# Quillpine Brand System

**What it looks like:** warm paper surfaces with ink text, a tight Fraunces display, uppercase mono labels marked with §, a ruled-notebook card with an orange margin line, and one forest-green band. Orange appears only in small marks.

This package was extracted from `../site/` by the [brand-extractor](../../../skills/brand-extractor/SKILL.md) skill. Nothing in the site was changed.

## How to use it

- **People:** start with [BRAND_GUIDELINES.md](BRAND_GUIDELINES.md).
- **AI agents:** load [skills/brand-identity/SKILL.md](skills/brand-identity/SKILL.md).
- **Code:** use the tokens in [tokens/](tokens/), or drop in [tokens/colors.css](tokens/colors.css).
- **Marketing assets:** start from [templates/](templates/).

## Files

| Path | Contents |
|---|---|
| [BRAND_GUIDELINES.md](BRAND_GUIDELINES.md) | Readable guide with do/don't lists |
| [BRAND_AUDIT.md](BRAND_AUDIT.md) | Evidence, frequency counts, conflicts, gaps |
| [BRAND_VOICE.md](BRAND_VOICE.md) | Voice, headline and CTA patterns |
| [tokens/](tokens/) | `colors`, `typography`, `spacing`, `radii`, `shadows`, `motion`, `layout` (.json), plus `colors.css` |
| [references/](references/) | Visual DNA, typography, colors, composition, graphics, components, imagery, motion, voice, consistency model |
| [templates/](templates/) | 4 HTML examples and `templates.json` |
| [assets/logos/](assets/logos/) | Copy of `site/assets/logo.svg` |
| [skills/brand-identity/](skills/brand-identity/) | Agent skill |

## Status labels

- **Observed:** taken directly from code or the rendered page.
- **Inferred:** a pattern seen in several places.
- **Recommended:** a proposal; not part of the brand yet.
- **Not established:** the source gives no evidence either way.

## Left out, and why

| Item | Reason |
|---|---|
| `references/3d-language.md` | No 3D or WebGL in the source |
| `assets/icons/` | No icon set; graphic marks are typographic glyphs |
| `assets/graphics/` | The ruled motif is pure CSS; see `template-base.css` |
| `templates/presentations/` | No evidence of decks or reports |
| Dark theme tokens | The site has no dark mode |

## Regenerating

Run the brand-extractor skill again on `site/`, then check the result:

```bash
python3 ../../../skills/brand-extractor/scripts/validate_brand.py validate .
```
