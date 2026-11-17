#!/usr/bin/env python3
"""Validate a brand-extractor `brand/` directory and check color contrast.

Stdlib only. Usage:
  validate_brand.py validate <brand_dir>
  validate_brand.py contrast <fg> <bg>
  validate_brand.py matrix <colors.json> [--min RATIO]
"""
import argparse
import colorsys
import json
import re
import sys
import xml.etree.ElementTree as ET
from itertools import combinations
from pathlib import Path

TOKEN_REQUIRED = ("$value", "$type", "$description", "status", "source")
STATUSES = {"observed", "inferred", "recommended"}


# ---------- color ----------

def parse_color(value):
    """Return (r, g, b) in 0..255 or None if unsupported."""
    if not isinstance(value, str):
        return None
    v = value.strip().lower()
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h[:3])
        elif len(h) in (6, 8):
            h = h[:6]
        else:
            return None
        return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
    m = re.fullmatch(r"rgba?\(\s*([\d.]+)[\s,]+([\d.]+)[\s,]+([\d.]+).*\)", v)
    if m:
        return tuple(round(float(x)) for x in m.groups())
    m = re.fullmatch(r"hsla?\(\s*([\d.]+)(?:deg)?[\s,]+([\d.]+)%[\s,]+([\d.]+)%.*\)", v)
    if m:
        h, s, l = (float(x) for x in m.groups())
        r, g, b = colorsys.hls_to_rgb(h / 360, l / 100, s / 100)
        return tuple(round(x * 255) for x in (r, g, b))
    return None


def luminance(rgb):
    def ch(c):
        c /= 255
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (ch(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(a, b):
    la, lb = sorted((luminance(a), luminance(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def wcag_levels(ratio):
    return {
        "AA normal": ratio >= 4.5,
        "AA large/UI": ratio >= 3.0,
        "AAA normal": ratio >= 7.0,
        "AAA large": ratio >= 4.5,
    }


# ---------- validate ----------

class Report:
    def __init__(self):
        self.errors, self.warnings = [], []

    def err(self, path, msg):
        self.errors.append(f"ERROR   {path}: {msg}")

    def warn(self, path, msg):
        self.warnings.append(f"WARN    {path}: {msg}")


def check_tokens(path, data, rep):
    if not isinstance(data, dict) or "tokens" not in data:
        rep.warn(path, "no top-level 'tokens' object (expected brand-extractor token envelope)")
        return
    for section in ("tokens", "recommended"):
        group = data.get(section, {})
        if not isinstance(group, dict):
            rep.err(path, f"'{section}' must be an object")
            continue
        for name, tok in iter_tokens(group):
            where = f"{section}.{name}"
            missing = [k for k in TOKEN_REQUIRED if k not in tok]
            if missing:
                rep.err(path, f"{where} missing {', '.join(missing)}")
            status = tok.get("status")
            if status and status not in STATUSES:
                rep.err(path, f"{where} has invalid status '{status}'")
            if section == "tokens" and status == "recommended":
                rep.err(path, f"{where} is 'recommended' but lives in 'tokens'")
            if section == "recommended" and status in ("observed", "inferred"):
                rep.warn(path, f"{where} is '{status}' but lives in 'recommended'")
            if status in ("observed", "inferred") and not tok.get("source"):
                rep.err(path, f"{where} is {status} but has no source")
            if tok.get("$type") == "color" and parse_color(tok.get("$value")) is None:
                rep.warn(path, f"{where} color value '{tok.get('$value')}' not parseable for contrast checks")


def iter_tokens(group, prefix=""):
    """Yield (name, token) for token objects, allowing nested groups."""
    for k, v in group.items():
        if not isinstance(v, dict):
            continue
        name = f"{prefix}{k}"
        if "$value" in v:
            yield name, v
        else:
            yield from iter_tokens(v, prefix=f"{name}.")


def check_css(path, text, rep):
    stripped = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
    stripped = re.sub(r"(['\"]).*?\1", "", stripped)
    depth = 0
    for i, c in enumerate(stripped):
        depth += c == "{"
        depth -= c == "}"
        if depth < 0:
            rep.err(path, f"unexpected '}}' near char {i}")
            return
    if depth:
        rep.err(path, f"{depth} unclosed '{{'")
    for m in re.finditer(r"(?m)^\s*(--[^:\s]*)\s*:", stripped):
        if not re.fullmatch(r"--[A-Za-z0-9_-]+", m.group(1)):
            rep.err(path, f"invalid custom property name '{m.group(1)}'")


def check_svg(path, rep):
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as e:
        rep.err(path, f"invalid XML: {e}")
        return
    if not root.tag.endswith("svg"):
        rep.err(path, f"root element is <{root.tag}>, expected <svg>")


LINK_PATTERNS = [
    re.compile(r"\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)"),         # markdown
    re.compile(r"""(?:src|href)\s*=\s*["']([^"']+)["']"""),          # html
    re.compile(r"""url\(\s*["']?([^"')]+)["']?\s*\)"""),               # css
    re.compile(r"""@import\s+["']([^"']+)["']"""),
]


def check_links(path, text, rep):
    text = re.sub(r"```.*?```", "", text, flags=re.S) if path.suffix == ".md" else text
    for pat in LINK_PATTERNS:
        for m in pat.finditer(text):
            target = m.group(1).split("#")[0].split("?")[0]
            if not target or re.match(r"^(?:[a-z]+:|//|#|\{\{|<)", target, re.I):
                continue
            if not (path.parent / target).exists():
                rep.err(path, f"broken local reference '{m.group(1)}'")


def check_skill(path, text, rep):
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        rep.err(path, "SKILL.md missing YAML frontmatter")
        return
    fm = m.group(1)
    name = re.search(r"(?m)^name:\s*(\S.*)$", fm)
    if not name:
        rep.err(path, "frontmatter missing 'name'")
    elif not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name.group(1).strip().strip("'\"")):
        rep.err(path, f"name '{name.group(1)}' should be lowercase-hyphenated")
    if not re.search(r"(?m)^description:\s*\S", fm):
        rep.err(path, "frontmatter missing 'description'")
    if "{{" in text:
        rep.warn(path, "contains unfilled {{placeholders}}")


def cmd_validate(args):
    root = Path(args.brand_dir)
    if not root.is_dir():
        print(f"not a directory: {root}")
        return 2
    rep = Report()
    counts = {}
    for p in sorted(root.rglob("*")):
        if not p.is_file():
            continue
        rel = p.relative_to(root.parent) if root.parent != p else p
        counts[p.suffix] = counts.get(p.suffix, 0) + 1
        try:
            if p.suffix == ".json":
                data = json.loads(p.read_text(encoding="utf-8"))
                if "tokens" in p.parts:
                    check_tokens(rel, data, rep)
            elif p.suffix == ".css":
                text = p.read_text(encoding="utf-8")
                check_css(rel, text, rep)
                check_links(p, text, rep)
            elif p.suffix == ".svg":
                check_svg(p, rep)
            elif p.suffix in (".md", ".html", ".htm"):
                text = p.read_text(encoding="utf-8")
                check_links(p, text, rep)
                if p.name == "SKILL.md":
                    check_skill(rel, text, rep)
                elif p.suffix == ".md" and p.stat().st_size == 0:
                    rep.warn(rel, "empty file")
        except json.JSONDecodeError as e:
            rep.err(rel, f"invalid JSON: {e}")
        except UnicodeDecodeError:
            rep.warn(rel, "not UTF-8 text")

    for line in rep.errors + rep.warnings:
        print(line)
    summary = ", ".join(f"{n} {s or 'no-ext'}" for s, n in sorted(counts.items()))
    print(f"\nChecked: {summary or 'no files'}")
    print(f"{len(rep.errors)} error(s), {len(rep.warnings)} warning(s)")
    return 1 if rep.errors else 0


def cmd_contrast(args):
    a, b = parse_color(args.fg), parse_color(args.bg)
    if a is None or b is None:
        print("unsupported color (use hex, rgb() or hsl())")
        return 2
    r = contrast_ratio(a, b)
    print(f"{args.fg} on {args.bg}: {r:.2f}:1")
    for level, ok in wcag_levels(r).items():
        print(f"  {'PASS' if ok else 'FAIL'}  {level}")
    return 0


def cmd_matrix(args):
    data = json.loads(Path(args.colors_json).read_text(encoding="utf-8"))
    colors = {}
    for name, tok in iter_tokens(data.get("tokens", data)):
        rgb = parse_color(tok.get("$value"))
        if rgb:
            colors[name] = (tok["$value"], rgb)
        for theme, val in (tok.get("themes") or {}).items():
            rgb = parse_color(val)
            if rgb:
                colors[f"{name}@{theme}"] = (val, rgb)
    rows = []
    for (n1, (v1, c1)), (n2, (v2, c2)) in combinations(colors.items(), 2):
        r = contrast_ratio(c1, c2)
        if r >= args.min:
            rows.append((r, n1, v1, n2, v2))
    rows.sort(reverse=True)
    print(f"{'ratio':>7}  {'AA':<4} {'AAA':<4} pair")
    for r, n1, v1, n2, v2 in rows:
        lv = wcag_levels(r)
        aa = "yes" if lv["AA normal"] else ("lg" if lv["AA large/UI"] else "no")
        aaa = "yes" if lv["AAA normal"] else ("lg" if lv["AAA large"] else "no")
        print(f"{r:7.2f}  {aa:<4} {aaa:<4} {n1} ({v1}) / {n2} ({v2})")
    print(f"\n{len(colors)} colors, {len(rows)} pairs with ratio >= {args.min}")
    print("AA/AAA: yes = normal text passes, lg = large text/UI only, no = fails")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("validate", help="validate a brand/ directory")
    p.add_argument("brand_dir")
    p.set_defaults(fn=cmd_validate)
    p = sub.add_parser("contrast", help="WCAG contrast of two colors")
    p.add_argument("fg")
    p.add_argument("bg")
    p.set_defaults(fn=cmd_contrast)
    p = sub.add_parser("matrix", help="contrast for all color token pairs")
    p.add_argument("colors_json")
    p.add_argument("--min", type=float, default=3.0, help="only show pairs at or above this ratio (default 3.0)")
    p.set_defaults(fn=cmd_matrix)
    args = ap.parse_args()
    sys.exit(args.fn(args))


if __name__ == "__main__":
    main()
