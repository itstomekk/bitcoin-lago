#!/usr/bin/env python3
"""Check Hallmark variants at 320/375/414/768px and save bilingual screenshots."""
from __future__ import annotations

import functools
import http.server
import sys
import threading
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
WIDTHS = (320, 375, 414, 768)
LANGS = (("en", ""), ("es", "es/"))
VARIANTS = tuple(sys.argv[1].split(",")) if len(sys.argv) > 1 else ("f",)
SHOT_DIR = ROOT / "qa" / "screenshots"


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, _format: str, *_args: object) -> None:
        pass


class QuietServer(http.server.ThreadingHTTPServer):
    def handle_error(self, _request, _client_address) -> None:
        pass


def inspect_page(page) -> dict:
    return page.evaluate(
        """() => {
          const visible = e => {
            const r = e.getBoundingClientRect(), s = getComputedStyle(e);
            return r.width > 0 && r.height > 0 && s.display !== 'none' &&
              s.visibility !== 'hidden' && !e.closest('[hidden]');
          };
          const wrapped = [];
          document.querySelectorAll('button,.btn,.chip,.nav a,.topbar a,.lang a,.site-footer .foot-brand,.vsw a').forEach(e => {
            if (!visible(e)) return;
            const walker = document.createTreeWalker(e, NodeFilter.SHOW_TEXT);
            const tops = [];
            while (walker.nextNode()) {
              const node = walker.currentNode;
              if (!node.textContent.trim() || node.parentElement.closest('.sr-only,[aria-hidden="true"],svg')) continue;
              const range = document.createRange();
              range.selectNodeContents(node);
              tops.push(...[...range.getClientRects()].map(r => r.top));
            }
            const lines = [];
            tops.sort((a, b) => a - b).forEach(top => {
              if (!lines.length || top - lines[lines.length - 1] > 5) lines.push(top);
            });
            if (lines.length > 1 && (e.textContent || '').trim()) {
              wrapped.push({text: e.textContent.trim().replace(/\\s+/g, ' ').slice(0, 70),
                className: String(e.className || ''), href: e.getAttribute('href'), lines: lines.length});
            }
          });
          const overflow = [];
          document.querySelectorAll('body *').forEach(e => {
            if (!visible(e)) return;
            const r = e.getBoundingClientRect();
            if ((r.left < -1 || r.right > innerWidth + 1) &&
                !e.closest('.topbar-variants,.topbar-in,.vsw,.vsw-links,.cards,#map,.leaflet-container')) {
              overflow.push({tag: e.tagName, className: String(e.className || ''), text: (e.textContent || '').trim().replace(/\\s+/g, ' ').slice(0, 55), parents: [e.parentElement, e.parentElement?.parentElement, e.parentElement?.parentElement?.parentElement].filter(Boolean).map(p => ({tag: p.tagName, className: String(p.className || ''), left: Math.round(p.getBoundingClientRect().left), right: Math.round(p.getBoundingClientRect().right), grid: getComputedStyle(p).gridTemplateColumns})),
                left: Math.round(r.left), right: Math.round(r.right)});
            }
          });
          const hero = document.querySelector('.hero');
          const proof = hero && hero.querySelector('.hero-proof');
          const photo = proof && proof.querySelector('.hero-visual');
          const image = photo && photo.querySelector('img');
          const caption = photo && photo.querySelector('figcaption');
          const guide = document.querySelector('.guide-map');
          const guideLinks = guide ? [...guide.querySelectorAll('.guide-nodes .node a')] : [];
          const guideTargets = guideLinks.map(a => document.querySelector(a.getAttribute('href')));
          return {width: innerWidth, rootWidth: document.documentElement.clientWidth,
            documentWidth: document.documentElement.scrollWidth,
            cards: document.querySelectorAll('#cards .card').length,
            sections: [...document.querySelectorAll('main section[id]')].map(e => e.id),
            heroTrackCount: hero ? getComputedStyle(hero).gridTemplateColumns.split(/\\s+/).filter(Boolean).length : 0,
            heroProof: Boolean(photo && proof.querySelector('.hero-stats')),
            heroPhoto: Boolean(image && image.alt.trim() && image.currentSrc.includes('community-tuktuk-') && image.naturalWidth > 0 && caption && caption.querySelector('.credit')?.textContent.includes('Photo: community archive (source to confirm)')),
            heroLoading: Boolean(image && image.getAttribute('loading') === 'eager' && image.getAttribute('fetchpriority') === 'high'),
            heroDiagram: Boolean(guide && guide.querySelector('svg.diagram-lines') && guideLinks.length === 7 && guideLinks.every((a, i) => a.textContent.trim() && guideTargets[i] && a.getAttribute('href').startsWith('#'))),
            wrapped: wrapped.slice(0, 12), overflow: overflow.slice(0, 12)};
        }"""
    )


def main() -> int:
    handler = functools.partial(QuietHandler, directory=str(ROOT))
    server = None
    for port in range(18432, 18464):
        try:
            server = QuietServer(("127.0.0.1", port), handler)
            break
        except OSError:
            continue
    if server is None:
        raise OSError("No available safe local browser-test port in 18432–18463")
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    base = f"http://127.0.0.1:{server.server_address[1]}/"
    failures: list[str] = []
    SHOT_DIR.mkdir(parents=True, exist_ok=True)
    pages = 0
    passed = 0
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=True)
            for variant in VARIANTS:
                for lang, route in LANGS:
                    for width in WIDTHS:
                        page = browser.new_page(viewport={"width": width, "height": 900}, device_scale_factor=1)
                        page.add_init_script(f"localStorage.setItem('lbc-lang', '{lang}')")
                        errors: list[str] = []
                        page.on("pageerror", lambda error: errors.append(str(error)))
                        url = f"{base}v/{variant}/{route}"
                        response = page.goto(url, wait_until="domcontentloaded", timeout=60000)
                        if response is None or response.status != 200:
                            failures.append(f"{variant}-{lang}-{width}: HTTP {response.status if response else 'none'}")
                        if variant == "f":
                            page.wait_for_function("() => { const i = document.querySelector('.hero-visual img'); return i && i.complete && i.naturalWidth > 0; }", timeout=30000)
                        elif variant == "h":
                            page.wait_for_function("() => { const n = document.querySelector('.guide-map'); return n && n.querySelector('svg.diagram-lines') && n.querySelectorAll('.guide-nodes .node a').length === 7; }", timeout=30000)
                        page.wait_for_function("document.querySelectorAll('#cards .card').length >= 117", timeout=60000)
                        page.wait_for_function("() => [...document.querySelectorAll('.stats-main dd[data-count]')].every(e => e.textContent.trim() === e.dataset.count)", timeout=10000)
                        result = inspect_page(page)
                        shot = SHOT_DIR / variant / f"{variant}-{lang}-{width}.png"
                        shot.parent.mkdir(parents=True, exist_ok=True)
                        page.screenshot(path=str(shot), full_page=True, animations="disabled", timeout=60000)
                        if result["documentWidth"] > result["rootWidth"] + 1:
                            failures.append(f"{variant}-{lang}-{width}: horizontal document overflow {result['documentWidth']} > {result['rootWidth']}")
                        if result["wrapped"]:
                            failures.append(f"{variant}-{lang}-{width}: clickable text wrapped: {result['wrapped']}")
                        if result["overflow"]:
                            failures.append(f"{variant}-{lang}-{width}: off-screen visible elements: {result['overflow']}")
                        if variant == "f" and (not result["heroProof"] or not result["heroPhoto"] or not result["heroLoading"]):
                            failures.append(f"{variant}-{lang}-{width}: Split Studio hero needs the eager, accessible, credited tuk-tuk photo and supporting figures")
                        if variant == "h" and not result["heroDiagram"]:
                            failures.append(f"{variant}-{lang}-{width}: Grid hero needs the accessible seven-link section diagram")
                        if result["heroTrackCount"] != 1:
                            failures.append(f"{variant}-{lang}-{width}: mobile hero should use one track, got {result['heroTrackCount']}")
                        if result["cards"] != 117:
                            failures.append(f"{variant}-{lang}-{width}: expected 117 cards, got {result['cards']}")
                        if errors:
                            failures.append(f"{variant}-{lang}-{width}: page errors: {errors[:3]}")
                        pages += 1
                        passed += not any(f"{variant}-{lang}-{width}:" in failure for failure in failures)
                        print(f"{'FAIL' if any(f'{variant}-{lang}-{width}:' in x for x in failures) else 'PASS'} {variant} {lang.upper()} {width}px :: cards={result['cards']} root={result['rootWidth']} document={result['documentWidth']} clickable_wraps={len(result['wrapped'])} offscreen={len(result['overflow'])} page_errors={len(errors)} screenshot={shot.relative_to(ROOT)}", flush=True)
                        page.close()
            for lang, route in (LANGS if "f" in VARIANTS else ()):
                page = browser.new_page(viewport={"width": 1280, "height": 800}, device_scale_factor=1)
                page.add_init_script(f"localStorage.setItem('lbc-lang', '{lang}')")
                page.goto(f"{base}v/f/{route}", wait_until="domcontentloaded", timeout=60000)
                page.wait_for_function("() => { const i = document.querySelector('.hero-visual img'); return i && i.complete && i.naturalWidth > 0; }", timeout=30000)
                page.wait_for_function("document.querySelectorAll('#cards .card').length >= 117", timeout=60000)
                page.wait_for_function("() => [...document.querySelectorAll('.stats-main dd[data-count]')].every(e => e.textContent.trim() === e.dataset.count)", timeout=10000)
                fold = page.evaluate("""() => ({
              width: innerWidth, height: innerHeight,
              heroTrackCount: getComputedStyle(document.querySelector('.hero')).gridTemplateColumns.split(/\\s+/).filter(Boolean).length,
              regions: ['.hero', '.hero-visual', '.hero-stats', '.stats-main', '.stats-main .stats-lead', '.stats-main > div:nth-child(2)', '.stats-main > div:nth-child(3)', '.hero-copy', '.hero-copy h1', '.hero-copy .lede', '.hero-copy .cta-row'].map(s => {
                const e = document.querySelector(s), r = e.getBoundingClientRect();
                return {selector: s, top: Math.round(r.top), bottom: Math.round(r.bottom), text: (e.textContent || '').trim().replace(/\\s+/g, ' ').slice(0, 90)};
              }),
              essentials: ['.hero-visual', '.stats-main .stats-lead', '.stats-main > div:nth-child(2)', '.stats-main > div:nth-child(3)', '.hero-copy h1', '.hero-copy .lede', '.hero-copy .cta-row'].map(s => {
                const e = document.querySelector(s), r = e.getBoundingClientRect();
                return {selector: s, bottom: Math.round(r.bottom), visible: r.bottom <= innerHeight};
              }),
              splitPairs: [
                ['.hero-copy', '.hero-visual'],
                ['#lake .lake-photos', '#lake .lake-text'],
                ['#bitcoin .finder', '#bitcoin .btc-head'],
                ['#transport .transport-main', '#transport .atm'],
                ['#community .bento', '#community .community-head'],
                ['#tours .tours-text', '#tours .tours-photo'],
                ['#expats > .photo', '#expats .expats-inner'],
                ['#about .about-text', '#about .history-video']
              ].map(([leftSelector, rightSelector]) => {
                const left = document.querySelector(leftSelector), right = document.querySelector(rightSelector);
                if (!left || !right) return {leftSelector, rightSelector, missing: true};
                const a = left.getBoundingClientRect(), b = right.getBoundingClientRect();
                return {leftSelector, rightSelector, leftOfRight: a.left < b.left,
                  verticalOverlap: Math.round(Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top))};
              })
                })""")
                shot = SHOT_DIR / "f" / f"f-{lang}-1280x800.png"
                page.screenshot(path=str(shot), full_page=False, animations="disabled", timeout=60000)
                label = f"f-{lang}-1280x800"
                if fold["heroTrackCount"] != 2:
                    failures.append(f"{label}: Split Studio hero should use two desktop tracks, got {fold['heroTrackCount']}")
                if any(not item["visible"] for item in fold["essentials"]):
                    failures.append(f"{label}: hero essentials miss the first fold: {fold}")
                invalid_pairs = [pair for pair in fold["splitPairs"] if pair.get("missing") or not pair.get("leftOfRight") or pair.get("verticalOverlap", 0) < 50]
                if invalid_pairs:
                    failures.append(f"{label}: Split Studio content/proof pairs are not side-by-side as specified: {invalid_pairs}")
                pages += 1
                passed += not any(f"{label}:" in failure for failure in failures)
                print(f"{'PASS' if not any(f'{label}:' in failure for failure in failures) else 'FAIL'} f {lang.upper()} 1280x800 hero fold :: {fold} screenshot={shot.relative_to(ROOT)}", flush=True)
                page.close()
            for lang, route in (LANGS if "h" in VARIANTS else ()):
                page = browser.new_page(viewport={"width": 1280, "height": 800}, device_scale_factor=1)
                page.add_init_script(f"localStorage.setItem('lbc-lang', '{lang}')")
                page.goto(f"{base}v/h/{route}", wait_until="domcontentloaded", timeout=60000)
                page.wait_for_function("() => document.querySelectorAll('.guide-nodes .node a').length === 7")
                fold = page.evaluate("""() => {
                  const selectors = ['.hero-copy h1', '.hero-copy .lede', '.map-action a', '.guide-nodes .guide-core', ...[...document.querySelectorAll('.guide-nodes .node a')].map((_, i) => `.guide-nodes .node:nth-of-type(${i + 2}) a`)];
                  return {width: innerWidth, height: innerHeight, selectors: selectors.map(s => {
                    const e = document.querySelector(s), r = e?.getBoundingClientRect();
                    return {selector: s, found: Boolean(e), bottom: r ? Math.round(r.bottom) : null, visible: Boolean(r && r.bottom <= innerHeight)};
                  })};
                }""")
                shot = SHOT_DIR / "h" / f"h-{lang}-1280x800.png"
                shot.parent.mkdir(parents=True, exist_ok=True)
                page.screenshot(path=str(shot), full_page=False, animations="disabled", timeout=60000)
                label = f"h-{lang}-1280x800"
                if any(not item["found"] or not item["visible"] for item in fold["selectors"]):
                    failures.append(f"{label}: title, map CTA, or section nodes miss the first fold: {fold}")
                pages += 1
                passed += not any(f"{label}:" in failure for failure in failures)
                print(f"{'PASS' if not any(f'{label}:' in failure for failure in failures) else 'FAIL'} h {lang.upper()} 1280x800 map fold :: {fold} screenshot={shot.relative_to(ROOT)}", flush=True)
                page.close()
            browser.close()
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)
    print(f"\nMobile checks: {passed}/{pages} page checks passed; {len(failures)} failure(s)")
    for failure in failures:
        print(f"FAILURE {failure}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
