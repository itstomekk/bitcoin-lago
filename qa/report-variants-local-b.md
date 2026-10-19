# Variants QA report (local-b)

Base URL: http://127.0.0.1:18431/
Variants: b
PASS 96 / FAIL 0

| Result | Gate | Evidence |
|---|---|---|
| PASS | robots.txt Disallow while private | 200 |
| PASS | [b/en] HTTP 200 http://127.0.0.1:18431/v/b/ | 200 |
| PASS | [b/en] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin on Lake Atitlán, Guatemala", "desc_len": 158} |
| PASS | [b/en] meta robots noindex,nofollow | "present" |
| PASS | [b/en] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/b/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/b/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/b/"]] |
| PASS | [b/en] html lang + data-design | "en" |
| PASS | [b/en] every referenced asset and link returns 200 | {"checked": 48, "bad": []} |
| PASS | [b/en] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [b/en] page weight under 3 MB excluding map tiles | "746 KB" |
| PASS | [b/en] no horizontal overflow at 1440 | {"sw": 1440, "cw": 1440} |
| PASS | [b/en] no text leaves the screen at 1440 | [] |
| PASS | [b/en] every section fills the screen (>=0.95 of viewport height) | [["hero", 1], ["lake", 1.65], ["bitcoin", 2.64], ["transport", 1.24], ["community", 1.06], ["tours", 1.04], ["expats", 1], ["about", 1]] |
| PASS | [b/en] map ready and renders 117 markers | {"state": "ready", "markers": 117, "tiles": 24} |
| PASS | [b/en] list count == marker count == 117 | {"cards": 117, "markers": 117, "hook": {"m": 117, "c": 117, "v": 117, "p": 117}} |
| PASS | [b/en] count text shows 117 | "Showing 117 of 117 places" |
| PASS | [b/en] markers use the design's own colour token | {"fills": ["#0f0f0f"], "token": "#0f0f0f"} |
| PASS | [b/en] search filters list and map together | {"c": 6, "m": 6, "paths": 6} |
| PASS | [b/en] category chip filters (stay) | {"c": 16, "m": 16, "pressed": "stay"} |
| PASS | [b/en] village filter | {"c": 10, "m": 10} |
| PASS | [b/en] empty state | {"c": 0, "m": 0, "empty": true} |
| PASS | [b/en] reset restores 117 | {"c": 117, "m": 117} |
| PASS | [b/en] ride 'Show on map' opens a popup | "popup" |
| PASS | [b/en] every image has alt text | {"images": 9, "bad": []} |
| PASS | [b/en] only local Commons photos, each with Commons + licence credit | {"photos": 8, "no_credit": [], "other_images": []} |
| PASS | [b/en] no broken images | "ok" |
| PASS | [b/en] no 'official'/'oficial' claim | "none" |
| PASS | [b/en] no em or en dashes in visible text | [] |
| PASS | [b/en] merchant check note present | "ok" |
| PASS | [b/en] 117 places + 50+ claim + data date | "ok" |
| PASS | [b/en] OSM/ODbL, BTC Map and Commons credits in footer | "ok" |
| PASS | [b/en] floating Design switcher: A B C D E, current marked, fixed, in view | {"letters": ["A", "B", "C", "D", "E"], "cur": ["B"], "hrefs": ["../a/", "./", "../c/", "../d/", "../e/", "../../variants/"], "inView": true, "fixed": "fixed"} |
| PASS | [b/en] switcher goes to design C in the same language and remembers it | {"url": "http://127.0.0.1:18431/v/c/", "stored": "c"} |
| PASS | [b/en] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [b/en] 1440 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 7, "lowest_ratio": 8.35, "failures": []} |
| PASS | [b/en] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [b/en] no text leaves the screen at 390 | [] |
| PASS | [b/en] no console errors at 390 | [] |
| PASS | [b/en] brand text does not run into the language switch or menu button at 390 | {"brandRight": 258, "langLeft": 304, "overlapLang": false, "overlapMenu": false} |
| PASS | [b/en] 117 markers at 390 | "ok" |
| PASS | [b/en] switcher fits at 390 | {"right": 382, "vw": 390, "h": 44} |
| PASS | [b/en] mobile menu opens | true |
| PASS | [b/en] menu link scrolls to the merchants section | 70 |
| PASS | [b/en] 390 axe-core WCAG A/AA violations | [] |
| PASS | [b/en] 390 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 7, "lowest_ratio": 8.35, "failures": []} |
| PASS | [b/es] HTTP 200 http://127.0.0.1:18431/v/b/es/ | 200 |
| PASS | [b/es] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin en el Lago de Atitlán, Guatemala", "desc_len": 179} |
| PASS | [b/es] meta robots noindex,nofollow | "present" |
| PASS | [b/es] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/b/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/b/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/b/"]] |
| PASS | [b/es] html lang + data-design | "es" |
| PASS | [b/es] every referenced asset and link returns 200 | {"checked": 48, "bad": []} |
| PASS | [b/es] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [b/es] page weight under 3 MB excluding map tiles | "747 KB" |
| PASS | [b/es] no horizontal overflow at 1440 | {"sw": 1440, "cw": 1440} |
| PASS | [b/es] no text leaves the screen at 1440 | [] |
| PASS | [b/es] every section fills the screen (>=0.95 of viewport height) | [["hero", 1], ["lake", 1.65], ["bitcoin", 2.64], ["transport", 1.24], ["community", 1.09], ["tours", 1.04], ["expats", 1], ["about", 1]] |
| PASS | [b/es] map ready and renders 117 markers | {"state": "ready", "markers": 117, "tiles": 24} |
| PASS | [b/es] list count == marker count == 117 | {"cards": 117, "markers": 117, "hook": {"m": 117, "c": 117, "v": 117, "p": 117}} |
| PASS | [b/es] count text shows 117 | "Mostrando 117 de 117 lugares" |
| PASS | [b/es] markers use the design's own colour token | {"fills": ["#0f0f0f"], "token": "#0f0f0f"} |
| PASS | [b/es] search filters list and map together | {"c": 17, "m": 17, "paths": 17} |
| PASS | [b/es] category chip filters (stay) | {"c": 16, "m": 16, "pressed": "stay"} |
| PASS | [b/es] village filter | {"c": 10, "m": 10} |
| PASS | [b/es] empty state | {"c": 0, "m": 0, "empty": true} |
| PASS | [b/es] reset restores 117 | {"c": 117, "m": 117} |
| PASS | [b/es] ride 'Show on map' opens a popup | "popup" |
| PASS | [b/es] every image has alt text | {"images": 9, "bad": []} |
| PASS | [b/es] only local Commons photos, each with Commons + licence credit | {"photos": 8, "no_credit": [], "other_images": []} |
| PASS | [b/es] no broken images | "ok" |
| PASS | [b/es] no 'official'/'oficial' claim | "none" |
| PASS | [b/es] no em or en dashes in visible text | [] |
| PASS | [b/es] merchant check note present | "ok" |
| PASS | [b/es] 117 places + 50+ claim + data date | "ok" |
| PASS | [b/es] OSM/ODbL, BTC Map and Commons credits in footer | "ok" |
| PASS | [b/es] floating Design switcher: A B C D E, current marked, fixed, in view | {"letters": ["A", "B", "C", "D", "E"], "cur": ["B"], "hrefs": ["../../a/es/", "./", "../../c/es/", "../../d/es/", "../../e/es/", "../../../variants/es/"], "inView": true, "fixed": "fixed"} |
| PASS | [b/es] switcher goes to design C in the same language and remembers it | {"url": "http://127.0.0.1:18431/v/c/es/", "stored": "c"} |
| PASS | [b/es] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [b/es] 1440 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 7, "lowest_ratio": 7.34, "failures": []} |
| PASS | [b/es] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [b/es] no text leaves the screen at 390 | [] |
| PASS | [b/es] no console errors at 390 | [] |
| PASS | [b/es] brand text does not run into the language switch or menu button at 390 | {"brandRight": 258, "langLeft": 304, "overlapLang": false, "overlapMenu": false} |
| PASS | [b/es] 117 markers at 390 | "ok" |
| PASS | [b/es] switcher fits at 390 | {"right": 382, "vw": 390, "h": 44} |
| PASS | [b/es] mobile menu opens | true |
| PASS | [b/es] menu link scrolls to the merchants section | 70 |
| PASS | [b] EN/ES parity: same section ids in same order | ["hero", "lake", "bitcoin", "transport", "community", "tours", "expats", "about"] |
| PASS | [b] EN/ES parity: placeholders, nav targets, h2 and image counts | {"placeholders": ["atm-locations", "contact-email", "expat-contact", "facebook", "meetup-dates", "meetup-venues", "school-list", "tomek-bio-photo", "tour-booking", "tour-booking-details", "whatsapp-invite-url"], "h2": 7, |
| PASS | [b] every nav link targets an existing section | ["#lake", "#bitcoin", "#transport", "#community", "#tours", "#expats", "#about"] |
| PASS | [b] no section dropped (map, merchants, community, tours, expats, boat/tuk tuk, ATM, history) | [] |
| PASS | [b] browser language es: opening EN redirects to /es/ | "http://127.0.0.1:18431/v/b/es/" |
| PASS | [b] EN switch stays in this design and stores the choice | "http://127.0.0.1:18431/v/b/" |
| PASS | [b] ES switch stays in this design | "http://127.0.0.1:18431/v/b/es/" |
| PASS | [b] browser language en: opening /es/ redirects to EN | "http://127.0.0.1:18431/v/b/" |
| PASS | [b] placeholder button shows 'coming soon' toast | "toast" |
| PASS | [b] placeholder badge visible in preview | "\"Placeholder: whatsapp-invite-url\"" |
| PASS | every data-placeholder is listed in HANDOFF.md | {"placeholders": ["atm-locations", "contact-email", "expat-contact", "facebook", "meetup-dates", "meetup-venues", "school-list", "tomek-bio-photo", "tour-booking", "tour-booking-details", "whatsapp-invite-url"], "missing |