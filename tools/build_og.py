"""Render page-specific 1200x630 social cards with existing brand fonts and real imagery.
Run: C:/Python314/python.exe tools/build_og.py
No hosted generation API, no paid calls, no publishing.
"""
import argparse
import base64
import io
import json
from html import escape
from pathlib import Path
from PIL import Image, ImageOps, ImageDraw
from playwright.sync_api import sync_playwright
import seo

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'images/og'


def data_uri(path, mime):
    return 'data:'+mime+';base64,'+base64.b64encode(path.read_bytes()).decode()


def markup(a):
    font = data_uri(ROOT/'fonts/bricolage-grotesque-latin-wght-normal.woff2', 'font/woff2')
    sans = data_uri(ROOT/'fonts/geist-latin-wght-normal.woff2', 'font/woff2')
    photo = data_uri(ROOT/'images/hero-1600.jpg', 'image/jpeg')
    heading = a['heading']; size = 76 if len(heading)<34 else 62 if len(heading)<49 else 54
    sub = ('A bitcoin community on Lake Atitlán.' if a['lang']=='en' else 'Una comunidad bitcoin en el Lago de Atitlán.')
    return f'''<!doctype html><html lang="{a['lang']}"><head><meta charset="utf-8"><style>
@font-face{{font-family:Bricolage;src:url("{font}")}}@font-face{{font-family:Geist;src:url("{sans}")}}
*{{box-sizing:border-box}}body{{margin:0;width:1200px;height:630px;background:#F5EFDF;color:#1E2760;position:relative;overflow:hidden;font-family:Geist,sans-serif}}
.photo{{position:absolute;right:0;top:0;width:552px;height:594px;object-fit:cover;object-position:36% center}}
.left{{position:absolute;inset:0 auto 36px 0;width:648px;background:#F5EFDF;padding:46px 52px}}
.brand{{font-family:Bricolage;font-size:37px;font-weight:700;letter-spacing:-1.2px;display:flex;gap:14px;align-items:center}}
.coin{{width:46px;height:46px;background:#C04E32;color:#F5EFDF;font-family:Geist;font-size:32px;font-weight:700;text-align:center;line-height:46px}}
.label{{margin:40px 0 21px;font-size:14px;letter-spacing:1.8px;font-weight:650;color:#28736D}}
h1{{font-family:Bricolage;font-size:{size}px;font-weight:750;line-height:1.03;letter-spacing:-2.8px;margin:0;max-width:548px;text-wrap:balance}}
.sub{{font-size:20px;line-height:1.45;margin:23px 0 0;max-width:490px}}
.edge{{position:absolute;left:630px;top:0;width:18px;height:594px;background:repeating-linear-gradient(to bottom,#1E2760 0 28px,#C04E32 28px 42px,#E6AD38 42px 56px,#28736D 56px 84px)}}
.credit{{position:absolute;bottom:0;left:0;width:1200px;height:36px;background:#1E2760;color:#F5EFDF;font-size:12px;line-height:36px;padding:0 28px;display:flex;justify-content:space-between}}
</style></head><body><img class="photo" src="{photo}" alt=""><div class="left"><div class="brand"><span class="coin">₿</span>Bitcoin Lago</div><p class="label">{escape(a['label'])}</p><h1>{escape(heading)}</h1><p class="sub">{sub}</p></div><div class="edge"></div><div class="credit"><span>Photo: Vikulinkaaa / Wikimedia Commons · CC BY-SA 4.0 · cropped</span><span>{'ENGLISH' if a['lang']=='en' else 'ESPAÑOL'} · ATITLÁN</span></div></body></html>'''


def main():
    parser = argparse.ArgumentParser(); parser.add_argument('--only', nargs='*'); args = parser.parse_args()
    manifest = seo.write_manifest()
    items = [a for a in manifest['pages'].values() if not args.only or a['key'] in args.only]
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=True)
        page = browser.new_page(viewport={'width':1200, 'height':630}, device_scale_factor=1)
        for a in items:
            page.set_content(markup(a), wait_until='load')
            page.evaluate('document.fonts.ready')
            page.wait_for_function('Array.from(document.images).every(i => i.complete && i.naturalWidth > 0)')
            bounds = page.locator('h1').bounding_box()
            sub = page.locator('.sub').bounding_box()
            if bounds['y']+bounds['height'] > 438 or sub['y'] < bounds['y']+bounds['height']+14 or sub['y']+sub['height'] > 550:
                raise RuntimeError('Title/subtitle collision or clipping: '+a['path'])
            png = page.screenshot(type='png')
            image = Image.open(io.BytesIO(png)).convert('RGB')
            dest = ROOT/a['image']; image.save(dest, 'JPEG', quality=91, optimize=True, progressive=True)
            print('wrote', dest.relative_to(ROOT), dest.stat().st_size, flush=True)
        browser.close()
    if len(items)==len(manifest['pages']):
        thumb_w, thumb_h = 400, 210
        rows = (len(items)+2)//3
        sheet = Image.new('RGB', (1200, rows*(thumb_h+26)), '#ffffff')
        d = ImageDraw.Draw(sheet)
        for n,a in enumerate(items):
            x,y=(n%3)*thumb_w,(n//3)*(thumb_h+26)
            with Image.open(ROOT/a['image']) as im: sheet.paste(im.resize((thumb_w,thumb_h)),(x,y))
            d.text((x+8,y+thumb_h+5),f'{n+1}. {a["key"][:43]} ({a["lang"]})',fill='#1E2760')
        review = ROOT/'qa/og-contact-sheet.jpg'; sheet.save(review, quality=88)
    print('Rendered', len(items), 'cards', flush=True)

if __name__ == '__main__': main()
