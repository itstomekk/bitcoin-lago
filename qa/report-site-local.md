# Site QA report (local)

Base URL: http://127.0.0.1:18431/
Variants: ad
PASS 97 / FAIL 0

| Result | Gate | Evidence |
|---|---|---|
| PASS | robots.txt Disallow while private | 200 |
| PASS | [ad/en] HTTP 200 http://127.0.0.1:18431/ | 200 |
| PASS | [ad/en] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin on Lake Atitlán, Guatemala", "desc_len": 158} |
| PASS | [ad/en] meta robots noindex,nofollow | "present" |
| PASS | [ad/en] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/"]] |
| PASS | [ad/en] html lang + data-design | "en" |
| PASS | [ad/en] every referenced asset and link returns 200 | {"checked": 110, "bad": []} |
| PASS | [ad/en] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [ad/en] page weight under 3 MB excluding map tiles | "2326 KB" |
| PASS | [ad/en] no horizontal overflow at 1440 | {"sw": 1440, "cw": 1440} |
| PASS | [ad/en] no text leaves the screen at 1440 | [] |
| PASS | [ad/en] every section fills the screen (>=0.95 of viewport height) | [["hero", 1], ["lake", 1.18], ["bitcoin", 1.8], ["transport", 1.53], ["community", 1.68], ["tours", 1.02], ["expats", 1], ["about", 5.92]] |
| PASS | [ad/en] map ready and renders 117 markers | {"state": "ready", "markers": 117, "tiles": 16} |
| PASS | [ad/en] list count == marker count == 117 | {"cards": 117, "markers": 117, "hook": {"m": 117, "c": 117, "v": 117, "p": 117}} |
| PASS | [ad/en] count text shows 117 | "Showing 117 of 117 places" |
| PASS | [ad/en] markers use the design's own colour token | {"fills": ["#f2b632"], "token": "#f2b632"} |
| PASS | [ad/en] search filters list and map together | {"c": 6, "m": 6, "paths": 6} |
| PASS | [ad/en] category chip filters (stay) | {"c": 16, "m": 16, "pressed": "stay"} |
| PASS | [ad/en] village filter | {"c": 10, "m": 10} |
| PASS | [ad/en] empty state | {"c": 0, "m": 0, "empty": true} |
| PASS | [ad/en] reset restores 117 | {"c": 117, "m": 117} |
| PASS | [ad/en] ride 'Show on map' opens a popup | "popup" |
| PASS | [ad/en] every image has alt text | {"images": 51, "bad": []} |
| PASS | [ad/en] only local photos, each with a Commons, approved community-archive, or linked press credit | {"photos": 49, "no_credit": [], "other_images": []} |
| PASS | [ad/en] all 30 press photos appear once with visible linked credits | {"count": 30, "unique": 30, "missing": [], "bad_credit": []} |
| PASS | [ad/en] no broken images | "ok" |
| PASS | [ad/en] no 'official'/'oficial' claim | "none" |
| PASS | [ad/en] no em or en dashes in visible text | [] |
| PASS | [ad/en] merchant check note present | "ok" |
| PASS | [ad/en] 117 places + 50+ claim + data date | "ok" |
| PASS | [ad/en] OSM/ODbL, BTC Map and Commons credits in footer | "ok" |
| PASS | [ad/en] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [ad/en] 1440 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 11, "candidates": 11, "lowest_ratio": 8.9, "failures": []} |
| PASS | [ad/en] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [ad/en] no text leaves the screen at 390 | [] |
| PASS | [ad/en] no console errors at 390 | [] |
| PASS | [ad/en] brand does not overlap its CTA or menu button at 390 | {"brandRight": 229, "overlapCta": false, "overlapMenu": false} |
| PASS | [ad/en] 117 markers at 390 | "ok" |
| PASS | [ad/en] mobile menu opens | true |
| PASS | [ad/en] navigation link scrolls to the merchants section | 72 |
| PASS | [ad/en] 390 axe-core WCAG A/AA violations | [] |
| PASS | [ad/en] 390 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 11, "candidates": 11, "lowest_ratio": 9.3, "failures": []} |
| PASS | [ad/es] HTTP 200 http://127.0.0.1:18431/es/ | 200 |
| PASS | [ad/es] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin en el Lago de Atitlán, Guatemala", "desc_len": 179} |
| PASS | [ad/es] meta robots noindex,nofollow | "present" |
| PASS | [ad/es] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/"]] |
| PASS | [ad/es] html lang + data-design | "es" |
| PASS | [ad/es] every referenced asset and link returns 200 | {"checked": 110, "bad": []} |
| PASS | [ad/es] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [ad/es] page weight under 3 MB excluding map tiles | "2327 KB" |
| PASS | [ad/es] no horizontal overflow at 1440 | {"sw": 1440, "cw": 1440} |
| PASS | [ad/es] no text leaves the screen at 1440 | [] |
| PASS | [ad/es] every section fills the screen (>=0.95 of viewport height) | [["hero", 1], ["lake", 1.2], ["bitcoin", 1.8], ["transport", 1.56], ["community", 1.64], ["tours", 1.05], ["expats", 1], ["about", 5.92]] |
| PASS | [ad/es] map ready and renders 117 markers | {"state": "ready", "markers": 117, "tiles": 16} |
| PASS | [ad/es] list count == marker count == 117 | {"cards": 117, "markers": 117, "hook": {"m": 117, "c": 117, "v": 117, "p": 117}} |
| PASS | [ad/es] count text shows 117 | "Mostrando 117 de 117 lugares" |
| PASS | [ad/es] markers use the design's own colour token | {"fills": ["#f2b632"], "token": "#f2b632"} |
| PASS | [ad/es] search filters list and map together | {"c": 17, "m": 17, "paths": 17} |
| PASS | [ad/es] category chip filters (stay) | {"c": 16, "m": 16, "pressed": "stay"} |
| PASS | [ad/es] village filter | {"c": 10, "m": 10} |
| PASS | [ad/es] empty state | {"c": 0, "m": 0, "empty": true} |
| PASS | [ad/es] reset restores 117 | {"c": 117, "m": 117} |
| PASS | [ad/es] ride 'Show on map' opens a popup | "popup" |
| PASS | [ad/es] every image has alt text | {"images": 51, "bad": []} |
| PASS | [ad/es] only local photos, each with a Commons, approved community-archive, or linked press credit | {"photos": 49, "no_credit": [], "other_images": []} |
| PASS | [ad/es] all 30 press photos appear once with visible linked credits | {"count": 30, "unique": 30, "missing": [], "bad_credit": []} |
| PASS | [ad/es] no broken images | "ok" |
| PASS | [ad/es] no 'official'/'oficial' claim | "none" |
| PASS | [ad/es] no em or en dashes in visible text | [] |
| PASS | [ad/es] merchant check note present | "ok" |
| PASS | [ad/es] 117 places + 50+ claim + data date | "ok" |
| PASS | [ad/es] OSM/ODbL, BTC Map and Commons credits in footer | "ok" |
| PASS | [ad/es] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [ad/es] 1440 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 11, "candidates": 11, "lowest_ratio": 8.9, "failures": []} |
| PASS | [ad/es] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [ad/es] no text leaves the screen at 390 | [] |
| PASS | [ad/es] no console errors at 390 | [] |
| PASS | [ad/es] brand does not overlap its CTA or menu button at 390 | {"brandRight": 229, "overlapCta": false, "overlapMenu": false} |
| PASS | [ad/es] 117 markers at 390 | "ok" |
| PASS | [ad/es] mobile menu opens | true |
| PASS | [ad/es] navigation link scrolls to the merchants section | 72 |
| PASS | [ad] EN/ES parity: same section ids in same order | ["hero", "lake", "bitcoin", "transport", "community", "tours", "expats", "about"] |
| PASS | [ad] EN/ES parity: placeholders, nav targets, h2 and image counts | {"placeholders": ["atm-locations", "contact-email", "expat-contact", "facebook", "meetup-dates", "meetup-venues", "school-list", "tomek-bio-photo", "tour-booking", "tour-booking-details", "whatsapp-invite-url"], "h2": 7, |
| PASS | [ad] every nav link targets an existing section | ["#lake", "#bitcoin", "#transport", "#community", "#tours", "#expats", "#about"] |
| PASS | [ad] no section dropped (map, merchants, community, tours, expats, boat/tuk tuk, ATM, history) | [] |
| PASS | [ad] browser language es: opening EN redirects to /es/ | "http://127.0.0.1:18431/es/" |
| PASS | [ad] EN switch opens the English root and stores the choice | "http://127.0.0.1:18431/" |
| PASS | [ad] ES switch opens /es/ | "http://127.0.0.1:18431/es/" |
| PASS | [ad] browser language en: opening /es/ redirects to EN | "http://127.0.0.1:18431/" |
| PASS | [ad] configurable placeholder link shows 'coming soon' toast | "toast" |
| PASS | [ad] placeholder badge visible in preview | "\"Placeholder: whatsapp-invite-url\"" |
| PASS | old address /v/ redirects to the site | "http://127.0.0.1:18431/" |
| PASS | old address /v/ad/ redirects to the site | "http://127.0.0.1:18431/" |
| PASS | old address /v/ad/es/ redirects to the site | "http://127.0.0.1:18431/es/" |
| PASS | old address /variants/ redirects to the site | "http://127.0.0.1:18431/" |
| PASS | old address /variants/es/ redirects to the site | "http://127.0.0.1:18431/es/" |
| PASS | every data-placeholder is listed in HANDOFF.md | {"placeholders": ["atm-locations", "contact-email", "expat-contact", "facebook", "meetup-dates", "meetup-venues", "school-list", "tomek-bio-photo", "tour-booking", "tour-booking-details", "whatsapp-invite-url"], "missing |