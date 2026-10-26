"""Kaqchikel (cak) page and switcher link.

Gate: the page and the KAQ switch exist only when every string has a Kaqchikel text, a translator name and a
review date are set in tools/kaq.json. Until then build() writes a DRAFT (English fills the blanks, red banner)
to source-archive/kaq-draft/, which is gitignored and never published, and the switch link is empty.
Kaqchikel text is never machine-made: it comes from a native speaker via the brief in the program anchor.
"""
import json
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "tools" / "kaq.json"
DRAFT_DIR = ROOT / "source-archive" / "kaq-draft"
BRIEF = Path("C:/Users/Lenovo/Hermes/projects/community/lago-bitcoin/content/kaqchikel-translation-brief.md")


def load():
    return json.loads(SRC.read_text(encoding="utf-8"))


def is_live(data=None):
    d = data or load()
    return bool(d["translator"].strip() and d["reviewed_on"].strip() and all(s["kaq"].strip() for s in d["strings"]))


def kaq_link(T, live=None):
    """Switcher entry for the other pages ('' while the page is not live)."""
    if not (is_live() if live is None else live):
        return ""
    return (f'\n    <a href="{T["p"]}kaq/" lang="cak" hreflang="cak" data-lang="cak" title="Kaqchikel">KAQ</a>')


PAGE = """<!doctype html>
<!-- GENERATED FILE by tools/kaq.py from tools/kaq.json. Do not edit by hand. -->
<html lang="cak" data-design="ad">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | Bitcoin Lago</title>
<meta name="description" content="{description}">
<meta name="robots" content="noindex,nofollow">
<meta name="theme-color" content="#1e2760">
<link rel="icon" href="{p}favicon.svg" type="image/svg+xml">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="en" href="{base}">
<link rel="alternate" hreflang="es" href="{base}es/">
<link rel="alternate" hreflang="cak" href="{canonical}">
<link rel="alternate" hreflang="x-default" href="{base}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Bitcoin Lago">
<meta property="og:title" content="{title} | Bitcoin Lago">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{base}images/og/home-en.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="preload" href="{p}fonts/bricolage-grotesque-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{p}v/base.css">
<link rel="stylesheet" href="{p}v/ad.css">
<style>.kaq-draft{{background:#b8341f;color:#fff;padding:.75rem 1rem;font:600 1rem/1.4 system-ui,sans-serif;text-align:center}}
.kaq ol{{padding-left:1.25rem}} .kaq li{{margin:.4rem 0}} .kaq .credit-t{{color:var(--muted);font-size:.9rem;margin-top:2rem}}</style>
</head>
<body class="v-ad" data-base="{p}" data-design="ad">
{banner}<header class="rail" id="top">
  <span class="rail-weave" aria-hidden="true"></span>
  <a class="brand" href="{p}" aria-label="Bitcoin Lago"><img src="{p}images/logo/lago-bitcoin-logo.png" alt="" width="540" height="370"><span class="brand-t">Bitcoin Lago</span></a>
  <div class="lang" role="group" aria-label="Language">
    <a href="{p}" lang="en" hreflang="en" title="English">EN</a>
    <a href="{p}es/" lang="es" hreflang="es" title="Español">ES</a>
    <a href="./" lang="cak" hreflang="cak" title="Kaqchikel" aria-current="true">KAQ</a>
  </div>
</header>
<main id="main" class="story blog kaq">
<section class="scr story-hero" id="hero" aria-labelledby="kaq-h1">
<h1 id="kaq-h1">{title}</h1>
<p class="lede">{lead}</p>
<h2>{how_h}</h2>
<ol><li>{step1}</li><li>{step2}</li><li>{step3}</li></ol>
<h2>{where_h}</h2>
<p>{where_p} <a href="{p}#bitcoin" lang="en">English</a> · <a href="{p}es/#bitcoin" lang="es">Español</a></p>
<h2>{full_h}</h2>
<p>{full_p} <a href="{p}" lang="en">English</a> · <a href="{p}es/" lang="es">Español</a></p>
{credit}
</section>
</main>
<footer class="site-footer"><div class="weave-band" aria-hidden="true"></div><div class="foot"><a class="foot-brand" href="{p}"><img src="{p}images/logo/lago-bitcoin-logo.png" alt="Bitcoin Lago" width="540" height="370"></a></div></footer>
</body>
</html>
"""


def render(data, base_url, p, draft):
    vals = {}
    for s in data["strings"]:
        txt = s["kaq"].strip() or s["en"]
        vals[s["key"]] = escape(txt, quote=True)
    credit = ""
    if not draft:
        credit = f'<p class="credit-t">{vals["credit"]}: {escape(data["translator"].strip())}</p>'
    banner = ('<div class="kaq-draft" role="note">DRAFT, NOT TRANSLATED YET. Blank Kaqchikel fields show the English source. Never publish.</div>\n'
              if draft else "")
    return PAGE.format(p=p, base=base_url, canonical=base_url + "kaq/", banner=banner, **{**vals, "credit": credit})


def build(site_url):
    """Returns the path written. Live page at kaq/index.html; otherwise the ignored draft."""
    data = load()
    if is_live(data):
        out = ROOT / "kaq" / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render(data, site_url, "../", False), encoding="utf-8")
        return out
    stale = ROOT / "kaq" / "index.html"
    if stale.exists():
        stale.unlink()
        try:
            stale.parent.rmdir()
        except OSError:
            pass
    DRAFT_DIR.mkdir(parents=True, exist_ok=True)
    out = DRAFT_DIR / "index.html"
    out.write_text(render(data, site_url, "../../", True), encoding="utf-8")
    write_brief(data)
    return out


def write_brief(data):
    rows = "\n".join(f"| {s['key']} | {s['en']} | {s['es']} | |" for s in data["strings"])
    BRIEF.parent.mkdir(parents=True, exist_ok=True)
    BRIEF.write_text(f"""# Kaqchikel page: translation brief

For a native Kaqchikel speaker (Panajachel / north shore variety is the target). Please fill the last column.
Short, plain, spoken-style text. Loanwords such as bitcoin, Lightning, wallet, QR can stay as they are if that is
what people actually say. Tell us if a line sounds wrong or unnatural in English or Spanish source.

We also need: your name as you want it credited (shown on the page as "Translation: name"), and the date you reviewed it.
Nothing goes live until every line is filled and reviewed.

| key | English | Español | Kaqchikel |
|---|---|---|---|
{rows}

How it goes live (Tomek / agent): put the texts in `tools/kaq.json` (field `kaq`), set `translator` and `reviewed_on`,
run `python tools/build_variants.py`. The KAQ switch appears on every page and `/kaq/` is built.
""", encoding="utf-8")
