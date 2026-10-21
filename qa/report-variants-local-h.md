# Variants QA report (local-h)

Base URL: http://127.0.0.1:18500/
Variants: h
PASS 98 / FAIL 0

| Result | Gate | Evidence |
|---|---|---|
| PASS | robots.txt Disallow while private | 200 |
| PASS | [h/en] HTTP 200 http://127.0.0.1:18500/v/h/ | 200 |
| PASS | [h/en] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin on Lake Atitlán, Guatemala", "desc_len": 158} |
| PASS | [h/en] meta robots noindex,nofollow | "present" |
| PASS | [h/en] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/h/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/h/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/h/"]] |
| PASS | [h/en] html lang + data-design | "en" |
| PASS | [h/en] every referenced asset and link returns 200 | {"checked": 116, "bad": []} |
| PASS | [h/en] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [h/en] page weight under 3 MB excluding map tiles | "2163 KB" |
| PASS | [h/en] no horizontal overflow at 1440 | {"sw": 1440, "cw": 1440} |
| PASS | [h/en] no text leaves the screen at 1440 | [] |
| PASS | [h/en] every section fills the screen (>=0.95 of viewport height) | [["hero", 0.95], ["lake", 2.56], ["bitcoin", 1.75], ["transport", 1.97], ["community", 2.64], ["tours", 1.85], ["expats", 0.95], ["about", 6.65]] |
| PASS | [h/en] map ready and renders 117 markers | {"state": "ready", "markers": 117, "tiles": 16} |
| PASS | [h/en] list count == marker count == 117 | {"cards": 117, "markers": 117, "hook": {"m": 117, "c": 117, "v": 117, "p": 117}} |
| PASS | [h/en] count text shows 117 | "Showing 117 of 117 places" |
| PASS | [h/en] markers use the design's own colour token | {"fills": ["oklch(45% 0.19 264)"], "token": "oklch(45% 0.19 264)"} |
| PASS | [h/en] search filters list and map together | {"c": 6, "m": 6, "paths": 6} |
| PASS | [h/en] category chip filters (stay) | {"c": 16, "m": 16, "pressed": "stay"} |
| PASS | [h/en] village filter | {"c": 10, "m": 10} |
| PASS | [h/en] empty state | {"c": 0, "m": 0, "empty": true} |
| PASS | [h/en] reset restores 117 | {"c": 117, "m": 117} |
| PASS | [h/en] ride 'Show on map' opens a popup | "popup" |
| PASS | [h/en] every image has alt text | {"images": 49, "bad": []} |
| PASS | [h/en] only local photos, each with a Commons, approved community-archive, or linked press credit | {"photos": 48, "no_credit": [], "other_images": []} |
| PASS | [h/en] all 30 press photos appear once with visible linked credits | {"count": 30, "unique": 30, "missing": [], "bad_credit": []} |
| PASS | [h/en] no broken images | "ok" |
| PASS | [h/en] no 'official'/'oficial' claim | "none" |
| PASS | [h/en] no em or en dashes in visible text | [] |
| PASS | [h/en] merchant check note present | "ok" |
| PASS | [h/en] 117 places + 50+ claim + data date | "ok" |
| PASS | [h/en] OSM/ODbL, BTC Map and Commons credits in footer | "ok" |
| PASS | [h/en] floating Design switcher: all finished designs, current marked, fixed, in view | {"letters": ["A", "C", "D", "AC", "AD", "CD", "F", "G", "H"], "cur": ["H"], "hrefs": ["../a/", "../c/", "../d/", "../ac/", "../ad/", "../cd/", "../f/", "../g/", "./", "../../variants/"], "inView": true, "fixed": "fixed"} |
| PASS | [h/en] switcher goes to design C in the same language and remembers it | {"url": "http://127.0.0.1:18500/v/c/", "stored": "c"} |
| PASS | [h/en] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [h/en] 1440 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 31, "candidates": 741, "lowest_ratio": 6.71, "failures": []} |
| PASS | [h/en] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [h/en] no text leaves the screen at 390 | [] |
| PASS | [h/en] no console errors at 390 | [] |
| PASS | [h/en] brand does not overlap its CTA or menu button at 390 | {"brandRight": 92, "overlapCta": false, "overlapMenu": false} |
| PASS | [h/en] 117 markers at 390 | "ok" |
| PASS | [h/en] switcher fits at 390 | {"right": 382, "vw": 390, "h": 40} |
| PASS | [h/en] mobile section map has seven links | true |
| PASS | [h/en] navigation link scrolls to the merchants section | 52 |
| PASS | [h/en] 390 axe-core WCAG A/AA violations | [] |
| PASS | [h/en] 390 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 30, "candidates": 740, "lowest_ratio": 5.74, "failures": []} |
| PASS | [h/es] HTTP 200 http://127.0.0.1:18500/v/h/es/ | 200 |
| PASS | [h/es] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin en el Lago de Atitlán, Guatemala", "desc_len": 179} |
| PASS | [h/es] meta robots noindex,nofollow | "present" |
| PASS | [h/es] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/h/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/h/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/h/"]] |
| PASS | [h/es] html lang + data-design | "es" |
| PASS | [h/es] every referenced asset and link returns 200 | {"checked": 124, "bad": []} |
| PASS | [h/es] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [h/es] page weight under 3 MB excluding map tiles | "2164 KB" |
| PASS | [h/es] no horizontal overflow at 1440 | {"sw": 1440, "cw": 1440} |
| PASS | [h/es] no text leaves the screen at 1440 | [] |
| PASS | [h/es] every section fills the screen (>=0.95 of viewport height) | [["hero", 0.95], ["lake", 2.44], ["bitcoin", 1.77], ["transport", 1.97], ["community", 2.82], ["tours", 1.69], ["expats", 1], ["about", 6.65]] |
| PASS | [h/es] map ready and renders 117 markers | {"state": "ready", "markers": 117, "tiles": 16} |
| PASS | [h/es] list count == marker count == 117 | {"cards": 117, "markers": 117, "hook": {"m": 117, "c": 117, "v": 117, "p": 117}} |
| PASS | [h/es] count text shows 117 | "Mostrando 117 de 117 lugares" |
| PASS | [h/es] markers use the design's own colour token | {"fills": ["oklch(45% 0.19 264)"], "token": "oklch(45% 0.19 264)"} |
| PASS | [h/es] search filters list and map together | {"c": 17, "m": 17, "paths": 17} |
| PASS | [h/es] category chip filters (stay) | {"c": 16, "m": 16, "pressed": "stay"} |
| PASS | [h/es] village filter | {"c": 10, "m": 10} |
| PASS | [h/es] empty state | {"c": 0, "m": 0, "empty": true} |
| PASS | [h/es] reset restores 117 | {"c": 117, "m": 117} |
| PASS | [h/es] ride 'Show on map' opens a popup | "popup" |
| PASS | [h/es] every image has alt text | {"images": 49, "bad": []} |
| PASS | [h/es] only local photos, each with a Commons, approved community-archive, or linked press credit | {"photos": 48, "no_credit": [], "other_images": []} |
| PASS | [h/es] all 30 press photos appear once with visible linked credits | {"count": 30, "unique": 30, "missing": [], "bad_credit": []} |
| PASS | [h/es] no broken images | "ok" |
| PASS | [h/es] no 'official'/'oficial' claim | "none" |
| PASS | [h/es] no em or en dashes in visible text | [] |
| PASS | [h/es] merchant check note present | "ok" |
| PASS | [h/es] 117 places + 50+ claim + data date | "ok" |
| PASS | [h/es] OSM/ODbL, BTC Map and Commons credits in footer | "ok" |
| PASS | [h/es] floating Design switcher: all finished designs, current marked, fixed, in view | {"letters": ["A", "C", "D", "AC", "AD", "CD", "F", "G", "H"], "cur": ["H"], "hrefs": ["../../a/es/", "../../c/es/", "../../d/es/", "../../ac/es/", "../../ad/es/", "../../cd/es/", "../../f/es/", "../../g/es/", "./", "../. |
| PASS | [h/es] switcher goes to design C in the same language and remembers it | {"url": "http://127.0.0.1:18500/v/c/es/", "stored": "c"} |
| PASS | [h/es] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [h/es] 1440 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 30, "candidates": 740, "lowest_ratio": 6.91, "failures": []} |
| PASS | [h/es] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [h/es] no text leaves the screen at 390 | [] |
| PASS | [h/es] no console errors at 390 | [] |
| PASS | [h/es] brand does not overlap its CTA or menu button at 390 | {"brandRight": 92, "overlapCta": false, "overlapMenu": false} |
| PASS | [h/es] 117 markers at 390 | "ok" |
| PASS | [h/es] switcher fits at 390 | {"right": 382, "vw": 390, "h": 40} |
| PASS | [h/es] mobile section map has seven links | true |
| PASS | [h/es] navigation link scrolls to the merchants section | 52 |
| PASS | [h] EN/ES parity: same section ids in same order | ["hero", "lake", "bitcoin", "transport", "community", "tours", "expats", "about"] |
| PASS | [h] EN/ES parity: placeholders, nav targets, h2 and image counts | {"placeholders": ["atm-locations", "contact-email", "expat-contact", "facebook", "meetup-dates", "meetup-venues", "school-list", "tomek-bio-photo", "tour-booking", "tour-booking-details", "whatsapp-invite-url"], "h2": 7, |
| PASS | [h] every nav link targets an existing section | ["#lake", "#community", "#bitcoin", "#transport", "#about", "#expats", "#tours", "#bitcoin"] |
| PASS | [h] no section dropped (map, merchants, community, tours, expats, boat/tuk tuk, ATM, history) | [] |
| PASS | [h] browser language es: opening EN redirects to /es/ | "http://127.0.0.1:18500/v/h/es/" |
| PASS | [h] EN switch stays in this design and stores the choice | "http://127.0.0.1:18500/v/h/" |
| PASS | [h] ES switch stays in this design | "http://127.0.0.1:18500/v/h/es/" |
| PASS | [h] browser language en: opening /es/ redirects to EN | "http://127.0.0.1:18500/v/h/" |
| PASS | [h] configurable placeholder link shows 'coming soon' toast | "toast" |
| PASS | [h] placeholder badge visible in preview | "\"Placeholder: atm-locations\"" |
| PASS | every data-placeholder is listed in HANDOFF.md | {"placeholders": ["atm-locations", "contact-email", "expat-contact", "facebook", "meetup-dates", "meetup-venues", "school-list", "tomek-bio-photo", "tour-booking", "tour-booking-details", "whatsapp-invite-url"], "missing |