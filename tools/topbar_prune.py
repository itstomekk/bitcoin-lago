"""Drop top-bar chips for designs whose layout file does not exist yet, so the live site never shows dead links.
Chips come back automatically once tools/variants/<id>.html exists."""
import re
from pathlib import Path

VDIR = Path(__file__).resolve().parent / "variants"
ALL = ["a", "c", "d", "ac", "ad", "cd", "f", "g", "h"]


def existing():
    return {d for d in ALL if (VDIR / f"{d}.html").exists()}


def prune(html: str) -> str:
    have = existing()
    for d in ALL:
        if d in have:
            continue
        html = re.sub(r'[ \t]*<a [^>]*data-design="%s"[^>]*>.*?</a>\s*\n?' % d, "", html, flags=re.S)
    return html
