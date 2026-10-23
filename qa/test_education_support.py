"""Education/support page contract: approved contact, sourced history, no invented offers."""
import json
from pathlib import Path
import re
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
SLUG = 'learning-and-supporting-bitcoin-lago'


class EducationSupportTest(unittest.TestCase):
    def test_bilingual_sources_and_approved_contact(self):
        path = ROOT / 'tools/topics' / (SLUG + '.json')
        self.assertTrue(path.is_file(), 'Education/support page is not implemented')
        page = json.loads(path.read_text(encoding='utf-8'))
        self.assertEqual(page['kind'], 'topic')
        self.assertEqual(page['quotes'], [])
        self.assertEqual(len(page['body_en']), len(page['body_es']))
        self.assertGreaterEqual(len(page['open_questions']), 3)
        for en, es in zip(page['body_en'], page['body_es']):
            self.assertEqual(set(en), set(es))
            self.assertEqual([s['u'] for s in en.get('src', [])], [s['u'] for s in es.get('src', [])])
            if en.get('p'):
                self.assertTrue(en.get('src'))
                self.assertTrue(es['p'])
        for lang in ('en', 'es'):
            refs = [s['u'] for b in page['body_' + lang] for s in b.get('src', [])]
            self.assertIn('https://x.com/LakeBitcoin', refs)
            self.assertFalse(any(u.startswith(('https://wa.me/', 'https://chat.whatsapp.com/', 'mailto:', 'lightning:', 'bitcoin:')) for u in refs))
        raw = path.read_text(encoding='utf-8')
        self.assertNotRegex(raw, '[\u2013\u2014]')
        self.assertNotRegex(raw, r'\b(?:official|oficial)\b')
        self.assertNotRegex(raw, r'bc1[a-z0-9]{20,}')
        en = ' '.join(b.get('p', '') for b in page['body_en'])
        for phrase in ('2023', 'not a current class timetable', 'not a verified current vacancy', 'no verified donation address', '@LakeBitcoin'):
            self.assertIn(phrase, en)
        import seo
        self.assertIn(SLUG, seo.SHORT_TITLES)
        for lang, prefix in [('en', ''), ('es', 'es/')]:
            self.assertEqual(seo.records()[prefix + 'blog/' + SLUG + '/']['lang'], lang)


if __name__ == '__main__':
    unittest.main(verbosity=2)
