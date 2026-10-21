# HANDOFF: Lago Bitcoin Community site

Status: **preview, `noindex,nofollow` ON** until Tomek says go public.
Repo: https://github.com/itstomekk/lago-bitcoin-community (branch `main`).
Live preview: see "Deployment" at the bottom.

This is Tomek's own community site for Lake Atitlán. It is an independent site and says so. It is
**not** the site of Bitcoin Lake / Lago Bitcoin (Patrick Melder's project), and the word "official"
is never used. Bitcoin Lake is credited only as history (it started the merchant network) with a
link to https://x.com/LakeBitcoin.

## How the site is built (plain language)

| File or folder | What it is | Edit here? |
|---|---|---|
| `index.html`, `es/index.html` | The English and Spanish pages. **Generated.** | No. Edit the sources below, then rebuild. |
| `tools/content.py` | Every visible word, EN and ES, in one file. Photo captions, press list. | **Yes, for wording.** |
| `tools/page.template.html` | The page layout shared by both languages (sections, ids). | Yes, for structure. |
| `tools/build_pages.py` | Builds both pages. `python tools/build_pages.py` | Run after any edit. |
| `style.css` | All styling. Colours and sizes are at the top (tokens). | Yes, for look. |
| `script.js` | Language memory, menu, map, merchant list, filters. | Rarely. |
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
class `show-placeholders`. To hide every badge at go-live, remove that class in `tools/page.template.html` and rebuild.

| `data-placeholder` | Where | What Tomek must supply |
|---|---|---|
| `whatsapp-invite-url` | Hero button and Community tile | WhatsApp group invite link. Put it in `config.js` (`whatsapp`). Both buttons go live and both badges vanish. |
| `meetup-dates` | Community, Meetups | Meetup dates (edit `meet_when` in `tools/content.py`, EN and ES). |
| `meetup-venues` | Community, Meetups | Meetup venues (edit `meet_where`). |
| `school-list` | Community, School visits | Which schools are visited (edit `school_list`). Add names only with the schools' agreement. |
| `facebook` | Community, "Follow and write to us" | Facebook page URL. `config.js` (`facebook`). |
| `contact-email` | Community, "Follow and write to us" | Contact email. `config.js` (`email`). |
| `tomek-bio-photo` | Community, "Who we are" | Tomek's bio and photo. Needs a new image added through `tools/optimize_images.py` or a plain image file. |
| `tour-booking` | VIP tours button | Booking link. `config.js` (`tourBooking`). cal.com/itstomekk is Tomek's calendar: **ask before wiring it**. |
| `tour-booking-details` | VIP tours note | Hidden automatically once `tourBooking` is set. |
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

Final live QA on 2026-10-21 (https://itstomekk.github.io/lago-bitcoin-community/): baseline 80/80; nine designs 893/899 on the first pass, the 6 misses were lazy photos still downloading on a slow link (all assets 200), so the runner now scrolls and waits up to 25 s for images; D, F and G rerun 290/290 (`qa/report-variants-live.md`; first pass in `qa/report-variants-live-acdacadcdfgh.md`).

Final local QA on 2026-10-21 (all nine designs): baseline 80/80 (`qa/report-local.md`); A, C, D, AC, AD, CD, F, G and H 899/899 in `qa/report-variants-local-acdacadcdfgh.md`; Hallmark F/G/H mobile 28/28 at 320/375/414/768 plus the 1280x800 fold. Fixed on 2026-10-21: the hidden "coming soon" toast no longer peeks above the bottom edge, and H's node arrows no longer touch the next label.

Local F + press-photo phase on 2026-10-20: baseline 80/80; A, C, D, AC, AD, CD and F 703/703 in `qa/report-variants-local-acdacadcdf.md`, including the exact 30-photo set and linked credits. Hallmark F mobile 10/10 at 320/375/414/768; AB23 privacy and keyboard activation 16/16. The last full browser QA preceded the final quote shortening; the builders were rerun and now reject any press quote that is not exactly one sentence.

```
python qa/run_qa.py http://127.0.0.1:18431/ qa/screenshots      # local, after: python -m http.server 18431
python qa/run_qa.py https://itstomekk.github.io/lago-bitcoin-community/ qa/screenshots/live
python qa/check_links.py
```

## Go-live checklist (when Tomek says go)

1. Fill `config.js`; replace placeholder texts in `tools/content.py`; remove `show-placeholders` from the body tag.
2. Remove the `noindex,nofollow` meta tag from `tools/page.template.html` and the `Disallow: /` line from `robots.txt`.
3. `python tools/build_pages.py`, run QA, commit, push to `main` (GitHub Pages redeploys from `main`).
4. Optional: custom domain (add `CNAME`), and a real social share image.

## Deployment

* Live URL (English): https://itstomekk.github.io/lago-bitcoin-community/
* Live URL (Spanish): https://itstomekk.github.io/lago-bitcoin-community/es/
* GitHub Pages from `main` (root). The repo was created **private** as planned, but the account plan does not allow Pages on
  private repositories (GitHub API: HTTP 422), so, as the brief's addendum allows, the repo was made **public** with
  `noindex,nofollow` in both pages and `Disallow: /` in `robots.txt`. Nothing private is in the repo (see `.gitignore`).
  The site is not hidden from people who have the link; it is only kept out of search engines until Tomek says go public.
* Verified from the live URL on 2026-10-19: `qa/report-live.md` (82 of 82 gates), screenshots in `qa/screenshots/live/`.
* `DESIGN-VARIANTS-BRIEF.md` (Tomek's voice notes) was expanded; see the current set and build status below.
  The root pages stay the baseline until Tomek picks.

## Design variants (nine current looks, same content)

Live (noindex, like the rest of the preview): `/v/a/`, `/v/c/`, `/v/d/`, `/v/ac/`, `/v/ad/`, `/v/cd/`, `/v/f/`, `/v/g/`, `/v/h/` and their `/es/` pages, the index `/variants/` (and `/variants/es/`),
and `/v/` (sends you to the design you looked at last). Every variant page has the fixed switcher and language bar plus the floating design switcher.
(it keeps the language and remembers the choice in `localStorage` key `lbc-design`).

| Design | Idea |
|---|---|
| A | Maya 1500 / 2100: stone, jade, cinnabar; step-fret lines, dot-and-bar section numerals, a rail that opens on hover. Tomek's first choice. |
| C | Volcano night: dark and cinematic, logo cinnabar and jade accents, Bebas Neue titles, film strips, map console with a side drawer. |
| D | Textile and craft: woven colour blocks (indigo, cinnabar, marigold, jade), arch photo frames, pill controls. |
| AC | C's night palette with A-inspired restraint, stepped details and more open spacing. |
| AD | A's restraint and stepped motifs combined with D's woven colour blocks and arch frames. |
| CD | C's night scenes combined with D's textile colour blocks and arch frames. |
| F | Split Studio: a credited community tuk-tuk portrait paired with the dated merchant map and alternating evidence-led sections. Hallmark: Coral tokens. |
| G | Field Notes: newspaper masthead, one long reading column, short credited photo plates, prose and lists instead of cards. Hallmark: light paper, serif, green accent. |
| H | Section map: a 12-column wayfinding grid, a hand-built diagram whose seven nodes link to the sections, and the geographic merchant map. Hallmark: Grid tokens (Archivo, ultramarine). |

All designs share one content source and merchant dataset. Designs B and E were removed. F, G and H were built with the Hallmark skill (catalog theme, locked tokens in `v/*.tokens.css`, pre-emit critique stamp in `.hallmark/log.json`, mobile checks at 320/375/414/768). A, C, D, AC, AD and CD did not use Hallmark.

| File | What it is | Edit here? |
|---|---|---|
| `tools/content.py` | The same words as the root pages, plus the names of the variants and the switcher / index strings. | **Yes, for wording (all current variants follow).** |
| `tools/variants/a.html`, `c.html`, `d.html`, `f.html`, `g.html`, `h.html` | The page layouts of A, C, D, F, G and H. AC/CD use C's layout base, AD uses D's; each design has its own visual treatment. | Yes, for structure. |
| `v/base.css` | Shared floor: buttons, merchant finder, switcher, placeholders, toast. Colours come from tokens. | Rarely. |
| `v/a.css`, `c.css`, `d.css`, `ac.css`, `ad.css`, `cd.css`, `f.css`, `g.css`, `h.css` and `f/g/h.tokens.css` | The look and locked Hallmark tokens for each current design. | **Yes, for look.** |
| `v/app.js` | Behaviour shared by the designs (copy of `script.js` plus marker colours, design memory, count-up and click-to-play AB23 embed). | Rarely. |
| `tools/build_variants.py` | Builds all `v/*/index.html`, `v/*/es/index.html` and `variants/` pages. `python tools/build_variants.py` (or `... a c` for some). | Run after any edit. |
| `tools/variants/index.html`, `variants/variants.css` | The `/variants/` page and its look. Thumbnails: `variants/thumbs/*.webp` (made by `qa/make_thumbs.py`). | Yes. |
| `fonts/` (new files) | Newsreader, Bebas Neue, Bricolage Grotesque, Sora, Geist Mono (all SIL OFL, self-hosted). | No. |
| `images/bw-*.jpg/webp`, `lake-5-*`, `lake-12-*` | Four more Commons photos used only by the variants (credits in `data/photos.json`; `python tools/optimize_images.py --extra`). | Via the script. |
| `images/community-tuktuk-*`, `community-boat-*` | Optimized Tomek-supplied tuk tuk and boat photos, used in the transport section on the baseline and all current designs. Source originals stay in ignored `source-archive/tomek-supplied/`. | `python tools/optimize_community_photos.py`. |

Rules that hold in every variant: same 8 sections and ids, same 117 places and the same data file, every placeholder keeps its
`data-placeholder` badge (so the table above still applies), photo credits stay visible, `noindex,nofollow`, WCAG AA text.
Each design has one fixed theme (no automatic dark mode); C is dark by design.

### Photo credits to confirm

The supplied `tuktuk-bitcoin-lake-road.jpg` and `pier-to-pier-bitcoin-boat.jpg` are credited on-page as exactly
"Photo: community archive (source to confirm)". Do not invent a photographer; replace this provisional credit only when Tomek confirms the source.

QA for the variants: `python qa/run_qa_variants.py <site URL> <screenshot dir> [a,c,d,ac,ad,cd,f,g,h]`. Reports: `qa/report-variants-local.md`
and `qa/report-variants-live.md`; live screenshots are stored under `qa/screenshots/`.
The runner also measures contrast of text that sits over photos or patterns with a pixel check (axe cannot do that).
It needs `qa/.cache/axe.min.js` (download command is at the top of the script).

Choosing the winner: tell the builder which design should become `/`. The root `index.html` / `es/index.html` would then be
generated from that design's layout (path prefix changes from `../../` to `./`); until then the root is the first build.
