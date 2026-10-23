"""Visitor-guide content contract. Run from the site root, before and after build."""
import json
from pathlib import Path
import re
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
SLUG = 'visiting-lake-atitlan-with-bitcoin'


class VisitorGuideTest(unittest.TestCase):
    def test_bilingual_sourced_practical_guide(self):
        path = ROOT / 'tools' / 'topics' / (SLUG + '.json')
        self.assertTrue(path.is_file(), 'A practical visitor guide has not been created yet')
        guide = json.loads(path.read_text(encoding='utf-8'))
        self.assertEqual(guide['slug'], SLUG)
        self.assertEqual(guide['kind'], 'topic')
        self.assertEqual(len(guide['body_en']), len(guide['body_es']))
        self.assertGreaterEqual(len(guide['open_questions']), 3)
        for en, es in zip(guide['body_en'], guide['body_es']):
            self.assertEqual(set(en), set(es), 'Translation must preserve block types')
            self.assertEqual([s['u'] for s in en.get('src', [])], [s['u'] for s in es.get('src', [])])
            if 'p' in en:
                self.assertTrue(en['p'] and es['p'])
                self.assertTrue(en.get('src'), 'Every advice or factual paragraph needs provenance')
        raw = path.read_text(encoding='utf-8')
        self.assertIsNone(re.search('[\u2013\u2014]', raw))
        self.assertIsNone(re.search(r'\b(?:official|oficial)\b', raw, re.I))
        en = ' '.join(b.get('p', '') for b in guide['body_en'])
        for concept in ('Lightning', 'quetzales', 'before ordering', 'not a current merchant audit', 'ATM', 'pending'):
            self.assertIn(concept, en)
        self.assertTrue(any('¿' in b.get('p', '') for b in guide['body_es']))
        self.assertEqual(guide['quotes'], [], 'Advice must not masquerade as verbatim video quotes')
        import seo
        self.assertIn(SLUG, seo.SHORT_TITLES)
        for lang, prefix in [('en', ''), ('es', 'es/')]:
            record = seo.records()[prefix + 'blog/' + SLUG + '/']
            self.assertEqual(record['lang'], lang)
            self.assertEqual(record['type'], 'WebPage')


if __name__ == '__main__':
    unittest.main(verbosity=2)
