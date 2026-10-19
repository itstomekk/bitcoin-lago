"""Check that every external link on the site (pages + merchant data) resolves.
Writes qa/links.json. Bot-blocking statuses (401/403/429/999) are recorded as 'blocked'
(the server answered, so the host exists) and listed separately so a human can see them.
Usage: python qa/check_links.py
"""
import json, re, sys, urllib.request, urllib.error, concurrent.futures as cf
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"

def collect():
    urls = {}
    for f in ("index.html", "es/index.html"):
        html = (ROOT / f).read_text(encoding="utf-8")
        for u in re.findall(r'href="(https?://[^"]+)"', html):
            urls.setdefault(u, set()).add(f)
    data = json.loads((ROOT / "data" / "merchants.json").read_text(encoding="utf-8"))["places"]
    for p in data:
        for k in ("website", "facebook"):
            if p.get(k):
                urls.setdefault(p[k], set()).add("data:" + (p["name"] or p["id"]))
        if p.get("instagram"):
            urls.setdefault("https://www.instagram.com/" + p["instagram"].lstrip("@") + "/", set()).add("data:" + p["name"])
    return urls

def check(u):
    last = None
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(u, method=method, headers={"User-Agent": UA, "Accept": "text/html,*/*"})
            with urllib.request.urlopen(req, timeout=25) as r:
                return {"url": u, "status": r.status, "final": r.geturl(), "result": "ok"}
        except urllib.error.HTTPError as e:
            blocked = e.code in (401, 403, 405, 429, 999) or (e.code == 400 and "facebook.com" in u)  # platforms that refuse non-browser clients
            last = {"url": u, "status": e.code, "final": u, "result": "blocked" if blocked and method == "GET" else "http-error"}
            if method == "HEAD" and e.code in (403, 405, 400, 404, 501, 999, 429):
                continue
            return last
        except Exception as e:
            last = {"url": u, "status": None, "final": u, "result": "error", "error": type(e).__name__ + ": " + str(e)[:120]}
            if method == "HEAD":
                continue
            return last
    return last

if __name__ == "__main__":
    urls = collect()
    with cf.ThreadPoolExecutor(8) as ex:
        res = list(ex.map(check, sorted(urls)))
    for r in res:
        r["where"] = sorted(urls[r["url"]])[:3]
    (ROOT / "qa" / "links.json").write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding="utf-8")
    from collections import Counter
    print(Counter(r["result"] for r in res), len(res), "links")
    for r in res:
        if r["result"] != "ok":
            print(r["result"], r["status"], r["url"], r.get("error", ""), r["where"])
