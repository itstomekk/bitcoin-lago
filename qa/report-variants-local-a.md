# Variants QA report (local-a)

Base URL: http://127.0.0.1:18431/
Variants: a
PASS 92 / FAIL 2

| Result | Gate | Evidence |
|---|---|---|
| PASS | robots.txt Disallow while private | 200 |
| PASS | [a/en] HTTP 200 http://127.0.0.1:18431/v/a/ | 200 |
| PASS | [a/en] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin on Lake Atitlán, Guatemala", "desc_len": 158} |
| PASS | [a/en] meta robots noindex,nofollow | "present" |
| PASS | [a/en] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/a/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/a/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/a/"]] |
| PASS | [a/en] html lang + data-design | "en" |
| FAIL | [a/en] every referenced asset and link returns 200 | {"checked": 44, "bad": [["http://127.0.0.1:18431/v/c/", 404], ["http://127.0.0.1:18431/v/d/", 404], ["http://127.0.0.1:18431/v/e/", 404]]} |
| PASS | [a/en] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [a/en] page weight under 3 MB excluding map tiles | "687 KB" |
| PASS | [a/en] no horizontal overflow at 1440 | {"sw": 1440, "cw": 1440} |
| PASS | [a/en] no text leaves the screen at 1440 | [] |
| PASS | [a/en] every section fills the screen (>=0.95 of viewport height) | [["hero", 1], ["lake", 1.16], ["bitcoin", 1.8], ["transport", 1.01], ["community", 1], ["tours", 1], ["expats", 1], ["about", 1]] |
| PASS | [a/en] map ready and renders 117 markers | {"state": "ready", "markers": 117, "tiles": 16} |
| PASS | [a/en] list count == marker count == 117 | {"cards": 117, "markers": 117, "hook": {"m": 117, "c": 117, "v": 117, "p": 117}} |
| PASS | [a/en] count text shows 117 | "Showing 117 of 117 places" |
| PASS | [a/en] markers use the design's own colour token | {"fills": ["#b03a24"], "token": "#b03a24"} |
| PASS | [a/en] search filters list and map together | {"c": 6, "m": 6, "paths": 6} |
| PASS | [a/en] category chip filters (stay) | {"c": 16, "m": 16, "pressed": "stay"} |
| PASS | [a/en] village filter | {"c": 10, "m": 10} |
| PASS | [a/en] empty state | {"c": 0, "m": 0, "empty": true} |
| PASS | [a/en] reset restores 117 | {"c": 117, "m": 117} |
| PASS | [a/en] ride 'Show on map' opens a popup | "popup" |
| PASS | [a/en] every image has alt text | {"images": 8, "bad": []} |
| PASS | [a/en] only local Commons photos, each with Commons + licence credit | {"photos": 7, "no_credit": [], "other_images": []} |
| PASS | [a/en] no broken images | "ok" |
| PASS | [a/en] no 'official'/'oficial' claim | "none" |
| PASS | [a/en] no em or en dashes in visible text | [] |
| PASS | [a/en] merchant check note present | "ok" |
| PASS | [a/en] 117 places + 50+ claim + data date | "ok" |
| PASS | [a/en] OSM/ODbL, BTC Map and Commons credits in footer | "ok" |
| PASS | [a/en] floating Design switcher: A B C D E, current marked, fixed, in view | {"letters": ["A", "B", "C", "D", "E"], "cur": ["A"], "hrefs": ["./", "../b/", "../c/", "../d/", "../e/", "../../variants/"], "inView": true, "fixed": "fixed"} |
| PASS | [a/en] switcher goes to design B in the same language and remembers it | {"url": "http://127.0.0.1:18431/v/b/", "stored": "b"} |
| PASS | [a/en] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [a/en] 1440 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 3, "lowest_ratio": 5.96, "failures": []} |
| PASS | [a/en] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [a/en] no text leaves the screen at 390 | [] |
| PASS | [a/en] no console errors at 390 | [] |
| PASS | [a/en] 117 markers at 390 | "ok" |
| PASS | [a/en] switcher fits at 390 | {"right": 382, "vw": 390, "h": 44} |
| PASS | [a/en] mobile menu opens | true |
| PASS | [a/en] menu link scrolls to the merchants section | -0.0 |
| PASS | [a/en] 390 axe-core WCAG A/AA violations | [] |
| PASS | [a/en] 390 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 3, "lowest_ratio": 5.89, "failures": []} |
| PASS | [a/es] HTTP 200 http://127.0.0.1:18431/v/a/es/ | 200 |
| PASS | [a/es] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin en el Lago de Atitlán, Guatemala", "desc_len": 179} |
| PASS | [a/es] meta robots noindex,nofollow | "present" |
| PASS | [a/es] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/a/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/a/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/a/"]] |
| PASS | [a/es] html lang + data-design | "es" |
| FAIL | [a/es] every referenced asset and link returns 200 | {"checked": 44, "bad": [["http://127.0.0.1:18431/v/b/es/", 404], ["http://127.0.0.1:18431/v/c/es/", 404], ["http://127.0.0.1:18431/v/d/es/", 404], ["http://127.0.0.1:18431/v/e/es/", 404]]} |
| PASS | [a/es] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [a/es] page weight under 3 MB excluding map tiles | "688 KB" |
| PASS | [a/es] no horizontal overflow at 1440 | {"sw": 1440, "cw": 1440} |
| PASS | [a/es] no text leaves the screen at 1440 | [] |
| PASS | [a/es] every section fills the screen (>=0.95 of viewport height) | [["hero", 1], ["lake", 1.19], ["bitcoin", 1.8], ["transport", 1.05], ["community", 1], ["tours", 1], ["expats", 1], ["about", 1]] |
| PASS | [a/es] map ready and renders 117 markers | {"state": "ready", "markers": 117, "tiles": 16} |
| PASS | [a/es] list count == marker count == 117 | {"cards": 117, "markers": 117, "hook": {"m": 117, "c": 117, "v": 117, "p": 117}} |
| PASS | [a/es] count text shows 117 | "Mostrando 117 de 117 lugares" |
| PASS | [a/es] markers use the design's own colour token | {"fills": ["#b03a24"], "token": "#b03a24"} |
| PASS | [a/es] search filters list and map together | {"c": 17, "m": 17, "paths": 17} |
| PASS | [a/es] category chip filters (stay) | {"c": 16, "m": 16, "pressed": "stay"} |
| PASS | [a/es] village filter | {"c": 10, "m": 10} |
| PASS | [a/es] empty state | {"c": 0, "m": 0, "empty": true} |
| PASS | [a/es] reset restores 117 | {"c": 117, "m": 117} |
| PASS | [a/es] ride 'Show on map' opens a popup | "popup" |
| PASS | [a/es] every image has alt text | {"images": 8, "bad": []} |
| PASS | [a/es] only local Commons photos, each with Commons + licence credit | {"photos": 7, "no_credit": [], "other_images": []} |
| PASS | [a/es] no broken images | "ok" |
| PASS | [a/es] no 'official'/'oficial' claim | "none" |
| PASS | [a/es] no em or en dashes in visible text | [] |
| PASS | [a/es] merchant check note present | "ok" |
| PASS | [a/es] 117 places + 50+ claim + data date | "ok" |
| PASS | [a/es] OSM/ODbL, BTC Map and Commons credits in footer | "ok" |
| PASS | [a/es] floating Design switcher: A B C D E, current marked, fixed, in view | {"letters": ["A", "B", "C", "D", "E"], "cur": ["A"], "hrefs": ["./", "../../b/es/", "../../c/es/", "../../d/es/", "../../e/es/", "../../../variants/es/"], "inView": true, "fixed": "fixed"} |
| PASS | [a/es] switcher goes to design B in the same language and remembers it | {"url": "http://127.0.0.1:18431/v/b/es/", "stored": "b"} |
| PASS | [a/es] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [a/es] 1440 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 3, "lowest_ratio": 5.81, "failures": []} |
| PASS | [a/es] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [a/es] no text leaves the screen at 390 | [] |
| PASS | [a/es] no console errors at 390 | [] |
| PASS | [a/es] 117 markers at 390 | "ok" |
| PASS | [a/es] switcher fits at 390 | {"right": 382, "vw": 390, "h": 44} |
| PASS | [a/es] mobile menu opens | true |
| PASS | [a/es] menu link scrolls to the merchants section | 0 |
| PASS | [a] EN/ES parity: same section ids in same order | ["hero", "lake", "bitcoin", "transport", "community", "tours", "expats", "about"] |
| PASS | [a] EN/ES parity: placeholders, nav targets, h2 and image counts | {"placeholders": ["atm-locations", "contact-email", "expat-contact", "facebook", "meetup-dates", "meetup-venues", "school-list", "tomek-bio-photo", "tour-booking", "tour-booking-details", "whatsapp-invite-url"], "h2": 7, |
| PASS | [a] every nav link targets an existing section | ["#lake", "#bitcoin", "#transport", "#community", "#tours", "#expats", "#about"] |
| PASS | [a] no section dropped (map, merchants, community, tours, expats, boat/tuk tuk, ATM, history) | [] |
| PASS | [a] browser language es: opening EN redirects to /es/ | "http://127.0.0.1:18431/v/a/es/" |
| PASS | [a] EN switch stays in this design and stores the choice | "http://127.0.0.1:18431/v/a/" |
| PASS | [a] ES switch stays in this design | "http://127.0.0.1:18431/v/a/es/" |
| PASS | [a] browser language en: opening /es/ redirects to EN | "http://127.0.0.1:18431/v/a/" |
| PASS | [a] placeholder button shows 'coming soon' toast | "toast" |
| PASS | [a] placeholder badge visible in preview | "\"Placeholder: whatsapp-invite-url\"" |
| PASS | every data-placeholder is listed in HANDOFF.md | {"placeholders": ["atm-locations", "contact-email", "expat-contact", "facebook", "meetup-dates", "meetup-venues", "school-list", "tomek-bio-photo", "tour-booking", "tour-booking-details", "whatsapp-invite-url"], "missing |