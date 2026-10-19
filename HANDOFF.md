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
| `images/` | Wikimedia Commons photos only (CC BY / CC BY-SA), WebP + JPG, 800 and 1600 px. | Via `tools/optimize_images.py`. |
| `vendor/leaflet/`, `fonts/`, `icons.svg` | Leaflet map library (BSD), Geist font (OFL), Phosphor icons (MIT). | No. |
| `qa/` | QA scripts, reports and screenshots. | No. |
| `robots.txt` | `Disallow: /` while private. | At go-live. |

Private material is **not** in the repo (see `.gitignore`): `source-archive/` (press articles, curated
press photos and logos, raw research), `plans/`, `BUILD-BRIEF.md`. Press and logo images are never used on the site.

Data and rights: merchant data © OpenStreetMap contributors (ODbL), as shown on BTC Map; credited in the footer.
Every photo carries its Commons credit and licence under the picture. Map tiles © OpenStreetMap contributors (Leaflet attribution).

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
* An unrelated file `DESIGN-VARIANTS-BRIEF.md` (five design variants) appeared in the project folder during the build. It conflicts
  with the brief's addendum ("do NOT show variants, build one strong design"), so it was left untouched, untracked and not implemented.
  Tell the builder if variants are wanted after all.
