"""Screenshot selected sections: python qa/shot_sections.py <url> <outdir> <css selector>..."""
import sys, os
from playwright.sync_api import sync_playwright

url, out, sels = sys.argv[1], sys.argv[2], sys.argv[3:]
os.makedirs(out, exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch()
    for w in (1440, 390):
        pg = b.new_page(viewport={"width": w, "height": 900})
        pg.goto(url, wait_until="load")
        pg.evaluate("document.querySelectorAll('.reveal').forEach(e=>e.classList.add('in','is-visible','visible'))")
        pg.evaluate("document.querySelectorAll('img[loading=lazy]').forEach(i=>i.loading='eager')")
        pg.wait_for_timeout(1500)
        for i, s in enumerate(sels):
            el = pg.locator(s).first
            el.scroll_into_view_if_needed()
            pg.wait_for_timeout(600)
            el.screenshot(path=os.path.join(out, f"{w}-{i}.jpg"), quality=80)
            print("ok", w, s)
    b.close()
