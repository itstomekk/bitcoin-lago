"""QA for the story page: python qa/test_story.py <base url> <shot dir>
Checks EN and ES at 1440 and 390: no console errors, no failed requests, every image loads with alt,
every photo has a credit link, no em/en dashes, no horizontal overflow, language links work."""
import os
import sys

from playwright.sync_api import sync_playwright

base, out = sys.argv[1].rstrip("/") + "/", sys.argv[2]
os.makedirs(out, exist_ok=True)
fails = 0


def gate(name, ok, info=""):
    global fails
    print(("PASS " if ok else "FAIL ") + name + (f" :: {info}" if info else ""))
    fails += 0 if ok else 1


with sync_playwright() as p:
    b = p.chromium.launch()
    for path in ("story/", "es/story/"):
        for w in (1440, 390):
            pg = b.new_page(viewport={"width": w, "height": 900}, locale="es-ES" if path.startswith("es/") else "en-US")
            errs, bad = [], []
            pg.on("console", lambda m: errs.append(m.text) if m.type in ("error", "warning") and "goatcounter: not counting" not in m.text else None)
            pg.on("requestfailed", lambda r: bad.append(r.url))
            pg.on("response", lambda r: bad.append(f"{r.status} {r.url}") if r.status >= 400 else None)
            pg.goto(base + path, wait_until="load")
            pg.evaluate("document.querySelectorAll('img[loading=lazy]').forEach(i => i.loading = 'eager')")
            pg.evaluate("document.querySelectorAll('.reveal').forEach(e => e.classList.add('in','is-visible','visible'))")
            pg.evaluate("async () => { for (let y = 0; y < document.body.scrollHeight; y += 700) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 60)); } }")
            pg.wait_for_timeout(2500)
            L = f"[{path} {w}]"
            info = pg.evaluate("""() => ({
              imgs: [...document.querySelectorAll('img')].map(i => ({src: i.currentSrc, ok: i.complete && i.naturalWidth > 0, alt: i.getAttribute('alt')})),
              uncredited: [...document.querySelectorAll('figure.xph')].filter(f => !f.querySelector('a.credit[href*="x.com/JUN_AJPU_btc/status/"]')).length,
              photos: document.querySelectorAll('figure.xph').length,
              moments: document.querySelectorAll('.sy-list li').length,
              topics: document.querySelectorAll('.topic').length,
              dashes: (document.body.innerText.match(/[\\u2013\\u2014]/g) || []).length,
              overflow: document.documentElement.scrollWidth - window.innerWidth,
              official: /\\bofficial\\b/i.test(document.body.innerText),
              oldname: /Lago Bitcoin/.test(document.querySelector('header').innerText + document.title),
              h1: document.querySelector('h1')?.innerText,
              langs: [...document.querySelectorAll('.lang a')].map(a => a.href),
              robots: document.querySelector('meta[name=robots]')?.content,
            })""")
            broken = [i["src"] for i in info["imgs"] if not i["ok"]]
            noalt = [i["src"] for i in info["imgs"] if i["alt"] is None]
            gate(f"{L} no console errors or warnings", not errs, errs[:3])
            gate(f"{L} no failed requests", not bad, bad[:3])
            gate(f"{L} all images load", not broken, broken[:3])
            gate(f"{L} all images have alt", not noalt, noalt[:3])
            gate(f"{L} 40+ photos, each credited to its tweet", info["photos"] >= 40 and info["uncredited"] == 0, f'{info["photos"]} photos, {info["uncredited"]} uncredited')
            gate(f"{L} 46 moments and 30+ topics", info["moments"] == 46 and info["topics"] >= 30, f'{info["moments"]} / {info["topics"]}')
            gate(f"{L} no em or en dashes", info["dashes"] == 0, info["dashes"])
            gate(f"{L} no horizontal overflow", info["overflow"] <= 1, info["overflow"])
            gate(f"{L} never says official, header and title say Bitcoin Lago", not info["official"] and not info["oldname"])
            gate(f"{L} noindex", info["robots"] == "noindex,nofollow", info["robots"])
            gate(f"{L} language links point to story pages", all(u.rstrip("/").endswith("story") for u in info["langs"]), info["langs"])
            pg.evaluate("window.scrollTo(0, 0)")
            pg.screenshot(path=os.path.join(out, f"{path.replace('/', '_')}{w}-top.jpg"), quality=75)
            pg.screenshot(path=os.path.join(out, f"{path.replace('/', '_')}{w}-full.jpg"), quality=60, full_page=True)
            pg.close()
    b.close()
print(f"SUMMARY fail={fails}")
