"""QA for /bitcoin.pdf, /bitcoin_es.pdf and the /whitepaper/ + /es/whitepaper/ reading pages.

USAGE  python qa/test_whitepaper.py http://127.0.0.1:18431/ <shots-dir>
Playwright Firefox. Prints SUMMARY fail=N. Fails while the paper text is still the TEXT PENDING placeholder.
The paper text itself is verbatim (it contains dashes); the dash rule applies only to the page chrome around it.
"""
import hashlib, re, sys, urllib.request
from pathlib import Path
from playwright.sync_api import sync_playwright

base = (sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:18431/").rstrip("/") + "/"
shots = Path(sys.argv[2] if len(sys.argv) > 2 else "qa/screenshots/whitepaper"); shots.mkdir(parents=True, exist_ok=True)
SHA = "b1674191a88ec5cdd733e4240a81803105dc412d6c6708d53ab94fc248f4f553"
fail = 0


def check(ok, msg):
    global fail
    print(("ok   " if ok else "FAIL ") + msg)
    if not ok:
        fail += 1


data = urllib.request.urlopen(base + "bitcoin.pdf").read()
check(hashlib.sha256(data).hexdigest() == SHA and len(data) == 184292, "bitcoin.pdf 184292 bytes, SHA-256 matches")
local = Path(__file__).resolve().parent.parent / "bitcoin.pdf"
check(local.is_file() and hashlib.sha256(local.read_bytes()).hexdigest() == SHA, "repo bitcoin.pdf SHA-256 matches")

SHA_ES = "9956fcc0adaece85a350276f5c3c0330e7196883a9a65f23407cce91a87cea2f"  # official bitcoin_es.pdf from bitcoin.org, as received
data = urllib.request.urlopen(base + "bitcoin_es.pdf").read()
check(hashlib.sha256(data).hexdigest() == SHA_ES, "bitcoin_es.pdf SHA-256 matches the official copy")

PAGES = [("whitepaper/", "en", "Thank you, Satoshi."), ("es/whitepaper/", "es", "Gracias, Satoshi.")]
with sync_playwright() as pw:
    br = pw.firefox.launch()
    for path, lang, thanks in PAGES:
        for tag, vw, vh in (("desk", 1440, 900), ("mob", 390, 844)):
            ctx = br.new_context(viewport={"width": vw, "height": vh}, locale="es-ES" if lang == "es" else "en-US")
            pg = ctx.new_page()
            errs = []
            pg.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
            r = pg.goto(base + path, wait_until="load")
            pg.wait_for_timeout(600)
            name = f"{path.strip('/').replace('/', '-')}-{tag}"
            P = f"{path} {tag}"
            check(r.status == 200, f"{P} 200")
            check(pg.evaluate("document.documentElement.lang") == lang, f"{P} html lang={lang}")
            check(pg.evaluate("document.querySelector('meta[name=robots]').content") == "noindex,nofollow", f"{P} noindex,nofollow")
            ov = pg.evaluate("Math.max(document.documentElement.scrollWidth, document.body.scrollWidth)")
            check(ov <= vw, f"{P} no horizontal overflow ({ov} <= {vw})")
            check(pg.evaluate("!!document.querySelector('script[data-goatcounter]')"), f"{P} GoatCounter present")
            txt = pg.evaluate("document.querySelector('#wp-text').innerText")
            check("TEXT PENDING" not in txt and len(txt) > 5000, f"{P} paper text present ({len(txt)} chars)")
            check(pg.evaluate("document.querySelectorAll('#wp-text h2').length") >= 1, f"{P} section headings")
            # measure: article column width, images fit and loaded (figures are lazy: scroll them in first)
            pg.evaluate("""async () => { for (const i of document.querySelectorAll('#wp-text img')) { i.scrollIntoView(); await new Promise(r => setTimeout(r, 120)); } }""")
            pg.wait_for_load_state("networkidle")
            pg.evaluate("scrollTo(0, 0)")
            m = pg.evaluate("""() => { const a = document.querySelector('#wp-text'); const w = a.getBoundingClientRect();
                const imgs = [...a.querySelectorAll('img')];
                return {w: w.width, left: w.left, right: w.right, imgs: imgs.length, bad: imgs.filter(i => !(i.complete && i.naturalWidth > 0) || i.getBoundingClientRect().right > w.right + 1 || i.getBoundingClientRect().left < w.left - 1).length,
                        fs: parseFloat(getComputedStyle(a).fontSize)}; }""")
            check(m["bad"] == 0, f"{P} {m['imgs']} figures loaded and inside the text column")
            check(m["right"] <= vw + 0.5 and m["left"] >= 0 and (vw > 700 or m["fs"] >= 16), f"{P} text column within viewport, font {m['fs']}px")
            # chrome: hero + footer bar copy has no dashes; Original PDF link near top
            chrome = pg.evaluate("document.querySelector('#hero').innerText + ' ' + document.querySelector('.wp-thanks').innerText")
            check(not re.search("[\u2013\u2014]", chrome), f"{P} no em/en dashes in page chrome")
            check(pg.evaluate("document.querySelector('#hero a[href$=\"bitcoin.pdf\"]') !== null"), f"{P} Original PDF link in hero")
            pg.screenshot(path=str(shots / f"{name}-top.png"))
            pg.evaluate("document.querySelector('.wp-thanks').scrollIntoView({block: 'end'})")
            pg.wait_for_timeout(300)
            box = pg.evaluate("(() => { const r = document.querySelector('.wp-thanks').getBoundingClientRect(); return [r.top, r.bottom, r.left, r.right]; })()")
            check(box[0] >= 0 and box[1] <= vh + 0.5 and box[2] >= 0 and box[3] <= vw + 0.5, f"{P} gratitude bar fully visible when scrolled to {box}")
            check(thanks in pg.evaluate("document.querySelector('.wp-thanks').innerText"), f"{P} has '{thanks}'")
            check(pg.evaluate("document.querySelector('.wp-thanks .hash').title") == "SHA-256 " + SHA, f"{P} full hash in title")
            pg.screenshot(path=str(shots / f"{name}-bar.png"))
            if tag == "desk":
                pg.screenshot(path=str(shots / f"{name}-full.png"), full_page=True)
                hrefs = pg.evaluate("[...document.querySelectorAll('#hero a, .wp-thanks a')].map(a => a.href)")
                for h in sorted(set(hrefs)):
                    try:
                        code = urllib.request.urlopen(h).status
                    except Exception as e:
                        code = str(e)
                    check(code == 200, f"{path} link {h} -> {code}")
            errs = [e for e in errs if "goatcounter" not in e.lower()]
            check(not errs, f"{P} no console errors {errs[:2]}")
            ctx.close()
    br.close()
print(f"SUMMARY fail={fail}")
sys.exit(1 if fail else 0)
