# QA report (live)

Base URL: https://itstomekk.github.io/lago-bitcoin-community/
PASS 80 / FAIL 0

| Result | Gate | Evidence |
|---|---|---|
| PASS | HTTP 200 https://itstomekk.github.io/lago-bitcoin-community/ | 200 |
| PASS | [en] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin on Lake Atitlán, Guatemala", "title_len": 59, "desc_len": 158} |
| PASS | [en] meta robots noindex,nofollow | "present" |
| PASS | [en] hreflang alternates en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/"]] |
| PASS | [en] html lang attribute | "en" |
| PASS | HTTP 200 https://itstomekk.github.io/lago-bitcoin-community/es/ | 200 |
| PASS | [es] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin en el Lago de Atitlán, Guatemala", "title_len": 65, "desc_len": 179} |
| PASS | [es] meta robots noindex,nofollow | "present" |
| PASS | [es] hreflang alternates en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/"]] |
| PASS | [es] html lang attribute | "es" |
| PASS | robots.txt Disallow while private | 200 |
| PASS | asset 200 style.css | 200 |
| PASS | asset 200 script.js | 200 |
| PASS | asset 200 config.js | 200 |
| PASS | asset 200 icons.svg | 200 |
| PASS | asset 200 favicon.svg | 200 |
| PASS | asset 200 data/merchants.json | 200 |
| PASS | asset 200 vendor/leaflet/leaflet.js | 200 |
| PASS | asset 200 vendor/leaflet/leaflet.css | 200 |
| PASS | asset 200 fonts/geist-latin-wght-normal.woff2 | 200 |
| PASS | [en] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [en] page weight under 3 MB excluding map tiles | "2247 KB (tiles excluded: 258 KB)" |
| PASS | [en] no horizontal overflow at 1440 | {"sw": 1440, "cw": 1440} |
| PASS | [en] map ready and renders 117 markers (SVG paths in DOM) | {"state": "ready", "svg_markers": 117, "tiles_loaded": 16} |
| PASS | [en] list count == marker count == 117 | {"cards": 117, "markers": 117, "hook": {"m": 117, "c": 117, "v": 117, "p": 117}} |
| PASS | [en] count text | "Showing 117 of 117 places" |
| PASS | [en] search filters list and map together | {"c": 6, "m": 6, "paths": 6} |
| PASS | [en] category chip filters (stay) | {"c": 16, "m": 16, "pressed": "stay"} |
| PASS | [en] village filter (San Marcos La Laguna) | {"c": 10, "m": 10} |
| PASS | [en] empty state | {"c": 0, "m": 0, "empty": true} |
| PASS | [en] reset restores 117 | {"c": 117, "m": 117} |
| PASS | [en] ride 'Show on map' opens a popup | true |
| PASS | [en] every image has alt text | {"images": 50, "bad": []} |
| PASS | [en] every photo has a linked source credit | {"photos": 49, "bad": []} |
| PASS | [en] all 30 press photos appear once with visible linked credits | {"count": 30, "unique": 30, "missing": [], "bad_credit": []} |
| PASS | [en] no broken images | [] |
| PASS | [en] no 'official'/'oficial' claim | [] |
| PASS | [en] no em or en dashes in visible text | [] |
| PASS | [en] 'Always check with the merchant' note present | "ok" |
| PASS | [en] 117 places + 50+ claim + data date | "ok" |
| PASS | [en] OSM/ODbL, BTC Map and Commons credits in footer | "ok" |
| PASS | [en] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [en] no console errors at 390 | [] |
| PASS | [en] 117 markers at 390 | 117 |
| PASS | [en] mobile menu opens | true |
| PASS | [es] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [es] page weight under 3 MB excluding map tiles | "2248 KB (tiles excluded: 258 KB)" |
| PASS | [es] no horizontal overflow at 1440 | {"sw": 1440, "cw": 1440} |
| PASS | [es] map ready and renders 117 markers (SVG paths in DOM) | {"state": "ready", "svg_markers": 117, "tiles_loaded": 16} |
| PASS | [es] list count == marker count == 117 | {"cards": 117, "markers": 117, "hook": {"m": 117, "c": 117, "v": 117, "p": 117}} |
| PASS | [es] count text | "Mostrando 117 de 117 lugares" |
| PASS | [es] search filters list and map together | {"c": 17, "m": 17, "paths": 17} |
| PASS | [es] category chip filters (stay) | {"c": 16, "m": 16, "pressed": "stay"} |
| PASS | [es] village filter (San Marcos La Laguna) | {"c": 10, "m": 10} |
| PASS | [es] empty state | {"c": 0, "m": 0, "empty": true} |
| PASS | [es] reset restores 117 | {"c": 117, "m": 117} |
| PASS | [es] ride 'Show on map' opens a popup | true |
| PASS | [es] every image has alt text | {"images": 50, "bad": []} |
| PASS | [es] every photo has a linked source credit | {"photos": 49, "bad": []} |
| PASS | [es] all 30 press photos appear once with visible linked credits | {"count": 30, "unique": 30, "missing": [], "bad_credit": []} |
| PASS | [es] no broken images | [] |
| PASS | [es] no 'official'/'oficial' claim | [] |
| PASS | [es] no em or en dashes in visible text | [] |
| PASS | [es] 'Always check with the merchant' note present | "ok" |
| PASS | [es] 117 places + 50+ claim + data date | "ok" |
| PASS | [es] OSM/ODbL, BTC Map and Commons credits in footer | "ok" |
| PASS | [es] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [es] no console errors at 390 | [] |
| PASS | [es] 117 markers at 390 | 117 |
| PASS | [es] mobile menu opens | true |
| PASS | EN/ES parity: same section ids in same order | ["hero", "lake", "bitcoin", "transport", "community", "tours", "expats", "about"] |
| PASS | EN/ES parity: same placeholders, nav targets, h2 and image counts | {"placeholders": ["atm-locations", "contact-email", "expat-contact", "facebook", "meetup-dates", "meetup-venues", "school-list", "tomek-bio-photo", "tour-booking", "tour-booking-details", "whatsapp-invite-url"], "h2": 7, "imgs": 66} |
| PASS | browser language es: opening / redirects to /es/ | "https://itstomekk.github.io/lago-bitcoin-community/es/" |
| PASS | switcher EN: goes to English page and stores choice | {"url": "https://itstomekk.github.io/lago-bitcoin-community/", "stored": "en"} |
| PASS | stored choice (en) beats browser language (es) on reload | "https://itstomekk.github.io/lago-bitcoin-community/" |
| PASS | switcher ES: goes to /es/ and stores choice | "https://itstomekk.github.io/lago-bitcoin-community/es/" |
| PASS | browser language en: opening /es/ redirects to / | "https://itstomekk.github.io/lago-bitcoin-community/" |
| PASS | placeholder button shows 'coming soon' toast | true |
| PASS | placeholder badge visible in preview | "\"Placeholder: whatsapp-invite-url\"" |
| PASS | every data-placeholder is listed in HANDOFF.md | {"placeholders": ["atm-locations", "contact-email", "expat-contact", "facebook", "meetup-dates", "meetup-venues", "school-list", "tomek-bio-photo", "tour-booking", "tour-booking-details", "whatsapp-invite-url"], "missing": []} |