# Phases 1–2: Source Discovery and Rendered Audit

## Phase 1 — Discover

Do not assume a framework. Find the actual architecture.

### Inspection order

1. Project structure (`ls`, `package.json`, lockfiles, monorepo workspaces).
2. Framework and styling tools.
3. Global styling.
4. Design tokens.
5. Typography sources.
6. Palette sources.
7. Reusable components.
8. Layouts and page sections.
9. Image assets.
10. Icons and logos.
11. Animations.
12. Responsive rules.
13. Existing marketing material / brand docs.
14. Run and visually inspect (Phase 2).

### Where to look

| Concern | Typical locations / signals |
|---|---|
| Framework | `package.json` deps: `next`, `nuxt`, `vue`, `@angular/core`, `svelte`, `@sveltejs/kit`, `astro`, `react`, `vite`, `gatsby`, `remix`; plain `*.html` for static sites |
| Styling | `tailwind.config.*`, `@theme` blocks in CSS (Tailwind v4), `postcss.config.*`, `*.scss`, `*.module.css`, `styled-components`, `@emotion`, `vanilla-extract`, `stitches`, `panda.config.*`, `uno.config.*`, CSS-in-JS theme objects |
| Global CSS | `globals.css`, `app.css`, `index.css`, `styles/`, `src/app/layout.*`, `_app.*`, `_document.*`, `app.vue`, `nuxt.config.*` |
| Tokens | `:root { --* }`, `[data-theme]`, `.dark {}`, `theme.ts`, `tokens.json`, Style Dictionary configs, `@theme`, shadcn `components.json` |
| Fonts | `next/font` imports, `@font-face`, Google Fonts `<link>`, `@fontsource/*` packages, `public/fonts/`, `*.woff2`, Typekit/Adobe embed ids |
| Components | `components/`, `ui/`, `src/lib/`, design-system packages in `packages/` |
| Assets | `public/`, `static/`, `assets/`, `src/assets/`, `*.svg`, `*.png`, `*.jpg`, `*.webp`, `*.avif`, `*.mp4`, `*.lottie`, `*.json` (Lottie), `*.glb`/`*.gltf` |
| Logos | filenames containing `logo`, `mark`, `wordmark`, `brand`, `favicon`, `icon`; `app/icon.*`, `manifest.json`, `apple-touch-icon` |
| Motion | `gsap`, `ScrollTrigger`, `framer-motion`, `motion`, `@react-spring`, `lenis`, `@studio-freight/lenis`, `animejs`, `@keyframes`, `transition:`, `requestAnimationFrame`, `element.animate(` |
| 3D | `three`, `@react-three/fiber`, `@react-three/drei`, `@react-three/postprocessing`, `ogl`, `regl`, `*.glsl`, `*.vert`, `*.frag`, `<canvas>` |
| Copy | page components, `content/`, `*.mdx`, i18n files (`locales/`, `messages/`), CMS fixtures, `metadata` exports, `<title>`/meta descriptions |
| Brand docs | `BRAND*.md`, `docs/`, `design/`, Figma exports, `README` |

Useful commands:

```bash
git ls-files | head -500                       # or find . -type f -not -path '*/node_modules/*'
grep -rn --include='*.{css,scss}' -- '--' src app styles 2>/dev/null | head
grep -rEn 'font-family|@font-face|next/font|fontsource' --exclude-dir=node_modules .
grep -rEn '#[0-9a-fA-F]{3,8}\b|rgba?\(|hsla?\(|oklch\(' --exclude-dir=node_modules --include='*.{css,scss,ts,tsx,js,jsx,vue,svelte}' . | wc -l
```

Count frequency of colors/radii/spacing values — frequency tells you what is systemic vs. one-off.

## Phase 2 — Observe (rendered audit)

If a browser/automation tool is available (Playwright, a browser MCP, the host's built-in browser), start the dev server and inspect real output. If not, say so in the audit and rely on code; mark visual-only claims as Inferred.

Starting the app: read `package.json` scripts; prefer `dev` or `preview`. Don't install new global tooling. If install is required and not yet done, ask or use the project's own package manager. Stop the server when finished.

### Capture

Screenshots (save to `brand/references/screenshots/` only if the user is fine committing images; otherwise keep in a temp dir and reference by description):

- Homepage, major sections, navigation, footer
- Buttons and interaction states (hover/focus where possible)
- Dark and light themes if both exist
- Important secondary pages and marketing pages

Viewports: **390, 768, 1280, 1440 px** wide. Add others if a breakpoint changes layout significantly.

If you can evaluate JS in the page, `getComputedStyle` on key elements (h1, h2, body, nav links, buttons, cards) gives exact rendered font, size, line-height, letter-spacing, colors, radii — the highest-priority evidence.

### Analyze

- Visual hierarchy and color distribution (rough % of dark vs. light vs. accent area)
- Typography proportions (display-to-body ratio)
- Section transitions, whitespace, grid, alignment
- Image cropping, component proportions, borders
- Background composition, graphic details, repeated motifs

### Overall visual impression

Write 1–2 sentences describing the impression, e.g. *"Dark editorial interface with high-contrast typography, blue accent lighting, soft rounded panels and cinematic 3D backgrounds."* Every adjective must be backed by evidence you can cite.

## Brand DNA (feeds `references/visual-dna.md`)

Answer from evidence:

- What distinguishes this interface from similar products?
- Which visual features repeat throughout?
- What makes the design coherent?
- How do typography and imagery relate?
- How are accents distributed?
- How is depth established (shadow, blur, layering, 3D, contrast)?
- What gives it personality?
- What must be preserved in future work?

Produce **5–10 core brand principles**. Each has:

- **Name**
- **Description**
- **Evidence** (sources)
- **Application** (what to do)
- **Constraints** (what not to do)
- **Status** (Observed / Inferred)
