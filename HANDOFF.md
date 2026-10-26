# HANDOFF: Bitcoin Lago Community site

Status: **preview, `noindex,nofollow` ON** until Tomek says go public.
Repo: https://github.com/itstomekk/bitcoin-lago (branch `main`).
Live preview: see "Deployment" at the bottom.

This is Tomek's own community site for Lake Atitlán. It is an independent site and says so. It is
**not** the site of Bitcoin Lake / Bitcoin Lago (Patrick Melder's project), and the word "official"
is never used. Bitcoin Lake is credited only as history (it started the merchant network) with a
link to https://x.com/LakeBitcoin.

The English and Spanish canonical pages (home, story, blog index, FAQ, 12 video stories and 6 topic pages) use page-specific titles, descriptions, canonical/hreflang, Open Graph, Twitter, and JSON-LD metadata from `tools/seo.py`. Matching 1200×630 JPEG share cards live in `images/og/`; their provenance and page mapping are in `images/og/manifest.json`. After changing page content or adding a story, update `tools/seo.py`, run `python tools/build_variants.py`, then `C:/Python314/python.exe tools/build_og.py` and `python qa/test_seo.py`. The site remains `noindex,nofollow` and `robots.txt` remains disallowed until Tomek explicitly says go public. Status 2026-10-23: Eliazar approved the public preview on GitHub Pages; indexing waits until a good custom domain is connected (then change SITE_URL, rebuild, drop noindex/Disallow, add sitemap).

## Kaqchikel (KAQ) page, added 2026-10-23
- Short page at `/kaq/` plus a third KAQ entry in the language switch, built by `tools/kaq.py` from `tools/kaq.json` (lang `cak`, noindex like the rest).
- **Gate:** page and switch exist only when every `kaq` string, `translator` and `reviewed_on` are filled. Until then `python tools/build_variants.py` writes only a DRAFT to `source-archive/kaq-draft/` (gitignored). Never machine-translate: texts come from a native speaker. Brief to send them: `C:/Users/Lenovo/Hermes/projects/community/lago-bitcoin/content/kaqchikel-translation-brief.md`.
- When it goes live, the `qa/test_story.py` language-link check will see a third link (KAQ); update that expectation then. Test: `python qa/test_kaq.py`.
- Tz'utujil (south shore) would follow the same pattern if wanted.

## Review page `/review/`, added 2026-10-26
- Single-file page (Kaqchikel line review + 26 questions for Eliazar, `#eliazar`). Source and tests live in `C:/Users/Lenovo/Hermes/projects/community/lago-bitcoin/translation-review/`; rebuild there (`python build.py`), then copy `dist/index.html` to `review/index.html` here. noindex; `robots.txt` already disallows all. Answers go to Tomek as encrypted Nostr DMs; no server.

## How the site is built (plain language)

| File or folder | What it is | Edit here? |
|---|---|---|
| `index.html`, `es/index.html` | The English and Spanish pages. **Generated.** | No. Edit the sources below, then rebuild. |
| `tools/content.py` | Every visible word, EN and ES, in one file. Photo captions, press list. | **Yes, for wording.** |
| `tools/build_variants.py` | Builds both pages (design AD). `python tools/build_variants.py` | Run after any edit. |
| `config.js` | **Switches placeholder links on** (WhatsApp, Facebook, email, tour booking, newcomers contact). | **Yes. Start here.** |
| `data/merchants.json` | The 117 places (trimmed OpenStreetMap export, dated 2026-10-19). | Rebuild with `tools/build_data.py`. |
| `data/photos.json` | Credit line for each photo (artist, licence, Commons page). | Via `tools/optimize_images.py`. |
| `images/` | Optimized Wikimedia Commons and Tomek-supplied community photos, WebP + JPG. | Via `tools/optimize_images.py` and `tools/optimize_community_photos.py`. |
| `vendor/leaflet/`, `fonts/`, `icons.svg` | Leaflet map library (BSD), Geist font (OFL), Phosphor icons (MIT). | No. |
| `qa/` | QA scripts, reports and screenshots. | No. |
| `robots.txt` | `Disallow: /` while private. | At go-live. |

Private material is **not** in the repo (see `.gitignore`): `source-archive/` (raw press articles and photos,
research originals), `plans/`, `BUILD-BRIEF.md`. Approved, optimized press-photo derivatives and the approved
brand logo are copied into `images/` with credits and are used on the site; unrelated reference images and raw sources stay private.

Data and rights: merchant data © OpenStreetMap contributors (ODbL), as shown on BTC Map; credited in the footer.
Wikimedia photos carry their Commons credit and licence; community-supplied photos use the provisional source credit shown in the page.
`data/press-photos.json` retains the publisher, article title, source URL and rights note for each of the 30 curated press photos.
Publisher/photographer copyrights remain; some source articles credit images as "courtesy Bitcoin Lake". These optimized
derivatives are used at Tomek's direction on this noindex preview, with a visible "Photo: <publisher>, via <article title>"
credit linked to the article; remove on request. Raw press photos and research originals remain in ignored `source-archive/`.
Map tiles © OpenStreetMap contributors (Leaflet attribution).

## Placeholders (all visibly badged in preview, all carry `data-placeholder`)

The badge ("Placeholder: ...") is drawn by CSS for every `[data-placeholder]` element while `<body>` has the
class `show-placeholders`. To hide every badge at go-live, remove that class in `tools/build_variants.py` (head_html) and rebuild.

| `data-placeholder` | Where | What Tomek must supply |
|---|---|---|
| `whatsapp-invite-url` | Hero button and Community tile | WhatsApp group invite link. Put it in `config.js` (`whatsapp`). Both buttons go live and both badges vanish. |
| `facebook` | Community, "Follow and write to us" | Facebook page URL. `config.js` (`facebook`). |
| `contact-email` | Community, "Follow and write to us" | Contact email. `config.js` (`email`). |
| `eliazar-bio-photo` | Community, "Who we are" | Eliazar's photo and short bio (Bitcoin Lago's local leader). |
| `whatsapp-number` | Plan your stay, "Send on WhatsApp" | Bitcoin Lago's WhatsApp number in `config.js` (`whatsappNumber`, digits with country code). The request form opens a chat with this number. |
| `expat-contact` | Newcomers button | Contact link or email. `config.js` (`expatContact`). |
| `atm-locations` | Bitcoin ATMs block | ATM locations. **None are in the data**, so none are listed. Add them in `tools/content.py` / the template. |

Until a value is set, clicking a placeholder button only shows a small "This link is coming soon" message.

## Claims to confirm with Tomek before go-live

The page states these in "we" voice because they were in Tomek's brief; nothing else on the site backs them up, and
none is attributed to Bitcoin Lake or Patrick Melder:

1. We go to different schools and teach Bitcoin.
2. We organize VIP tours; we onboard Maya merchants to Bitcoin; we work with cooperatives that accept Bitcoin.
   No community or cooperative is named, and no price, duration or itinerary is stated.
3. There is a group of expats on the lake and we serve them.
4. There are Bitcoin ATMs in the area (locations not stated).
5. "More than 50 merchants in the network" is supported by the data (117 places tagged on OpenStreetMap on 2026-10-19).
   Old press figures are not used.

Please also read the Maya wording in the VIP tours section once (plain terms only: culture, education, onboarding merchants, cooperatives).
The Spanish was written for natural Guatemalan usage ("tuc tuc", "lancha", "comercios", "tú" forms); a native read-through is still worthwhile.

## Data notes

* The village shown on each card is the nearest village centre to the place's coordinates (OSM has no village tag for most places). Approximate, and the page says so.
* The three tuk tuk numbers were embedded in their OSM names ("Niul - Tuk Tuk 4120 0757"); the number is shown as the phone, unchanged.
* Four merchant website links from OSM were dead on 2026-10-19 and are not linked (the places stay listed): imagenchocolate.com (no DNS), eaglesretreats.com (TLS certificate mismatch), lax-travel-panajachel.business.site (404), tekoaspaces.com (404). See `tools/build_data.py`.
* Facebook, TripAdvisor and one merchant site refuse non-browser requests (HTTP 400/403 in the link checker); the servers answered, so the hosts exist, but a human should click through once. List in `qa/links.json`.
* One place has no name on OpenStreetMap; the card says "Unnamed place".
* Survey dates are the OSM `survey:date` tag. Where a place has none, the card says so.

## QA

`qa/report-local.md` and `qa/report-live.md` list every gate with the measured evidence. Screenshots: `qa/screenshots/` (local) and `qa/screenshots/live/` (from the live URL). Re-run:

Final live QA on 2026-10-21 (https://itstomekk.github.io/bitcoin-lago/): baseline 80/80; nine designs 893/899 on the first pass, the 6 misses were lazy photos still downloading on a slow link (all assets 200), so the runner now scrolls and waits up to 25 s for images; D, F and G rerun 290/290 (`qa/report-variants-live.md`; first pass in `qa/report-variants-live-acdacadcdfgh.md`).

Final local QA on 2026-10-21 (all nine designs): baseline 80/80 (`qa/report-local.md`); A, C, D, AC, AD, CD, F, G and H 899/899 in `qa/report-variants-local-acdacadcdfgh.md`; Hallmark F/G/H mobile 28/28 at 320/375/414/768 plus the 1280x800 fold. Fixed on 2026-10-21: the hidden "coming soon" toast no longer peeks above the bottom edge, and H's node arrows no longer touch the next label.

Local F + press-photo phase on 2026-10-20: baseline 80/80; A, C, D, AC, AD, CD and F 703/703 in `qa/report-variants-local-acdacadcdf.md`, including the exact 30-photo set and linked credits. Hallmark F mobile 10/10 at 320/375/414/768; AB23 privacy and keyboard activation 16/16. The last full browser QA preceded the final quote shortening; the builders were rerun and now reject any press quote that is not exactly one sentence.

```
python qa/run_qa.py http://127.0.0.1:18431/ qa/screenshots      # local, after: python -m http.server 18431
python qa/run_qa.py https://itstomekk.github.io/bitcoin-lago/ qa/screenshots/live
python qa/check_links.py
```

## Go-live checklist (when Tomek says go)

1. Fill `config.js`; replace placeholder texts in `tools/content.py`; remove `show-placeholders` from the body tag.
2. Remove the `noindex,nofollow` meta tag from `tools/build_variants.py` (head_html) and the `Disallow: /` line from `robots.txt`.
3. `python tools/build_variants.py`, run `qa/run_qa_site.py`, commit, push to `main` (GitHub Pages redeploys from `main`).
4. Optional: custom domain (add `CNAME`), and a real social share image.

## Deployment

* Live URL (English): https://itstomekk.github.io/bitcoin-lago/
* Live URL (Spanish): https://itstomekk.github.io/bitcoin-lago/es/
* GitHub Pages from `main` (root). The repo was created **private** as planned, but the account plan does not allow Pages on
  private repositories (GitHub API: HTTP 422), so, as the brief's addendum allows, the repo was made **public** with
  `noindex,nofollow` in both pages and `Disallow: /` in `robots.txt`. Nothing private is in the repo (see `.gitignore`).
  The site is not hidden from people who have the link; it is only kept out of search engines until Tomek says go public.
* Verified from the live URL on 2026-10-19: `qa/report-live.md` (82 of 82 gates), screenshots in `qa/screenshots/live/`.
* `DESIGN-VARIANTS-BRIEF.md` (Tomek's voice notes) was expanded; see the current set and build status below.
  The root pages stay the baseline until Tomek picks.

## Design (one design since 2026-10-21)

Tomek picked AD and asked to remove every other design. The site root (`/` and `/es/`) is now design AD, "Woven Maya":
D's colours and warmth (indigo, jade, cinnabar, marigold and linen panels, woven stripe bands, checker hero, Bricolage Grotesque
headlines) with A's symbols and clean structure (left rail with dot-and-bar section numerals, step-fret bands, stepped photo
silhouettes, hairline grids and lists, mono figures, square corners, no hard offset shadows).

Removed: the baseline page (`style.css`, `script.js`, `tools/page.template.html`), designs A, C, D, AC, CD, F, G, H, the
`/variants/` index, the design switcher and the top test bar. They stay in git history (last commit with all of them: `4dc4f58`).
Old preview links `/v/`, `/v/ad/`, `/v/ad/es/`, `/variants/` and `/variants/es/` are small redirect pages to the site.

| File | What it is | Edit here? |
|---|---|---|
| `index.html`, `es/index.html` | The English and Spanish pages. **Generated.** | No. |
| `tools/content.py` | Every visible word, EN and ES. | **Yes, for wording.** |
| `tools/variants/ad.html` | The page layout (sections, ids). | Yes, for structure. |
| `v/ad.css` | The look: colour tokens at the top, then each section. | **Yes, for look.** |
| `v/base.css` | Shared floor: buttons, merchant finder, placeholders, toast. | Rarely. |
| `v/app.js` | Language memory, menu, map, merchant list, filters, count-up, AB23 click-to-play. | Rarely. |
| `tools/build_variants.py` | Builds both pages and the redirect pages: `python tools/build_variants.py`. | Run after any edit. |
| `tools/build_pages.py` | Shared helpers only (photos, icons, merchant data). Running it directly is refused. | No. |

Rules: same 8 sections and ids, 117 places from one data file, every placeholder keeps its `data-placeholder` badge,
photo credits stay visible, `noindex,nofollow` until go-live, WCAG AA text on every panel.

QA: `python qa/run_qa_site.py <site URL> <screenshot dir>` writes `qa/report-site-local.md` or `qa/report-site-live.md`.
It needs `qa/.cache/axe.min.js`. The older runners (`run_qa.py`, `run_qa_variants.py`) are for the removed designs.

### Photo credits to confirm

The supplied `tuktuk-bitcoin-lake-road.jpg` and `pier-to-pier-bitcoin-boat.jpg` are credited on-page as exactly
"Photo: community archive (source to confirm)". Do not invent a photographer; replace this provisional credit only when Tomek confirms the source.

QA for the variants: `python qa/run_qa_variants.py <site URL> <screenshot dir> [a,c,d,ac,ad,cd,f,g,h]`. Reports: `qa/report-variants-local.md`
and `qa/report-variants-live.md`; live screenshots are stored under `qa/screenshots/`.
The runner also measures contrast of text that sits over photos or patterns with a pixel check (axe cannot do that).
It needs `qa/.cache/axe.min.js` (download command is at the top of the script).

Choosing the winner: tell the builder which design should become `/`. The root `index.html` / `es/index.html` would then be
generated from that design's layout (path prefix changes from `../../` to `./`); until then the root is the first build.

## 2026-10-21: Bitcoin Lago's own site
- Tomek decided the site is Bitcoin Lago's own: founded 2021 by Patrick Melder with friends and supporters; Eliazar (@JUN_AJPU_btc) is the local leader.
- New content lives at the end of `tools/content.py`: `LB_PHOTOS`, `GALLERY`, `TIMELINE` (each year links its X sources), `SERVICES`, and the form strings.
- Photos: `python tools/optimize_lago_photos.py` builds `images/lb-*` from the ignored `source-archive/` (Eliazar's Telegram photos, and public X posts of @JUN_AJPU_btc and @AtitlanTours21).
- Full X history notes moved 2026-10-22 to the program anchor `C:\Users\Lenovo\Hermes\projects\community\lago-bitcoin\research\x-2026-10-21\` (tweets.json, manifest.json, lago-bitcoin-history.md). Tweet images stay in `source-archive/x-2026-10-21/` (build input). Content plan and blog ideas: `...\lago-bitcoin\content\content-plan.md`. Open work for the whole project: `...\lago-bitcoin\PLAN.md`.
- The "Plan your stay" section (`#tours`) is a concierge funnel: no prices, one form that opens WhatsApp with the message filled in.


## 2026-10-22: Bitcoin Lago rename, partners, story page
- Name is **Bitcoin Lago** everywhere (logo wordmark words swapped; originals in source-archive/logo-before-rename/). Site moved to https://itstomekk.github.io/bitcoin-lago/ (repo renamed).
- Partners band (`C.PARTNERS`, logos in images/partners/).
- Story page `/story/` and `/es/story/`: built from `tools/story_data.json`, which `python tools/import_x_harvest.py` makes from the gitignored X harvest `source-archive/x-harvest-2026-10-21.json` (1,660 tweets of @JUN_AJPU_btc, 2022 to 2026). Only photos with child_faces false are published (7 withheld).
- Main page: Atitlán Bitcoin Tours offer list (`C.TOURS_OFFER`), link to the story page under the timeline.
- QA: `python qa/run_qa_site.py <base> <shots>` (main pages) and `python qa/test_story.py <base> <shots>` (story pages).


## 2026-10-26: GoatCounter analytics
- GoatCounter site `bitcoinlago` (https://bitcoinlago.goatcounter.com, cookieless). The snippet is in `FOOT` in `tools/build_variants.py`, so all 48 content pages (EN and ES: home, story, FAQ, blog index, 12 stories, 8 topics) get it after `python tools/build_variants.py`. The 5 redirect stubs (`v/`, `variants/`) do not carry it. The site stays `noindex,nofollow`.
