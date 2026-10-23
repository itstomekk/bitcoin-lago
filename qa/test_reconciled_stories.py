"""Regression checks for dated claims and plain-text topic links."""
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


def topic(slug):
    return json.loads((ROOT / 'tools/topics' / (slug + '.json')).read_text(encoding='utf-8'))


class ReconciledStoriesTest(unittest.TestCase):
    def test_merchant_intro_is_dated_and_sourced_not_live_audit(self):
        data = topic('merchants-over-time')
        for lang in ('en', 'es'):
            first = data['body_' + lang][0]
            self.assertTrue(first.get('src'), 'Opening figures need provenance next to them')
            self.assertIn('2026', first['p'])
            self.assertNotRegex(first['p'], r'Both are true|Las dos son ciertas|active today|activos hoy')

    def test_no_escaped_html_in_plain_text_body(self):
        for path in (ROOT / 'tools/topics').glob('*.json'):
            data = json.loads(path.read_text(encoding='utf-8'))
            for lang in ('en', 'es'):
                for block in data.get('body_' + lang, []):
                    self.assertNotRegex(block.get('p', ''), r'<a\b', str(path))

    def test_kaboom_opening_is_historical_and_latest_status_attributed(self):
        data = topic('kaboom-cooking-oil-generator')
        for lang in ('en', 'es'):
            first = data['body_' + lang][0]
            self.assertIn('2025', first['p'])
            self.assertTrue(any('f2Q1_bRi_Sc' in s.get('u', '') for s in first['src']))

    def test_walking_atm_is_not_a_current_service_offer(self):
        data = topic('how-bitcoin-lago-started')
        for lang in ('en', 'es'):
            block = next(b for b in data['body_' + lang] if 'walking ATM' in b.get('h', '') or 'cajero ambulante' in b.get('h', '').lower())
            self.assertTrue(any('visiting-lake-atitlan-with-bitcoin' in s.get('u', '') for s in block['src']))


if __name__ == '__main__':
    unittest.main(verbosity=2)
