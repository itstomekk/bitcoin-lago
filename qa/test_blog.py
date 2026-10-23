"""QA for the blog: python qa/test_blog.py <base url> <shot dir>
Every blog page (index + each article, EN and ES) at 1440 and 390: no console errors or failed requests,
images load with alt, no em/en dashes, no 'official', no overflow, language links resolve, and the
video facade turns into a youtube-nocookie iframe on click."""
import glob
import json
import os
import sys
import urllib.request

from playwright.sync_api import sync_playwright

base, out = sys.argv[1].rstrip("/") + "/", sys.argv[2]
os.makedirs(out, exist_ok=True)
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
slugs = [json.load(open(f, encoding="utf-8"))["slug"] for f in glob.glob(os.path.join(root, "tools", "blog", "*.json"))]
paths = ["blog/", "es/blog/"] + [f"blog/{s}/" for s in slugs] + [f"es/blog/{s}/" for s in slugs]
fails = 0


def gate(name, ok, info=""):
    global fails
    if not ok:
        print("FAIL " + name + (f" :: {info}" if info else ""))
    fails += 0 if ok else 1


with sync_playwright() as p:
    b = p.chromium.launch()
    for path in paths:
        for w in (1440, 390):
            pg = b.new_page(viewport={"width": w, "height": 900})
            errs, bad = [], []
            pg.on("console", lambda m: errs.append(m.text) if m.type in ("error", "warning") else None)
            pg.on("response", lambda r: bad.append(f"{r.status} {r.url}") if r.status >= 400 else None)
            pg.goto(base + path, wait_until="load")
            pg.evaluate("document.querySelectorAll('img[loading=lazy]').forEach(i => i.loading = 'eager')")
            pg.evaluate("document.querySelectorAll('.reveal').forEach(e => e.classList.add('in','is-visible','visible'))")
            pg.wait_for_timeout(1200)
            L = f"[{path} {w}]"
            info = pg.evaluate("""() => ({
              broken: [...document.querySelectorAll('img')].filter(i => !(i.complete && i.naturalWidth > 0)).map(i => i.currentSrc),
              noalt: [...document.querySelectorAll('img')].filter(i => i.getAttribute('alt') === null).length,
              dashes: (document.body.innerText.match(/[\\u2013\\u2014]/g) || []).length,
              official: /\\bofficial\\b/i.test(document.body.innerText),
              oldname: /Lago Bitcoin/.test(document.querySelector('header').innerText + document.title),
              overflow: document.documentElement.scrollWidth - window.innerWidth,
              h1: !!document.querySelector('h1'), langs: [...document.querySelectorAll('.lang a')].map(a => a.href),
              robots: document.querySelector('meta[name=robots]')?.content,
              play: !!document.querySelector('[data-youtube-play]') })""")
            gate(f"{L} no console errors", not errs, errs[:2])
            gate(f"{L} no failed requests", not bad, bad[:2])
            gate(f"{L} images load", not info["broken"], info["broken"][:2])
            gate(f"{L} images have alt", info["noalt"] == 0)
            gate(f"{L} no dashes", info["dashes"] == 0, info["dashes"])
            gate(f"{L} no 'official', name is Bitcoin Lago", not info["official"] and not info["oldname"])
            gate(f"{L} no overflow", info["overflow"] <= 1, info["overflow"])
            gate(f"{L} has h1 and noindex", info["h1"] and info["robots"] == "noindex,nofollow")
            if w == 1440:
                for u in info["langs"]:
                    try:
                        code = urllib.request.urlopen(u, timeout=20).status
                    except Exception as e:
                        code = str(e)
                    gate(f"{L} language link works {u}", code == 200, code)
                if info["play"]:
                    pg.click("[data-youtube-play]")
                    pg.wait_for_timeout(800)
                    src = pg.evaluate("document.querySelector('iframe')?.src || ''")
                    gate(f"{L} play loads youtube-nocookie iframe", "youtube-nocookie.com/embed/" in src, src)
            pg.screenshot(path=os.path.join(out, f"{path.strip('/').replace('/', '_') or 'root'}-{w}.jpg"), quality=70, full_page=True)
            pg.close()
    b.close()
print(f"pages {len(paths)}  SUMMARY fail={fails}")
