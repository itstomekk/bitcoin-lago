import sys, json
from playwright.sync_api import sync_playwright
url = sys.argv[1]; out = sys.argv[2]; w = int(sys.argv[3]); h = int(sys.argv[4]) if len(sys.argv)>4 else 900
with sync_playwright() as p:
    b = p.chromium.launch()
    ctx = b.new_context(viewport={'width': w, 'height': h}, locale='en-US')
    pg = ctx.new_page()
    errs = []
    pg.on('console', lambda m: errs.append(('console', m.type, m.text)) if m.type in ('error','warning') else None)
    pg.on('pageerror', lambda e: errs.append(('pageerror', str(e))))
    pg.on('requestfailed', lambda r: errs.append(('reqfail', r.url, r.failure)))
    pg.goto(url, wait_until='networkidle')
    pg.wait_for_timeout(1500)
    print(pg.evaluate("({sw:document.documentElement.scrollWidth, cw:document.documentElement.clientWidth, st:document.getElementById('map').dataset.state, mk:window.LBC_STATE&&[LBC_STATE.markers(),LBC_STATE.cards()], paths:document.querySelectorAll('#map path.leaflet-interactive').length})"))
    pg.screenshot(path=out, full_page=False)
    print(errs[:10])
    b.close()
