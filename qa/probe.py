import sys, json
from playwright.sync_api import sync_playwright
JS = r"""
() => {
  const r = e => { const b = e.getBoundingClientRect(); return [Math.round(b.left),Math.round(b.top+scrollY),Math.round(b.width),Math.round(b.height)]; };
  const out = {};
  const h1 = document.querySelector('h1'); const lh = parseFloat(getComputedStyle(h1).lineHeight);
  out.h1 = {rect:r(h1), lines: Math.round(h1.getBoundingClientRect().height/lh), fs:getComputedStyle(h1).fontSize};
  out.ctas = [...document.querySelectorAll('.hero .btn')].map(b=>({t:b.innerText.replace(/\n/g,' | '), rect:r(b)}));
  out.heroPhoto = r(document.querySelector('.hero-photo'));
  out.navTop = [...document.querySelectorAll('.nav a')].map(a=>a.getBoundingClientRect().top|0);
  out.header = r(document.querySelector('.site-header'));
  out.wide = [...document.querySelectorAll('body *')].filter(e=>{const b=e.getBoundingClientRect(); return b.right>innerWidth+1 && b.width>0 && getComputedStyle(e).position!=='fixed' && !e.closest('.leaflet-container') && !e.closest('.nav') && !e.closest('.toast')}).slice(0,8).map(e=>e.tagName+'.'+e.className+' '+JSON.stringify(r(e)));
  out.imgs = [...document.images].map(i=>[i.currentSrc.split('/').slice(-2).join('/'), i.naturalWidth, i.complete]);
  out.fonts = [...document.fonts].map(f=>f.family+':'+f.status);
  out.docH = document.documentElement.scrollHeight;
  return out;
}
"""
url, w, h = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
with sync_playwright() as p:
    b = p.chromium.launch(); ctx = b.new_context(viewport={'width':w,'height':h}, locale='en-US'); pg = ctx.new_page()
    pg.goto(url, wait_until='networkidle'); pg.wait_for_timeout(1200)
    d = pg.evaluate(JS)
    print(json.dumps(d, indent=1))
    b.close()
