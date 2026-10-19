#!/usr/bin/env python3
"""Resize the press photos for the web (WebP + JPG fallback).

WHAT IT DOES
  Takes the raw press photos in images/press/ (source files, ~28 MB)
  and writes optimized versions to images/press/<slug>-800.{webp,jpg}
  and images/press/<slug>-1600.{webp,jpg}.
  Updates data/press-photos.json with the optimized slug paths.

Run:  python tools/optimize_press_images.py
"""
import json
import re
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "images" / "press"  # raw source files
OUT = ROOT / "images" / "press"  # optimized output (same folder, different names)

# Load press photo metadata
PRESS_DATA = json.loads((ROOT / "data" / "press-photos.json").read_text(encoding="utf-8"))

WIDTHS = (800, 1600)

# Map source filename -> slug (for optimized filenames)
# Slugs are derived from the source filename without extension
def slugify(fname):
    return Path(fname).stem


def main():
    OUT.mkdir(exist_ok=True)
    
    # Update press-photos.json with optimized slugs
    updated = []
    for item in PRESS_DATA:
        src_file = Path(item["file"]).name  # e.g., "images/press/elfaro_01.jpg" -> "elfaro_01.jpg"
        slug = slugify(src_file)
        
        src_path = SRC / src_file
        if not src_path.exists():
            print(f"WARNING: Source file not found: {src_path}")
            updated.append(item)
            continue
        
        try:
            im = Image.open(src_path).convert("RGB")
        except Exception as e:
            print(f"ERROR opening {src_path}: {e}")
            updated.append(item)
            continue
        
        # Generate optimized versions
        for w in WIDTHS:
            h = round(im.height * w / im.width)
            r = im.resize((w, h), Image.LANCZOS) if im.width > w else im.copy()
            r.save(OUT / f"{slug}-{w}.webp", "WEBP", quality=72, method=6)
            r.save(OUT / f"{slug}-{w}.jpg", "JPEG", quality=78, optimize=True, progressive=True)
        
        # Update item with optimized slug
        item["slug"] = slug
        item["width_1600"] = 1600
        item["height_1600"] = round(im.height * 1600 / im.width) if im.width > 1600 else im.height
        print(f"Optimized: {src_file} -> {slug} ({im.size} -> {item['height_1600']} at 1600w)")
        
        updated.append(item)
    
    # Write updated press-photos.json
    (ROOT / "data" / "press-photos.json").write_text(
        json.dumps(updated, ensure_ascii=False, indent=1), encoding="utf-8"
    )
    print("Updated data/press-photos.json with slugs")


if __name__ == "__main__":
    main()