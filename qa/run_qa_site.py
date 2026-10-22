#!/usr/bin/env python3
"""Release QA for the finished design variants (each with /es/) and the /variants/ index.

USAGE
  python qa/run_qa_site.py <site root URL> <screenshot dir> [variants, e.g. a,c,d] [--no-index]
  local : python qa/run_qa_site.py http://127.0.0.1:18431/ qa/.cache/shots-local
  live  : python qa/run_qa_site.py https://itstomekk.github.io/lago-bitcoin-community/ qa/screenshots
  (needs qa/.cache/axe.min.js: curl -L -o qa/.cache/axe.min.js https://cdn.jsdelivr.net/npm/axe-core@4.10.2/axe.min.js)

WRITES
  <screenshot dir>/<variant>/*.jpg      screenshots per variant (1440 and 390, EN and ES, map, menu, switcher)
  qa/report-variants-<local|live>.json  every gate with PASS/FAIL and the measured evidence
  qa/report-variants-<local|live>.md    the same, readable

GATES PER VARIANT (EN and ES unless noted)
  HTTP 200 for both pages and every asset they reference (css, js, data, fonts, every image); title and description;
  noindex,nofollow; hreflang; no console errors/warnings or failed requests; page weight; every section fills the screen
  (>= 95% of the viewport height at 1440x900); no horizontal overflow at 1440 and 390 and no text leaving the screen;
  map shows 117 markers in the design's own colour and the list shows 117 cards; search, chip, village, empty and reset
  filters; ride "Show on map"; every image has alt text; local Commons photos have Commons/licence links and community-archive
  photos use the approved provisional credit; only local images are used;
  no "official", no dashes; footer credits; Design switcher (all finished designs, current marked, keeps language, remembers the
  choice); the mobile menu or H's section map; EN/ES parity; WCAG A/AA with axe-core at 1440 and 390; and a pixel contrast check of every piece
  of text that sits over a photo, gradient or pattern (axe cannot measure those).
"""
import io
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urljoin, urlparse

from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
PRESS_SLUGS = {item["slug"] for item in json.loads((ROOT / "data" / "press-photos.json").read_text(encoding="utf-8"))}
args = [a for a in sys.argv[1:] if not a.startswith("--")]
BASE = args[0].rstrip("/") + "/"
SHOTS = Path(args[1]) if Path(args[1]).is_absolute() else ROOT / args[1]
IDS = ["ad"]  # the site is one design (AD) at the root since 2026-10-21
LABEL = "live" if BASE.startswith("https://") else "local"
AXE_PATH = ROOT / "qa" / ".cache" / "axe.min.js"
AXE = AXE_PATH.read_text(encoding="utf-8") if AXE_PATH.exists() else None
EXPECT = 117
results = []
PLACEHOLDERS = set()


def gate(name, ok, evidence):
    results.append({"gate": name, "result": "PASS" if ok else "FAIL", "evidence": evidence})
    print(("PASS " if ok else "FAIL ") + name + " :: " + str(evidence)[:260], flush=True)


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "lbc-qa"})
    try:
        with urllib.request.urlopen(req, timeout=40) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        return e.code, b""
    except Exception as e:  # noqa: BLE001
        return 0, str(e).encode()


OVERFLOW_JS = "({sw: document.documentElement.scrollWidth, cw: document.documentElement.clientWidth})"
LEAK_JS = """() => { const vw = innerWidth, out = []; const inScroller = e => { for (let q = e.parentElement; q && q !== document.body; q = q.parentElement) { const o = getComputedStyle(q).overflowX; if ((o === 'auto' || o === 'scroll') && q.scrollWidth > q.clientWidth + 1) return true; } return false; };
  document.querySelectorAll('h1,h2,h3,p,a,button,li,dt,dd,label,input,select,figcaption').forEach(e => {
    if (e.closest('.sr-only,.skip,.leaflet-container,[aria-hidden=true]') || e.classList.contains('sr-only')) return;
    const r = e.getBoundingClientRect(); if (!r.width || !r.height) return;
    const cs = getComputedStyle(e); if (cs.visibility === 'hidden') return;
    if (e.closest('.nav') && !e.closest('.nav').offsetParent && getComputedStyle(e.closest('.nav')).position !== 'fixed') return;
    if ((r.right > vw + 1 || r.left < -1) && !inScroller(e)) out.push((e.className || e.tagName) + ' ' + Math.round(r.left) + '..' + Math.round(r.right) + ' ' + (e.textContent || '').trim().slice(0, 30));
  }); return out.slice(0, 8); }"""
PARITY_JS = """() => ({
  sections: [...document.querySelectorAll('main section[id]')].map(s => s.id),
  placeholders: [...document.querySelectorAll('[data-placeholder]')].map(e => e.dataset.placeholder),
  navTargets: [...document.querySelectorAll('.nav a')].map(a => a.getAttribute('href')),
  cards: document.querySelectorAll('#cards .card').length,
  h2: document.querySelectorAll('h2').length,
  imgs: document.querySelectorAll('img').length })"""
IMG_JS = """() => [...document.querySelectorAll('img')].filter(i => !i.closest('.leaflet-container') && !i.closest('.partner-logo')).map(i => ({
  src: i.currentSrc, alt: i.getAttribute('alt'), nat: i.naturalWidth, inFigure: !!i.closest('figure'),
  credit: !!(i.closest('figure') && ((i.closest('figure').querySelector('.credit a[href*="commons.wikimedia.org"]') && i.closest('figure').querySelector('.credit a[href*="creativecommons.org"]')) || i.closest('figure').querySelector('.credit')?.textContent.includes('Photo: community archive (source to confirm)') || (i.closest('.lb-photo') && /^(Photo|Foto): (Bitcoin Lago|@JUN_AJPU_btc|@AtitlanTours21)/.test(i.closest('figure').querySelector('.credit')?.textContent || '')) || i.closest('figure').querySelector('.press-photo-credit[href]') || (i.closest('.history-video') && i.closest('figure').querySelector('figcaption a[href*="youtube.com/watch"]')))) }))"""
PRESS_JS = """() => { const fs = [...document.querySelectorAll('.press .press-photo')];
  return {slugs: fs.map(f => f.dataset.pressSlug), bad: fs.filter(f => {
    const c = f.querySelector('.press-photo-credit[href]');
    return !f.dataset.pressUrl || !c || c.getAttribute('href') !== f.dataset.pressUrl || !c.textContent.startsWith('Photo:');
  }).map(f => f.dataset.pressSlug || 'missing-slug')}; }"""
FILL_JS = """() => [...document.querySelectorAll('main section[id]')].map(s => [s.id, +(s.getBoundingClientRect().height / innerHeight).toFixed(2)])"""

# Text that sits over a photo, gradient or pattern: found by looking at what is painted below each text element.
OVER_JS = """() => {
  const found = [], seen = new Set();
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  let n;
  while ((n = walker.nextNode())) {
    if (!n.textContent.trim()) continue;
    const el = n.parentElement; if (!el || seen.has(el)) continue; seen.add(el);
    if (el.closest('.sr-only,.leaflet-container,script,style,noscript,.vsw,.toast,[hidden],[aria-hidden=true],.nav .lbl,.nav .n')) continue;
    const cs = getComputedStyle(el); if (cs.visibility === 'hidden' || cs.display === 'none') continue;
    let hid = false; for (let q = el; q; q = q.parentElement) { if (getComputedStyle(q).opacity === '0') { hid = true; break; } } if (hid) continue;
    const r = el.getBoundingClientRect(); if (r.width < 2 || r.height < 2) continue;
    el.setAttribute('data-qa-i', String(found.length)); found.push(el);
  }
  const res = [];
  found.forEach((el, i) => {
    el.scrollIntoView({block: 'center', behavior: 'instant'});
    const r = el.getBoundingClientRect();
    if (r.top < 0 || r.bottom > innerHeight || r.width < 2) return;
    let over = false, surface = null;
    [[0.5, 0.5], [0.15, 0.5], [0.85, 0.5]].forEach(([fx, fy]) => {
      const hits = document.elementsFromPoint(r.left + r.width * fx, r.top + r.height * fy);
      const idx = hits.findIndex(h => h === el || el.contains(h));
      if (idx < 0) return;
      for (const h of hits.slice(idx + 1)) {
        if (h === document.body || h === document.documentElement) break;  // the page background itself is a light, gentle gradient (design E)
        const c = getComputedStyle(h);
        if (h.tagName === 'IMG' || h.tagName === 'CANVAS' || (c.backgroundImage && c.backgroundImage !== 'none')) { over = true; surface = h; break; }
        const m = (c.backgroundColor.match(/[\d.]+/g) || []).map(Number);
        if (!h.contains(el) && m.length >= 3 && (m.length === 3 || m[3] >= 0.98)) break;  // an opaque layer (not one of the text's own ancestors) hides whatever is below
      }
    });
    if (over) { const c = getComputedStyle(el), s = getComputedStyle(surface);
      const surfaceKey = surface.tagName === 'IMG' ? surface.currentSrc : [surface.tagName, surface.id, String(surface.className || ''), s.backgroundImage, s.backgroundColor].join('|');
      res.push({i, surface: surfaceKey, color: c.color, size: parseFloat(c.fontSize), weight: parseInt(c.fontWeight, 10) || 400, text: el.textContent.trim().slice(0, 40)}); }
  });
  return res; }"""


def lum(rgb):
    def ch(v):
        v /= 255
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    return 0.2126 * ch(rgb[0]) + 0.7152 * ch(rgb[1]) + 0.0722 * ch(rgb[2])


def ratio(a, b):
    hi, lo = max(a, b), min(a, b)
    return (hi + 0.05) / (lo + 0.05)


def over_contrast(pg, label):
    """Pixel check: hide all text, photograph the area behind each overlay text, compare to the text colour."""
    items = pg.evaluate(OVER_JS)
    if not items:
        gate(f"{label} text over photos/gradients: contrast", True, "no overlay text found")
        return
    candidate_count = len(items)
    if pg.locator("body.v-h").count():
        groups = {}
        for item in items:
            key = (item.get("surface", ""), item["color"], item["size"], item["weight"])
            groups.setdefault(key, []).append(item)
        items = [group[index] for group in groups.values() for index in sorted({0, len(group) // 2, len(group) - 1})]
    pg.evaluate("""() => { const st = document.createElement('style'); st.id = 'qa-hide';
        st.textContent = '*{color:transparent!important;-webkit-text-fill-color:transparent!important;text-shadow:none!important}.vsw,.toast,[data-placeholder]::after{visibility:hidden!important}';
        document.head.appendChild(st); st.disabled = true; }""")
    bad, lowest = [], 99.0
    for it in items:
        sel = f'[data-qa-i="{it["i"]}"]'
        pg.evaluate("(s) => document.querySelector(s).scrollIntoView({block:'center', behavior:'instant'})", sel)
        if not pg.locator("body.v-h").count():
            pg.wait_for_timeout(250)  # let scroll-driven states (active nav item, reveal) settle
        # measure the text itself (Range), and its colour at this very moment
        info = pg.evaluate("""(s) => { const el = document.querySelector(s); const rg = document.createRange(); rg.selectNodeContents(el);
            const r = rg.getBoundingClientRect(); const c = getComputedStyle(el);
            const ctx = document.createElement('canvas').getContext('2d');
            ctx.fillStyle = c.color; ctx.fillRect(0, 0, 1, 1);
            const rgb = [...ctx.getImageData(0, 0, 1, 1).data].slice(0, 3);
            const out = {box: [r.left, r.top, r.width, r.height], color: c.color, rgb, size: parseFloat(c.fontSize), weight: parseInt(c.fontWeight, 10) || 400};
            document.getElementById('qa-hide').disabled = false;
            return out; }""", sel)
        x, y, w, h = info["box"]
        x, y = max(0, x), max(0, y)
        w, h = min(w, pg.viewport_size["width"] - x), min(h, pg.viewport_size["height"] - y)
        if w < 2 or h < 2:
            continue
        im = Image.open(io.BytesIO(pg.screenshot(clip={"x": x, "y": y, "width": w, "height": h}))).convert("RGB")
        pg.evaluate("document.getElementById('qa-hide').disabled = true")
        ls = sorted(lum(p) for p in im.resize((max(1, min(48, int(w))), max(1, min(24, int(h))))).get_flattened_data() if True) if hasattr(im, "get_flattened_data") else sorted(lum(p) for p in im.resize((max(1, min(48, int(w))), max(1, min(24, int(h))))).getdata())
        p3, p97 = ls[int(len(ls) * 0.03)], ls[min(len(ls) - 1, int(len(ls) * 0.97))]
        tl = lum(info["rgb"])
        r_ = min(ratio(tl, p3), ratio(tl, p97))
        need = 3.0 if (info["size"] >= 24 or (info["size"] >= 18.66 and info["weight"] >= 700)) else 4.5
        lowest = min(lowest, r_)
        if r_ < need:
            bad.append(f'{it["text"]!r} {r_:.2f}<{need} (text L={tl:.2f}, behind {p3:.2f}..{p97:.2f})')
    pg.evaluate("document.getElementById('qa-hide').remove()")
    gate(f"{label} text over photos/gradients: contrast >= AA (pixel check)", not bad, {"checked": len(items), "candidates": candidate_count, "lowest_ratio": round(lowest, 2), "failures": bad[:6]})


def run_axe(pg, label):
    if not AXE:
        gate(f"{label} axe-core available", False, "qa/.cache/axe.min.js missing")
        return
    pg.evaluate(AXE)
    ax = pg.evaluate("axe.run(document, {runOnly:['wcag2a','wcag2aa'], resultTypes:['violations']}).then(r => r.violations.map(v => ({id: v.id, impact: v.impact, n: v.nodes.length, sample: v.nodes.slice(0,3).map(n => n.target.join(' ') + ' :: ' + (n.any[0] ? n.any[0].message : ''))})))")
    gate(f"{label} axe-core WCAG A/AA violations", not ax, ax)


def reveal_all(pg, step=600):
    h = pg.evaluate("document.documentElement.scrollHeight")
    y = 0
    while y < h:
        pg.evaluate(f"window.scrollTo(0,{y})")
        pg.wait_for_timeout(110)
        y += step
    pg.evaluate("window.scrollTo(0,0)")
    pg.wait_for_timeout(700)
    pg.wait_for_load_state("networkidle")


def shot(pg, path, full=False):
    path.parent.mkdir(parents=True, exist_ok=True)
    pg.screenshot(path=str(path), full_page=full, type="jpeg", quality=70)


def check_assets(label, html, page_url):
    urls = set(m.group(1) for m in re.finditer(r'(?:href|src)="([^"#]+)"', html))
    for m in re.finditer(r'srcset="([^"]+)"', html):
        for part in m.group(1).split(","):
            urls.add(part.strip().split(" ")[0])
    local = sorted({urljoin(page_url, u) for u in urls if not u.startswith(("http:", "https:", "mailto:", "tel:", "data:", "javascript:"))})
    local = [u for u in local if urlparse(u).netloc == urlparse(BASE).netloc]
    bad = []
    for u in local:
        st, _ = fetch(u)
        if st != 200:
            bad.append((u, st))
    gate(f"{label} every referenced asset and link returns 200", not bad, {"checked": len(local), "bad": bad[:5]})


def variant(browser, vid):
    out = SHOTS / vid
    parity, page_html = {}, {}
    for lang, path in (("en", ""), ("es", "es/")):
        url = f"{BASE}{path}"
        L = f"[{vid}/{lang}]"
        st, body = fetch(url)
        html = body.decode("utf-8", "replace")
        page_html[lang] = html
        gate(f"{L} HTTP 200 {url}", st == 200, st)
        t = re.search(r"<title>(.*?)</title>", html, re.S)
        d = re.search(r'<meta name="description" content="([^"]*)"', html)
        gate(f"{L} title + meta description", bool(t and d and 20 < len(t.group(1)) < 90 and 80 < len(d.group(1)) <= 200), {"title": t and t.group(1), "desc_len": d and len(d.group(1))})
        gate(f"{L} meta robots noindex,nofollow", '<meta name="robots" content="noindex,nofollow">' in html, "present")
        hl = re.findall(r'<link rel="alternate" hreflang="([^"]+)" href="([^"]+)"', html)
        gate(f"{L} hreflang en/es/x-default", {h for h, _ in hl} == {"en", "es", "x-default"}, hl)
        gate(f"{L} html lang + data-design", f'<html lang="{lang}" data-design="{vid}">' in html, lang)
        check_assets(L, html, url)

        # ---- 1440 ----
        ctx = browser.new_context(viewport={"width": 1440, "height": 900}, locale="en-US" if lang == "en" else "es-GT")
        pg = ctx.new_page()
        errs, failed, weight = [], [], {"b": 0, "t": 0}

        def on_resp(r, weight=weight):
            try:
                n = len(r.body())
            except Exception:  # noqa: BLE001
                return
            weight["t" if "tile.openstreetmap.org" in r.url else "b"] += n
        pg.on("response", on_resp)
        pg.on("console", lambda m, errs=errs: errs.append(m.text) if m.type in ("error", "warning") else None)
        pg.on("pageerror", lambda e, errs=errs: errs.append(str(e)))
        pg.on("requestfailed", lambda r, failed=failed: failed.append(r.url))
        pg.goto(url, wait_until="networkidle")
        pg.wait_for_timeout(1500)
        reveal_all(pg)
        gate(f"{L} no console errors/warnings, no failed requests", not errs and not failed, {"console": errs[:4], "failed": failed[:4]})
        gate(f"{L} page weight under 3.5 MB after scrolling every lazy photo in, excluding map tiles", weight["b"] < 3.5 * 1024 * 1024, f'{weight["b"] / 1024:.0f} KB')
        ov = pg.evaluate(OVERFLOW_JS)
        gate(f"{L} no horizontal overflow at 1440", ov["sw"] <= ov["cw"], ov)
        leak = pg.evaluate(LEAK_JS)
        gate(f"{L} no text leaves the screen at 1440", not leak, leak)
        fill = pg.evaluate(FILL_JS)
        gate(f"{L} every section fills the screen (>=0.95 of viewport height)", all(r >= 0.95 for _, r in fill), fill)

        st_ = pg.evaluate("document.getElementById('map').dataset.state")
        paths = pg.evaluate("document.querySelectorAll('#map path.leaflet-interactive').length")
        cards = pg.evaluate("document.querySelectorAll('#cards .card').length")
        hooks = pg.evaluate("({m: LBC_STATE.markers(), c: LBC_STATE.cards(), v: LBC_STATE.visibleCards(), p: LBC_STATE.places()})")
        tiles = pg.evaluate("document.querySelectorAll('#map .leaflet-tile-loaded').length")
        gate(f"{L} map ready and renders {EXPECT} markers", st_ == "ready" and paths == EXPECT and tiles > 0, {"state": st_, "markers": paths, "tiles": tiles})
        gate(f"{L} list count == marker count == {EXPECT}", cards == paths == hooks["m"] == hooks["p"] == EXPECT, {"cards": cards, "markers": paths, "hook": hooks})
        gate(f"{L} count text shows {EXPECT}", str(EXPECT) in pg.inner_text("#count"), pg.inner_text("#count"))
        mk = pg.evaluate("""() => ({fills: [...new Set([...document.querySelectorAll('#map path.leaflet-interactive')].map(p => p.getAttribute('fill').toLowerCase()))],
                                  token: getComputedStyle(document.getElementById('map')).getPropertyValue('--marker-fill').trim().toLowerCase()})""")
        gate(f"{L} markers use the design's own colour token", mk["fills"] == [mk["token"]], mk)

        pg.fill("#q", "coffee" if lang == "en" else "café")
        pg.wait_for_timeout(500)
        v1 = pg.evaluate("({c: LBC_STATE.visibleCards(), m: LBC_STATE.markers(), paths: document.querySelectorAll('#map path.leaflet-interactive').length})")
        gate(f"{L} search filters list and map together", 0 < v1["c"] < EXPECT and v1["c"] == v1["m"] == v1["paths"], v1)
        pg.click("#reset")
        pg.wait_for_timeout(300)
        pg.click('.chip[data-group="stay"]')
        pg.wait_for_timeout(300)
        v2 = pg.evaluate("({c: LBC_STATE.visibleCards(), m: LBC_STATE.markers(), pressed: document.querySelector('.chip[aria-pressed=true]').dataset.group})")
        gate(f"{L} category chip filters (stay)", 0 < v2["c"] < EXPECT and v2["c"] == v2["m"] and v2["pressed"] == "stay", v2)
        pg.click("#reset")
        pg.select_option("#town", "San Marcos La Laguna")
        pg.wait_for_timeout(300)
        v3 = pg.evaluate("({c: LBC_STATE.visibleCards(), m: LBC_STATE.markers()})")
        gate(f"{L} village filter", v3["c"] == v3["m"] and 0 < v3["c"] < EXPECT, v3)
        pg.fill("#q", "zzzzqq")
        pg.wait_for_timeout(300)
        v4 = pg.evaluate("({c: LBC_STATE.visibleCards(), m: LBC_STATE.markers(), empty: !!document.getElementById('empty')})")
        gate(f"{L} empty state", v4["c"] == 0 and v4["m"] == 0 and v4["empty"], v4)
        pg.click("#reset")
        pg.wait_for_timeout(300)
        v5 = pg.evaluate("({c: LBC_STATE.visibleCards(), m: LBC_STATE.markers()})")
        gate(f"{L} reset restores {EXPECT}", v5 == {"c": EXPECT, "m": EXPECT}, v5)
        pg.click(".show-btn >> nth=0")
        pg.wait_for_timeout(900)
        gate(f"{L} ride 'Show on map' opens a popup", pg.evaluate("!!document.querySelector('.leaflet-popup')"), "popup")

        # live sites on a slow link: scroll every lazy image into range and give them up to 25 s to arrive
        pg.evaluate("async () => { for (let y = 0; y < document.body.scrollHeight; y += 600) { scrollTo(0, y); await new Promise(r => setTimeout(r, 80)); } }")
        try:
            pg.wait_for_function("[...document.images].every(i => i.complete && i.naturalWidth > 0)", timeout=25000)
        except Exception:
            pass  # the gates below report whatever is still missing
        imgs = pg.evaluate(IMG_JS)
        bad_alt = [i for i in imgs if i["alt"] is None or (i["alt"] == "" and "favicon" not in i["src"] and "logo" not in i["src"])]
        photos = [i for i in imgs if "/images/" in i["src"] and "/logo/" not in i["src"]]
        bad_credit = [i["src"][-30:] for i in photos if not i["credit"]]
        foreign = [i["src"] for i in imgs if "/images/" not in i["src"] and "favicon" not in i["src"]]
        gate(f"{L} every image has alt text", not bad_alt, {"images": len(imgs), "bad": bad_alt[:3]})
        gate(f"{L} only local photos, each with a Commons, approved community-archive, or linked press credit", bool(photos) and not bad_credit and not foreign, {"photos": len(photos), "no_credit": bad_credit, "other_images": foreign})
        press = pg.evaluate(PRESS_JS)
        gate(f"{L} all 30 press photos appear once with visible linked credits", len(press["slugs"]) == 30 and set(press["slugs"]) == PRESS_SLUGS and not press["bad"], {"count": len(press["slugs"]), "unique": len(set(press["slugs"])), "missing": sorted(PRESS_SLUGS - set(press["slugs"])), "bad_credit": press["bad"]})
        gate(f"{L} no broken images", not [i for i in imgs if i["nat"] == 0], "ok")
        text = pg.evaluate("document.body.innerText")
        gate(f"{L} no 'official'/'oficial' claim", not re.search(r"\b(official|oficial)\b", text, re.I), "none")
        gate(f"{L} no em or en dashes in visible text", not re.search("[\u2014\u2013]", text), re.findall(".{12}[\u2014\u2013].{12}", text)[:3])
        gate(f"{L} merchant check note present", ("Always check with the merchant" in text) if lang == "en" else ("Confirma siempre con el comercio" in text), "ok")
        gate(f"{L} 117 places + 50+ claim + data date", ("117 places listed on BTC Map / OpenStreetMap, data of 2026-10-19" in text and "More than 50 merchants" in text) if lang == "en" else ("117 lugares registrados en BTC Map / OpenStreetMap, datos del 2026-10-19" in text and "Más de 50 comercios" in text), "ok")
        gate(f"{L} OSM/ODbL, BTC Map and Commons credits in footer", all(s in html for s in ("openstreetmap.org/copyright", "btcmap.org/community/lago-bitcoin", "Wikimedia Commons", "ODbL")), "ok")
        parity[lang] = pg.evaluate(PARITY_JS)
        PLACEHOLDERS.update(parity[lang]["placeholders"])

        # screenshots (fresh load so the first view is a real first view)
        pg.goto(url, wait_until="networkidle")
        pg.wait_for_timeout(1800)
        shot(pg, out / f"{lang}-1440-top.jpg")
        reveal_all(pg)
        if lang == "en":
            shot(pg, out / "en-1440-full.jpg", full=True)
        pg.evaluate("document.querySelector('#bitcoin').scrollIntoView()")
        pg.wait_for_timeout(900)
        shot(pg, out / f"{lang}-1440-merchants.jpg")
        if lang == "en":
            for sec in ("lake", "community", "tours"):
                pg.evaluate(f"document.querySelector('#{sec}').scrollIntoView()")
                pg.wait_for_timeout(700)
                shot(pg, out / f"en-1440-{sec}.jpg")
        run_axe(pg, f"{L} 1440")
        over_contrast(pg, f"{L} 1440")
        ctx.close()

        # ---- 390 ----
        ctx = browser.new_context(viewport={"width": 390, "height": 844}, locale="en-US" if lang == "en" else "es-GT", is_mobile=True, device_scale_factor=2)
        pg = ctx.new_page()
        merrs = []
        pg.on("console", lambda m, merrs=merrs: merrs.append(m.text) if m.type in ("error", "warning") else None)
        pg.on("pageerror", lambda e, merrs=merrs: merrs.append(str(e)))
        pg.goto(url, wait_until="networkidle")
        pg.wait_for_timeout(1500)
        shot(pg, out / f"{lang}-390-top.jpg")
        reveal_all(pg, 500)
        ov = pg.evaluate(OVERFLOW_JS)
        gate(f"{L} no horizontal overflow at 390", ov["sw"] <= ov["cw"], ov)
        leak = pg.evaluate(LEAK_JS)
        gate(f"{L} no text leaves the screen at 390", not leak, leak)
        gate(f"{L} no console errors at 390", not merrs, merrs[:4])
        hdr = pg.evaluate("""() => { const brand = document.querySelector('.brand'), cta = document.querySelector('.nav-cta'), m = document.querySelector('.menu-btn');
            const a = brand.getBoundingClientRect();
            const hit = (b) => { if (!b) return false; const r = b.getBoundingClientRect(); return r.width && a.right > r.left + 1 && a.left < r.right && a.bottom > r.top && a.top < r.bottom; };
            return {brandRight: Math.round(a.right), overlapCta: hit(cta), overlapMenu: hit(m)}; }""")
        gate(f"{L} brand does not overlap its CTA or menu button at 390", not hdr["overlapCta"] and not hdr["overlapMenu"], hdr)
        gate(f"{L} {EXPECT} markers at 390", pg.evaluate("document.querySelectorAll('#map path.leaflet-interactive').length") == EXPECT, "ok")
        menu = pg.locator(".menu-btn")
        if menu.count():
            menu.click()
            pg.wait_for_timeout(350)
            opened = pg.evaluate("document.getElementById('nav').classList.contains('open') && document.querySelector('.menu-btn').getAttribute('aria-expanded') === 'true'")
            gate(f"{L} mobile menu opens", opened, opened)
            shot(pg, out / f"{lang}-390-menu.jpg")
        else:
            section_map = pg.evaluate("() => document.querySelectorAll('#nav .guide-nodes .node a[href^=\"#\"]').length === 7")
            gate(f"{L} mobile section map has seven links", section_map, section_map)
            shot(pg, out / f"{lang}-390-section-map.jpg")
        pg.click('.nav a[href="#bitcoin"]')
        pg.wait_for_timeout(1200)
        top = pg.evaluate("Math.round(document.querySelector('#bitcoin').getBoundingClientRect().top)")
        gate(f"{L} navigation link scrolls to the merchants section", -20 < top < 300, top)
        shot(pg, out / f"{lang}-390-merchants.jpg")
        if lang == "en":
            run_axe(pg, f"{L} 390")
            over_contrast(pg, f"{L} 390")
        ctx.close()

    pe, ps = parity["en"], parity["es"]
    gate(f"[{vid}] EN/ES parity: same section ids in same order", pe["sections"] == ps["sections"] and len(pe["sections"]) == 9, pe["sections"])
    gate(f"[{vid}] EN/ES parity: placeholders, nav targets, h2 and image counts", pe["placeholders"] == ps["placeholders"] and pe["navTargets"] == ps["navTargets"] and pe["h2"] == ps["h2"] and pe["imgs"] == ps["imgs"],
         {"placeholders": sorted(set(pe["placeholders"])), "h2": pe["h2"], "imgs": pe["imgs"], "nav": pe["navTargets"]})
    ids_en = set(re.findall(r'id="([^"]+)"', page_html["en"]))
    gate(f"[{vid}] every nav link targets an existing section", all(t.lstrip("#") in ids_en for t in pe["navTargets"]), pe["navTargets"])
    need = {"hero", "lake", "bitcoin", "transport", "community", "tours", "expats", "about", "map", "cards", "atm", "finder"}
    gate(f"[{vid}] no section dropped (map, merchants, community, tours, expats, boat/tuk tuk, ATM, history)", need <= ids_en, sorted(need - ids_en))

    # language switch + browser default, once per variant
    ctx = browser.new_context(viewport={"width": 1440, "height": 900}, locale="es-GT")
    pg = ctx.new_page()
    pg.goto(f"{BASE}", wait_until="networkidle")
    gate(f"[{vid}] browser language es: opening EN redirects to /es/", pg.url.rstrip("/").endswith("/es"), pg.url)
    pg.click('.lang a[data-lang="en"]')
    pg.wait_for_load_state("networkidle")
    gate(f"[{vid}] EN switch opens the English root and stores the choice", pg.url.split("#")[0] == BASE and pg.evaluate("localStorage.getItem('lbc-lang')") == "en", pg.url)
    pg.click('.lang a[data-lang="es"]')
    pg.wait_for_load_state("networkidle")
    gate(f"[{vid}] ES switch opens /es/", pg.url.split("#")[0] == BASE + "es/", pg.url)
    ctx.close()
    ctx = browser.new_context(viewport={"width": 1440, "height": 900}, locale="en-US")
    pg = ctx.new_page()
    pg.goto(f"{BASE}es/", wait_until="networkidle")
    gate(f"[{vid}] browser language en: opening /es/ redirects to EN", not pg.url.rstrip("/").endswith("/es"), pg.url)
    placeholder_link = pg.locator('[data-config-link][data-placeholder]:visible').first
    if placeholder_link.count():
        placeholder_link.click()
        pg.wait_for_timeout(300)
    gate(f"[{vid}] configurable placeholder link shows 'coming soon' toast", bool(placeholder_link.count()) and pg.evaluate("document.getElementById('toast').classList.contains('show')"), "toast")
    badge = pg.evaluate("getComputedStyle(document.querySelector('[data-placeholder]'), '::after').content")
    gate(f"[{vid}] placeholder badge visible in preview", "Placeholder" in badge, badge)
    ctx.close()


def old_addresses(browser):
    """Old preview links (/v/, /v/ad/, /variants/) now send visitors to the site."""
    for rel, want in (("v/", BASE), ("v/ad/", BASE), ("v/ad/es/", BASE + "es/"), ("variants/", BASE), ("variants/es/", BASE + "es/")):
        ctx = browser.new_context(viewport={"width": 1440, "height": 900}, locale="es-GT" if want.endswith("es/") else "en-US")
        pg = ctx.new_page()
        pg.goto(BASE + rel, wait_until="networkidle")
        gate(f"old address /{rel} redirects to the site", pg.url.split("#")[0] == want, pg.url)
        ctx.close()


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        st, rb = fetch(BASE + "robots.txt")
        gate("robots.txt Disallow while private", st == 200 and b"Disallow: /" in rb, st)
        for vid in IDS:
            variant(browser, vid)
        old_addresses(browser)
        browser.close()
    handoff = (ROOT / "HANDOFF.md").read_text(encoding="utf-8")
    missing = [n for n in sorted(PLACEHOLDERS) if f"`{n}`" not in handoff]
    gate("every data-placeholder is listed in HANDOFF.md", not missing, {"placeholders": sorted(PLACEHOLDERS), "missing": missing})
    summary = {"base": BASE, "variants": IDS, "pass": sum(r["result"] == "PASS" for r in results), "fail": sum(r["result"] == "FAIL" for r in results), "gates": results}
    tag = LABEL
    (ROOT / "qa" / f"report-site-{tag}.json").write_text(json.dumps(summary, indent=1, ensure_ascii=False), encoding="utf-8")
    md = [f"# Site QA report ({tag})", "", f"Base URL: {BASE}", f"Variants: {', '.join(IDS)}", f"PASS {summary['pass']} / FAIL {summary['fail']}", "", "| Result | Gate | Evidence |", "|---|---|---|"]
    for r in results:
        ev = json.dumps(r["evidence"], ensure_ascii=False)
        md.append(f"| {r['result']} | {r['gate']} | {ev[:220].replace('|', '/')} |")
    (ROOT / "qa" / f"report-site-{tag}.md").write_text("\n".join(md), encoding="utf-8")
    print(f"\nSUMMARY pass={summary['pass']} fail={summary['fail']}")
    sys.exit(1 if summary["fail"] else 0)


if __name__ == "__main__":
    main()
