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
from topbar_prune import prune
import re
import sys
from collections import Counter
from html import escape
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import content as C  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = (ROOT / "tools" / "page.template.html").read_text(encoding="utf-8")
DATA = json.loads((ROOT / "data" / "merchants.json").read_text(encoding="utf-8"))
PLACES = DATA["places"]
PHOTOS = json.loads((ROOT / "data" / "photos.json").read_text(encoding="utf-8"))

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


def press_html(T):
    out = []
    for item in C.PRESS:
        outlet, month, title, url, quote = item
        out.append(
            f'<li><a href="{url}" rel="noopener"><span class="outlet">{outlet}, {C.MONTHS[T["lang"]][month]}</span>'
            f'<span class="ptitle" lang="en">{escape(title)}</span>'
            f'<span class="pquote">{escape(quote)}</span>'
            f'<span class="read">{T["press_read"]}{icon("arrow-up-right")}</span></a></li>'
        )
    return "".join(out)


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
        "press": press_html(T),
        "i18n_json": json.dumps(
            {**{k: T[k] for k in C.I18N_KEYS}, "categories": C.CATEGORIES[lang]}, ensure_ascii=False
        ).replace("</", "<\/"),
    }
    html = TEMPLATE
    html = re.sub(r"\{\{@(\w+)\}\}", lambda m: blocks[m.group(1)], html)
    html = re.sub(r"\{\{icon:([\w-]+)\}\}", lambda m: icon(m.group(1)), html)

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
        path.write_text(prune(render(lang)), encoding="utf-8")
        print("wrote", path)


if __name__ == "__main__":
    main()
