# Variants QA report (local-e)

Base URL: http://127.0.0.1:18431/
Variants: e
PASS 96 / FAIL 0

| Result | Gate | Evidence |
|---|---|---|
| PASS | robots.txt Disallow while private | 200 |
| PASS | [e/en] HTTP 200 http://127.0.0.1:18431/v/e/ | 200 |
| PASS | [e/en] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin on Lake Atitlán, Guatemala", "desc_len": 158} |
| PASS | [e/en] meta robots noindex,nofollow | "present" |
| PASS | [e/en] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/e/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/e/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/e/"]] |
| PASS | [e/en] html lang + data-design | "en" |
| PASS | [e/en] every referenced asset and link returns 200 | {"checked": 48, "bad": []} |
| PASS | [e/en] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [e/en] page weight under 3 MB excluding map tiles | "947 KB" |
| PASS | [e/en] no horizontal overflow at 1440 | {"sw": 1440, "cw": 1440} |
| PASS | [e/en] no text leaves the screen at 1440 | [] |
| PASS | [e/en] every section fills the screen (>=0.95 of viewport height) | [["hero", 1], ["lake", 2.56], ["bitcoin", 1.64], ["transport", 1.06], ["community", 1.07], ["tours", 1], ["expats", 1], ["about", 1.07]] |
| PASS | [e/en] map ready and renders 117 markers | {"state": "ready", "markers": 117, "tiles": 16} |
| PASS | [e/en] list count == marker count == 117 | {"cards": 117, "markers": 117, "hook": {"m": 117, "c": 117, "v": 117, "p": 117}} |
| PASS | [e/en] count text shows 117 | "Showing 117 of 117 places" |
| PASS | [e/en] markers use the design's own colour token | {"fills": ["#f7931a"], "token": "#f7931a"} |
| PASS | [e/en] search filters list and map together | {"c": 6, "m": 6, "paths": 6} |
| PASS | [e/en] category chip filters (stay) | {"c": 16, "m": 16, "pressed": "stay"} |
| PASS | [e/en] village filter | {"c": 10, "m": 10} |
| PASS | [e/en] empty state | {"c": 0, "m": 0, "empty": true} |
| PASS | [e/en] reset restores 117 | {"c": 117, "m": 117} |
| PASS | [e/en] ride 'Show on map' opens a popup | "popup" |
| PASS | [e/en] every image has alt text | {"images": 9, "bad": []} |
| PASS | [e/en] only local Commons photos, each with Commons + licence credit | {"photos": 8, "no_credit": [], "other_images": []} |
| PASS | [e/en] no broken images | "ok" |
| PASS | [e/en] no 'official'/'oficial' claim | "none" |
| PASS | [e/en] no em or en dashes in visible text | [] |
| PASS | [e/en] merchant check note present | "ok" |
| PASS | [e/en] 117 places + 50+ claim + data date | "ok" |
| PASS | [e/en] OSM/ODbL, BTC Map and Commons credits in footer | "ok" |
| PASS | [e/en] floating Design switcher: A B C D E, current marked, fixed, in view | {"letters": ["A", "B", "C", "D", "E"], "cur": ["E"], "hrefs": ["../a/", "../b/", "../c/", "../d/", "./", "../../variants/"], "inView": true, "fixed": "fixed"} |
| PASS | [e/en] switcher goes to design B in the same language and remembers it | {"url": "http://127.0.0.1:18431/v/b/", "stored": "b"} |
| PASS | [e/en] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [e/en] 1440 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 38, "lowest_ratio": 5.21, "failures": []} |
| PASS | [e/en] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [e/en] no text leaves the screen at 390 | [] |
| PASS | [e/en] no console errors at 390 | [] |
| PASS | [e/en] brand text does not run into the language switch or menu button at 390 | {"brandRight": 0, "langLeft": 228, "overlapLang": false, "overlapMenu": false} |
| PASS | [e/en] 117 markers at 390 | "ok" |
| PASS | [e/en] switcher fits at 390 | {"right": 382, "vw": 390, "h": 44} |
| PASS | [e/en] mobile menu opens | true |
| PASS | [e/en] menu link scrolls to the merchants section | 90 |
| PASS | [e/en] 390 axe-core WCAG A/AA violations | [] |
| PASS | [e/en] 390 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 32, "lowest_ratio": 5.07, "failures": []} |
| PASS | [e/es] HTTP 200 http://127.0.0.1:18431/v/e/es/ | 200 |
| PASS | [e/es] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin en el Lago de Atitlán, Guatemala", "desc_len": 179} |
| PASS | [e/es] meta robots noindex,nofollow | "present" |
| PASS | [e/es] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/e/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/e/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/e/"]] |
| PASS | [e/es] html lang + data-design | "es" |
| PASS | [e/es] every referenced asset and link returns 200 | {"checked": 48, "bad": []} |
| PASS | [e/es] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [e/es] page weight under 3 MB excluding map tiles | "948 KB" |
| PASS | [e/es] no horizontal overflow at 1440 | {"sw": 1440, "cw": 1440} |
| PASS | [e/es] no text leaves the screen at 1440 | [] |
| PASS | [e/es] every section fills the screen (>=0.95 of viewport height) | [["hero", 1], ["lake", 2.56], ["bitcoin", 1.64], ["transport", 1.06], ["community", 1.09], ["tours", 1], ["expats", 1], ["about", 1.07]] |
| PASS | [e/es] map ready and renders 117 markers | {"state": "ready", "markers": 117, "tiles": 16} |
| PASS | [e/es] list count == marker count == 117 | {"cards": 117, "markers": 117, "hook": {"m": 117, "c": 117, "v": 117, "p": 117}} |
| PASS | [e/es] count text shows 117 | "Mostrando 117 de 117 lugares" |
| PASS | [e/es] markers use the design's own colour token | {"fills": ["#f7931a"], "token": "#f7931a"} |
| PASS | [e/es] search filters list and map together | {"c": 17, "m": 17, "paths": 17} |
| PASS | [e/es] category chip filters (stay) | {"c": 16, "m": 16, "pressed": "stay"} |
| PASS | [e/es] village filter | {"c": 10, "m": 10} |
| PASS | [e/es] empty state | {"c": 0, "m": 0, "empty": true} |
| PASS | [e/es] reset restores 117 | {"c": 117, "m": 117} |
| PASS | [e/es] ride 'Show on map' opens a popup | "popup" |
| PASS | [e/es] every image has alt text | {"images": 9, "bad": []} |
| PASS | [e/es] only local Commons photos, each with Commons + licence credit | {"photos": 8, "no_credit": [], "other_images": []} |
| PASS | [e/es] no broken images | "ok" |
| PASS | [e/es] no 'official'/'oficial' claim | "none" |
| PASS | [e/es] no em or en dashes in visible text | [] |
| PASS | [e/es] merchant check note present | "ok" |
| PASS | [e/es] 117 places + 50+ claim + data date | "ok" |
| PASS | [e/es] OSM/ODbL, BTC Map and Commons credits in footer | "ok" |
| PASS | [e/es] floating Design switcher: A B C D E, current marked, fixed, in view | {"letters": ["A", "B", "C", "D", "E"], "cur": ["E"], "hrefs": ["../../a/es/", "../../b/es/", "../../c/es/", "../../d/es/", "./", "../../../variants/es/"], "inView": true, "fixed": "fixed"} |
| PASS | [e/es] switcher goes to design B in the same language and remembers it | {"url": "http://127.0.0.1:18431/v/b/es/", "stored": "b"} |
| PASS | [e/es] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [e/es] 1440 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 38, "lowest_ratio": 5.21, "failures": []} |
| PASS | [e/es] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [e/es] no text leaves the screen at 390 | [] |
| PASS | [e/es] no console errors at 390 | [] |
| PASS | [e/es] brand text does not run into the language switch or menu button at 390 | {"brandRight": 0, "langLeft": 228, "overlapLang": false, "overlapMenu": false} |
| PASS | [e/es] 117 markers at 390 | "ok" |
| PASS | [e/es] switcher fits at 390 | {"right": 382, "vw": 390, "h": 44} |
| PASS | [e/es] mobile menu opens | true |
| PASS | [e/es] menu link scrolls to the merchants section | 90 |
| PASS | [e] EN/ES parity: same section ids in same order | ["hero", "lake", "bitcoin", "transport", "community", "tours", "expats", "about"] |
| PASS | [e] EN/ES parity: placeholders, nav targets, h2 and image counts | {"placeholders": ["atm-locations", "contact-email", "expat-contact", "facebook", "meetup-dates", "meetup-venues", "school-list", "tomek-bio-photo", "tour-booking", "tour-booking-details", "whatsapp-invite-url"], "h2": 7, |
| PASS | [e] every nav link targets an existing section | ["#lake", "#bitcoin", "#transport", "#community", "#tours", "#expats", "#about"] |
| PASS | [e] no section dropped (map, merchants, community, tours, expats, boat/tuk tuk, ATM, history) | [] |
| PASS | [e] browser language es: opening EN redirects to /es/ | "http://127.0.0.1:18431/v/e/es/" |
| PASS | [e] EN switch stays in this design and stores the choice | "http://127.0.0.1:18431/v/e/" |
| PASS | [e] ES switch stays in this design | "http://127.0.0.1:18431/v/e/es/" |
| PASS | [e] browser language en: opening /es/ redirects to EN | "http://127.0.0.1:18431/v/e/" |
| PASS | [e] placeholder button shows 'coming soon' toast | "toast" |
| PASS | [e] placeholder badge visible in preview | "\"Placeholder: whatsapp-invite-url\"" |
| PASS | every data-placeholder is listed in HANDOFF.md | {"placeholders": ["atm-locations", "contact-email", "expat-contact", "facebook", "meetup-dates", "meetup-venues", "school-list", "tomek-bio-photo", "tour-booking", "tour-booking-details", "whatsapp-invite-url"], "missing |