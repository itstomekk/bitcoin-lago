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
import sys as _s, pathlib as _p; _s.path.insert(0,str(_p.Path(__file__).resolve().parent))
import re
import sys
from html import escape
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import content as C  # noqa: E402
import build_pages as BP  # noqa: E402

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
    """A Lago Bitcoin photo (Eliazar's archive or a public X post) with its credit."""
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
    return (f'<dl class="stats"><div><dt>{T["btc_stat_places"]}</dt><dd data-count="{len(BP.PLACES)}">{len(BP.PLACES)}</dd></div>'
            f'<div><dt>{T["btc_stat_ln"]}</dt><dd data-count="{ln}">{ln}</dd></div>'
            f'<div><dt>{T["btc_stat_chain"]}</dt><dd data-count="{chain}">{chain}</dd></div></dl>')


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
        f'<meta property="og:type" content="website">\n'
        f'<meta property="og:site_name" content="Lago Bitcoin">\n'
        f'<meta property="og:title" content="{{{{title}}}}">\n'
        f'<meta property="og:description" content="{{{{description}}}}">\n'
        f'<meta property="og:url" content="{{{{canonical}}}}">\n'
        f'<meta property="og:locale" content="{{{{og_locale}}}}">\n'
        f'<meta property="og:image" content="{{{{og_image}}}}">\n'
        f'<meta name="twitter:card" content="summary_large_image">\n'
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


REDIRECT = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="robots" content="noindex,nofollow">
<title>Lago Bitcoin Community</title><meta http-equiv="refresh" content="0; url={to}">
<link rel="canonical" href="{canon}"></head>
<body><p><a href="{to}">Lago Bitcoin Community</a></p>
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
    for rel, to in OLD_PAGES.items():
        out = ROOT / rel / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        canon = C.SITE_URL + ("es/" if rel.endswith("es/") else "")
        out.write_text(REDIRECT.format(to=to, canon=canon), encoding="utf-8")
        print("wrote", out.relative_to(ROOT), "->", to)


if __name__ == "__main__":
    main()
