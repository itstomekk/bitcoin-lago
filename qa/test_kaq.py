"""Kaqchikel gate tests (offline). Run: python qa/test_kaq.py"""
import copy, json, re, sys, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import kaq  # noqa: E402


def filled():
    d = kaq.load()
    d = copy.deepcopy(d)
    for s in d["strings"]:
        s["kaq"] = s["kaq"] or "x"
    d["translator"], d["reviewed_on"] = "T", "2026-01-01"
    return d


class KaqGate(unittest.TestCase):
    def test_gate_requires_text_translator_and_review(self):
        d = filled()
        self.assertTrue(kaq.is_live(d))
        for mutate in (lambda x: x["strings"][0].update(kaq=""), lambda x: x.update(translator=""), lambda x: x.update(reviewed_on="")):
            e = copy.deepcopy(d); mutate(e)
            self.assertFalse(kaq.is_live(e))

    def test_switch_link_only_when_live(self):
        T = {"p": "../../"}
        self.assertEqual(kaq.kaq_link(T, live=False), "")
        self.assertIn('href="../../kaq/"', kaq.kaq_link(T, live=True))

    def test_live_page_is_clean(self):
        html = kaq.render(filled(), "https://example.org/", "../", False)
        self.assertIn('<html lang="cak"', html)
        self.assertIn("noindex,nofollow", html)
        self.assertNotIn("DRAFT", html)
        self.assertNotIn("lbc-lang", html)  # no auto language redirect on this page
        self.assertIn('hreflang="cak"', html)

    def test_draft_never_published(self):
        data = kaq.load()
        if not kaq.is_live(data):
            self.assertFalse((ROOT / "kaq").exists(), "unreviewed page must not be in the published tree")
            for f in ROOT.rglob("index.html"):
                rel = f.relative_to(ROOT).parts
                if rel[0] in ("source-archive", "qa", "node_modules"):
                    continue
                self.assertNotIn('data-lang="cak"', f.read_text(encoding="utf-8"), f"switch leaked into {f}")
            draft = (kaq.DRAFT_DIR / "index.html").read_text(encoding="utf-8")
            self.assertIn("DRAFT", draft)


if __name__ == "__main__":
    unittest.main(verbosity=2)
