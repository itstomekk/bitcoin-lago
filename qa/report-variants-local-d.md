# Variants QA report (local-d)

Base URL: http://127.0.0.1:18431/
Variants: d
PASS 96 / FAIL 0

| Result | Gate | Evidence |
|---|---|---|
| PASS | robots.txt Disallow while private | 200 |
| PASS | [d/en] HTTP 200 http://127.0.0.1:18431/v/d/ | 200 |
| PASS | [d/en] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin on Lake Atitlán, Guatemala", "desc_len": 158} |
| PASS | [d/en] meta robots noindex,nofollow | "present" |
| PASS | [d/en] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/d/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/d/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/d/"]] |
| PASS | [d/en] html lang + data-design | "en" |
| PASS | [d/en] every referenced asset and link returns 200 | {"checked": 48, "bad": []} |
| PASS | [d/en] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [d/en] page weight under 3 MB excluding map tiles | "762 KB" |
| PASS | [d/en] no horizontal overflow at 1440 | {"sw": 1440, "cw": 1440} |
| PASS | [d/en] no text leaves the screen at 1440 | [] |
| PASS | [d/en] every section fills the screen (>=0.95 of viewport height) | [["hero", 1], ["lake", 1.29], ["bitcoin", 1.78], ["transport", 1.09], ["community", 1.06], ["tours", 1], ["expats", 1], ["about", 1]] |
| PASS | [d/en] map ready and renders 117 markers | {"state": "ready", "markers": 117, "tiles": 16} |
| PASS | [d/en] list count == marker count == 117 | {"cards": 117, "markers": 117, "hook": {"m": 117, "c": 117, "v": 117, "p": 117}} |
| PASS | [d/en] count text shows 117 | "Showing 117 of 117 places" |
| PASS | [d/en] markers use the design's own colour token | {"fills": ["#f2b632"], "token": "#f2b632"} |
| PASS | [d/en] search filters list and map together | {"c": 6, "m": 6, "paths": 6} |
| PASS | [d/en] category chip filters (stay) | {"c": 16, "m": 16, "pressed": "stay"} |
| PASS | [d/en] village filter | {"c": 10, "m": 10} |
| PASS | [d/en] empty state | {"c": 0, "m": 0, "empty": true} |
| PASS | [d/en] reset restores 117 | {"c": 117, "m": 117} |
| PASS | [d/en] ride 'Show on map' opens a popup | "popup" |
| PASS | [d/en] every image has alt text | {"images": 9, "bad": []} |
| PASS | [d/en] only local Commons photos, each with Commons + licence credit | {"photos": 8, "no_credit": [], "other_images": []} |
| PASS | [d/en] no broken images | "ok" |
| PASS | [d/en] no 'official'/'oficial' claim | "none" |
| PASS | [d/en] no em or en dashes in visible text | [] |
| PASS | [d/en] merchant check note present | "ok" |
| PASS | [d/en] 117 places + 50+ claim + data date | "ok" |
| PASS | [d/en] OSM/ODbL, BTC Map and Commons credits in footer | "ok" |
| PASS | [d/en] floating Design switcher: A B C D E, current marked, fixed, in view | {"letters": ["A", "B", "C", "D", "E"], "cur": ["D"], "hrefs": ["../a/", "../b/", "../c/", "./", "../e/", "../../variants/"], "inView": true, "fixed": "fixed"} |
| PASS | [d/en] switcher goes to design B in the same language and remembers it | {"url": "http://127.0.0.1:18431/v/b/", "stored": "b"} |
| PASS | [d/en] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [d/en] 1440 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 8, "lowest_ratio": 9.64, "failures": []} |
| PASS | [d/en] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [d/en] no text leaves the screen at 390 | [] |
| PASS | [d/en] no console errors at 390 | [] |
| PASS | [d/en] brand text does not run into the language switch or menu button at 390 | {"brandRight": 223, "langLeft": 246, "overlapLang": false, "overlapMenu": false} |
| PASS | [d/en] 117 markers at 390 | "ok" |
| PASS | [d/en] switcher fits at 390 | {"right": 382, "vw": 390, "h": 44} |
| PASS | [d/en] mobile menu opens | true |
| PASS | [d/en] menu link scrolls to the merchants section | 84 |
| PASS | [d/en] 390 axe-core WCAG A/AA violations | [] |
| PASS | [d/en] 390 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 8, "lowest_ratio": 9.67, "failures": []} |
| PASS | [d/es] HTTP 200 http://127.0.0.1:18431/v/d/es/ | 200 |
| PASS | [d/es] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin en el Lago de Atitlán, Guatemala", "desc_len": 179} |
| PASS | [d/es] meta robots noindex,nofollow | "present" |
| PASS | [d/es] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/d/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/d/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/d/"]] |
| PASS | [d/es] html lang + data-design | "es" |
| PASS | [d/es] every referenced asset and link returns 200 | {"checked": 48, "bad": []} |
| PASS | [d/es] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [d/es] page weight under 3 MB excluding map tiles | "763 KB" |
| PASS | [d/es] no horizontal overflow at 1440 | {"sw": 1440, "cw": 1440} |
| PASS | [d/es] no text leaves the screen at 1440 | [] |
| PASS | [d/es] every section fills the screen (>=0.95 of viewport height) | [["hero", 1], ["lake", 1.29], ["bitcoin", 1.78], ["transport", 1.09], ["community", 1.07], ["tours", 1], ["expats", 1], ["about", 1]] |
| PASS | [d/es] map ready and renders 117 markers | {"state": "ready", "markers": 117, "tiles": 16} |
| PASS | [d/es] list count == marker count == 117 | {"cards": 117, "markers": 117, "hook": {"m": 117, "c": 117, "v": 117, "p": 117}} |
| PASS | [d/es] count text shows 117 | "Mostrando 117 de 117 lugares" |
| PASS | [d/es] markers use the design's own colour token | {"fills": ["#f2b632"], "token": "#f2b632"} |
| PASS | [d/es] search filters list and map together | {"c": 17, "m": 17, "paths": 17} |
| PASS | [d/es] category chip filters (stay) | {"c": 16, "m": 16, "pressed": "stay"} |
| PASS | [d/es] village filter | {"c": 10, "m": 10} |
| PASS | [d/es] empty state | {"c": 0, "m": 0, "empty": true} |
| PASS | [d/es] reset restores 117 | {"c": 117, "m": 117} |
| PASS | [d/es] ride 'Show on map' opens a popup | "popup" |
| PASS | [d/es] every image has alt text | {"images": 9, "bad": []} |
| PASS | [d/es] only local Commons photos, each with Commons + licence credit | {"photos": 8, "no_credit": [], "other_images": []} |
| PASS | [d/es] no broken images | "ok" |
| PASS | [d/es] no 'official'/'oficial' claim | "none" |
| PASS | [d/es] no em or en dashes in visible text | [] |
| PASS | [d/es] merchant check note present | "ok" |
| PASS | [d/es] 117 places + 50+ claim + data date | "ok" |
| PASS | [d/es] OSM/ODbL, BTC Map and Commons credits in footer | "ok" |
| PASS | [d/es] floating Design switcher: A B C D E, current marked, fixed, in view | {"letters": ["A", "B", "C", "D", "E"], "cur": ["D"], "hrefs": ["../../a/es/", "../../b/es/", "../../c/es/", "./", "../../e/es/", "../../../variants/es/"], "inView": true, "fixed": "fixed"} |
| PASS | [d/es] switcher goes to design B in the same language and remembers it | {"url": "http://127.0.0.1:18431/v/b/es/", "stored": "b"} |
| PASS | [d/es] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [d/es] 1440 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 8, "lowest_ratio": 9.67, "failures": []} |
| PASS | [d/es] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [d/es] no text leaves the screen at 390 | [] |
| PASS | [d/es] no console errors at 390 | [] |
| PASS | [d/es] brand text does not run into the language switch or menu button at 390 | {"brandRight": 223, "langLeft": 246, "overlapLang": false, "overlapMenu": false} |
| PASS | [d/es] 117 markers at 390 | "ok" |
| PASS | [d/es] switcher fits at 390 | {"right": 382, "vw": 390, "h": 44} |
| PASS | [d/es] mobile menu opens | true |
| PASS | [d/es] menu link scrolls to the merchants section | 84 |
| PASS | [d] EN/ES parity: same section ids in same order | ["hero", "lake", "bitcoin", "transport", "community", "tours", "expats", "about"] |
| PASS | [d] EN/ES parity: placeholders, nav targets, h2 and image counts | {"placeholders": ["atm-locations", "contact-email", "expat-contact", "facebook", "meetup-dates", "meetup-venues", "school-list", "tomek-bio-photo", "tour-booking", "tour-booking-details", "whatsapp-invite-url"], "h2": 7, |
| PASS | [d] every nav link targets an existing section | ["#lake", "#bitcoin", "#transport", "#community", "#tours", "#expats", "#about"] |
| PASS | [d] no section dropped (map, merchants, community, tours, expats, boat/tuk tuk, ATM, history) | [] |
| PASS | [d] browser language es: opening EN redirects to /es/ | "http://127.0.0.1:18431/v/d/es/" |
| PASS | [d] EN switch stays in this design and stores the choice | "http://127.0.0.1:18431/v/d/" |
| PASS | [d] ES switch stays in this design | "http://127.0.0.1:18431/v/d/es/" |
| PASS | [d] browser language en: opening /es/ redirects to EN | "http://127.0.0.1:18431/v/d/" |
| PASS | [d] placeholder button shows 'coming soon' toast | "toast" |
| PASS | [d] placeholder badge visible in preview | "\"Placeholder: whatsapp-invite-url\"" |
| PASS | every data-placeholder is listed in HANDOFF.md | {"placeholders": ["atm-locations", "contact-email", "expat-contact", "facebook", "meetup-dates", "meetup-venues", "school-list", "tomek-bio-photo", "tour-booking", "tour-booking-details", "whatsapp-invite-url"], "missing |