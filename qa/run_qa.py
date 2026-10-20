#!/usr/bin/env python3
"""Full QA run for the Lago Bitcoin Community site. Works against a local server or the live URL.

USAGE
  python qa/run_qa.py http://127.0.0.1:18431/ qa/screenshots            (local)
  python qa/run_qa.py https://itstomekk.github.io/lago-bitcoin-community/ qa/screenshots/live

WRITES
  <screenshot dir>/*.png      screenshots (1440 and 390, EN and ES, plus filter and menu states)
  qa/report-<label>.json      every gate with PASS/FAIL and the measured evidence
  qa/report-<label>.md        the same, readable

Gates (from BUILD-BRIEF.md): HTTP 200; title + description EN/ES; noindex,nofollow; no console
errors; no horizontal overflow at 1440 and 390; map shows 117 markers; list == markers == 117;
filter and search work; images have alt + credit; EN/ES parity; page weight under 3 MB;
language switcher and default-by-browser-language; placeholders listed in HANDOFF.md;
no "official" claim, no em dashes; contrast and ARIA check with axe-core.
External-link resolution is checked by qa/check_links.py (run separately, local only).
"""
import json
import re
import sys
import urllib.request
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
BASE = sys.argv[1].rstrip("/") + "/"
SHOTS = ROOT / sys.argv[2] if not Path(sys.argv[2]).is_absolute() else Path(sys.argv[2])
LABEL = "live" if BASE.startswith("https://") else "local"
SHOTS.mkdir(parents=True, exist_ok=True)
AXE = Path(sys.argv[3]).read_text(encoding="utf-8") if len(sys.argv) > 3 else None

results = []


def gate(name, ok, evidence):
    results.append({"gate": name, "result": "PASS" if ok else "FAIL", "evidence": evidence})
    print(("PASS " if ok else "FAIL ") + name + " :: " + str(evidence)[:300])


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "lbc-qa"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        return e.code, b""


OVERFLOW_JS = "({sw: document.documentElement.scrollWidth, cw: document.documentElement.clientWidth})"
PARITY_JS = """() => ({
  sections: [...document.querySelectorAll('main section[id]')].map(s => s.id),
  placeholders: [...document.querySelectorAll('[data-placeholder]')].map(e => e.dataset.placeholder),
  navTargets: [...document.querySelectorAll('.nav a')].map(a => a.getAttribute('href')),
  cards: document.querySelectorAll('#cards .card').length,
  h2: document.querySelectorAll('h2').length,
  imgs: document.querySelectorAll('img').length
})"""
IMG_JS = """() => [...document.querySelectorAll('img')].filter(i => !i.closest('.leaflet-container')).map(i => ({
  src: i.currentSrc.split('/').slice(-2).join('/'), alt: i.getAttribute('alt'), nat: i.naturalWidth,
  inFigure: !!i.closest('figure'), credit: !!(i.closest('figure') && i.closest('figure').querySelector('.credit a[href*="commons.wikimedia.org"]') && i.closest('figure').querySelector('.credit a[href*="creativecommons.org"]'))
}))"""
TEXT_JS = "() => document.body.innerText"


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch()

        # ---- 1. HTTP, head metadata, robots ----
        pages = {}
        for lang, path in (("en", ""), ("es", "es/")):
            st, body = fetch(BASE + path)
            html = body.decode("utf-8", "replace")
            pages[lang] = html
            gate(f"HTTP 200 {BASE + path}", st == 200, st)
            title = re.search(r"<title>(.*?)</title>", html, re.S)
            desc = re.search(r'<meta name="description" content="([^"]*)"', html)
            gate(f"[{lang}] title + meta description", bool(title and desc and 20 < len(title.group(1)) < 80 and 80 < len(desc.group(1)) <= 200),
                 {"title": title and title.group(1), "title_len": title and len(title.group(1)), "desc_len": desc and len(desc.group(1))})
            gate(f"[{lang}] meta robots noindex,nofollow", '<meta name="robots" content="noindex,nofollow">' in html, "present" if '<meta name="robots" content="noindex,nofollow">' in html else "missing")
            hl = re.findall(r'<link rel="alternate" hreflang="([^"]+)" href="([^"]+)"', html)
            gate(f"[{lang}] hreflang alternates en/es/x-default", {h for h, _ in hl} == {"en", "es", "x-default"}, hl)
            gate(f"[{lang}] html lang attribute", f'<html lang="{lang}">' in html, lang)
        st, rb = fetch(BASE + "robots.txt")
        gate("robots.txt Disallow while private", st == 200 and b"Disallow: /" in rb, st)
        for asset in ("style.css", "script.js", "config.js", "icons.svg", "favicon.svg", "data/merchants.json",
                      "vendor/leaflet/leaflet.js", "vendor/leaflet/leaflet.css", "fonts/geist-latin-wght-normal.woff2"):
            st, _ = fetch(BASE + asset)
            gate(f"asset 200 {asset}", st == 200, st)

        # ---- 2. per-language browser checks ----
        parity = {}
        for lang, path in (("en", ""), ("es", "es/")):
            ctx = browser.new_context(viewport={"width": 1440, "height": 900}, locale="en-US" if lang == "en" else "es-GT")
            pg = ctx.new_page()
            errs, failed, weight = [], [], {"bytes": 0, "tiles": 0}

            def on_resp(r, weight=weight):
                try:
                    n = len(r.body())
                except Exception:
                    return
                if "tile.openstreetmap.org" in r.url:
                    weight["tiles"] += n
                else:
                    weight["bytes"] += n
            pg.on("response", on_resp)
            pg.on("console", lambda m, errs=errs: errs.append(m.text) if m.type in ("error", "warning") else None)
            pg.on("pageerror", lambda e, errs=errs: errs.append(str(e)))
            pg.on("requestfailed", lambda r, failed=failed: failed.append(r.url))
            # Visiting the other language first would redirect; the locale above matches each page, so no redirect.
            pg.goto(BASE + path, wait_until="networkidle")
            pg.wait_for_timeout(1500)
            # reveal everything for full-page screenshots and weight (lazy images)
            h = pg.evaluate("document.documentElement.scrollHeight")
            y = 0
            while y < h:
                pg.evaluate(f"window.scrollTo(0,{y})")
                pg.wait_for_timeout(120)
                y += 700
            pg.evaluate("window.scrollTo(0,0)")
            pg.wait_for_timeout(800)
            pg.wait_for_load_state("networkidle")
            gate(f"[{lang}] no console errors/warnings, no failed requests", not errs and not failed, {"console": errs[:5], "failed": failed[:5]})
            gate(f"[{lang}] page weight under 3 MB excluding map tiles", weight["bytes"] < 3 * 1024 * 1024,
                 f'{weight["bytes"] / 1024:.0f} KB (tiles excluded: {weight["tiles"] / 1024:.0f} KB)')

            ov = pg.evaluate(OVERFLOW_JS)
            gate(f"[{lang}] no horizontal overflow at 1440", ov["sw"] <= ov["cw"], ov)

            # map + list
            st = pg.evaluate("document.getElementById('map').dataset.state")
            paths = pg.evaluate("document.querySelectorAll('#map path.leaflet-interactive').length")
            cards = pg.evaluate("document.querySelectorAll('#cards .card').length")
            hooks = pg.evaluate("({m: LBC_STATE.markers(), c: LBC_STATE.cards(), v: LBC_STATE.visibleCards(), p: LBC_STATE.places()})")
            tiles_ok = pg.evaluate("document.querySelectorAll('#map .leaflet-tile-loaded').length")
            gate(f"[{lang}] map ready and renders 117 markers (SVG paths in DOM)", st == "ready" and paths == 117 and tiles_ok > 0, {"state": st, "svg_markers": paths, "tiles_loaded": tiles_ok})
            gate(f"[{lang}] list count == marker count == 117", cards == paths == hooks["m"] == hooks["p"] == 117, {"cards": cards, "markers": paths, "hook": hooks})
            gate(f"[{lang}] count text", "117" in pg.inner_text("#count"), pg.inner_text("#count"))

            # filters
            pg.fill("#q", "coffee" if lang == "en" else "café")
            pg.wait_for_timeout(500)
            v1 = pg.evaluate("({c: LBC_STATE.visibleCards(), m: LBC_STATE.markers(), paths: document.querySelectorAll('#map path.leaflet-interactive').length})")
            gate(f"[{lang}] search filters list and map together", 0 < v1["c"] < 117 and v1["c"] == v1["m"] == v1["paths"], v1)
            pg.screenshot(path=str(SHOTS / f"{lang}-1440-filter-search.png"))
            pg.click("#reset")
            pg.wait_for_timeout(400)
            pg.click('.chip[data-group="stay"]')
            pg.wait_for_timeout(400)
            v2 = pg.evaluate("({c: LBC_STATE.visibleCards(), m: LBC_STATE.markers(), pressed: document.querySelector('.chip[aria-pressed=true]').dataset.group})")
            gate(f"[{lang}] category chip filters (stay)", 0 < v2["c"] < 117 and v2["c"] == v2["m"] and v2["pressed"] == "stay", v2)
            pg.click("#reset")
            pg.select_option("#town", "San Marcos La Laguna")
            pg.wait_for_timeout(400)
            v3 = pg.evaluate("({c: LBC_STATE.visibleCards(), m: LBC_STATE.markers()})")
            gate(f"[{lang}] village filter (San Marcos La Laguna)", v3["c"] == v3["m"] and 0 < v3["c"] < 117, v3)
            pg.fill("#q", "zzzzqq")
            pg.wait_for_timeout(400)
            v4 = pg.evaluate("({c: LBC_STATE.visibleCards(), m: LBC_STATE.markers(), empty: !!document.getElementById('empty')})")
            gate(f"[{lang}] empty state", v4["c"] == 0 and v4["m"] == 0 and v4["empty"], v4)
            pg.click("#reset")
            pg.wait_for_timeout(400)
            v5 = pg.evaluate("({c: LBC_STATE.visibleCards(), m: LBC_STATE.markers()})")
            gate(f"[{lang}] reset restores 117", v5 == {"c": 117, "m": 117}, v5)
            # "Show on map" from a ride row
            pg.click(".show-btn >> nth=0")
            pg.wait_for_timeout(900)
            pop = pg.evaluate("!!document.querySelector('.leaflet-popup')")
            gate(f"[{lang}] ride 'Show on map' opens a popup", pop, pop)

            # images
            imgs = pg.evaluate(IMG_JS)
            bad_alt = [i for i in imgs if i["alt"] is None or (i["alt"] == "" and "favicon" not in i["src"] and "logo" not in i["src"])]  # map tiles are excluded: Leaflet draws them as decorative images
            bad_credit = [i for i in imgs if "images/" in i["src"] and "logo" not in i["src"] and not i["credit"]]
            broken = [i for i in imgs if i["nat"] == 0]
            gate(f"[{lang}] every image has alt text", not bad_alt, {"images": len(imgs), "bad": bad_alt})
            gate(f"[{lang}] every photo has a credit line (Commons page + licence links)", not bad_credit, {"photos": sum(1 for i in imgs if 'images/' in i['src'] and 'logo' not in i['src']), "bad": bad_credit})
            gate(f"[{lang}] no broken images", not broken, broken)

            # text rules
            text = pg.evaluate(TEXT_JS)
            html = pages[lang]
            gate(f"[{lang}] no 'official'/'oficial' claim", not re.search(r"\b(official|oficial)\b", text, re.I), re.findall(r"\b(?:official|oficial)\b", text, re.I))
            gate(f"[{lang}] no em or en dashes in visible text", not re.search("[\u2014\u2013]", text), re.findall(".{15}[\u2014\u2013].{15}", text)[:3])
            gate(f"[{lang}] 'Always check with the merchant' note present", ("Always check with the merchant" in text) if lang == "en" else ("Confirma siempre con el comercio" in text), "ok")
            gate(f"[{lang}] 117 places + 50+ claim + data date", ("117 places listed on BTC Map / OpenStreetMap, data of 2026-10-19" in text and "More than 50 merchants" in text) if lang == "en" else ("117 lugares registrados en BTC Map / OpenStreetMap, datos del 2026-10-19" in text and "Más de 50 comercios" in text), "ok")
            gate(f"[{lang}] OSM/ODbL, BTC Map and Commons credits in footer", all(s in html for s in ("openstreetmap.org/copyright", "btcmap.org/community/lago-bitcoin", "Wikimedia Commons", "ODbL")), "ok")

            parity[lang] = pg.evaluate(PARITY_JS)
            if AXE:
                pg.evaluate(AXE)
                ax = pg.evaluate("axe.run(document, {runOnly:['wcag2a','wcag2aa'], resultTypes:['violations']}).then(r => r.violations.map(v => ({id: v.id, impact: v.impact, n: v.nodes.length, sample: v.nodes.slice(0,3).map(n => n.target.join(' ') + ' :: ' + (n.any[0] ? n.any[0].message : ''))})))")
                gate(f"[{lang}] axe-core WCAG A/AA violations (1440)", not ax, ax)

            # screenshots
            pg.screenshot(path=str(SHOTS / f"{lang}-1440-top.png"))
            pg.screenshot(path=str(SHOTS / f"{lang}-1440-full.png"), full_page=True)
            pg.evaluate("document.querySelector('#bitcoin').scrollIntoView()")
            pg.wait_for_timeout(700)
            pg.screenshot(path=str(SHOTS / f"{lang}-1440-merchants.png"))
            ctx.close()

            # mobile
            ctx = browser.new_context(viewport={"width": 390, "height": 844}, locale="en-US" if lang == "en" else "es-GT", is_mobile=True, device_scale_factor=2)
            pg = ctx.new_page()
            merrs = []
            pg.on("console", lambda m, merrs=merrs: merrs.append(m.text) if m.type in ("error", "warning") else None)
            pg.on("pageerror", lambda e, merrs=merrs: merrs.append(str(e)))
            pg.goto(BASE + path, wait_until="networkidle")
            pg.wait_for_timeout(1200)
            ov = pg.evaluate(OVERFLOW_JS)
            gate(f"[{lang}] no horizontal overflow at 390", ov["sw"] <= ov["cw"], ov)
            gate(f"[{lang}] no console errors at 390", not merrs, merrs[:5])
            paths390 = pg.evaluate("document.querySelectorAll('#map path.leaflet-interactive').length")
            gate(f"[{lang}] 117 markers at 390", paths390 == 117, paths390)
            pg.screenshot(path=str(SHOTS / f"{lang}-390-top.png"))
            pg.click(".menu-btn")
            pg.wait_for_timeout(300)
            menu_open = pg.evaluate("document.getElementById('nav').classList.contains('open') && document.querySelector('.menu-btn').getAttribute('aria-expanded') === 'true'")
            gate(f"[{lang}] mobile menu opens", menu_open, menu_open)
            pg.screenshot(path=str(SHOTS / f"{lang}-390-menu.png"))
            pg.click('.nav a[href="#bitcoin"]')
            pg.wait_for_timeout(900)
            pg.screenshot(path=str(SHOTS / f"{lang}-390-merchants.png"))
            h = pg.evaluate("document.documentElement.scrollHeight")
            y = 0
            while y < h:
                pg.evaluate(f"window.scrollTo(0,{y})")
                pg.wait_for_timeout(100)
                y += 600
            pg.evaluate("window.scrollTo(0,0)")
            pg.wait_for_timeout(600)
            pg.screenshot(path=str(SHOTS / f"{lang}-390-full.png"), full_page=True)
            ctx.close()

        # ---- 3. parity ----
        pe, ps = parity["en"], parity["es"]
        gate("EN/ES parity: same section ids in same order", pe["sections"] == ps["sections"], pe["sections"])
        gate("EN/ES parity: same placeholders, nav targets, h2 and image counts", pe["placeholders"] == ps["placeholders"] and pe["navTargets"] == ps["navTargets"] and pe["h2"] == ps["h2"] and pe["imgs"] == ps["imgs"], {"placeholders": sorted(set(pe["placeholders"])), "h2": pe["h2"], "imgs": pe["imgs"]})

        # ---- 4. language switcher + default by browser language ----
        ctx = browser.new_context(viewport={"width": 1440, "height": 900}, locale="es-GT")
        pg = ctx.new_page()
        pg.goto(BASE, wait_until="networkidle")
        gate("browser language es: opening / redirects to /es/", pg.url.rstrip("/").endswith("/es"), pg.url)
        pg.click('.lang a[data-lang="en"]')
        pg.wait_for_load_state("networkidle")
        stored = pg.evaluate("localStorage.getItem('lbc-lang')")
        gate("switcher EN: goes to English page and stores choice", (not pg.url.rstrip("/").endswith("/es")) and stored == "en", {"url": pg.url, "stored": stored})
        pg.goto(BASE, wait_until="networkidle")
        pg.reload(wait_until="networkidle")
        gate("stored choice (en) beats browser language (es) on reload", not pg.url.rstrip("/").endswith("/es") and pg.evaluate("document.documentElement.lang") == "en", pg.url)
        pg.click('.lang a[data-lang="es"]')
        pg.wait_for_load_state("networkidle")
        gate("switcher ES: goes to /es/ and stores choice", pg.url.rstrip("/").endswith("/es") and pg.evaluate("localStorage.getItem('lbc-lang')") == "es", pg.url)
        ctx.close()
        ctx = browser.new_context(viewport={"width": 1440, "height": 900}, locale="en-US")
        pg = ctx.new_page()
        pg.goto(BASE + "es/", wait_until="networkidle")
        gate("browser language en: opening /es/ redirects to /", not pg.url.rstrip("/").endswith("/es"), pg.url)
        # placeholder config wiring: with empty config, clicking a placeholder shows toast and does not navigate
        pg.click("#hero .btn-primary")
        pg.wait_for_timeout(300)
        toast = pg.evaluate("document.getElementById('toast').classList.contains('show')")
        gate("placeholder button shows 'coming soon' toast", toast, toast)
        badge = pg.evaluate("getComputedStyle(document.querySelector('[data-placeholder]'), '::after').content")
        gate("placeholder badge visible in preview", "Placeholder" in badge, badge)
        ctx.close()

        # ---- dark mode: contrast check and screenshot ----
        if AXE:
            for lang, path in (("en", ""), ("es", "es/")):
                ctx = browser.new_context(viewport={"width": 1440, "height": 900}, locale="en-US" if lang == "en" else "es-GT", color_scheme="dark")
                pg = ctx.new_page()
                pg.goto(BASE + path, wait_until="networkidle")
                pg.wait_for_timeout(1000)
                h = pg.evaluate("document.documentElement.scrollHeight")
                for y in range(0, h, 700):
                    pg.evaluate(f"window.scrollTo(0,{y})")
                    pg.wait_for_timeout(100)
                pg.evaluate("window.scrollTo(0,0)")
                pg.wait_for_timeout(700)
                pg.evaluate(AXE)
                ax = pg.evaluate("axe.run(document, {runOnly:['wcag2a','wcag2aa'], resultTypes:['violations']}).then(r => r.violations.map(v => ({id: v.id, n: v.nodes.length, sample: v.nodes.slice(0,3).map(n => n.target.join(' '))})))")
                gate(f"[{lang}] axe-core WCAG A/AA violations in dark mode", not ax, ax)
                pg.screenshot(path=str(SHOTS / f"{lang}-1440-dark-top.png"))
                ctx.close()

        browser.close()

    # ---- 5. HANDOFF lists every placeholder ----
    handoff = (ROOT / "HANDOFF.md").read_text(encoding="utf-8")
    names = sorted(set(parity["en"]["placeholders"]))
    missing = [n for n in names if f"`{n}`" not in handoff]
    gate("every data-placeholder is listed in HANDOFF.md", not missing, {"placeholders": names, "missing": missing})

    summary = {"base": BASE, "pass": sum(r["result"] == "PASS" for r in results), "fail": sum(r["result"] == "FAIL" for r in results), "gates": results}
    (ROOT / "qa" / f"report-{LABEL}.json").write_text(json.dumps(summary, indent=1, ensure_ascii=False), encoding="utf-8")
    md = [f"# QA report ({LABEL})", "", f"Base URL: {BASE}", f"PASS {summary['pass']} / FAIL {summary['fail']}", "", "| Result | Gate | Evidence |", "|---|---|---|"]
    for r in results:
        ev = json.dumps(r["evidence"], ensure_ascii=False)
        md.append(f"| {r['result']} | {r['gate']} | {ev[:240].replace('|', '/')} |")
    (ROOT / "qa" / f"report-{LABEL}.md").write_text("\n".join(md), encoding="utf-8")
    print(f"\nSUMMARY pass={summary['pass']} fail={summary['fail']}")
    sys.exit(1 if summary["fail"] else 0)


if __name__ == "__main__":
    main()
