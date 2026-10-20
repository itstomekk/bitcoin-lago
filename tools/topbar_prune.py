"""Drop top-bar chips for designs without a production layout or explicit layout fallback."""
import re
from pathlib import Path

VDIR = Path(__file__).resolve().parent / "variants"
ALL = ["a", "c", "d", "ac", "ad", "cd", "f", "g", "h"]
LAYOUT_FALLBACKS = {"ac": "c", "ad": "d", "cd": "c"}


def existing():
    return {d for d in ALL if (VDIR / f"{d}.html").exists() or d in LAYOUT_FALLBACKS}


def prune(html: str) -> str:
    have = existing()
    for d in ALL:
        if d in have:
            continue
        html = re.sub(r'[ \t]*<a [^>]*data-design="%s"[^>]*>.*?</a>\s*\n?' % d, "", html, flags=re.S)
    return html
