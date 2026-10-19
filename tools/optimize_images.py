#!/usr/bin/env python3
"""Resize the Wikimedia Commons photos for the web (WebP + JPG fallback).

WHAT IT DOES
  Takes the CC-licensed photos in source-archive/images/commons/ (ONLY that folder;
  press photos and logos in _curated/ are reference material and are never used)
  and writes images/<slug>-800.{webp,jpg} and images/<slug>-1600.{webp,jpg}.
  Also writes data/photos.json with the credit line for each photo, copied from
  source-archive/images/commons/_attribution.json (artist, licence, Commons page).

Run:  python tools/optimize_images.py      (needs Pillow)
"""
import json
import re
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "source-archive" / "images" / "commons"
OUT = ROOT / "images"

# slug -> source file. Slugs say what the photo is used for on the page.
PICKS = {
    "hero": "commons_04.jpg",
    "lake-view": "commons_01.jpg",
    "sunrise": "commons_14.jpg",
    "street": "commons_15.jpg",
    "history-1975": "commons_03.jpg",
    "panorama": "commons_16.jpg",
    "shore": "commons_06.jpg",
    "tours": "commons_11.jpg",
}
WIDTHS = (800, 1600)
LICENCE_URLS = {
    "CC BY 2.0": "https://creativecommons.org/licenses/by/2.0/",
    "CC BY 4.0": "https://creativecommons.org/licenses/by/4.0/",
    "CC BY-SA 2.0": "https://creativecommons.org/licenses/by-sa/2.0/",
    "CC BY-SA 3.0": "https://creativecommons.org/licenses/by-sa/3.0/",
    "CC BY-SA 4.0": "https://creativecommons.org/licenses/by-sa/4.0/",
}


def main():
    OUT.mkdir(exist_ok=True)
    attr = {a["file"]: a for a in json.loads((SRC / "_attribution.json").read_text(encoding="utf-8"))}
    photos = {}
    for slug, fname in PICKS.items():
        im = Image.open(SRC / fname).convert("RGB")
        for w in WIDTHS:
            h = round(im.height * w / im.width)
            r = im.resize((w, h), Image.LANCZOS) if im.width > w else im.copy()
            r.save(OUT / f"{slug}-{w}.webp", "WEBP", quality=72, method=6)
            r.save(OUT / f"{slug}-{w}.jpg", "JPEG", quality=78, optimize=True, progressive=True)
        a = attr[fname]
        title = re.sub(r"^File:", "", a["title"])
        photos[slug] = {
            "file": fname,
            "title": title,
            "artist": a["artist"].replace("User:", ""),
            "license": a["license"],
            "license_url": LICENCE_URLS[a["license"]],
            "page": a["page"],
            "width": 1600,
            "height": round(im.height * 1600 / im.width) if im.width > 1600 else im.height,
        }
        print(slug, fname, im.size, "->", photos[slug]["height"])
    (ROOT / "data" / "photos.json").write_text(json.dumps(photos, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
