"""Start here contract: run before implementation and after each build."""
import copy
import json
from pathlib import Path
import re
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
import build_variants as build

SLUGS = ['visiting-lake-atitlan-with-bitcoin', 'wallets-at-the-lake',
         'how-bitcoin-lago-started', 'kaboom-cooking-oil-generator']


class ReadingPathTest(unittest.TestCase):
    def setUp(self):
        path = ROOT / 'tools/reading_path.json'
        self.assertTrue(path.is_file(), 'Visitor-first reading path is not implemented')
        self.data = json.loads(path.read_text(encoding='utf-8'))

    def test_four_ordered_links_before_full_archive_in_both_languages(self):
        topics = build.topic_articles()
        arts = build.blog_articles()
        for lang, title in [('en', 'Start here'), ('es', 'Empieza aquí')]:
            html = build.render_blog_index(lang, arts)
            self.assertIn('<h2 id="start-h">' + title + '</h2>', html)
            match = re.search(r'<ol class="blog-reading-path">(.*?)</ol>', html, re.S)
            self.assertIsNotNone(match, 'Reading order must have ordered-list semantics')
            hrefs = re.findall(r'href="([^"]+)"', match[1])
            self.assertEqual(hrefs, [slug + '/' for slug in SLUGS])
            for slug in SLUGS:
                self.assertTrue((ROOT / 'tools/topics' / (slug + '.json')).is_file())
            self.assertLess(html.index('id="start-h"'), html.index('id="tp-h"'))
            self.assertLess(html.index('id="tp-h"'), html.index('id="vd-h"'))
            self.assertEqual(html.count('class="blog-card topic-card reveal"'), len(topics))
            self.assertEqual(html.count('class="blog-card reveal"'), len(arts))
            self.assertIn('noindex,nofollow', html)
            for item in self.data['items']:
                self.assertIn(item['title_' + lang], match[1])
                self.assertIn(item['summary_' + lang], match[1])

    def test_unknown_destination_fails_instead_of_shipping_dead_link(self):
        data = copy.deepcopy(self.data)
        data['items'][0]['slug'] = 'this-article-does-not-exist'
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'reading_path.json'
            path.write_text(json.dumps(data), encoding='utf-8')
            with patch.object(build, 'READING_PATH_FILE', path):
                with self.assertRaisesRegex(ValueError, 'this-article-does-not-exist'):
                    build.render_reading_path('en')

    def test_editorial_labels_are_escaped(self):
        data = copy.deepcopy(self.data)
        data['items'][0]['title_en'] = '<script>do_not_run()</script>'
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'reading_path.json'
            path.write_text(json.dumps(data), encoding='utf-8')
            with patch.object(build, 'READING_PATH_FILE', path):
                rendered = build.render_reading_path('en')
                self.assertNotIn('<script>', rendered)
                self.assertIn('&lt;script&gt;do_not_run()&lt;/script&gt;', rendered)


if __name__ == '__main__':
    unittest.main(verbosity=2)
