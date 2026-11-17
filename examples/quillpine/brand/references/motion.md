# Motion

Source of truth: [../tokens/motion.json](../tokens/motion.json). The site uses CSS transitions and an IntersectionObserver, with no animation library.

## Personality

**Calm and precise.** There is one entrance and two hover behaviors. Distances are small (16px, 3px, 2px). The ease starts quickly and settles slowly, with no overshoot.

## Patterns

| Pattern | Spec |
|---|---|
| Reveal | `opacity 0→1`, `translateY(16px)→0`, 600ms, `cubic-bezier(0.2, 0.7, 0.2, 1)`. Fires once when 15% visible (rootMargin bottom -10%). |
| Stagger | 80ms × `--i` (0–3), in order: eyebrow, headline, lede, actions |
| Card hover | `translateY(-2px)` plus `qp-shadow-lift`, 180ms ease-out |
| Button hover | Background or color change, 180ms ease-out; `→` moves 3px right |
| Reduced motion | Everything is visible immediately, and all transitions are off |

## CSS preset (copy into templates)

```css
.reveal { opacity: 0; transform: translateY(16px);
  transition: opacity 600ms cubic-bezier(.2,.7,.2,1), transform 600ms cubic-bezier(.2,.7,.2,1);
  transition-delay: calc(var(--i, 0) * 80ms); }
.reveal.is-visible { opacity: 1; transform: none; }
@media (prefers-reduced-motion: reduce) { .reveal { opacity: 1; transform: none; transition: none; } }
```

## For video and animated social posts `[Inferred]`

Use the same fade-rise per text block in hierarchy order, with an 80ms stagger. Hold the end frame. Never use scale, spin or bounce.
