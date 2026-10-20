"""Build public WebP and JPG sizes from Tomek's ignored source-archive photos.

The source archive stays private and ignored; only the optimized images are published.
"""
from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source-archive" / "tomek-supplied"
DEST = ROOT / "images"
PHOTOS = {
    "community-tuktuk": "tuktuk-bitcoin-lake-road.jpg",
    "community-boat": "pier-to-pier-bitcoin-boat.jpg",
}
SIZES = (800, 1600)


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    for slug, filename in PHOTOS.items():
        source = SOURCE / filename
        if not source.is_file():
            raise FileNotFoundError(f"Required private source photo is missing: {source}")
        with Image.open(source) as original:
            image = ImageOps.exif_transpose(original).convert("RGB")
            source_width, source_height = image.size
            widths = sorted({min(size, source_width) for size in SIZES})
            for width in widths:
                height = round(source_height * width / source_width)
                resized = image.resize((width, height), Image.Resampling.LANCZOS)
                stem = f"{slug}-{width}"
                resized.save(DEST / f"{stem}.webp", "WEBP", quality=82, method=6)
                resized.save(DEST / f"{stem}.jpg", "JPEG", quality=84, optimize=True, progressive=True)
                print(f"wrote images/{stem}.webp and .jpg ({width}x{height})")


if __name__ == "__main__":
    main()
