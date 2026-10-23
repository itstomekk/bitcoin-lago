"""Offline SEO regression checks. Run after the site build, no dependencies beyond Pillow."""
import json
import sys
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlsplit
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://itstomekk.github.io/bitcoin-lago/'

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(); self.meta = {}; self.links = []; self.titles = []; self.ld = []; self.mode = ''; self.buf = ''; self.h1 = 0; self.in_head = False
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'head': self.in_head = True
        if tag == 'meta':
            self.meta.setdefault(a.get('property', a.get('name', '')), []).append(a.get('content', ''))
        if tag == 'link': self.links.append(a)
        if tag == 'h1': self.h1 += 1
        if tag == 'title' and self.in_head or (tag == 'script' and a.get('type') == 'application/ld+json'):
            self.mode = tag; self.buf = ''
    def handle_data(self, data):
        if self.mode: self.buf += data
    def handle_endtag(self, tag):
        if tag == 'head': self.in_head = False
        if tag == self.mode:
            if tag == 'title': self.titles.append(self.buf)
            else: self.ld.append(json.loads(self.buf))
            self.mode = ''; self.buf = ''


def pages():
    paths = ['index.html', 'es/index.html', 'story/index.html', 'es/story/index.html', 'blog/index.html', 'es/blog/index.html', 'faq/index.html', 'es/faq/index.html']
    for folder in ('blog', 'topics'):
        for f in sorted((ROOT / 'tools' / folder).glob('*.json')):
            a = json.loads(f.read_text(encoding='utf-8'))
            if 'slug' in a:
                paths.extend([f'blog/{a["slug"]}/index.html', f'es/blog/{a["slug"]}/index.html'])
    return sorted(paths)

class SEOTest(unittest.TestCase):
    def test_every_page(self):
        titles = []; descriptions = []; images = []
        for rel in pages():
            with self.subTest(page=rel):
                text = (ROOT / rel).read_text(encoding='utf-8'); p = Page(text)
                self.assertEqual(p.h1, 1)
                self.assertEqual(len(p.titles), 1)
                self.assertTrue(30 <= len(p.titles[0]) <= 70, p.titles)
                titles.extend(p.titles)
                required = ['description', 'robots', 'og:title', 'og:description', 'og:url', 'og:type', 'og:image', 'og:image:width', 'og:image:height', 'og:image:type', 'og:image:alt', 'og:locale', 'og:locale:alternate', 'twitter:card', 'twitter:title', 'twitter:description', 'twitter:image', 'twitter:image:alt']
                for key in required: self.assertEqual(len(p.meta.get(key, [])), 1, key)
                desc = p.meta['description'][0]; descriptions.append(desc)
                self.assertTrue(100 <= len(desc) <= 165, desc)
                self.assertEqual(p.meta['robots'], ['noindex,nofollow'])
                self.assertEqual(p.meta['twitter:card'], ['summary_large_image'])
                canon = [a['href'] for a in p.links if a.get('rel') == 'canonical']
                expected = BASE + rel.removesuffix('index.html')
                self.assertEqual(canon, [expected]); self.assertEqual(p.meta['og:url'], canon)
                alts = {a['hreflang']: a['href'] for a in p.links if a.get('rel') == 'alternate'}
                self.assertEqual(set(alts), {'en', 'es', 'x-default'})
                for alt in alts.values():
                    self.assertTrue(alt.startswith(BASE)); self.assertTrue((ROOT / alt[len(BASE):] / 'index.html').is_file(), alt)
                image = p.meta['og:image'][0]; images.append(image)
                self.assertTrue(image.startswith(BASE + 'images/og/'), image)
                self.assertEqual(p.meta['twitter:image'], [image])
                with Image.open(ROOT / image[len(BASE):]) as im:
                    self.assertEqual(im.size, (1200, 630)); self.assertEqual(im.format, 'JPEG')
                self.assertEqual(p.meta['og:image:width'], ['1200']); self.assertEqual(p.meta['og:image:height'], ['630'])
                nodes = [n for obj in p.ld for n in obj.get('@graph', [obj])]
                types = [n.get('@type') for n in nodes]
                self.assertIn('WebSite', types); self.assertTrue({'WebPage', 'CollectionPage', 'FAQPage'} & set(types))
                if '/blog/' in '/' + rel and rel.count('/') >= (3 if rel.startswith('es/') else 2):
                    self.assertIn('BlogPosting', types); self.assertEqual(p.meta['og:type'], ['article'])
                if rel not in ('index.html', 'es/index.html'): self.assertIn('BreadcrumbList', types)
                self.assertNotIn('{{', text)
        self.assertEqual(len(titles), len(set(titles)), 'duplicate titles')
        self.assertEqual(len(descriptions), len(set(descriptions)), 'duplicate descriptions')
        self.assertEqual(len(images), len(set(images)), 'every language/page needs its own card')

    def test_preview_gate(self):
        self.assertIn('Disallow: /', (ROOT / 'robots.txt').read_text())
        self.assertNotIn('Sitemap:', (ROOT / 'robots.txt').read_text())
        sitemap = ROOT / 'sitemap.xml'
        if sitemap.exists():
            import xml.etree.ElementTree as ET
            self.assertEqual(len(list(ET.parse(sitemap).getroot())), 0, 'noindex pages must not be advertised')

if __name__ == '__main__':
    print(f'Canonical pages under test: {len(pages())}', flush=True)
    unittest.main(verbosity=2)
