"""Browser acceptance for the visitor-first reading path; no external services required."""
import json
from pathlib import Path
import sys

from playwright.sync_api import sync_playwright

base = sys.argv[1].rstrip('/') + '/'
out = Path(sys.argv[2])
out.mkdir(parents=True, exist_ok=True)
rows = []
with sync_playwright() as p:
    browser = p.chromium.launch()
    for lang in ('en', 'es'):
        for width in (320, 390, 1440):
            page = browser.new_page(viewport={'width': width, 'height': 900}, locale='es-ES' if lang == 'es' else 'en-US')
            errors = []
            page.on('pageerror', lambda e: errors.append(str(e)))
            path = ('es/' if lang == 'es' else '') + 'blog/'
            response = page.goto(base + path, wait_until='networkidle')
            assert response.status == 200
            assert page.locator('html').get_attribute('lang') == lang
            nav = page.locator('nav[aria-labelledby="start-h"]')
            assert nav.is_visible()
            links = nav.locator('ol > li > a')
            assert links.count() == 4
            assert links.first.get_attribute('href') == 'visiting-lake-atitlan-with-bitcoin/'
            assert page.locator('#start-h').inner_text() == ('Start here' if lang == 'en' else 'Empieza aquí')
            assert page.evaluate('Math.max(document.documentElement.scrollWidth,document.body.scrollWidth) <= innerWidth + 1')
            assert nav.evaluate("e => getComputedStyle(e.querySelector('ol')).listStyleType") == 'decimal'
            targets = []
            for link in links.all():
                assert link.bounding_box()['height'] >= 44
                link.focus()
                assert link.evaluate('e => document.activeElement === e')
                url = link.evaluate('e => e.href')
                target = page.request.get(url)
                assert target.status == 200, url
                assert '<html lang="' + lang + '"' in target.text(), url
                targets.append(url)
            assert not errors, errors
            page.locator('body').click(position={'x': width - 10, 'y': 10})
            nav.screenshot(path=str(out / f'start-here-{lang}-{width}.png'))
            row = {'lang': lang, 'width': width, 'targets': targets,
                   'nav_height': nav.bounding_box()['height'], 'pass': True}
            rows.append(row)
            print('PASS', lang, width, 'navigation, order, target locale, 44px links, keyboard focus, no overflow/errors')
            page.close()
    browser.close()
(out / 'report.json').write_text(json.dumps(rows, indent=2), encoding='utf-8')
print('Reading-path browser acceptance: PASS')
