#!/usr/bin/env python3
"""Verify the AB23 video facade is idle until keyboard activation on every built page.

Usage: python qa/run_ab23_privacy.py [site-root-url]
Defaults to the local preview at http://127.0.0.1:18432/.
"""
from __future__ import annotations

import sys
from pathlib import Path
from urllib.parse import urljoin

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
BASE = (sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:18432/").rstrip("/") + "/"
ALL_DESIGNS = ["a", "c", "d", "ac", "ad", "cd", "f", "g", "h"]
FALLBACKS = {"ac", "ad", "cd"}
BUILT_DESIGNS = [d for d in ALL_DESIGNS if (ROOT / "tools" / "variants" / f"{d}.html").is_file() or d in FALLBACKS]
VIDEO_ID = "79cIKf_T3N0"


def page_path(design: str, lang: str) -> str:
    if design == "base":
        return "" if lang == "en" else "es/"
    return f"v/{design}/" if lang == "en" else f"v/{design}/es/"


def main() -> int:
    failures: list[str] = []
    cases = [(d, lang) for d in ["base", *BUILT_DESIGNS] for lang in ("en", "es")]
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        for design, lang in cases:
            label = f"{design}/{lang}"
            context = browser.new_context(locale="en-US" if lang == "en" else "es-GT")
            page = context.new_page()
            youtube_requests: list[str] = []
            page.on("request", lambda request: youtube_requests.append(request.url) if "youtube" in request.url.lower() else None)
            response = page.goto(urljoin(BASE, page_path(design, lang)), wait_until="domcontentloaded", timeout=60000)
            page.wait_for_selector("button[data-youtube-play]", state="visible", timeout=60000)
            before = page.evaluate("""() => {
              const b = document.querySelector('button[data-youtube-play]');
              const a = document.querySelector('.video-channel strong');
              return {
                lang: document.documentElement.lang,
                id: b?.getAttribute('data-youtube-play'),
                tag: b?.tagName,
                type: b?.getAttribute('type'),
                label: b?.getAttribute('aria-label'),
                title: b?.getAttribute('data-youtube-title'),
                poster: b?.querySelector('img')?.getAttribute('src'),
                channel: a?.textContent.trim(),
                iframeCount: document.querySelectorAll('iframe').length
              };
            }""")
            idle = response is not None and response.status == 200 and before["lang"] == lang and before["id"] == VIDEO_ID and before["tag"] == "BUTTON" and before["type"] == "button" and bool(before["label"]) and bool(before["title"]) and bool(before["poster"]) and before["channel"] == "Adopting Bitcoin" and before["iframeCount"] == 0 and not youtube_requests
            page.locator("button[data-youtube-play]").focus()
            page.keyboard.press("Enter")
            try:
                page.wait_for_function("() => { const f = document.querySelector('[data-youtube-facade] iframe'); return !!f && f.src.includes('youtube-nocookie.com/embed/'); }", timeout=8000)
            except Exception:
                pass
            after = page.evaluate("""() => {
              const f = document.querySelector('[data-youtube-facade] iframe');
              return {src: f?.getAttribute('src') || '', title: f?.getAttribute('title') || '', facadeHasFrame: !!f};
            }""")
            activated = after["facadeHasFrame"] and f"youtube-nocookie.com/embed/{VIDEO_ID}" in after["src"] and after["title"] == before["title"]
            ok = idle and activated
            print(f"{'PASS' if ok else 'FAIL'} {label} :: idle_before_click={idle} keyboard_embed={activated} before={before} after={after}", flush=True)
            if not ok:
                failures.append(label)
            context.close()
        browser.close()
    print(f"\nAB23 privacy checks: {len(cases) - len(failures)}/{len(cases)} passed; {len(failures)} failure(s)")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
