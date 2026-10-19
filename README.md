# Lago Bitcoin Community

Static, bilingual (EN / ES) community site for Lake Atitlán, Guatemala. Vanilla HTML, CSS and JavaScript, no framework,
no API keys. Hosted on GitHub Pages from the `main` branch.

Start with **HANDOFF.md**: it explains every file, lists every placeholder Tomek must fill, and says how to rebuild and go live.

Quick rebuild after editing words (`tools/content.py`) or layout (`tools/page.template.html`):

    python tools/build_pages.py

Preview locally: `python -m http.server 18431` then open http://127.0.0.1:18431/

Design variants (five looks, same content): `python tools/build_variants.py`, then open http://127.0.0.1:18431/variants/ .
See "Design variants" in HANDOFF.md.
