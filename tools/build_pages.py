#!/usr/bin/env python3
"""Build index.html (English) and es/index.html (Spanish) from one template.

WHAT IT DOES
  Fills tools/page.template.html with the words in tools/content.py and with a few blocks
  generated from the data files (village counts, boat and tuk tuk rows, photo credits,
  press list). Because both languages come from the same template, they always have the
  same sections and ids. Missing keys stop the build.

READS   tools/page.template.html, tools/content.py, data/merchants.json, data/photos.json
WRITES  index.html, es/index.html
RUN     python tools/build_pages.py
"""
import json
import sys as _s, pathlib as _p; _s.path.insert(0,str(_p.Path(__file__).resolve().parent))
import re
import sys
from collections import Counter
from html import escape
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import content as C  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ""  # the old baseline page template was removed on 2026-10-21 (the site is design AD now)
DATA = json.loads((ROOT / "data" / "merchants.json").read_text(encoding="utf-8"))
PLACES = DATA["places"]
PHOTOS = json.loads((ROOT / "data" / "photos.json").read_text(encoding="utf-8"))
PRESS_PHOTOS = json.loads((ROOT / "data" / "press-photos.json").read_text(encoding="utf-8"))

# The five Bitcoin boat / tuk tuk listings the brief asks for (names as cleaned in data/merchants.json).
RIDES = [
    ("Bitcoin Boat", "boat"),
    ("Pier 2 Pier Bitcoin Boat Taxi", "boat"),
    ("Niul - Tuk Tuk", "tuk"),
    ("Victor Tuk Tuk", "tuk"),
    ("AugustoMac Tuk Tuk", "tuk"),
]


def icon(name, cls="ico"):
    return f'<svg class="{cls}" aria-hidden="true" focusable="false"><use href="{{{{p}}}}icons.svg#i-{name}"/></svg>'


def picture(slug, T, sizes, eager=False, cls=""):
    alt = escape(C.PHOTOS[T["lang"]][slug][1], quote=True)
    ph = PHOTOS[slug]
    w, h = ph["width"], ph["height"]
    load = 'loading="eager" fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    return (
        f'<picture>'
        f'<source type="image/webp" srcset="{{{{p}}}}images/{slug}-800.webp 800w, {{{{p}}}}images/{slug}-1600.webp 1600w" sizes="{sizes}">'
        f'<img class="{cls}" src="{{{{p}}}}images/{slug}-800.jpg" srcset="{{{{p}}}}images/{slug}-800.jpg 800w, {{{{p}}}}images/{slug}-1600.jpg 1600w" '
        f'sizes="{sizes}" width="{w}" height="{h}" alt="{alt}" {load}>'
        f'</picture>'
    )


def credit(slug, T):
    ph = PHOTOS[slug]
    return (
        f'<span class="credit">{T["photo_credit"]}: '
        f'<a href="{ph["page"]}" rel="noopener">{escape(ph["artist"])}</a>, '
        f'<a href="{ph["license_url"]}" rel="noopener">{ph["license"]}</a>, {T["photo_via"]}</span>'
    )


def figure(slug, T, sizes, eager=False, cls="", fig_cls=""):
    cap = escape(C.PHOTOS[T["lang"]][slug][0])
    return (
        f'<figure class="photo {fig_cls}">{picture(slug, T, sizes, eager, cls)}'
        f'<figcaption>{cap}. {credit(slug, T)}</figcaption></figure>'
    )


COMMUNITY_PHOTO_WIDTHS = {"community-tuktuk": (800, 940), "community-boat": (800, 1058)}
COMMUNITY_PHOTO_DIMENSIONS = {"community-tuktuk": (940, 627), "community-boat": (1058, 543)}


def community_photo(slug, T, sizes, fig_cls, eager=False):
    """Responsive picture and provisional credit for Tomek-supplied, private-source photos."""
    widths = COMMUNITY_PHOTO_WIDTHS[slug]
    width, height = COMMUNITY_PHOTO_DIMENSIONS[slug]
    srcset_webp = ", ".join(f"{{{{p}}}}images/{slug}-{w}.webp {w}w" for w in widths)
    srcset_jpg = ", ".join(f"{{{{p}}}}images/{slug}-{w}.jpg {w}w" for w in widths)
    alt = escape(C.PHOTOS[T["lang"]][slug][1], quote=True)
    caption = escape(C.PHOTOS[T["lang"]][slug][0])
    load = 'loading="eager" fetchpriority="high" decoding="async"' if eager else 'loading="lazy" decoding="async"'
    return (
        f'<figure class="photo community-photo {fig_cls}"><picture>'
        f'<source type="image/webp" srcset="{srcset_webp}" sizes="{sizes}">'
        f'<img src="{{{{p}}}}images/{slug}-{widths[0]}.jpg" srcset="{srcset_jpg}" sizes="{sizes}" '
        f'width="{width}" height="{height}" alt="{alt}" {load}>'
        f'</picture><figcaption>{caption}. <span class="credit">Photo: community archive (source to confirm)</span></figcaption></figure>'
    )


def community_transport_photos(T):
    return (
        '<div class="community-transport-photos">'
        + community_photo("community-tuktuk", T, "(min-width: 900px) 38vw, 92vw", "community-tuktuk")
        + community_photo("community-boat", T, "(min-width: 900px) 25vw, 92vw", "community-boat")
        + '</div>'
    )


def ab23_video(T):
    """Privacy-first, click-to-play facade for the AB23 community-history talk."""
    video_id = "79cIKf_T3N0"
    title = escape(T["video_title"], quote=True)
    button_label = escape(T["video_play_label"], quote=True)
    thumbnail_alt = escape(T["video_thumbnail_alt"], quote=True)
    return (
        f'<article class="history-video" aria-labelledby="ab23-title">'
        f'<div class="video-details"><h3 id="ab23-title" lang="en">{title}</h3>'
        f'<p>{escape(T["video_summary"])}</p>'
        f'<p class="video-channel"><span>{escape(T["video_channel_label"])}:</span> <strong>Adopting Bitcoin</strong></p>'
        f'<p class="video-privacy">{escape(T["video_privacy"])}</p>'
        f'<p><a class="video-watch" href="https://www.youtube.com/watch?v={video_id}" rel="noopener">{escape(T["video_watch"])}</a></p>'
        f'<noscript><p><a href="https://www.youtube.com/watch?v={video_id}" rel="noopener">{escape(T["video_watch"])}</a></p></noscript>'
        f'</div><figure class="video-poster"><div class="video-facade" data-youtube-facade="{video_id}">'
        f'<button class="video-play" type="button" data-youtube-play="{video_id}" data-youtube-title="{title}" aria-label="{button_label}">'
        f'<img src="{{{{p}}}}images/ab23-talk-poster.webp" alt="{thumbnail_alt}" width="480" height="360" loading="lazy" decoding="async">'
        f'<span class="video-play-mark" aria-hidden="true">▶</span></button></div>'
        f'<figcaption><a href="https://www.youtube.com/watch?v={video_id}" rel="noopener">{escape(T["video_channel_label"])}: Adopting Bitcoin</a></figcaption></figure></article>'
    )


def towns_html():
    counts = Counter(p["town"] for p in PLACES).most_common()
    return "".join(f'<li><span>{escape(t)}</span><b>{n}</b></li>' for t, n in counts)


def ride_html(T):
    by_name = {p["name"]: p for p in PLACES}
    out = []
    for name, kind in RIDES:
        p = by_name[name]
        kind_label = T["transport_boat"] if kind == "boat" else T["transport_tuk"]
        survey = T["survey"].format(d=p["survey"]) if p["survey"] else T["survey_none"]
        bits = []
        if p["phone"]:
            tel = re.sub(r"[^\d+]", "", p["phone"])
            bits.append(f'<span>{T["phone"]}: <a href="tel:{tel}">{escape(p["phone"])}</a></span>')
        if p["operator"]:
            bits.append(f'<span>{T["operator"]}: {escape(p["operator"])}</span>')
        bits.append(f'<span>{survey}</span>')
        out.append(
            f'<li class="ride reveal">{icon("boat" if kind == "boat" else "taxi", "ico ride-ico")}'
            f'<div class="ride-body"><h3>{escape(p["name"])}</h3><p class="kind">{kind_label}</p>'
            f'<p class="meta">{" ".join(bits)}</p></div>'
            f'<button class="btn btn-quiet show-btn" type="button" data-place-id="{p["id"]}">{icon("map-pin")}{T["show_on_map"]}</button></li>'
        )
    return "".join(out)


def press_groups():
    """Match every curated press photo to its quoted article; fail closed on omissions."""
    groups = []
    used = set()
    for outlet, month, title, url, quote in C.PRESS:
        if len(re.findall(r"[.!?](?=\s|$)", quote)) != 1:
            raise ValueError(f"Press quote must be exactly one sentence: {outlet} / {title}")
        photos = [photo for photo in PRESS_PHOTOS if photo["url"].rstrip("/").casefold() == url.rstrip("/").casefold()]
        if not photos:
            title_key = re.sub(r"[^a-z0-9]+", "", title.casefold())
            photos = [
                photo for photo in PRESS_PHOTOS
                if photo["publisher"].casefold() == outlet.casefold()
                and (lambda key: key in title_key or title_key in key)(re.sub(r"[^a-z0-9]+", "", photo["article"].casefold()))
            ]
        if not photos:
            raise ValueError(f"No press photos match article: {outlet} / {title}")
        slugs = {photo["slug"] for photo in photos}
        if used.intersection(slugs):
            raise ValueError(f"Press photos assigned to more than one article: {sorted(used.intersection(slugs))}")
        used.update(slugs)
        groups.append((outlet, month, title, url, quote, photos))
    expected = {photo["slug"] for photo in PRESS_PHOTOS}
    if used != expected or len(expected) != 30:
        raise ValueError(f"Press archive must map all 30 photos exactly once; mapped {len(used)} of {len(expected)}")
    return groups


def press_photo_figure(photo, lang, sizes):
    slug = escape(photo["slug"], quote=True)
    article_url = escape(photo["url"], quote=True)
    publisher = escape(photo["publisher"])
    article = escape(photo["article"])
    width = int(photo["width_1600"])
    height = int(photo["height_1600"])
    alt = (
        f"Photograph accompanying the article {photo['article']} by {photo['publisher']}"
        if lang == "en" else
        f"Fotografía del artículo {photo['article']} de {photo['publisher']}"
    )
    return (
        f'<figure class="press-photo" data-press-slug="{slug}" data-press-url="{article_url}">'
        f'<picture><source type="image/webp" srcset="{{{{p}}}}images/press/{slug}-800.webp 800w" sizes="{sizes}">'
        f'<img src="{{{{p}}}}images/press/{slug}-800.jpg" srcset="{{{{p}}}}images/press/{slug}-800.jpg 800w" '
        f'sizes="{sizes}" width="{width}" height="{height}" alt="{escape(alt, quote=True)}" loading="lazy" decoding="async"></picture>'
        f'<figcaption><a class="credit press-photo-credit" href="{article_url}" rel="noopener">Photo: {publisher}, via {article}</a></figcaption>'
        f'</figure>'
    )


def press_html(T):
    out = []
    for outlet, month, title, url, quote, photos in press_groups():
        out.append(
            f'<li class="press-item"><article class="press-entry"><div class="press-copy">'
            f'<span class="outlet">{escape(outlet)}, {C.MONTHS[T["lang"]][month]}</span>'
            f'<h4 class="ptitle" lang="en">{escape(title)}</h4>'
            f'<p class="pquote">{escape(quote)}</p>'
            f'<a class="read" href="{escape(url, quote=True)}" rel="noopener">{escape(T["press_read"])}{icon("arrow-up-right")}</a>'
            f'</div><div class="press-photos">'
            f'{"".join(press_photo_figure(photo, T["lang"], "(min-width: 1100px) 18vw, (min-width: 700px) 30vw, 44vw") for photo in photos)}'
            f'</div></article></li>'
        )
    return "".join(out)


def press_highlights_html(T):
    figures = "".join(
        press_photo_figure(photos[0], T["lang"], "(min-width: 1100px) 18vw, (min-width: 700px) 28vw, 72vw")
        for _outlet, _month, _title, _url, _quote, photos in press_groups()
    )
    return f'<div class="press-highlights reveal"><h3>{escape(T["press_highlights_h"])}</h3><div class="press-highlights-grid">{figures}</div></div>'


def render(lang):
    T = dict(C.LANGS[lang])
    prefix = "" if lang == "en" else "../"
    ln = sum(1 for p in PLACES if p["lightning"] == "yes")
    chain = sum(1 for p in PLACES if p["onchain"] == "yes")
    T.update(
        p=prefix,
        p_en="./" if lang == "en" else "../",
        p_es="es/" if lang == "en" else "./",
        cur_en='aria-current="true"' if lang == "en" else "",
        cur_es='aria-current="true"' if lang == "es" else "",
        canonical=C.SITE_URL + ("" if lang == "en" else "es/"),
        url_en=C.SITE_URL,
        url_es=C.SITE_URL + "es/",
        og_image=C.SITE_URL + "images/hero-1600.jpg",
        x_lakebitcoin=C.X_LAKEBITCOIN,
        n_places=str(len(PLACES)),
        n_ln=str(ln),
        n_chain=str(chain),
        # Top bar active states: baseline is current on root pages
        topbar_baseline="topbar-current",
        topbar_a="",
        topbar_c="",
        topbar_d="",
        topbar_ac="",
        topbar_ad="",
        topbar_cd="",
        topbar_f="",
        topbar_g="",
        topbar_h="",
    )
    T["foot_updated"] = T["foot_updated"].format(d=C.LAST_UPDATED)
    blocks = {
        "fig_hero": figure("hero", T, "(min-width: 900px) 46vw, 92vw", eager=True, fig_cls="hero-photo"),
        "fig_panorama": figure("panorama", T, "100vw", fig_cls="pano"),
        "fig_lake_view": figure("lake-view", T, "(min-width: 900px) 34vw, 92vw", fig_cls="m1"),
        "fig_sunrise": figure("sunrise", T, "(min-width: 900px) 20vw, 46vw", fig_cls="m2"),
        "fig_street": figure("street", T, "(min-width: 900px) 20vw, 46vw", fig_cls="m3"),
        "fig_history": figure("history-1975", T, "(min-width: 900px) 34vw, 92vw", fig_cls="m4"),
        "fig_tours": figure("tours", T, "(min-width: 900px) 44vw, 92vw", fig_cls="tours-photo"),
        "towns": towns_html(),
        "rides": ride_html(T),
        "community_transport_photos": community_transport_photos(T),
        "ab23_video": ab23_video(T),
        "press": press_html(T),
        "press_highlights": press_highlights_html(T),
        "i18n_json": json.dumps(
            {**{k: T[k] for k in C.I18N_KEYS}, "categories": C.CATEGORIES[lang]}, ensure_ascii=False
        ).replace("</", "<\\/"),
    }
    html = TEMPLATE
    html = re.sub(r"\{\{@(\w+)\}\}", lambda m: blocks[m.group(1)], html)
    html = re.sub(r"\{\{icon:([\w-]+)\}\}", lambda m: icon(m.group(1)), html)

    def variant_sub(m):
        name = m.group(1)
        if name not in C.VARIANTS:
            raise KeyError(f"[{lang}] missing variant: {name}")
        return escape(C.VARIANTS[name][lang][0], quote=True)

    html = re.sub(r"\{\{VARIANTS\.(\w+)\.\[lang\]\.0\}\}", variant_sub, html)

    def sub(m):
        k = m.group(1)
        if k not in T:
            raise KeyError(f"[{lang}] missing key: {k}")
        v = T[k]
        # description/title go into attributes: keep them safe
        return escape(v, quote=True) if k in ("title", "description") else str(v)

    html = re.sub(r"\{\{(\w+)\}\}", sub, html)
    return html


def main():
    # The two languages must define the same keys.
    assert set(C.EN) == set(C.ES), set(C.EN) ^ set(C.ES)
    for lang, path in (("en", ROOT / "index.html"), ("es", ROOT / "es" / "index.html")):
        path.parent.mkdir(exist_ok=True)
        path.write_text(render(lang), encoding="utf-8")
        print("wrote", path)


if __name__ == "__main__":
    # Since 2026-10-21 the site root is design AD, built by tools/build_variants.py.
    # This file now only provides the shared helpers (photos, icons, merchant data) for that build.
    sys.exit("The root pages are built by: python tools/build_variants.py")
