# Changelog

## 2026-10-19 (variants)
- Five design variants at `/v/a/` to `/v/e/` (each with `/es/`), a floating Design switcher on every variant page and a `/variants/` index with thumbnails. Root pages unchanged.
- Shared content (`tools/content.py`) and data; new `tools/build_variants.py`, `v/` stylesheets and `v/app.js`, four extra Commons photos, five self-hosted OFL fonts.
- New QA runner `qa/run_qa_variants.py` (per-variant gates, pixel contrast check for text over photos).

## 2026-10-19
- First build of the Lago Bitcoin Community site (EN `/` and ES `/es/`), preview with `noindex,nofollow`.
- 117 OpenStreetMap / BTC Map places (data of 2026-10-19) on a Leaflet map and in a filterable list.
- Bitcoin boat and tuk tuk rows from the same data; Bitcoin ATM, WhatsApp, meetups, schools, VIP tours, newcomers and
  history sections. Unknown facts are visible `data-placeholder` badges (see HANDOFF.md).
- Wikimedia Commons photos only, with per-photo credit. Four dead merchant website links left out.
- QA scripts and reports in `qa/`.
