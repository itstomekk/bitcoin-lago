"""Element screenshots of the topic charts. Usage: python qa/shot_charts.py <base_url> <slug> <out_dir>"""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

base, slug, out = sys.argv[1].rstrip("/") + "/", sys.argv[2], Path(sys.argv[3])
out.mkdir(parents=True, exist_ok=True)
with sync_playwright() as p:
    br = p.chromium.launch()
    for lang, path in (("en", f"blog/{slug}/"), ("es", f"es/blog/{slug}/")):
        for w in (1440, 390):
            pg = br.new_page(viewport={"width": w, "height": 900}, locale="es-ES" if lang == "es" else "en-US")
            pg.goto(base + path, wait_until="networkidle")
            pg.add_style_tag(content=".reveal{opacity:1!important;transform:none!important}")
            for cid in ("chart-merchants", "chart-checks"):
                el = pg.query_selector(f"#{cid}")
                if el:
                    el.screenshot(path=str(out / f"{lang}-{w}-{cid}.png"))
            pg.screenshot(path=str(out / f"{lang}-{w}-full.jpg"), full_page=True, quality=60, type="jpeg")
            ow = pg.evaluate("document.documentElement.scrollWidth > window.innerWidth")
            print(lang, w, "overflow" if ow else "no-overflow")
            pg.close()
    br.close()
