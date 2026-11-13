#!/usr/bin/env python3
"""Regenerate the self-contained GitHub header SVGs. Standard library only."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PALETTES = {
    "light": {
        "bg": "#f6f8fa", "ink": "#18252d", "muted": "#536872",
        "line": "#b7c9c8", "grid": "#dce4e7", "accent": "#167d66",
    },
    "dark": {
        "bg": "#10171e", "ink": "#e9f0f4", "muted": "#a0b4be",
        "line": "#3a565c", "grid": "#23343d", "accent": "#80e3c3",
    },
}


def render(theme: str, colors: dict[str, str]) -> str:
    bg, ink, muted, line, grid, accent = (
        colors[key] for key in ("bg", "ink", "muted", "line", "grid", "accent")
    )
    signal = (
        "M560 142 H582 L594 132 L605 153 L618 111 L631 175 "
        "L644 134 L656 142 H690 Q710 142 710 122 V94 Q710 80 726 80 "
        "H760 Q776 80 776 96 V126 Q776 142 792 142 H866"
    )
    variables = ""
    if theme == "static":
        light = ";".join(f"--{key}:{value}" for key, value in PALETTES["light"].items())
        dark = ";".join(f"--{key}:{value}" for key, value in PALETTES["dark"].items())
        variables = f":root {{{light}}} @media (prefers-color-scheme: dark) {{ :root {{{dark}}} }}"
    motion_path = "" if theme == "static" else (
        f'<path class="flow" d="{signal}" pathLength="100" stroke="{accent}" '
        'stroke-width="2.5" stroke-linecap="round"/>'
    )
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="960" height="280" viewBox="0 0 960 280" fill="none" role="img" aria-labelledby="title desc">
  <title id="title">Yash Rai — from signal to system</title>
  <desc id="desc">AI and ML engineering. An abstract signal becomes a structured routing circuit. Decorative traces move slowly; reduced-motion preferences disable movement. This illustration is not measured data.</desc>
  <style>
    {variables}
    .sans {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif; }}
    .mono {{ font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', monospace; }}
    .flow {{ stroke-dasharray: 9 91; animation: trace 12s linear infinite; }}
    @keyframes trace {{ from {{ stroke-dashoffset: 100; }} to {{ stroke-dashoffset: 0; }} }}
    @media (prefers-reduced-motion: reduce) {{ .flow {{ animation: none; display: none; }} }}
  </style>
  <defs>
    <pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse">
      <circle cx="12" cy="12" r="0.8" fill="{grid}"/>
    </pattern>
  </defs>
  <rect width="960" height="280" rx="10" fill="{bg}"/>
  <path d="M48 44 H72" stroke="{accent}" stroke-width="2"/>
  <text x="84" y="48" class="mono" fill="{muted}" font-size="12" letter-spacing="2">FROM SIGNAL TO SYSTEM</text>
  <text x="46" y="170" class="sans" fill="{ink}" font-size="112" font-weight="600" letter-spacing="-6">Yash Rai<tspan fill="{accent}">.</tspan></text>
  <text x="50" y="206" class="mono" fill="{muted}" font-size="13" letter-spacing="1.8">AI / ML ENGINEERING</text>
  <rect x="548" y="54" width="368" height="168" fill="url(#grid)"/>
  <g stroke="{line}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
    <path d="M560 94 H644 Q662 94 662 112 V174 Q662 192 680 192 H724"/>
    <path d="M560 190 H618 Q638 190 638 208 H768 Q792 208 792 184 V172 Q792 158 808 158 H866"/>
    <path d="M710 142 H744 Q760 142 760 158 V176"/>
    <path d="{signal}"/>
  </g>
  {motion_path}
  <g fill="{bg}" stroke="{line}" stroke-width="1.5">
    <circle cx="560" cy="94" r="3"/>
    <circle cx="560" cy="142" r="3"/>
    <circle cx="560" cy="190" r="3"/>
    <rect x="724" y="176" width="52" height="32" rx="5"/>
    <rect x="866" y="124" width="34" height="52" rx="5"/>
  </g>
  <g stroke="{accent}" stroke-width="1.5" stroke-linecap="round">
    <path d="M738 192 H744 L749 186 L755 198 L761 192"/>
    <path d="M876 137 H890 M876 150 H890 M876 163 H884"/>
  </g>
  <circle cx="776" cy="80" r="3" fill="{accent}"/>
  <path d="M48 244 H912" stroke="{grid}"/>
  <g class="mono" fill="{muted}" font-size="10" letter-spacing="1.4">
    <text x="50" y="264">RESEARCH</text>
    <text x="450" y="264">MODELS</text>
    <text x="912" y="264" text-anchor="end">SOFTWARE</text>
  </g>
</svg>
'''
    return "\n".join(line.rstrip() for line in svg.splitlines()) + "\n"


def main() -> None:
    directory = ROOT / "assets"
    directory.mkdir(exist_ok=True)
    for theme, colors in PALETTES.items():
        path = directory / f"identity-{theme}.svg"
        path.write_text(render(theme, colors), encoding="utf-8")
        print(f"Generated {path.relative_to(ROOT)}")
    path = directory / "identity-static.svg"
    path.write_text(
        render("static", {key: f"var(--{key})" for key in PALETTES["light"]}),
        encoding="utf-8",
    )
    print(f"Generated {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
