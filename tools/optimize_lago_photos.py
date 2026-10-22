"""Build public WebP and JPG sizes for Lago Bitcoin's own photos (Eliazar's Telegram archive and
the public X posts of @JUN_AJPU_btc and @AtitlanTours21). Sources stay in the ignored source-archive.

Run: python tools/optimize_lago_photos.py   (writes images/lb-<slug>-<w>.webp/.jpg)
The slugs, captions and credits live in tools/content.py (LB_PHOTOS).
"""
from pathlib import Path
import sys

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import content as C  # noqa: E402

SA = ROOT / "source-archive"
DEST = ROOT / "images"
SIZES = (640, 1200)


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    for slug, meta in C.LB_PHOTOS.items():
        source = SA / meta["src"]
        if not source.is_file():
            raise FileNotFoundError(f"Missing private source photo: {source}")
        with Image.open(source) as original:
            image = ImageOps.exif_transpose(original).convert("RGB")
            box = meta.get("crop")
            if box:
                w, h = image.size
                image = image.crop((round(box[0] * w), round(box[1] * h), round(box[2] * w), round(box[3] * h)))
            sw, sh = image.size
            for width in sorted({min(s, sw) for s in SIZES}):
                height = round(sh * width / sw)
                resized = image.resize((width, height), Image.Resampling.LANCZOS)
                stem = f"lb-{slug}-{width}"
                resized.save(DEST / f"{stem}.webp", "WEBP", quality=80, method=6)
                resized.save(DEST / f"{stem}.jpg", "JPEG", quality=82, optimize=True, progressive=True)
                print(f"wrote images/{stem} ({width}x{height})")


if __name__ == "__main__":
    main()
