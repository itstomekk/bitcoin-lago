#!/usr/bin/env python3
"""Build icons.svg, the single SVG sprite used by both pages.

WHAT IT DOES
  Copies a short list of Phosphor Icons (MIT licence, https://phosphoricons.com) out of the
  npm package @phosphor-icons/core into one sprite. Pages use them as
  <svg><use href="icons.svg#i-boat"/></svg>.
  The icons are not hand drawn; to add one, put its name in NAMES and re-run.

Run:  python tools/build_icons.py <path-to>/node_modules/@phosphor-icons/core/assets/regular
"""
import re
import sys
from pathlib import Path

NAMES = [
    "whatsapp-logo", "map-pin", "boat", "taxi", "currency-btc", "graduation-cap", "users-three",
    "mountains", "handshake", "arrow-up-right", "magnifying-glass", "phone", "globe", "facebook-logo",
    "instagram-logo", "lightning", "link", "list", "x", "clock", "compass", "bank", "envelope-simple",
    "calendar-blank", "info", "caret-down", "path",
]


def main(src):
    src = Path(src)
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" style="display:none">']
    for n in NAMES:
        svg = (src / f"{n}.svg").read_text(encoding="utf-8")
        inner = re.search(r"<svg[^>]*>(.*)</svg>", svg, re.S).group(1)
        parts.append(f'<symbol id="i-{n}" viewBox="0 0 256 256" fill="currentColor">{inner}</symbol>')
    parts.append("</svg>")
    out = Path(__file__).resolve().parent.parent / "icons.svg"
    out.write_text("\n".join(parts), encoding="utf-8")
    print("wrote", out, len(NAMES), "icons")


if __name__ == "__main__":
    main(sys.argv[1])
