#!/usr/bin/env python3
"""Makes thumbnails for finished designs in the /variants/ index.

USAGE  python qa/make_thumbs.py http://127.0.0.1:18431/
       python qa/make_thumbs.py http://127.0.0.1:18431/ g
WRITES variants/thumbs/{a,c,d,ac,ad,cd,f,g,h,root}.webp  (640x400)
"""
import io
import sys
from pathlib import Path

from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
BASE = sys.argv[1].rstrip("/") + "/"
OUT = ROOT / "variants" / "thumbs"
OUT.mkdir(parents=True, exist_ok=True)
variants = ("a", "c", "d", "ac", "ad", "cd", "f", "g", "h")
fallbacks = {"ac", "ad", "cd"}
finished = [x for x in variants if (ROOT / "tools" / "variants" / f"{x}.html").is_file() or x in fallbacks]
selected = [x for x in sys.argv[2:] if x in finished] or finished
targets = {x: f"{BASE}v/{x}/" for x in selected}
if not sys.argv[2:] or "root" in sys.argv[2:]:
    targets["root"] = BASE
with sync_playwright() as p:
    b = p.chromium.launch()
    for name, url in targets.items():
        ctx = b.new_context(viewport={"width": 1440, "height": 900}, locale="en-US")
        pg = ctx.new_page()
        pg.goto(url, wait_until="networkidle")
        pg.wait_for_timeout(2600)  # let the opening animation finish
        im = Image.open(io.BytesIO(pg.screenshot())).convert("RGB").resize((640, 400), Image.LANCZOS)
        im.save(OUT / f"{name}.webp", "WEBP", quality=80, method=6)
        print(name, (OUT / f"{name}.webp").stat().st_size, "bytes")
        ctx.close()
    b.close()
