"""Optimize the privately archived AB23 talk thumbnail for local use.

The downloaded YouTube source stays in ignored source-archive/; only the
optimized WebP and JPG poster files are published in images/.
"""
from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source-archive" / "ab23-talk-thumbnail-original.jpg"
DEST = ROOT / "images" / "ab23-talk-poster"


def main():
    if not SOURCE.is_file():
        raise FileNotFoundError(f"Download the official hqdefault.jpg to {SOURCE} first")
    with Image.open(SOURCE) as original:
        image = ImageOps.exif_transpose(original).convert("RGB")
        image.save(DEST.with_suffix(".webp"), "WEBP", quality=82, method=6)
        image.save(DEST.with_suffix(".jpg"), "JPEG", quality=84, optimize=True, progressive=True)
        print(f"wrote {DEST.with_suffix('.webp')} and {DEST.with_suffix('.jpg')} ({image.width}x{image.height})")


if __name__ == "__main__":
    main()
