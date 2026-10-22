"""Turn the X archive harvest (source-archive/x-harvest-2026-10-21.json, gitignored) into
tools/story_data.json (committed) and web-sized photos in images/x/.

Run: python tools/import_x_harvest.py   then   python tools/build_variants.py
Only photos with child_faces == false are published.
"""
import json
import re
from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "source-archive" / "x-harvest-2026-10-21.json"
OUT = ROOT / "tools" / "story_data.json"
IMG = ROOT / "images" / "x"

FACT_ES = {
    "Where bitcoin is accepted, by town": "Dónde se acepta bitcoin, por pueblo",
    "Kaboom, waste to energy mining": "Kaboom, minería con aceite usado",
    "Mining class": "Clases de minería",
    "My First Bitcoin partnership": "Con Mi Primer Bitcoin",
    "Looking Glass diploma (ABC de Bitcoin)": "Diploma de Looking Glass (ABC de Bitcoin)",
    "First Lightning payments in class": "Primeros pagos Lightning en clase",
    "Schools reached": "Escuelas alcanzadas",
    "LTK School routines": "Un año en LTK School",
    "Education in local language": "Educación en idioma local",
    "Public library shelf": "Estante en la biblioteca pública",
    "Books donated and read": "Libros donados y leídos",
    "Swiss donations": "Donaciones desde Suiza",
    "Fedi at the lake": "Fedi en el lago",
    "Blink at the lake": "Blink en el lago",
    "Bullish Guatemala": "Bullish Guatemala",
    "Escuelita Bitcoin": "Escuelita Bitcoin",
    "Monthly meetups and venues": "Encuentros mensuales y lugares",
    "Pizza Day": "Pizza Day",
    "Tuk tuks": "Tuk tuks",
    "Bitcoin boat": "La lancha Bitcoin",
    "Murals, signs and ads": "Murales, rótulos y anuncios",
    "Bit Mayan Coffee": "Bit Mayan Coffee",
    "Real estate and rentals paid in bitcoin": "Alquileres y propiedades con bitcoin",
    "Everyday payments seen": "Pagos del día a día",
    "Bitcoin ATM": "Cajero de Bitcoin",
    "Lago Summit 2023": "Lago Summit 2023",
    "Adopting Bitcoin": "Adopting Bitcoin",
    "Bitcoin Beach and circular economy networks": "Bitcoin Beach y la red de economías circulares",
    "Visitors and visitor media": "Visitantes y sus videos",
    "Language and culture posts": "Lengua y cultura",
    "Eliazar as a guide before the tours account": "Eliazar como guía",
    "Google Maps and BTC Map": "Google Maps y BTC Map",
    "Tekoa Spaces": "Tekoa Spaces",
    "Amaranto": "Amaranto",
    "Giving back: local social needs": "Apoyo a la comunidad",
}
# Corrections after checking bullishguate.com (2026-10-21).
FIX = {
    ("Bullish Guatemala", "en"): [
        ("is an X account of the Guatemalan Bitcoin community.", "is a Bitcoin-only company in Guatemala: an exchange that sends sats to your own wallet, hardware wallets, advice and meetups."),
        (re.compile(r",? and in March 2025 introduced a tour agency run by Mario at the lake, with the Lightning address \S+?\."), "."),
    ],
    ("Bullish Guatemala", "es"): [
        ("es una cuenta de X de la comunidad Bitcoin de Guatemala.", "es una empresa solo Bitcoin en Guatemala: un exchange que envía los sats a tu propia billetera, hardware, asesorías y meetups."),
        (re.compile(r",? y en marzo de 2025 presentó a una agencia de tours dirigida por Mario en el lago, con la dirección Lightning \S+?\."), "."),
    ],
}


def fix(topic, lang, text):
    for old, new in FIX.get((topic, lang), []):
        text = old.sub(new, text) if hasattr(old, "sub") else text.replace(old, new)
    text = text.replace("Lago Bitcoin", "Bitcoin Lago")
    assert "\u2014" not in text and "\u2013" not in text, text
    return text


def main():
    h = json.loads(SRC.read_text(encoding="utf-8"))
    IMG.mkdir(parents=True, exist_ok=True)
    photos = []
    for p in h["photos"]:
        if p.get("child_faces"):
            continue
        src = Path(p["file"])
        if not src.is_absolute():
            src = ROOT / "source-archive" / "x-photos" / src.name
        if not src.is_file():
            src = ROOT / "source-archive" / "x-photos" / Path(p["file"]).name
        stem = src.stem  # date_tweetid_n
        with Image.open(src) as im:
            im = ImageOps.exif_transpose(im).convert("RGB")
            sizes = []
            for w in (480, 960):
                if im.width < w * 0.8 and w != 480:
                    continue
                r = im if im.width <= w else im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
                r.save(IMG / f"{stem}-{w}.jpg", quality=80, optimize=True, progressive=True)
                r.save(IMG / f"{stem}-{w}.webp", quality=76)
                sizes.append((w, r.width, r.height))
        photos.append({"stem": stem, "tweet_id": p["tweet_id"], "date": p["date"], "year": p["date"][:4],
                       "en": fix("", "en", p["caption_en"]), "es": fix("", "es", p["caption_es"]),
                       "w": sizes[0][1], "h": sizes[0][2], "widths": [s[0] for s in sizes]})
    timeline = [{"date": t["date"], "ids": t["source_tweet_ids"][:3],
                 "title_en": fix("", "en", t["title_en"]), "title_es": fix("", "es", t["title_es"]),
                 "en": fix("", "en", t["text_en"]), "es": fix("", "es", t["text_es"])} for t in h["timeline"]]
    facts = [{"topic_en": f["topic"], "topic_es": FACT_ES[f["topic"]], "ids": f["source_tweet_ids"][:3],
              "en": fix(f["topic"], "en", f["en"]), "es": fix(f["topic"], "es", f["es"])}
             for f in h["facts"] if f["topic"] in FACT_ES]
    tours = [{"en_t": i["topic"], "en": fix("", "en", i["en"]), "es": fix("", "es", i["es"]), "ids": i["source_tweet_ids"][:2]}
             for i in h["tours"]["includes"]]
    OUT.write_text(json.dumps({"timeline": timeline, "facts": facts, "photos": photos, "tours": tours},
                              ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"timeline {len(timeline)}, facts {len(facts)}, photos {len(photos)}, tours {len(tours)} -> {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
