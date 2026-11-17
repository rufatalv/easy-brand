# Motion

**Personality: calm and precise.** Movements are small, settle without overshoot, and play once.

| Pattern | Spec |
|---|---|
| Reveal | opacity 0→1 and translateY(16px)→0, 600ms, `cubic-bezier(0.2, 0.7, 0.2, 1)`, plays once at 15% visibility |
| Stagger | 80ms × index, in order: eyebrow, headline, body, actions |
| Card hover | translateY(-2px) plus the lift shadow, 180ms ease-out |
| Button hover | Color swap (ink → `#B83A16`), 180ms; `→` moves 3px right |
| Reduced motion | Show everything immediately; no transitions |

```css
.reveal { opacity:0; transform:translateY(16px);
  transition: opacity 600ms cubic-bezier(.2,.7,.2,1), transform 600ms cubic-bezier(.2,.7,.2,1);
  transition-delay: calc(var(--i,0) * 80ms); }
.reveal.is-visible { opacity:1; transform:none; }
@media (prefers-reduced-motion: reduce) { .reveal { opacity:1; transform:none; transition:none; } }
```

```js
const io = new IntersectionObserver((es) => es.forEach((e) => {
  if (e.isIntersecting) { e.target.classList.add("is-visible"); io.unobserve(e.target); }
}), { threshold: 0.15, rootMargin: "0px 0px -10% 0px" });
document.querySelectorAll(".reveal").forEach((el) => io.observe(el));
```

## Video and animated social `[Inferred]`

Apply the same fade-rise to each block with an 80ms stagger, then hold the final frame for at least 2 seconds. Don't use scale, spin, bounce, kinetic type or loops.
