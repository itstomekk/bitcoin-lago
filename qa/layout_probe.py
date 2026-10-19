import sys, json
from playwright.sync_api import sync_playwright
url=sys.argv[1]; w=int(sys.argv[2]); scheme=sys.argv[3] if len(sys.argv)>3 else 'light'
axe=open("C:/Users/Lenovo/AppData/Local/Temp/axe.min.js",encoding='utf8').read()
JS="""() => {
 const R=e=>{const b=e.getBoundingClientRect();return [Math.round(b.left),Math.round(b.top+scrollY),Math.round(b.width),Math.round(b.height)]};
 const o={};
 for (const sel of ['.hero-photo','.pano','.lake-text','.mosaic .m1','.mosaic .m2','.mosaic .m3','.mosaic .m4','.stats','.filters','.chips','#map','#cards','.transport-main','.atm','.tile-wa','.tile-meet','.tile-school','.tile-follow','.tile-who','.tours-photo','.tours-text','.expats-inner','.about-grid > div:first-child','.press','.site-footer']) { const e=document.querySelector(sel); o[sel]=e?R(e):null; }
 o.chipsCount=document.querySelectorAll('.chip').length;
 o.chipRows=new Set([...document.querySelectorAll('.chip')].map(c=>c.getBoundingClientRect().top|0)).size;
 o.btnWrap=[...document.querySelectorAll('.btn')].filter(b=>{const lh=parseFloat(getComputedStyle(b).lineHeight)||20;return b.getBoundingClientRect().height>lh*2.9 && !b.dataset.placeholder}).map(b=>b.innerText);
 o.bg=getComputedStyle(document.body).backgroundColor;
 return o}"""
with sync_playwright() as p:
    b=p.chromium.launch(); ctx=b.new_context(viewport={'width':w,'height':900},color_scheme=scheme,locale='en-US'); pg=ctx.new_page()
    pg.goto(url,wait_until='networkidle'); pg.wait_for_timeout(1000)
    h=pg.evaluate("document.documentElement.scrollHeight")
    for y in range(0,h,700): pg.evaluate(f"scrollTo(0,{y})"); pg.wait_for_timeout(80)
    pg.evaluate("scrollTo(0,0)"); pg.wait_for_timeout(600)
    print(json.dumps(pg.evaluate(JS)))
    pg.evaluate(axe)
    print('axe', json.dumps(pg.evaluate("axe.run(document,{runOnly:['wcag2a','wcag2aa'],resultTypes:['violations']}).then(r=>r.violations.map(v=>({id:v.id,n:v.nodes.length,s:v.nodes.slice(0,4).map(n=>n.target.join(' ')+' :: '+(n.any[0]?n.any[0].message:''))})))")))
    pg.screenshot(path=f"qa/screenshots/{scheme}-{w}-full-probe.png",full_page=True)
    b.close()
