#!/usr/bin/env python3
"""Build the three design variants (each in English and Spanish) and the /variants/ index.

WHAT IT DOES
  One content source (tools/content.py) and one data set (data/merchants.json, data/photos.json)
  feed three different page designs. Only the look differs: each variant has its own layout file
  (tools/variants/a.html, c.html, d.html) and its own stylesheet (v/a.css, c.css, d.css). Shared behaviour
  lives in v/app.js, shared base styles in v/base.css.

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
from topbar_prune import prune
import re
import sys
from html import escape
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import content as C  # noqa: E402
import build_pages as BP  # noqa: E402

ROOT = BP.ROOT
VDIR = ROOT / "tools" / "variants"
IDS = ["a", "c", "d", "ac", "ad", "cd", "f", "g", "h"]
SECTIONS = ["lake", "bitcoin", "transport", "community", "tours", "expats", "about"]

# Per-variant head settings: browser theme colour and the fonts to preload (files in /fonts).
META = {
    "a": {"theme": "#EEF0EB", "fonts": ["geist-latin-wght-normal.woff2", "geist-mono-latin-wght-normal.woff2"]},
    "c": {"theme": "#0C0B0B", "fonts": ["bebas-neue-latin-400-normal.woff2", "geist-latin-wght-normal.woff2"]},
    "d": {"theme": "#1E2760", "fonts": ["bricolage-grotesque-latin-wght-normal.woff2", "geist-latin-wght-normal.woff2"]},
    "ac": {"theme": "#0F1417", "fonts": ["geist-latin-wght-normal.woff2", "geist-mono-latin-wght-normal.woff2"]},
    "ad": {"theme": "#1E2760", "fonts": ["geist-latin-wght-normal.woff2", "geist-mono-latin-wght-normal.woff2"]},
    "cd": {"theme": "#0C0B0B", "fonts": ["bebas-neue-latin-400-normal.woff2", "geist-latin-wght-normal.woff2"]},
    "f": {"theme": "#FAFAF8", "fonts": ["coral-coral-latin-wght-normal.woff2", "space-grotesk-latin-wght-normal.woff2"]},
    "g": {"theme": "#FDFDFB", "fonts": ["newsreader-latin-wght-normal.woff2", "geist-latin-wght-normal.woff2"]},
    "h": {"theme": "#F2F6FF", "fonts": ["sora-latin-wght-normal.woff2", "geist-latin-wght-normal.woff2"]},
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
  <ul class="plain"><li data-placeholder="meetup-dates">{T["meet_when"]}</li><li data-placeholder="meetup-venues">{T["meet_where"]}</li></ul></article>
<article class="tile tile-school reveal">{BP.icon("graduation-cap")}<h3>{T["school_h"]}</h3><p>{T["school_p"]}</p>
  <p class="muted" data-placeholder="school-list">{T["school_list"]}</p></article>
<article class="tile tile-follow reveal">{BP.icon("envelope-simple")}<h3>{T["follow_h"]}</h3>
  <ul class="plain"><li><a class="link-arrow" href="#community" data-config-link="facebook" data-placeholder="facebook">{BP.icon("facebook-logo")}{T["facebook"]}</a></li>
  <li><a class="link-arrow" href="#community" data-config-link="email" data-placeholder="contact-email">{BP.icon("envelope-simple")}{T["email"]}</a></li></ul></article>
<article class="tile tile-who reveal">{BP.icon("users-three")}<h3>{T["who_h"]}</h3><p>{T["who_p"]}</p>
  <p class="muted" data-placeholder="tomek-bio-photo">{T["who_bio"]}</p></article>'''


def tour_points(T):
    return "".join(
        f'<li class="reveal">{BP.icon(ic)}<div><h3>{T[f"tours_{i}_h"]}</h3><p>{T[f"tours_{i}_p"]}</p></div></li>'
        for i, ic in ((1, "handshake"), (2, "compass"), (3, "currency-btc")))


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
        f'<meta property="og:site_name" content="Lago Bitcoin Community">\n'
        f'<meta property="og:title" content="{{{{title}}}}">\n'
        f'<meta property="og:description" content="{{{{description}}}}">\n'
        f'<meta property="og:url" content="{{{{canonical}}}}">\n'
        f'<meta property="og:locale" content="{{{{og_locale}}}}">\n'
        f'<meta property="og:image" content="{{{{og_image}}}}">\n'
        f'<meta name="twitter:card" content="summary_large_image">\n'
        f'{pre}<link rel="stylesheet" href="{{{{p}}}}v/base.css">\n'
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
        f'<!-- Fixed top bar: variant switcher + EN/ES toggle. Navy bar with coloured per-design chips. -->\n'
        f'<div class="topbar" role="navigation" aria-label="Design and language switcher">\n'
        f'  <div class="topbar-in">\n'
        f'    <nav class="topbar-variants" aria-label="Design variants">\n'
        f'      <a href="{{{{p}}}}" class="topbar-chip {{{{topbar_baseline}}}}" data-design="baseline" title="First design (baseline)">Base</a>\n'
        f'      <a href="{{{{p}}}}v/a/" class="topbar-chip {{{{topbar_a}}}}" data-design="a" title="{{{{vsw_label}}}} A: {{{{VARIANTS.a.[lang].0}}}}">A</a>\n'
        f'      <a href="{{{{p}}}}v/c/" class="topbar-chip {{{{topbar_c}}}}" data-design="c" title="{{{{vsw_label}}}} C: {{{{VARIANTS.c.[lang].0}}}}">C</a>\n'
        f'      <a href="{{{{p}}}}v/d/" class="topbar-chip {{{{topbar_d}}}}" data-design="d" title="{{{{vsw_label}}}} D: {{{{VARIANTS.d.[lang].0}}}}">D</a>\n'
        f'      <a href="{{{{p}}}}v/ac/" class="topbar-chip {{{{topbar_ac}}}}" data-design="ac" title="{{{{vsw_label}}}} AC: {{{{VARIANTS.ac.[lang].0}}}}">AC</a>\n'
        f'      <a href="{{{{p}}}}v/ad/" class="topbar-chip {{{{topbar_ad}}}}" data-design="ad" title="{{{{vsw_label}}}} AD: {{{{VARIANTS.ad.[lang].0}}}}">AD</a>\n'
        f'      <a href="{{{{p}}}}v/cd/" class="topbar-chip {{{{topbar_cd}}}}" data-design="cd" title="{{{{vsw_label}}}} CD: {{{{VARIANTS.cd.[lang].0}}}}">CD</a>\n'
        f'      <a href="{{{{p}}}}v/f/" class="topbar-chip {{{{topbar_f}}}}" data-design="f" title="{{{{vsw_label}}}} F: {{{{VARIANTS.f.[lang].0}}}}">F</a>\n'
        f'      <a href="{{{{p}}}}v/g/" class="topbar-chip {{{{topbar_g}}}}" data-design="g" title="{{{{vsw_label}}}} G: {{{{VARIANTS.g.[lang].0}}}}">G</a>\n'
        f'      <a href="{{{{p}}}}v/h/" class="topbar-chip {{{{topbar_h}}}}" data-design="h" title="{{{{vsw_label}}}} H: {{{{VARIANTS.h.[lang].0}}}}">H</a>\n'
        f'    </nav>\n'
        f'    <div class="topbar-lang" role="group" aria-label="{{{{lang_label}}}}">\n'
        f'      <a href="{{{{p_en}}}}" lang="en" hreflang="en" data-lang="en" title="{{{{lang_en_name}}}}" {{{{cur_en}}}}>EN</a>\n'
        f'      <a href="{{{{p_es}}}}" lang="es" hreflang="es" data-lang="es" title="{{{{lang_es_name}}}}" {{{{cur_es}}}}>ES</a>\n'
        f'    </div>\n'
        f'  </div>\n'
        f'</div>\n'
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
    T = dict(C.LANGS[lang])
    prefix = "../../" if lang == "en" else "../../../"
    ln = sum(1 for p in BP.PLACES if p["lightning"] == "yes")
    chain = sum(1 for p in BP.PLACES if p["onchain"] == "yes")
    path = f"v/{vid}/" + ("" if lang == "en" else "es/")
    # Top bar active states: current variant gets topbar-current
    topbar_states = {
        "topbar_baseline": "",
        "topbar_a": "topbar-current" if vid == "a" else "",
        "topbar_c": "topbar-current" if vid == "c" else "",
        "topbar_d": "topbar-current" if vid == "d" else "",
        "topbar_ac": "topbar-current" if vid == "ac" else "",
        "topbar_ad": "topbar-current" if vid == "ad" else "",
        "topbar_cd": "topbar-current" if vid == "cd" else "",
        "topbar_f": "topbar-current" if vid == "f" else "",
        "topbar_g": "topbar-current" if vid == "g" else "",
        "topbar_h": "topbar-current" if vid == "h" else "",
    }
    T.update(
        p=prefix,
        vid=vid,
        p_en="./" if lang == "en" else "../",
        p_es="es/" if lang == "en" else "./",
        cur_en='aria-current="true"' if lang == "en" else "",
        cur_es='aria-current="true"' if lang == "es" else "",
        canonical=C.SITE_URL + path,
        url_en=C.SITE_URL + f"v/{vid}/",
        url_es=C.SITE_URL + f"v/{vid}/es/",
        og_image=C.SITE_URL + "images/hero-1600.jpg",
        x_lakebitcoin=C.X_LAKEBITCOIN,
        n_places=str(len(BP.PLACES)),
        n_ln=str(ln),
        n_chain=str(chain),
        vname=C.VARIANTS[vid][lang][0],
        **topbar_states,
    )
    T["foot_updated"] = T["foot_updated"].format(d=C.LAST_UPDATED)
    blocks = {
        "towns": BP.towns_html(),
        "towns_bars": towns_bars(),
        "rides": BP.ride_html(T),
        "community_transport_photos": BP.community_transport_photos(T),
        "press": BP.press_html(T),
        "finder": finder(T),
        "finder_console": finder(T, console=True),
        "community": community(T),
        "tour_points": tour_points(T),
        "stats": stats(T, ln, chain),
        "atm": atm(T),
        "footer_text": footer_text(T),
        "switcher": switcher(vid, lang, T),
        "i18n_json": json.dumps({**{k: T[k] for k in C.I18N_KEYS}, "categories": C.CATEGORIES[lang]},
                                ensure_ascii=False).replace("</", "<\\/"),
    }
    html = head_html(vid) + (VDIR / f"{vid}.html").read_text(encoding="utf-8") + FOOT
    return fill(html, T, blocks, lang, f"{vid}/{lang}")


def fill(html, T, blocks, lang, label):
    html = re.sub(r"\{\{@(\w+)\}\}", lambda m: blocks[m.group(1)], html)
    html = re.sub(r"\{\{icon:([\w-]+)\}\}", lambda m: BP.icon(m.group(1)), html)
    html = re.sub(r"\{\{fig:([\w-]+)((?:\|[^|}]*){0,3})\}\}",
                  lambda m: fig(m.group(1), T, *(lambda a: (a[0] or "100vw", a[1] or "", a[2]))(
                      (m.group(2).lstrip("|").split("|") + ["", "", ""])[:3])), html)
    html = re.sub(r"\{\{maya:(\d+)(?:\|([\w -]+))?\}\}", lambda m: maya(int(m.group(1)), m.group(2) or "maya"), html)

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
    for x in [i for i in IDS if (VDIR / f"{i}.html").exists()]:
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


def main():
    assert set(C.EN) == set(C.ES), set(C.EN) ^ set(C.ES)
    assert set(C.VARIANTS) == set(IDS)
    ids = [a for a in sys.argv[1:] if a in IDS] or IDS  # optional: python tools/build_variants.py a c
    for vid in ids:
        if not (VDIR / f"{vid}.html").exists():
            print("skip (no layout file yet):", vid)
            continue
        for lang in ("en", "es"):
            out = ROOT / "v" / vid / ("" if lang == "en" else "es") / "index.html"
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(prune(render(vid, lang)), encoding="utf-8")
            print("wrote", out.relative_to(ROOT))
    # /v/ : send visitors to the design they looked at last (default A).
    (ROOT / "v" / "index.html").write_text((VDIR / "v-redirect.html").read_text(encoding="utf-8"), encoding="utf-8")
    for lang in ("en", "es"):
        out = ROOT / "variants" / ("" if lang == "en" else "es") / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(prune(build_index(lang)), encoding="utf-8")
        print("wrote", out.relative_to(ROOT))


if __name__ == "__main__":
    main()
