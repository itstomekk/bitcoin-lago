#!/usr/bin/env python3
"""Quick layout probe for one design variant (a developer aid, not a release gate; the gates are in run_qa_variants.py).

USAGE  python qa/variant_probe.py http://127.0.0.1:18431 a [en|es]
PRINTS per viewport (1440x900 and 390x844): console problems, page overflow, every section's height vs the screen,
       text elements that leave the screen, hero headline lines, smallest font used, image loading, map markers.
"""
import json
import sys

from playwright.sync_api import sync_playwright

BASE, VID = sys.argv[1].rstrip("/"), sys.argv[2]
LANG = sys.argv[3] if len(sys.argv) > 3 else "en"
URL = f"{BASE}/v/{VID}/" + ("" if LANG == "en" else "es/")

PROBE = """() => {
  const vw = innerWidth, vh = innerHeight;
  const out = {sw: document.documentElement.scrollWidth, cw: document.documentElement.clientWidth, sections: [], leaks: [], tiny: [], broken: []};
  document.querySelectorAll('main section[id]').forEach(s => { const r = s.getBoundingClientRect(); out.sections.push([s.id, Math.round(r.height), (r.height / vh).toFixed(2)]); });
  document.querySelectorAll('h1,h2,h3,p,a,button,li,dt,dd,label,input,select,figcaption').forEach(e => {
    if (e.closest('.sr-only,.skip,.leaflet-container,[aria-hidden=true]') || e.classList.contains('sr-only')) return;
    const r = e.getBoundingClientRect(); if (!r.width || !r.height) return;
    const cs = getComputedStyle(e); if (cs.visibility === 'hidden' || cs.opacity === '0') return;
    if (r.right > vw + 1 || r.left < -1) out.leaks.push((e.className || e.tagName) + ' ' + Math.round(r.left) + '..' + Math.round(r.right) + ' ' + (e.textContent || '').trim().slice(0, 30));
    const fs = parseFloat(cs.fontSize); if (fs < 11.5 && (e.textContent || '').trim()) out.tiny.push(fs + ' ' + (e.className || e.tagName) + ' ' + (e.textContent || '').trim().slice(0, 25));
  });
  document.querySelectorAll('img').forEach(i => { if (!i.closest('.leaflet-container') && (!i.complete || !i.naturalWidth)) out.broken.push(i.src.slice(-40)); });
  const h1 = document.querySelector('h1'); if (h1) { const lh = parseFloat(getComputedStyle(h1).lineHeight) || parseFloat(getComputedStyle(h1).fontSize) * 1.1; out.h1 = {lines: Math.round(h1.getBoundingClientRect().height / lh), px: getComputedStyle(h1).fontSize, bottom: Math.round(h1.getBoundingClientRect().bottom)}; }
  const hero = document.querySelector('#hero'); if (hero) { const b = hero.querySelector('.btn'); out.ctaBottom = b ? Math.round(b.getBoundingClientRect().bottom) : null; }
  const m = document.getElementById('map'); out.map = m ? m.dataset.state + ' paths=' + document.querySelectorAll('#map path.leaflet-interactive').length + ' h=' + Math.round(m.getBoundingClientRect().height) : null;
  out.cards = document.querySelectorAll('#cards .card').length;
  return out;
}"""

with sync_playwright() as p:
    b = p.chromium.launch()
    for name, vp, mobile in (("1440", {"width": 1440, "height": 900}, False), ("390", {"width": 390, "height": 844}, True)):
        ctx = b.new_context(viewport=vp, locale="en-US" if LANG == "en" else "es-GT", is_mobile=mobile)
        pg = ctx.new_page()
        errs = []
        pg.on("console", lambda m, errs=errs: errs.append(m.type + ': ' + m.text) if m.type in ("error", "warning") else None)
        pg.on("pageerror", lambda e, errs=errs: errs.append("pageerror: " + str(e)))
        pg.on("requestfailed", lambda r, errs=errs: errs.append("failed: " + r.url))
        pg.goto(URL, wait_until="networkidle")
        pg.wait_for_timeout(1200)
        h = pg.evaluate("document.documentElement.scrollHeight")
        for y in range(0, h, 500):
            pg.evaluate(f"window.scrollTo(0,{y})"); pg.wait_for_timeout(90)
        pg.evaluate("window.scrollTo(0,0)"); pg.wait_for_timeout(900)
        r = pg.evaluate(PROBE)
        print(f"== {VID} {LANG} {name}  page height {h}  console: {errs[:4]}")
        print(json.dumps(r, ensure_ascii=False)[:2600])
        ctx.close()
    b.close()
