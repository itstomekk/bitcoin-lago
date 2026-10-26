# Development notes

Technical notes for the Bitcoin Lago site. The welcoming overview is in [README.md](README.md). For every file, placeholder, QA report and the go-live checklist, read [HANDOFF.md](HANDOFF.md) first.

## What this is

A static, bilingual (EN at `/`, ES at `/es/`) community site for Lake Atitlán, Guatemala. Vanilla HTML, CSS and JavaScript, no framework, no API keys. Hosted on GitHub Pages from the `main` branch (root).

The pages are **generated**. Do not hand-edit the HTML. Edit the sources, then rebuild.

## Rebuild after editing

Words live in `tools/content.py` (EN and ES), the page layout in `tools/variants/ad.html`, the look in `v/ad.css`.

```bash
python tools/build_variants.py
```

`tools/build_pages.py` only holds shared helpers; running it directly is refused. The older instructions that mentioned `tools/page.template.html` and a design-variants index describe a build that was removed; the single current design is documented in HANDOFF.md ("Design").

Other build steps, each described in HANDOFF.md:

- Blog stories: `tools/blog/*.json`. Topic stories: `tools/topics/*.json`. Visitor FAQ: `tools/faq.json`.
- Page metadata and share cards: `tools/seo.py`, then `python tools/build_og.py`.
- Merchant data: `data/merchants.json`, rebuilt with `tools/build_data.py`.
- Site settings and placeholder links: `config.js`.

## Preview locally

```bash
python -m http.server 18431
```

Then open http://127.0.0.1:18431/

## QA

```bash
python qa/run_qa_site.py http://127.0.0.1:18431/ qa/screenshots
python qa/test_story.py http://127.0.0.1:18431/ qa/screenshots
python qa/check_links.py
```

Reports and the other test scripts are listed in HANDOFF.md.

## Preview status

The site is a public preview with `noindex,nofollow` in every page and `Disallow: /` in `robots.txt`. Do not remove either until the owner decides to go public. The go-live checklist is in HANDOFF.md.

## Pull requests

Keep changes small. Change the source (`tools/`, `config.js`, JSON files), rebuild, and include the regenerated pages in the same commit.
