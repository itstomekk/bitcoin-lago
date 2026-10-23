#!/usr/bin/env python3
"""Build the finished design variants (each in English and Spanish) and the /variants/ index.

WHAT IT DOES
  One content source (tools/content.py) and one data set (data/merchants.json, data/photos.json)
  feed every finished design variant. Layouts live in tools/variants/*.html, visual treatments in
  v/*.css, shared behaviour in v/app.js, and shared component styles in v/base.css.

READS   tools/variants/*.html, tools/content.py, data/merchants.json, data/photos.json
WRITES  v/ac/index.html, v/ad/index.html, v/cd/index.html, v/f/index.html, v/g/index.html, v/h/index.html, v/a/es/index.html, v/c/es/index.html, v/d/es/index.html,
        variants/index.html, variants/es/index.html
RUN     python tools/build_variants.py
        (the root index.html and es/index.html are NOT touched; build those with tools/build_pages.py)

PAGE TEMPLATE SYNTAX (same idea as tools/page.template.html)
  {{key}}                    a string from tools/content.py
  {{@block}}                 a generated block (see blocks() below)
  {{icon:name}}              an icon from icons.svg
  {{fig:slug|sizes|cls|eager}}  a Commons photo with caption and credit (sizes, cls and the loading flag are optional;
                             flag: eager = load first with high priority, load = load straight away)
  {{maya:N|cls}}             the number N (1 to 19) written in dot-and-bar notation, as decoration
"""
import json
from PIL import Image
import sys as _s, pathlib as _p; _s.path.insert(0,str(_p.Path(__file__).resolve().parent))
import re
import sys
from html import escape
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import content as C  # noqa: E402
import build_pages as BP  # noqa: E402
import seo as SEO  # noqa: E402

ROOT = BP.ROOT
VDIR = ROOT / "tools" / "variants"
IDS = ["ad"]  # the one design (Tomek picked AD on 2026-10-21; A, C, D, AC, CD, F, G, H and the baseline were removed)
LAYOUT_FALLBACKS = {}
SECTIONS = ["lake", "bitcoin", "transport", "community", "tours", "expats", "about"]

# Per-variant head settings: browser theme colour and the fonts to preload (files in /fonts).
META = {
    "ad": {"theme": "#1E2760", "fonts": ["bricolage-grotesque-latin-wght-normal.woff2", "geist-latin-wght-normal.woff2", "geist-mono-latin-wght-normal.woff2"]},
}


def maya(n, cls="maya"):
    """Dot-and-bar numeral (1 to 19). Plain arithmetic notation used as section numbering; decoration only."""
    bars, dots = n // 5, n % 5
    parts = []
    y = 0
    if dots:
        gap = 10
        x0 = 18 - (dots - 1) * gap / 2
        parts += [f'<circle cx="{x0 + i * gap:.1f}" cy="4" r="3.1"/>' for i in range(dots)]
        y = 11
    for _ in range(bars):
        parts.append(f'<rect x="3" y="{y}" width="30" height="5.2" rx="2.6"/>')
        y += 8
    h = max(y - 2.8, 8)
    return f'<svg class="{cls}" viewBox="0 0 36 {h:.0f}" aria-hidden="true" focusable="false" fill="currentColor">{"".join(parts)}</svg>'


def fig(slug, T, sizes="100vw", cls="", eager=False):
    cap = escape(C.PHOTOS[T["lang"]][slug][0])
    pic = BP.picture(slug, T, sizes, eager == "eager")
    if eager == "load":  # eager loading without high priority: for photos inside sideways scrolling strips
        pic = pic.replace('loading="lazy"', 'loading="eager"')
    return (f'<figure class="photo {cls}">{pic}'
            f'<figcaption>{cap}. {BP.credit(slug, T)}</figcaption></figure>')


def towns_bars():
    from collections import Counter
    counts = Counter(p["town"] for p in BP.PLACES).most_common()
    top = counts[0][1]
    return "".join(f'<li style="--w:{n / top:.3f}"><span>{escape(t)}</span><i aria-hidden="true"></i><b>{n}</b></li>' for t, n in counts)


def finder(T, console=False):
    """The merchant map + list. Ids and classes are what v/app.js and the QA runner rely on.
    console=True (design E) puts search, chips and the list in a side panel next to the map instead of above it."""
    filters = f"""<div class="filters">
    <div class="field grow"><label for="q">{T["search_label"]}</label><div class="input-ico">{BP.icon("magnifying-glass")}<input id="q" type="search" placeholder="{T["search_ph"]}" autocomplete="off"></div></div>
    <div class="field"><label for="town">{T["town_label"]}</label><select id="town"><option value="">{T["town_all"]}</option></select></div>
    <button class="btn btn-quiet" id="reset" type="button">{T["reset"]}</button>
  </div>
  <div class="chips" id="chips" role="group" aria-label="{T["chips_label"]}"></div>
  <p class="count" id="count" role="status" aria-live="polite"></p>"""
    mapbox = f'<div class="map-col"><div id="map" role="region" aria-label="{T["map_label"]}" data-loading="{T["map_loading"]}" data-error="{T["map_error"]}"></div></div>'
    cards = f'<ul class="cards" id="cards" aria-label="{T["list_label"]}"></ul>'
    tail = f"""<noscript><p class="note">{T["noscript"]} <a href="https://btcmap.org/community/lago-bitcoin/merchants">BTC Map</a></p></noscript>
  <p class="note check-note">{T["check_note"]}</p>
  <p><a class="link-arrow" href="https://btcmap.org/community/lago-bitcoin/merchants" rel="noopener">{T["btc_open_btcmap"]}{BP.icon("arrow-up-right")}</a></p>"""
    if console:
        return f'<div class="finder console" id="finder"><div class="console-grid"><div class="side">{filters}{cards}</div>{mapbox}</div>{tail}</div>'
    return f'<div class="finder" id="finder">{filters}<div class="split">{mapbox}{cards}</div>{tail}</div>'


def community(T):
    """The five community tiles (same content in every design; layout is up to each stylesheet)."""
    return f'''<article class="tile tile-wa reveal">{BP.icon("whatsapp-logo")}<h3>{T["wa_h"]}</h3><p>{T["wa_p"]}</p>
  <a class="btn btn-primary" href="#community" data-config-link="whatsapp" data-placeholder="whatsapp-invite-url">{T["cta_whatsapp"]}</a></article>
<article class="tile tile-meet reveal">{BP.icon("calendar-blank")}<h3>{T["meet_h"]}</h3><p>{T["meet_p"]}</p>
  <ul class="plain"><li>{T["meet_when"]}</li><li>{T["meet_where"]}</li></ul><p><a class="link-arrow" href="{C.X_ELI}" rel="noopener">@JUN_AJPU_btc{BP.icon("arrow-up-right")}</a></p></article>
<article class="tile tile-school reveal">{BP.icon("graduation-cap")}<h3>{T["school_h"]}</h3><p>{T["school_p"]}</p>
  <p class="muted">{T["school_list"]}</p></article>
<article class="tile tile-follow reveal">{BP.icon("envelope-simple")}<h3>{T["follow_h"]}</h3>
  <ul class="plain"><li><a class="link-arrow" href="#community" data-config-link="facebook" data-placeholder="facebook">{BP.icon("facebook-logo")}{T["facebook"]}</a></li>
  <li><a class="link-arrow" href="#community" data-config-link="email" data-placeholder="contact-email">{BP.icon("envelope-simple")}{T["email"]}</a></li></ul></article>
<article class="tile tile-who reveal">{BP.icon("users-three")}<h3>{T["who_h"]}</h3><p>{T["who_p"]}</p>
  <p class="muted" data-placeholder="eliazar-bio-photo">{T["who_bio"]}</p></article>'''


def tour_points(T):
    return "".join(
        f'<li class="reveal">{BP.icon(ic)}<div><h3>{T[f"tours_{i}_h"]}</h3><p>{T[f"tours_{i}_p"]}</p></div></li>'
        for i, ic in ((1, "handshake"), (2, "compass"), (3, "currency-btc")))



def lb_fig(slug, T, sizes="(min-width: 900px) 30vw, 92vw", cls=""):
    """A Bitcoin Lago photo (Eliazar's archive or a public X post) with its credit."""
    from PIL import Image
    meta = C.LB_PHOTOS[slug]
    files = sorted(ROOT.glob(f"images/lb-{slug}-*.jpg"), key=lambda f: int(f.stem.rsplit("-", 1)[1]))
    widths = [int(f.stem.rsplit("-", 1)[1]) for f in files]
    with Image.open(files[0]) as im:
        w, h = im.size
    webp = ", ".join(f"{{{{p}}}}images/lb-{slug}-{x}.webp {x}w" for x in widths)
    jpg = ", ".join(f"{{{{p}}}}images/lb-{slug}-{x}.jpg {x}w" for x in widths)
    cap = escape(C.LB_CAPTIONS[T["lang"]][slug])
    credit_txt = escape(T["lb_credit_" + meta["by"]])
    credit = (f'<a class="credit" href="{meta["url"]}" rel="noopener">{credit_txt}</a>' if meta.get("url")
              else f'<span class="credit">{credit_txt}</span>')
    return (f'<figure class="photo lb-photo {cls}"><picture><source type="image/webp" srcset="{webp}" sizes="{sizes}">'
            f'<img src="{{{{p}}}}images/lb-{slug}-{widths[0]}.jpg" srcset="{jpg}" sizes="{sizes}" width="{w}" height="{h}" '
            f'alt="{escape(C.LB_CAPTIONS[T["lang"]][slug], quote=True)}" loading="lazy" decoding="async"></picture>'
            f'<figcaption>{cap}. {credit}</figcaption></figure>')


def gallery(T):
    return (f'<div class="lb-gallery reveal"><h3>{T["gallery_h"]}</h3><div class="lb-grid">'
            + "".join(lb_fig(s, T, "(min-width: 1100px) 24vw, (min-width: 700px) 45vw, 92vw") for s in C.GALLERY)
            + "</div></div>")


def timeline(T):
    i = 2 if T["lang"] == "en" else 3
    items = []
    for row in C.TIMELINE:
        year, srcs, text = row[0], row[1], row[i]
        links = " ".join(f'<a href="{u}" rel="noopener">{n + 1}</a>' for n, u in enumerate(srcs))
        src = f' <span class="tl-src">{T["story_source"]}: {links}</span>' if links else ""
        items.append(f'<li><span class="tl-year">{year}</span><p>{escape(text)}{src}</p></li>')
    return f'<div class="timeline reveal"><h3>{T["story_timeline_h"]}</h3><ol>{"".join(items)}</ol></div>'


def story_cta(T):
    S = C.STORY[T["lang"]]
    return (f'<div class="story-cta reveal"><a class="btn btn-primary" href="story/">{S["st_cta"]}</a><p>{S["st_cta_p"]}</p></div>'
            f'<div class="story-cta reveal"><a class="btn btn-primary" href="blog/">{S["bl_cta"]}</a><p>{S["bl_cta_p"]}</p></div>'
            + (f'<div class="story-cta reveal"><a class="btn btn-primary" href="faq/">{FAQ_T[T["lang"]]["cta"]}</a><p>{FAQ_T[T["lang"]]["cta_p"]}</p></div>' if FAQ_FILE.exists() else ""))


def partners(T):
    i = 3 if T["lang"] == "en" else 4
    cards = []
    for slug, name, url, *desc in C.PARTNERS:
        im = Image.open(ROOT / "images" / "partners" / f"{slug}.png")
        cards.append(
            f'<li class="partner"><a href="{url}" rel="noopener"><span class="partner-logo">'
            f'<picture><source srcset="{T["p"]}images/partners/{slug}.webp" type="image/webp">'
            f'<img src="{T["p"]}images/partners/{slug}.png" alt="{escape(name)}" width="{im.width}" height="{im.height}" loading="lazy"></picture></span>'
            f'<span class="partner-name">{escape(name)}</span></a><p>{escape(desc[i - 3])}</p></li>')
    return ('<section class="scr partners" id="partners" aria-labelledby="partners-h2"><div class="partners-in reveal">'
            f'<h2 id="partners-h2">{T["partners_h"]}</h2><p class="lead">{T["partners_p"]}</p>'
            f'<ul class="partner-grid">{"".join(cards)}</ul></div></section>')


def services(T):
    en = T["lang"] == "en"
    cards, opts = [], []
    for key, ic, h_en, h_es, rows in C.SERVICES:
        h = h_en if en else h_es
        lis = "".join(f"<li>{escape(a if en else b)}</li>" for a, b in rows)
        cards.append(f'<article class="svc svc-{key} reveal">{BP.icon(ic)}<h3>{escape(h)}</h3><ul>{lis}</ul></article>')
        opts.append(f'<option value="{escape(h, quote=True)}">{escape(h)}</option>')
    opts.append(f'<option value="{escape(T["form_need_other"], quote=True)}">{escape(T["form_need_other"])}</option>')
    form = f"""<form class="ask reveal" id="ask" novalidate data-hello="{escape(T["form_hello"], quote=True)}">
  <h3>{T["form_h"]}</h3><p class="muted">{T["form_p"]}</p>
  <div class="field"><label for="ask-need">{T["form_need"]}</label><select id="ask-need" name="need">{"".join(opts)}</select></div>
  <div class="row2"><div class="field"><label for="ask-dates">{T["form_dates"]}</label><input id="ask-dates" name="dates" type="text" placeholder="{escape(T["form_dates_ph"], quote=True)}" autocomplete="off"></div>
  <div class="field"><label for="ask-people">{T["form_people"]}</label><input id="ask-people" name="people" type="number" min="1" max="200" inputmode="numeric"></div></div>
  <div class="field"><label for="ask-name">{T["form_name"]}</label><input id="ask-name" name="name" type="text" autocomplete="name"></div>
  <div class="field"><label for="ask-msg">{T["form_msg"]}</label><textarea id="ask-msg" name="msg" rows="3"></textarea></div>
  <div class="send-row"><button class="btn btn-primary" type="submit">{BP.icon("whatsapp-logo")}{T["form_send"]}</button><span class="send-ph" data-placeholder="whatsapp-number"></span></div>
  <p class="muted small">{T["form_note"]}</p>
</form>"""
    return f'<div class="svc-grid">{"".join(cards)}</div>{form}'

def stats(T, ln, chain):
    return (f'<dl class="stats"><div><dt>{T["btc_stat_active"]}</dt><dd>~50</dd></div>'
            f'<div><dt>{T["btc_stat_places"]}</dt><dd data-count="{len(BP.PLACES)}">{len(BP.PLACES)}</dd></div>'
            f'<div><dt>{T["btc_stat_ln"]}</dt><dd data-count="{ln}">{ln}</dd></div>'
            f'<div><dt>{T["btc_stat_chain"]}</dt><dd data-count="{chain}">{chain}</dd></div></dl>'
            f'<p class="datanote">{T["btc_active_note"]} <a href="blog/merchants-over-time/">{T["btc_count_link"]}</a></p>')


def atm(T):
    return (f'<aside class="atm reveal" id="atm" aria-labelledby="atm-h3"><span class="atm-ico">{BP.icon("bank")}</span>'
            f'<h3 id="atm-h3">{T["atm_h3"]}</h3><p>{T["atm_p"]}</p><p class="muted" data-placeholder="atm-locations">{T["atm_loc"]}</p></aside>')


def footer_text(T):
    return (f'<p class="legal">{T["foot_legal"]}</p><p>{T["foot_data_html"]}</p><p>{T["foot_photos"]}</p>'
            f'<p class="muted">{T["foot_updated"]}</p>')


def head_html(vid):
    m = META[vid]
    pre = "".join(f'<link rel="preload" href="{{{{p}}}}fonts/{f}" as="font" type="font/woff2" crossorigin>\n' for f in m["fonts"])
    tokens_path = ROOT / "v" / f"{vid}.tokens.css"
    tokens = f'<link rel="stylesheet" href="{{{{p}}}}v/{vid}.tokens.css">\n' if tokens_path.is_file() else ""
    theme = m["theme"]
    # f-string with all template/JS braces doubled; only vid, theme, pre are Python expressions
    return (
        f'<!doctype html>\n'
        f'<!--\n'
        f'  GENERATED FILE. Do not edit by hand. Edit tools/variants/{vid}.html (layout), v/{vid}.css (look)\n'
        f'  or tools/content.py (words), then run python tools/build_variants.py. See HANDOFF.md.\n'
        f'-->\n'
        f'<html lang="{{{{lang}}}}" data-design="{vid}">\n'
        f'<head>\n'
        f'<meta charset="utf-8">\n'
        f'<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f'<title>{{{{title}}}}</title>\n'
        f'<meta name="description" content="{{{{description}}}}">\n'
        f'<meta name="robots" content="noindex,nofollow">\n'
        f'<meta name="theme-color" content="{theme}">\n'
        f'<link rel="icon" href="{{{{p}}}}favicon.svg" type="image/svg+xml">\n'
        f'<link rel="canonical" href="{{{{canonical}}}}">\n'
        f'<link rel="alternate" hreflang="en" href="{{{{url_en}}}}">\n'
        f'<link rel="alternate" hreflang="es" href="{{{{url_es}}}}">\n'
        f'<link rel="alternate" hreflang="x-default" href="{{{{url_en}}}}">\n'
        f'<meta property="og:type" content="{{{{og_type}}}}">\n'
        f'<meta property="og:site_name" content="Bitcoin Lago">\n'
        f'<meta property="og:title" content="{{{{title}}}}">\n'
        f'<meta property="og:description" content="{{{{description}}}}">\n'
        f'<meta property="og:url" content="{{{{canonical}}}}">\n'
        f'<meta property="og:locale" content="{{{{og_locale}}}}">\n'
        f'<meta property="og:image" content="{{{{og_image}}}}">\n'
        f'<meta name="twitter:card" content="summary_large_image">\n'
        f'{{{{@seo}}}}\n'
        f'{pre}<link rel="stylesheet" href="{{{{p}}}}v/base.css">\n'
        f'{tokens}'
        f'<link rel="stylesheet" href="{{{{p}}}}v/{vid}.css">\n'
        f'<link rel="stylesheet" href="{{{{p}}}}vendor/leaflet/leaflet.css">\n'
        f'<script>\n'
        f'/* Language: remember the visitor\'s choice (localStorage "lbc-lang"); with no choice yet, follow the browser language. */\n'
        f'(function () {{\n'
        f'  var d = document.documentElement; d.className += \' js\';\n'
        f'  var here = d.lang, stored = null;\n'
        f'  try {{ stored = localStorage.getItem(\'lbc-lang\'); }} catch (e) {{}}\n'
        f'  var want = stored || (/^es/i.test(navigator.language || \'\') ? \'es\' : \'en\');\n'
        f'  if (want !== here && (want === \'en\' || want === \'es\')) {{ location.replace(\'{{{{alt_lang_href}}}}\' + location.hash); }}\n'
        f'}})();\n'
        f'</script>\n'
        f'</head>\n'
        f'<body class="show-placeholders v-{vid}" data-base="{{{{p}}}}" data-design="{vid}">\n'
        f'<a class="skip" href="#main">{{{{skip}}}}</a>\n'
        f'\n'
    )


FOOT = '''
{{@switcher}}
<div class="toast" id="toast" role="status" aria-live="polite" data-msg="{{toast_soon}}"></div>
<script type="application/json" id="i18n">{{@i18n_json}}</script>
<script src="{{p}}config.js"></script>
<script src="{{p}}vendor/leaflet/leaflet.js"></script>
<script src="{{p}}v/app.js" defer></script>
</body>
</html>
'''


def switcher(vid, lang, T):
    """Floating 'Design A B C D E' switcher. Links keep the current language."""
    out = []
    for x in IDS:
        name = C.VARIANTS[x][lang][0]
        href = f"../{x}/" if lang == "en" else f"../../{x}/es/"
        if x == vid:
            href = "./" if lang == "en" else "./"
        cur = ' aria-current="page"' if x == vid else ""
        out.append(f'<a href="{href}" data-design="{x}" title="{escape(name)}" aria-label="{T["vsw_label"]} {x.upper()}: {escape(name)}"{cur}>{x.upper()}</a>')
    allhref = "../../variants/" if lang == "en" else "../../../variants/es/"
    return (f'<nav class="vsw" aria-label="{T["vsw_aria"]}"><span class="vsw-l">{T["vsw_label"]}</span>'
            f'<span class="vsw-links">{"".join(out)}</span>'
            f'<a class="vsw-all" href="{allhref}" aria-label="{T["vsw_all"]}">{T["vsw_all_short"]}</a></nav>')


def render(vid, lang):
    """The site itself: the one design, at the site root (index.html and es/index.html)."""
    T = dict(C.LANGS[lang])
    T.update(C.STORY[lang])
    prefix = "" if lang == "en" else "../"
    ln = sum(1 for p in BP.PLACES if p["lightning"] == "yes")
    chain = sum(1 for p in BP.PLACES if p["onchain"] == "yes")
    path = "" if lang == "en" else "es/"
    T.update(
        p=prefix,
        vid=vid,
        p_en="./" if lang == "en" else "../",
        p_es="es/" if lang == "en" else "./",
        cur_en='aria-current="true"' if lang == "en" else "",
        cur_es='aria-current="true"' if lang == "es" else "",
        canonical=C.SITE_URL + path,
        url_en=C.SITE_URL,
        url_es=C.SITE_URL + "es/",
        og_image=C.SITE_URL + "images/hero-1600.jpg",
        x_lakebitcoin=C.X_LAKEBITCOIN,
        x_eli=C.X_ELI,
        x_tours=C.X_TOURS,
        n_places=str(len(BP.PLACES)),
        n_ln=str(ln),
        n_chain=str(chain),
        vname=C.VARIANTS[vid][lang][0],
    )
    T["foot_updated"] = T["foot_updated"].format(d=C.LAST_UPDATED)
    blocks = {
        "towns": BP.towns_html(),
        "towns_bars": towns_bars(),
        "rides": BP.ride_html(T),
        "community_transport_photos": BP.community_transport_photos(T),
        "community_tuktuk_hero": BP.community_photo("community-tuktuk", T, "(min-width: 900px) 46vw, 94vw", "hero-visual", eager=True),
        "ab23_video": BP.ab23_video(T),
        "press": BP.press_html(T),
        "press_highlights": BP.press_highlights_html(T),
        "finder": finder(T),
        "finder_console": finder(T, console=True),
        "community": community(T),
        "tour_points": tour_points(T),
        "gallery": gallery(T),
        "timeline": timeline(T),
        "services": services(T),
        "partners": partners(T),
        "tours_list": tours_list(T),
        "story_cta": story_cta(T),
        "stats": stats(T, ln, chain),
        "atm": atm(T),
        "footer_text": footer_text(T),
        "switcher": "",
        "i18n_json": json.dumps({**{k: T[k] for k in C.I18N_KEYS}, "categories": C.CATEGORIES[lang]},
                                ensure_ascii=False).replace("</", "<\\/"),
    }
    layout_id = vid if (VDIR / f"{vid}.html").exists() else LAYOUT_FALLBACKS.get(vid, vid)
    html = head_html(vid) + (VDIR / f"{layout_id}.html").read_text(encoding="utf-8") + FOOT
    return fill(html, T, blocks, lang, f"{vid}/{lang}")


def fill(html, T, blocks, lang, label):
    T = SEO.prepare(T)
    blocks = dict(blocks, seo=SEO.extra_meta(T))
    html = re.sub(r"\{\{@(\w+)\}\}", lambda m: blocks[m.group(1)], html)
    html = re.sub(r"\{\{icon:([\w-]+)\}\}", lambda m: BP.icon(m.group(1)), html)
    html = re.sub(r"\{\{fig:([\w-]+)((?:\|[^|}]*){0,3})\}\}",
                  lambda m: fig(m.group(1), T, *(lambda a: (a[0] or "100vw", a[1] or "", a[2]))(
                      (m.group(2).lstrip("|").split("|") + ["", "", ""])[:3])), html)
    html = re.sub(r"\{\{maya:(\d+)(?:\|([\w -]+))?\}\}", lambda m: maya(int(m.group(1)), m.group(2) or "maya"), html)

    def variant_sub(m):
        name = m.group(1)
        if name not in C.VARIANTS:
            raise KeyError(f"[{label}] missing variant: {name}")
        return escape(C.VARIANTS[name][lang][0], quote=True)

    html = re.sub(r"\{\{VARIANTS\.(\w+)\.\[lang\]\.0\}\}", variant_sub, html)

    def sub(m):
        k = m.group(1)
        if k not in T:
            raise KeyError(f"[{label}] missing key: {k}")
        v = T[k]
        return escape(v, quote=True) if k in ("title", "description", "vx_title", "vx_description") else str(v)

    return re.sub(r"\{\{(\w+)\}\}", sub, html)


def build_index(lang):
    """The /variants/ page: one card per design with a thumbnail (variants/thumbs/*.webp)."""
    T = dict(C.LANGS[lang])
    prefix = "../" if lang == "en" else "../../"
    cards = []
    for x in [i for i in IDS if (VDIR / f"{i}.html").exists() or i in LAYOUT_FALLBACKS]:
        name, desc = C.VARIANTS[x][lang]
        en_href = f"{prefix}v/{x}/"
        es_href = f"{prefix}v/{x}/es/"
        cards.append(f'''<li class="vcard" data-design="{x}">
  <a class="thumb" href="{en_href if lang == "en" else es_href}" tabindex="-1" aria-hidden="true"><img src="{prefix}variants/thumbs/{x}.webp" width="640" height="400" alt="" loading="lazy"></a>
  <div class="vbody"><p class="vletter" aria-hidden="true">{x.upper()}</p><h2>{escape(name)}</h2><p>{escape(desc)}</p>
  <p class="vlast" hidden>{T["vx_last"]}</p>
  <p class="vlinks"><a class="btn btn-primary" href="{en_href if lang == "en" else es_href}">{T["vx_open"]} {x.upper()}</a>
  <a class="alt" lang="en" href="{en_href}">EN</a> <a class="alt" lang="es" href="{es_href}">ES</a></p></div></li>''')
    root_href = prefix if lang == "en" else prefix + "es/"
    cards.append(f'''<li class="vcard vbase"><a class="thumb" href="{root_href}" tabindex="-1" aria-hidden="true"><img src="{prefix}variants/thumbs/root.webp" width="640" height="400" alt="" loading="lazy"></a>
  <div class="vbody"><p class="vletter" aria-hidden="true">0</p><h2>{T["vx_baseline_h"]}</h2><p>{T["vx_baseline_p"]}</p>
  <p class="vlinks"><a class="btn btn-quiet" href="{root_href}">{T["vx_open"]}</a></p></div></li>''')
    # Top bar active states: on variants index, no variant is current (could highlight baseline)
    topbar_states = {
        "topbar_baseline": "topbar-current",
        "topbar_a": "",
        "topbar_c": "",
        "topbar_d": "",
        "topbar_ac": "",
        "topbar_ad": "",
        "topbar_cd": "",
        "topbar_f": "",
        "topbar_g": "",
        "topbar_h": "",
    }
    T.update(
                p=prefix, lang=lang,
                p_en="./" if lang == "en" else "../",
                p_es="es/" if lang == "en" else "./",
                cur_en='aria-current="true"' if lang == "en" else "",
                cur_es='aria-current="true"' if lang == "es" else "",
                title=T["vx_title"], description=T["vx_description"],
                canonical=C.SITE_URL + "variants/" + ("" if lang == "en" else "es/"),
                url_en=C.SITE_URL + "variants/", url_es=C.SITE_URL + "variants/es/",
                alt_lang_href="es/" if lang == "en" else "../",
                other_name=T["vx_lang_other"],
                **topbar_states,
            )
    T["foot_updated"] = T["foot_updated"].format(d=C.LAST_UPDATED)
    blocks = {"cards": "".join(cards)}
    html = (VDIR / "index.html").read_text(encoding="utf-8")
    return fill(html, T, blocks, lang, f"index/{lang}")


# ---------- Story page (/story/, /es/story/) ----------
MONTH_NAMES = {"en": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
               "es": ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"]}


def fmt_date(d, lang):
    parts = d.split("-")
    if len(parts) == 1:
        return parts[0]
    m = MONTH_NAMES[lang][int(parts[1]) - 1]
    if len(parts) == 3:
        return f"{int(parts[2])} {m} {parts[0]}"
    return f"{m} {parts[0]}"


def xurl(tid):
    return f"https://x.com/JUN_AJPU_btc/status/{tid}"


def src_links(T, ids):
    if not ids:
        return ""
    links = " ".join(f'<a href="{xurl(i)}" rel="noopener">{n + 1}</a>' for n, i in enumerate(ids))
    return f' <span class="tl-src">{T["st_src"]}: {links}</span>'


def x_fig(ph, T):
    lang = T["lang"]
    sizes = "(min-width: 1100px) 22vw, (min-width: 700px) 30vw, 46vw"
    webp = ", ".join(f'{T["p"]}images/x/{ph["stem"]}-{w}.webp {w}w' for w in ph["widths"])
    jpg = ", ".join(f'{T["p"]}images/x/{ph["stem"]}-{w}.jpg {w}w' for w in ph["widths"])
    cap = escape(ph[lang])
    return (f'<figure class="photo lb-photo xph"><picture><source type="image/webp" srcset="{webp}" sizes="{sizes}">'
            f'<img src="{T["p"]}images/x/{ph["stem"]}-480.jpg" srcset="{jpg}" sizes="{sizes}" width="{ph["w"]}" height="{ph["h"]}" '
            f'alt="{escape(ph[lang], quote=True)}" loading="lazy" decoding="async"></picture>'
            f'<figcaption>{cap}. <a class="credit" href="{xurl(ph["tweet_id"])}" rel="noopener">{escape(T["st_photo_credit"])}</a></figcaption></figure>')


def story_blocks(T):
    lang = T["lang"]
    D = json.loads((ROOT / "tools" / "story_data.json").read_text(encoding="utf-8"))
    years = {}
    years.setdefault("2021", {"items": [], "photos": []})["items"].append(
        f'<li><time>{"dic 2021" if lang == "es" else "Dec 2021"}</time><p>{escape(T["st_2021"])} '
        f'<span class="tl-src">{T["st_src"]}: <a href="{C.INTERVIEWS[0][3]}" rel="noopener">1</a></span></p></li>')
    for t in D["timeline"]:
        y = t["date"][:4]
        years.setdefault(y, {"items": [], "photos": []})["items"].append(
            f'<li><time>{fmt_date(t["date"], lang)}</time><h4>{escape(t["title_" + lang])}</h4>'
            f'<p>{escape(t[lang])}{src_links(T, t["ids"])}</p></li>')
    for ph in D["photos"]:
        years.setdefault(ph["year"], {"items": [], "photos": []})["photos"].append(x_fig(ph, T))
    out, chips = [], []
    for y in sorted(years):
        chips.append(f'<a href="#y{y}">{y}</a>')
        ph = years[y]["photos"]
        gal = f'<div class="sy-photos">{"".join(ph)}</div>' if ph else ""
        out.append(f'<div class="sy reveal" id="y{y}"><h3 class="sy-year">{y}</h3><ol class="sy-list">{"".join(years[y]["items"])}</ol>{gal}</div>')
    topics = "".join(
        f'<article class="topic reveal"><h3>{escape(f["topic_" + lang])}</h3><p>{escape(f[lang])}{src_links(T, f["ids"])}</p></article>'
        for f in D["facts"])
    media = "".join(
        f'<li><span class="m-kind">{T["st_kinds"][kind]}, {fmt_date(d, lang)}</span>'
        f'<a href="{url}" rel="noopener"><span class="m-outlet">{escape(outlet)}</span> <span class="m-title" lang="{"es" if outlet.startswith(("Cripto", "Bitcoinismo")) else "en"}">{escape(title)}</span></a></li>'
        for outlet, d, title, url, kind in C.INTERVIEWS)
    chips.append(f'<a href="{T["home"]}blog/">{T["bl_h1"]}</a>')
    return {"year_chips": "".join(chips), "years": "".join(out), "topics": topics, "media": media}


def tours_list(T):
    en = T["lang"] == "en"
    items = "".join(
        f'<li><strong>{escape(le if en else ls)}.</strong> {escape(te if en else ts)} '
        f'<a class="tl-src" href="https://x.com/AtitlanTours21/status/{tid}" rel="noopener">{T["st_src"]}</a></li>'
        for le, te, ls, ts, tid in C.TOURS_OFFER)
    return f'<div class="tours-list reveal"><h3>{T["tours_list_h"]}</h3><ul>{items}</ul></div>'


def render_story(lang):
    T = dict(C.LANGS[lang])
    T.update(C.STORY[lang])
    en = lang == "en"
    prefix = "../" if en else "../../"
    T.update(
        p=prefix, vid="ad",
        home=prefix if en else prefix + "es/",
        p_en="./" if en else "../../story/",
        p_es="../es/story/" if en else "./",
        cur_en='aria-current="true"' if en else "",
        cur_es='aria-current="true"' if not en else "",
        canonical=C.SITE_URL + ("story/" if en else "es/story/"),
        url_en=C.SITE_URL + "story/", url_es=C.SITE_URL + "es/story/",
        alt_lang_href="../es/story/" if en else "../../story/",
        og_image=C.SITE_URL + "images/hero-1600.jpg",
        title=T["st_title"], description=T["st_description"],
    )
    T["foot_updated"] = T["foot_updated"].format(d=C.LAST_UPDATED)
    blocks = story_blocks(T)
    blocks.update(partners=partners(T), footer_text=footer_text(T), switcher="",
                  i18n_json=json.dumps({**{k: T[k] for k in C.I18N_KEYS}, "categories": C.CATEGORIES[lang]},
                                       ensure_ascii=False).replace("</", "<\\/"))
    html = head_html("ad") + (VDIR / "story.html").read_text(encoding="utf-8") + FOOT
    return fill(html, T, blocks, lang, f"story/{lang}")


# ---------- Blog: videos and stories (/blog/, /blog/<slug>/) ----------
BLOG_DIR = ROOT / "tools" / "blog"


def blog_articles():
    arts = [json.loads(f.read_text(encoding="utf-8")) for f in sorted(BLOG_DIR.glob("*.json"))]
    return sorted(arts, key=lambda a: a["date_published_video"], reverse=True)


def mmss_to_s(t):
    parts = [int(x) for x in t.split(":")]
    s = 0
    for x in parts:
        s = s * 60 + x
    return s


def page_T(lang, path_en, path_es, title, description):
    T = dict(C.LANGS[lang])
    T.update(C.STORY[lang])
    en = lang == "en"
    depth_en = path_en.count("/")
    prefix = "../" * depth_en if en else "../" * (depth_en + 1)
    T.update(
        p=prefix, vid="ad", home=prefix if en else prefix + "es/",
        p_en="./" if en else "../" * (depth_en + 1) + path_en,
        p_es="../" * depth_en + "es/" + path_en if en else "./",
        cur_en='aria-current="true"' if en else "", cur_es='aria-current="true"' if not en else "",
        canonical=C.SITE_URL + (path_en if en else path_es), url_en=C.SITE_URL + path_en, url_es=C.SITE_URL + path_es,
        alt_lang_href=("../" * depth_en + "es/" + path_en) if en else ("../" * (depth_en + 1) + path_en),
        og_image=C.SITE_URL + "images/hero-1600.jpg", title=title, description=description,
    )
    T["foot_updated"] = T["foot_updated"].format(d=C.LAST_UPDATED)
    return T


def render_page(T, lang, main_html, label):
    blocks = {"main": main_html, "footer_text": footer_text(T), "switcher": "",
              "i18n_json": json.dumps({**{k: T[k] for k in C.I18N_KEYS}, "categories": C.CATEGORIES[lang]},
                                      ensure_ascii=False).replace("</", "<\\/")}
    html = head_html("ad") + (VDIR / "page.html").read_text(encoding="utf-8") + FOOT
    return fill(html, T, blocks, lang, label)


def thumb(T, vid_id, alt, cls="blog-thumb", eager=False):
    return (f'<picture><source type="image/webp" srcset="{T["p"]}images/blog/{vid_id}.webp">'
            f'<img class="{cls}" src="{T["p"]}images/blog/{vid_id}.jpg" alt="{escape(alt, quote=True)}" width="640" height="360" '
            f'loading="{"eager" if eager else "lazy"}" decoding="async"></picture>')


def blog_card(T, a, href):
    lang = T["lang"]
    return (f'<li class="blog-card reveal"><a href="{href}">{thumb(T, a["video_id"], a["title_" + lang])}'
            f'<span class="bc-meta">{escape(a["channel"])}, {fmt_date(a["date_published_video"][:7], lang)}</span>'
            f'<span class="bc-title">{escape(a["title_" + lang])}</span></a><p>{escape(a["dek_" + lang])}</p></li>')


def render_blog_index(lang, arts):
    T = page_T(lang, "blog/", "es/blog/", C.STORY[lang]["bl_title"], C.STORY[lang]["bl_description"])
    cards = "".join(blog_card(T, a, f'{a["slug"]}/') for a in arts)
    TT = TOPIC_T[lang]
    by_id = {a["video_id"]: a for a in arts}
    tcards = "".join(topic_card(T, t, f'{t["slug"]}/', by_id) for t in topic_articles())
    topics = (f'<section class="scr blog-list blog-topics" aria-labelledby="tp-h"><h2 id="tp-h">{TT["tp_h"]}</h2><p class="lede-s">{TT["tp_lead"]}</p>'
              f'<ul class="blog-grid">{tcards}</ul></section>') if tcards else ""
    main = (f'<section class="scr story-hero" id="hero" aria-labelledby="bl-h1"><p><a class="link-arrow" href="{T["home"]}">{T["st_back"]}</a></p>'
            f'<h1 id="bl-h1">{T["bl_h1"]}</h1><p class="lede">{T["bl_lead"]}</p></section>' + topics +
            f'<section class="scr blog-list" aria-labelledby="vd-h"><h2 id="vd-h">{TT["tp_vids_h"]}</h2><ul class="blog-grid">{cards}</ul></section>')
    return render_page(T, lang, main, f"blog/{lang}")


def render_article(lang, a, arts):
    slug = a["slug"]
    T = page_T(lang, f"blog/{slug}/", f"es/blog/{slug}/", f'{a["title_" + lang]} | Bitcoin Lago', a["dek_" + lang])
    T["og_image"] = C.SITE_URL + f'images/blog/{a["video_id"]}.jpg'
    vid, url = a["video_id"], f'https://www.youtube.com/watch?v={a["video_id"]}'
    body = []
    for b in a["body_" + lang]:
        if b.get("h"):
            body.append(f'<h2>{escape(b["h"])}</h2>')
        if b.get("p"):
            body.append(f'<p>{escape(b["p"])}</p>')
    quotes = "".join(
        f'<blockquote class="bq"><p>{escape(q[lang] if lang != "orig" else q["original"])}</p>'
        f'<footer><a href="{url}&amp;t={mmss_to_s(q["t"])}s" rel="noopener">{T["bl_at"]} {q["t"]}</a></footer></blockquote>'
        for q in a.get("quotes", []))
    others = [o for o in arts if o["slug"] != slug][:3]
    more = "".join(blog_card(T, o, f'../{o["slug"]}/') for o in others)
    title = escape(a["title_" + lang], quote=True)
    video = (f'<figure class="blog-video"><div class="video-facade" data-youtube-facade="{vid}">'
             f'<button class="video-play" type="button" data-youtube-play="{vid}" data-youtube-title="{title}" aria-label="{T["bl_play"]}">'
             f'{thumb(T, vid, a["title_" + lang], "blog-thumb", eager=True)}<span class="video-play-mark" aria-hidden="true">▶</span></button></div>'
             f'<figcaption>{T["bl_privacy"]} <a href="{url}" rel="noopener">{T["bl_watch"]}</a></figcaption></figure>')
    main = (f'<article class="post"><header class="scr story-hero post-head"><p><a class="link-arrow" href="../">{T["bl_back"]}</a></p>'
            f'<h1>{escape(a["title_" + lang])}</h1><p class="lede">{escape(a["dek_" + lang])}</p>'
            f'<p class="post-meta">{T["bl_by"]}: <strong>{escape(a["channel"])}</strong>. {T["bl_recorded"]}: {fmt_date(a["date_published_video"], lang)}.</p></header>'
            f'<div class="scr post-body">{video}<div class="post-text">{"".join(body)}'
            + (f'<h2>{T["bl_quotes_h"]}</h2>{quotes}' if quotes else "")
            + f'<p class="post-note">{T["bl_note"]}</p></div></div></article>'
            + (f'<section class="scr blog-list more"><h2>{T["bl_more_h"]}</h2><ul class="blog-grid">{more}</ul></section>' if more else ""))
    return render_page(T, lang, main, f"blog/{slug}/{lang}")


# ---------- Topic articles (several sources) and charts ----------
TOPIC_DIR = ROOT / "tools" / "topics"
TOPIC_T = {
    "en": {"tp_h": "Topics", "tp_lead": "Longer stories that bring several videos, posts and data together.", "tp_vids_h": "Videos",
           "tp_meta": "Written by the Bitcoin Lago site team from the sources linked in each paragraph", "tp_used_h": "Videos used in this story",
           "tp_quotes_h": "In their words", "tp_note": "Numbers and dates come from the linked sources. When sources disagree we say so. If you know better, tell us and we will fix it.",
           "tp_src": "Source", "tp_card": "Story",
           "ch_title": "How many places take bitcoin? Every public count we found, 2022 to 2026",
           "ch_team": "Said by the Bitcoin Lago team", "ch_other": "Said by visitors, press or supporters",
           "ch_line": "Places on BTC Map today, by the date they were first listed",
           "ch_list": "All counts and their sources", "ch_to": "to",
           "ch_note": "Each dot links to its source. A plus means \u201cmore than\u201d. A bar shows a range. Some counts are Panajachel only, others the whole lake; some count businesses ever onboarded, others the ones active now. BTC Map data of 2026-10-22; places removed from the map are not in the line.",
           "ck_title": "When were the 117 places on BTC Map last checked on the ground?", "ck_none": "no date",
           "ck_note": "Year of the newest check date in OpenStreetMap for each place on BTC Map, data of 2026-10-19. Only {n} places were checked in the last 12 months.",
           "ck_places": "places"},
    "es": {"tp_h": "Temas", "tp_lead": "Historias más largas que reúnen varios videos, publicaciones y datos.", "tp_vids_h": "Videos",
           "tp_meta": "Escrito por el equipo del sitio Bitcoin Lago a partir de las fuentes enlazadas en cada párrafo", "tp_used_h": "Videos usados en esta historia",
           "tp_quotes_h": "En sus palabras", "tp_note": "Las cifras y fechas vienen de las fuentes enlazadas. Cuando las fuentes no coinciden, lo decimos. Si sabes algo mejor, avísanos y lo corregimos.",
           "tp_src": "Fuente", "tp_card": "Historia",
           "ch_title": "\u00bfCu\u00e1ntos lugares aceptan bitcoin? Todas las cifras p\u00fablicas que encontramos, 2022 a 2026",
           "ch_team": "Dicho por el equipo de Bitcoin Lago", "ch_other": "Dicho por visitantes, prensa o colaboradores",
           "ch_line": "Lugares en BTC Map hoy, por la fecha en que se registraron",
           "ch_list": "Todas las cifras y sus fuentes", "ch_to": "a",
           "ch_note": "Cada punto enlaza a su fuente. Un signo m\u00e1s significa \u201cm\u00e1s de\u201d. Una barra muestra un rango. Algunas cifras son solo de Panajachel, otras de todo el lago; unas cuentan los negocios que alguna vez se sumaron, otras los activos. Datos de BTC Map del 2026-10-22; los lugares eliminados del mapa no est\u00e1n en la l\u00ednea.",
           "ck_title": "\u00bfCu\u00e1ndo se revisaron en persona por \u00faltima vez los 117 lugares de BTC Map?", "ck_none": "sin fecha",
           "ck_note": "A\u00f1o de la revisi\u00f3n m\u00e1s reciente en OpenStreetMap para cada lugar de BTC Map, datos del 2026-10-19. Solo {n} lugares se revisaron en los \u00faltimos 12 meses.",
           "ck_places": "lugares"},
}
MC = json.loads((TOPIC_DIR / "merchant_counts.json").read_text(encoding="utf-8")) if (TOPIC_DIR / "merchant_counts.json").exists() else None


def _days(d):
    import datetime as _dt
    return (_dt.date.fromisoformat(d) - _dt.date(2022, 1, 1)).days


def claim_label(c, TT):
    if c["lo"] != c["hi"]:
        return f'{c["lo"]} {TT["ch_to"]} {c["hi"]}'
    return f'{c["lo"]}+' if c.get("plus") else str(c["lo"])


def chart_merchants(lang):
    TT = TOPIC_T[lang]
    W, H, L, R_, T_, B = 900, 470, 50, 24, 26, 44
    pw, ph = W - L - R_, H - T_ - B
    span = _days("2026-12-31")
    X = lambda d: L + pw * _days(d) / span
    Y = lambda v: T_ + ph * (1 - v / 125)
    g = []
    for v in (0, 25, 50, 75, 100, 125):
        g.append(f'<line x1="{L}" x2="{W - R_}" y1="{Y(v):.1f}" y2="{Y(v):.1f}" class="ch-grid"/><text x="{L - 8}" y="{Y(v) + 5:.1f}" class="ch-ax" text-anchor="end">{v}</text>')
    for yr in range(2022, 2027):
        x = X(f"{yr}-01-01")
        g.append(f'<line x1="{x:.1f}" x2="{x:.1f}" y1="{T_}" y2="{H - B}" class="ch-grid"/><text x="{X(f"{yr}-07-01"):.1f}" y="{H - B + 28}" class="ch-ax" text-anchor="middle">{yr}</text>')
    dates = MC["btcmap"]["added_dates"]
    pts, n = [f"M{X(dates[0]):.1f},{Y(0):.1f}"], 0
    for d in dates:
        n += 1
        pts.append(f"H{X(d):.1f}V{Y(n):.1f}")
    pts.append(f'H{X(MC["btcmap"]["data_date"]):.1f}')
    g.append(f'<path d="{"".join(pts)}" class="ch-line"/>')
    g.append(f'<text x="{X(MC["btcmap"]["data_date"]) - 4:.1f}" y="{Y(n) - 9:.1f}" class="ch-lab ch-lab-line" text-anchor="end">{n}</text>')
    for i, c in enumerate(MC["claims"]):
        x, cls = X(c["date"]), "ch-team" if c["team"] else "ch-other"
        tip = escape(f'{c["date"][:7]}: {c["what_" + lang]}. {c["who_" + lang]}.')
        dx, dy, anc = c.get("lab") or (0, -14, "middle")
        if c["lo"] != c["hi"]:
            mark = (f'<rect x="{x - 7:.1f}" y="{Y(c["hi"]):.1f}" width="14" height="{Y(c["lo"]) - Y(c["hi"]):.1f}" rx="7" class="{cls}"/>')
            yl = Y((c["lo"] + c["hi"]) / 2)
        else:
            mark = (f'<circle cx="{x:.1f}" cy="{Y(c["lo"]):.1f}" r="7.5" class="{cls}"/>' if c["team"] else
                    f'<rect x="{x - 6.5:.1f}" y="{Y(c["lo"]) - 6.5:.1f}" width="13" height="13" class="{cls}"/>')
            yl = Y(c["lo"])
        g.append(f'<a href="{escape(c["url"], quote=True)}" rel="noopener"><title>{tip}</title>{mark}'
                 f'<text x="{x + dx:.1f}" y="{yl + dy:.1f}" class="ch-lab" text-anchor="{anc}">{escape(claim_label(c, TT))}</text></a>')
    legend = (f'<ul class="ch-legend"><li><span class="lg lg-team"></span>{TT["ch_team"]}</li><li><span class="lg lg-other"></span>{TT["ch_other"]}</li>'
              f'<li><span class="lg lg-line"></span>{escape(TT["ch_line"])}</li></ul>')
    svg = (legend + f'<div class="chart-scroll"><svg viewBox="0 0 {W} {H}" role="img" aria-labelledby="chm-t" class="chart-svg"><title id="chm-t">{escape(TT["ch_title"])}</title>'
           f'{"".join(g)}</svg></div>')
    items = "".join(
        f'<li><span class="cl-d">{fmt_date(c["date"][:7], lang)}</span> <strong>{escape(claim_label(c, TT))}</strong>: {escape(c["what_" + lang])}. '
        f'{escape(c["who_" + lang])}, <a href="{escape(c["url"], quote=True)}" rel="noopener">{escape(c["src"])}</a>.</li>' for c in MC["claims"])
    return (f'<figure class="chart reveal" id="chart-merchants"><figcaption class="chart-h">{escape(TT["ch_title"])}</figcaption>{svg}'
            f'<p class="chart-note">{escape(TT["ch_note"])}</p><details class="chart-list"><summary>{TT["ch_list"]} ({len(MC["claims"])})</summary><ol>{items}</ol></details></figure>')


def chart_checks(lang):
    TT = TOPIC_T[lang]
    rows = MC["btcmap"]["last_check_by_year"]
    total = sum(rows.values())
    mx = max(rows.values())
    bars = []
    for k, v in rows.items():
        lab = TT["ck_none"] if k == "none" else k
        recent = k in ("2025", "2026")
        bars.append(f'<li><span class="ck-y">{lab}</span><span class="ck-bar{" ck-recent" if recent else ""}" style="width:{100 * v / mx:.1f}%"></span>'
                    f'<span class="ck-n">{v}</span></li>')
    return (f'<figure class="chart reveal" id="chart-checks"><figcaption class="chart-h">{escape(TT["ck_title"])}</figcaption>'
            f'<ol class="ck-bars" aria-label="{total} {TT["ck_places"]}">{"".join(bars)}</ol>'
            f'<p class="chart-note">{escape(TT["ck_note"].format(n=MC["btcmap"]["checked_last_12m"]))}</p></figure>')


CHARTS = {"merchants": chart_merchants, "checks": chart_checks}


VIDEO_META = json.loads((TOPIC_DIR / "video_meta.json").read_text(encoding="utf-8")) if (TOPIC_DIR / "video_meta.json").exists() else {}


def ext_video_card(T, vid):
    """A video without its own article: thumbnail and title link straight to YouTube."""
    lang = T["lang"]
    m = VIDEO_META[vid]
    img = thumb(T, vid, m["title"]) if (ROOT / "images" / "blog" / f"{vid}.webp").exists() else ""
    when = fmt_date(m["date"][:7], lang) if m.get("date") else ""
    return (f'<li class="blog-card reveal"><a href="https://www.youtube.com/watch?v={vid}" rel="noopener">{img}'
            f'<span class="bc-meta">{escape(m.get("channel") or "YouTube")}{", " + when if when else ""}</span>'
            f'<span class="bc-title">{escape(m["title"])}</span></a></li>')


def topic_articles():
    return [json.loads(f.read_text(encoding="utf-8")) for f in sorted(TOPIC_DIR.glob("*.json")) if f.name not in ("merchant_counts.json", "video_meta.json")]


def topic_card(T, t, href, arts_by_id):
    lang = T["lang"]
    TT = TOPIC_T[lang]
    vid = next((v for v in t.get("videos", []) if (ROOT / "images" / "blog" / f"{v}.webp").exists()), None)
    img = thumb(T, vid, t["title_" + lang]) if vid else ""
    return (f'<li class="blog-card topic-card reveal"><a href="{href}">{img}'
            f'<span class="bc-meta">{TT["tp_card"]}, {fmt_date(t["date"][:7], lang)}</span>'
            f'<span class="bc-title">{escape(t["title_" + lang])}</span></a><p>{escape(t["dek_" + lang])}</p></li>')


def render_topic(lang, t, arts, topics):
    slug = t["slug"]
    TT = TOPIC_T[lang]
    T = page_T(lang, f"blog/{slug}/", f"es/blog/{slug}/", f'{t["title_" + lang]} | Bitcoin Lago', t["dek_" + lang])
    by_id = {a["video_id"]: a for a in arts}
    first = next((v for v in t.get("videos", []) if (ROOT / "images" / "blog" / f"{v}.jpg").exists()), None)
    if first:
        T["og_image"] = C.SITE_URL + f'images/blog/{first}.jpg'
    body = []
    for b in t["body_" + lang]:
        if b.get("chart"):
            body.append(CHARTS[b["chart"]](lang))
            continue
        if b.get("h"):
            body.append(f'<h2>{escape(b["h"])}</h2>')
        if b.get("p"):
            srcs = []
            for s in b.get("src", []):
                u = s.get("u") or ""
                if u.startswith("blog/"):
                    u = "../" + u[5:]
                srcs.append(f'<a href="{escape(u, quote=True)}" rel="noopener">{escape(s["t"])}</a>' if u else escape(s["t"]))
            src = f' <span class="src">[{"; ".join(srcs)}]</span>' if srcs else ""
            body.append(f'<p>{escape(b["p"])}{src}</p>')
    quotes = "".join(
        f'<blockquote class="bq"><p>{escape(q[lang])}</p><footer>{escape(q.get("who", ""))}, '
        f'<a href="https://www.youtube.com/watch?v={q["video_id"]}&amp;t={mmss_to_s(q["t"])}s" rel="noopener">'
        f'{escape(by_id[q["video_id"]]["channel"]) if q["video_id"] in by_id else "YouTube"}, {T["bl_at"]} {q["t"]}</a></footer></blockquote>'
        for q in t.get("quotes", []))
    used = "".join(blog_card(T, by_id[v], f'../{by_id[v]["slug"]}/') for v in t.get("videos", []) if v in by_id)
    used += "".join(ext_video_card(T, v) for v in t.get("videos", []) if v not in by_id and v in VIDEO_META)
    main = (f'<article class="post"><header class="scr story-hero post-head"><p><a class="link-arrow" href="../">{T["bl_back"]}</a></p>'
            f'<h1>{escape(t["title_" + lang])}</h1><p class="lede">{escape(t["dek_" + lang])}</p>'
            f'<p class="post-meta">{TT["tp_meta"]}. {fmt_date(t["date"], lang)}.</p></header>'
            f'<div class="scr post-body topic-body"><div class="post-text">{"".join(body)}'
            + (f'<h2>{TT["tp_quotes_h"]}</h2>{quotes}' if quotes else "")
            + f'<p class="post-note">{TT["tp_note"]}</p></div></div></article>'
            + (f'<section class="scr blog-list more"><h2>{TT["tp_used_h"]}</h2><ul class="blog-grid">{used}</ul></section>' if used else ""))
    return render_page(T, lang, main, f"blog/{slug}/{lang}")


def build_blog():
    arts = blog_articles()
    if not arts:
        return
    for lang in ("en", "es"):
        base = ROOT / ("blog" if lang == "en" else "es/blog")
        base.mkdir(parents=True, exist_ok=True)
        (base / "index.html").write_text(render_blog_index(lang, arts), encoding="utf-8")
        for a in arts:
            d = base / a["slug"]
            d.mkdir(parents=True, exist_ok=True)
            (d / "index.html").write_text(render_article(lang, a, arts), encoding="utf-8")
        topics = topic_articles()
        for t in topics:
            d = base / t["slug"]
            d.mkdir(parents=True, exist_ok=True)
            (d / "index.html").write_text(render_topic(lang, t, arts, topics), encoding="utf-8")
    print("wrote blog:", len(arts), "articles +", len(topic_articles()), "topics x 2 languages")


# ---------- Visitor FAQ (/faq/) ----------
FAQ_FILE = ROOT / "tools" / "faq.json"
FAQ_T = {
    "en": {"h1": "Visitor questions", "title": "Visitor questions | Bitcoin Lago",
           "lead": "Practical answers for your trip to Lake Atitlán with bitcoin: paying, wallets, cash, getting around, tours and how to help. Each answer links to its source.",
           "confirm": "We are still confirming this with the team.", "src": "Sources", "ask": "Did not find your question? Ask us.",
           "cta": "Visitor questions", "cta_p": "Paying, wallets, cash, getting around and how to help, in short answers."},
    "es": {"h1": "Preguntas de visitantes", "title": "Preguntas de visitantes | Bitcoin Lago",
           "lead": "Respuestas prácticas para tu viaje al Lago de Atitlán con bitcoin: pagos, billeteras, efectivo, transporte, tours y cómo ayudar. Cada respuesta enlaza a su fuente.",
           "confirm": "Todavía lo estamos confirmando con el equipo.", "src": "Fuentes", "ask": "¿No encontraste tu pregunta? Pregúntanos.",
           "cta": "Preguntas de visitantes", "cta_p": "Pagos, billeteras, efectivo, transporte y cómo ayudar, en respuestas cortas."},
}


def render_faq(lang, faq):
    F = FAQ_T[lang]
    T = page_T(lang, "faq/", "es/faq/", F["title"], F["lead"])
    groups, ld = [], []
    for g in faq["groups"]:
        items = []
        for it in g["items"]:
            srcs = []
            for s in it.get("src", []):
                u = s.get("u") or ""
                if u.startswith("#"):
                    u = T["home"] + u
                elif u and not u.startswith("http"):
                    u = T["home"] + u
                srcs.append(f'<a href="{escape(u, quote=True)}" rel="noopener">{escape(s["t"])}</a>' if u else escape(s["t"]))
            conf = f'<p class="faq-confirm">{F["confirm"]}</p>' if it.get("confirm") else ""
            src = f'<p class="src">{F["src"]}: {"; ".join(srcs)}</p>' if srcs else ""
            items.append(f'<details class="faq-item" id="{escape(it["id"], quote=True)}"><summary>{escape(it["q_" + lang])}</summary>'
                         f'<div class="faq-a"><p>{escape(it["a_" + lang])}</p>{conf}{src}</div></details>')
            ld.append({"@type": "Question", "name": it["q_" + lang], "acceptedAnswer": {"@type": "Answer", "text": it["a_" + lang]}})
        groups.append(f'<section class="faq-group" aria-labelledby="fq-{g["id"]}"><h2 id="fq-{g["id"]}">{escape(g["h_" + lang])}</h2>{"".join(items)}</section>')
    toc = "".join(f'<a href="#fq-{g["id"]}">{escape(g["h_" + lang])}</a>' for g in faq["groups"])
    jsonld = json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": ld}, ensure_ascii=False).replace("</", "<\\/")
    main = (f'<section class="scr story-hero" id="hero" aria-labelledby="faq-h1"><p><a class="link-arrow" href="{T["home"]}">{T["st_back"]}</a></p>'
            f'<h1 id="faq-h1">{F["h1"]}</h1><p class="lede">{F["lead"]}</p><nav class="year-chips" aria-label="{F["h1"]}">{toc}</nav></section>'
            f'<div class="scr post-body topic-body faq"><div class="post-text">{"".join(groups)}'
            f'<p class="post-note"><a href="{T["home"]}#community">{F["ask"]}</a></p></div></div>'
            f'<script type="application/ld+json">{jsonld}</script>')
    return render_page(T, lang, main, f"faq/{lang}")


def build_faq():
    if not FAQ_FILE.exists():
        return
    faq = json.loads(FAQ_FILE.read_text(encoding="utf-8"))
    for lang in ("en", "es"):
        d = ROOT / ("faq" if lang == "en" else "es/faq")
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(render_faq(lang, faq), encoding="utf-8")
    print("wrote faq:", sum(len(g["items"]) for g in faq["groups"]), "questions x 2 languages")


REDIRECT = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="robots" content="noindex,nofollow">
<title>Bitcoin Lago Community</title><meta http-equiv="refresh" content="0; url={to}">
<link rel="canonical" href="{canon}"></head>
<body><p><a href="{to}">Bitcoin Lago Community</a></p>
<script>location.replace("{to}" + location.hash);</script></body></html>
"""

# Old preview addresses that people may still have: send them to the site.
OLD_PAGES = {"v/": "../", "v/ad/": "../../", "v/ad/es/": "../../../es/", "variants/": "../", "variants/es/": "../../es/"}


def main():
    assert set(C.EN) == set(C.ES), set(C.EN) ^ set(C.ES)
    for lang in ("en", "es"):
        out = ROOT / ("" if lang == "en" else "es") / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render("ad", lang), encoding="utf-8")
        print("wrote", out.relative_to(ROOT))
        out = ROOT / ("story" if lang == "en" else "es/story") / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render_story(lang), encoding="utf-8")
        print("wrote", out.relative_to(ROOT))
    build_blog()
    build_faq()
    for rel, to in OLD_PAGES.items():
        out = ROOT / rel / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        canon = C.SITE_URL + ("es/" if rel.endswith("es/") else "")
        out.write_text(REDIRECT.format(to=to, canon=canon), encoding="utf-8")
        print("wrote", out.relative_to(ROOT), "->", to)


if __name__ == "__main__":
    main()
