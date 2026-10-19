# Variants QA report (local-abc)

Base URL: http://127.0.0.1:18431/
Variants: a, b, c
PASS 274 / FAIL 10

| Result | Gate | Evidence |
|---|---|---|
| PASS | robots.txt Disallow while private | 200 |
| PASS | [a/en] HTTP 200 http://127.0.0.1:18431/v/a/ | 200 |
| PASS | [a/en] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin on Lake Atitlán, Guatemala", "desc_len": 158} |
| PASS | [a/en] meta robots noindex,nofollow | "present" |
| PASS | [a/en] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/a/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/a/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/a/"]] |
| PASS | [a/en] html lang + data-design | "en" |
| FAIL | [a/en] every referenced asset and link returns 200 | {"checked": 44, "bad": [["http://127.0.0.1:18431/v/e/", 404]]} |
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
| PASS | [a/en] 1440 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 3, "lowest_ratio": 6.04, "failures": []} |
| PASS | [a/en] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [a/en] no text leaves the screen at 390 | [] |
| PASS | [a/en] no console errors at 390 | [] |
| PASS | [a/en] brand text does not run into the language switch or menu button at 390 | {"brandRight": 215, "langLeft": 235, "overlapLang": false, "overlapMenu": false} |
| PASS | [a/en] 117 markers at 390 | "ok" |
| PASS | [a/en] switcher fits at 390 | {"right": 382, "vw": 390, "h": 44} |
| PASS | [a/en] mobile menu opens | true |
| PASS | [a/en] menu link scrolls to the merchants section | -0.0 |
| PASS | [a/en] 390 axe-core WCAG A/AA violations | [] |
| PASS | [a/en] 390 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 3, "lowest_ratio": 6.04, "failures": []} |
| PASS | [a/es] HTTP 200 http://127.0.0.1:18431/v/a/es/ | 200 |
| PASS | [a/es] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin en el Lago de Atitlán, Guatemala", "desc_len": 179} |
| PASS | [a/es] meta robots noindex,nofollow | "present" |
| PASS | [a/es] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/a/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/a/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/a/"]] |
| PASS | [a/es] html lang + data-design | "es" |
| FAIL | [a/es] every referenced asset and link returns 200 | {"checked": 44, "bad": [["http://127.0.0.1:18431/v/e/es/", 404]]} |
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
| PASS | [a/es] 1440 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 3, "lowest_ratio": 6.04, "failures": []} |
| PASS | [a/es] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [a/es] no text leaves the screen at 390 | [] |
| PASS | [a/es] no console errors at 390 | [] |
| PASS | [a/es] brand text does not run into the language switch or menu button at 390 | {"brandRight": 215, "langLeft": 235, "overlapLang": false, "overlapMenu": false} |
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
| PASS | [b/en] HTTP 200 http://127.0.0.1:18431/v/b/ | 200 |
| PASS | [b/en] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin on Lake Atitlán, Guatemala", "desc_len": 158} |
| PASS | [b/en] meta robots noindex,nofollow | "present" |
| PASS | [b/en] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/b/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/b/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/b/"]] |
| PASS | [b/en] html lang + data-design | "en" |
| FAIL | [b/en] every referenced asset and link returns 200 | {"checked": 48, "bad": [["http://127.0.0.1:18431/v/e/", 404]]} |
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
| FAIL | [b/en] brand text does not run into the language switch or menu button at 390 | {"brandRight": 333, "langLeft": 310, "overlapLang": true, "overlapMenu": false} |
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
| FAIL | [b/es] every referenced asset and link returns 200 | {"checked": 48, "bad": [["http://127.0.0.1:18431/v/e/es/", 404]]} |
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
| FAIL | [b/es] brand text does not run into the language switch or menu button at 390 | {"brandRight": 333, "langLeft": 310, "overlapLang": true, "overlapMenu": false} |
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
| PASS | [c/en] HTTP 200 http://127.0.0.1:18431/v/c/ | 200 |
| PASS | [c/en] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin on Lake Atitlán, Guatemala", "desc_len": 158} |
| PASS | [c/en] meta robots noindex,nofollow | "present" |
| PASS | [c/en] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/c/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/c/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/c/"]] |
| PASS | [c/en] html lang + data-design | "en" |
| PASS | [c/en] every referenced asset and link returns 200 | {"checked": 48, "bad": []} |
| PASS | [c/en] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [c/en] page weight under 3 MB excluding map tiles | "986 KB" |
| PASS | [c/en] no horizontal overflow at 1440 | {"sw": 1440, "cw": 1440} |
| PASS | [c/en] no text leaves the screen at 1440 | [] |
| PASS | [c/en] every section fills the screen (>=0.95 of viewport height) | [["hero", 1], ["lake", 1.12], ["bitcoin", 1.89], ["transport", 1.26], ["community", 1], ["tours", 1.13], ["expats", 1], ["about", 1]] |
| PASS | [c/en] map ready and renders 117 markers | {"state": "ready", "markers": 117, "tiles": 16} |
| PASS | [c/en] list count == marker count == 117 | {"cards": 117, "markers": 117, "hook": {"m": 117, "c": 117, "v": 117, "p": 117}} |
| PASS | [c/en] count text shows 117 | "Showing 117 of 117 places" |
| PASS | [c/en] markers use the design's own colour token | {"fills": ["#ff5b1f"], "token": "#ff5b1f"} |
| PASS | [c/en] search filters list and map together | {"c": 6, "m": 6, "paths": 6} |
| PASS | [c/en] category chip filters (stay) | {"c": 16, "m": 16, "pressed": "stay"} |
| PASS | [c/en] village filter | {"c": 10, "m": 10} |
| PASS | [c/en] empty state | {"c": 0, "m": 0, "empty": true} |
| PASS | [c/en] reset restores 117 | {"c": 117, "m": 117} |
| PASS | [c/en] ride 'Show on map' opens a popup | "popup" |
| PASS | [c/en] every image has alt text | {"images": 9, "bad": []} |
| PASS | [c/en] only local Commons photos, each with Commons + licence credit | {"photos": 8, "no_credit": [], "other_images": []} |
| PASS | [c/en] no broken images | "ok" |
| PASS | [c/en] no 'official'/'oficial' claim | "none" |
| PASS | [c/en] no em or en dashes in visible text | [] |
| PASS | [c/en] merchant check note present | "ok" |
| PASS | [c/en] 117 places + 50+ claim + data date | "ok" |
| PASS | [c/en] OSM/ODbL, BTC Map and Commons credits in footer | "ok" |
| PASS | [c/en] floating Design switcher: A B C D E, current marked, fixed, in view | {"letters": ["A", "B", "C", "D", "E"], "cur": ["C"], "hrefs": ["../a/", "../b/", "./", "../d/", "../e/", "../../variants/"], "inView": true, "fixed": "fixed"} |
| PASS | [c/en] switcher goes to design B in the same language and remembers it | {"url": "http://127.0.0.1:18431/v/b/", "stored": "b"} |
| PASS | [c/en] 1440 axe-core WCAG A/AA violations | [] |
| FAIL | [c/en] 1440 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 40, "lowest_ratio": 1.47, "failures": ["'VIP tours' 1.47<4.5 (text L=0.45, behind 0.01..0.29)"]} |
| PASS | [c/en] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [c/en] no text leaves the screen at 390 | [] |
| PASS | [c/en] no console errors at 390 | [] |
| FAIL | [c/en] brand text does not run into the language switch or menu button at 390 | {"brandRight": 257, "langLeft": 239, "overlapLang": true, "overlapMenu": false} |
| PASS | [c/en] 117 markers at 390 | "ok" |
| PASS | [c/en] switcher fits at 390 | {"right": 382, "vw": 390, "h": 44} |
| PASS | [c/en] mobile menu opens | true |
| PASS | [c/en] menu link scrolls to the merchants section | -0.0 |
| PASS | [c/en] 390 axe-core WCAG A/AA violations | [] |
| FAIL | [c/en] 390 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 32, "lowest_ratio": 1.0, "failures": ["'Lago Bitcoin Community' 1.00<4.5 (text L=0.82, behind 0.00..0.82)", "'Murray Foubister' 1.13<4.5 (text L=0.75, behind 0.00..0.85)", "'You integrate with the culture, to |
| PASS | [c/es] HTTP 200 http://127.0.0.1:18431/v/c/es/ | 200 |
| PASS | [c/es] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin en el Lago de Atitlán, Guatemala", "desc_len": 179} |
| PASS | [c/es] meta robots noindex,nofollow | "present" |
| PASS | [c/es] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/c/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/c/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/c/"]] |
| PASS | [c/es] html lang + data-design | "es" |
| PASS | [c/es] every referenced asset and link returns 200 | {"checked": 48, "bad": []} |
| PASS | [c/es] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [c/es] page weight under 3 MB excluding map tiles | "987 KB" |
| PASS | [c/es] no horizontal overflow at 1440 | {"sw": 1440, "cw": 1440} |
| PASS | [c/es] no text leaves the screen at 1440 | [] |
| PASS | [c/es] every section fills the screen (>=0.95 of viewport height) | [["hero", 1], ["lake", 1.24], ["bitcoin", 1.89], ["transport", 1.17], ["community", 1], ["tours", 1.1], ["expats", 1], ["about", 1]] |
| PASS | [c/es] map ready and renders 117 markers | {"state": "ready", "markers": 117, "tiles": 16} |
| PASS | [c/es] list count == marker count == 117 | {"cards": 117, "markers": 117, "hook": {"m": 117, "c": 117, "v": 117, "p": 117}} |
| PASS | [c/es] count text shows 117 | "Mostrando 117 de 117 lugares" |
| PASS | [c/es] markers use the design's own colour token | {"fills": ["#ff5b1f"], "token": "#ff5b1f"} |
| PASS | [c/es] search filters list and map together | {"c": 17, "m": 17, "paths": 17} |
| PASS | [c/es] category chip filters (stay) | {"c": 16, "m": 16, "pressed": "stay"} |
| PASS | [c/es] village filter | {"c": 10, "m": 10} |
| PASS | [c/es] empty state | {"c": 0, "m": 0, "empty": true} |
| PASS | [c/es] reset restores 117 | {"c": 117, "m": 117} |
| PASS | [c/es] ride 'Show on map' opens a popup | "popup" |
| PASS | [c/es] every image has alt text | {"images": 9, "bad": []} |
| PASS | [c/es] only local Commons photos, each with Commons + licence credit | {"photos": 8, "no_credit": [], "other_images": []} |
| PASS | [c/es] no broken images | "ok" |
| PASS | [c/es] no 'official'/'oficial' claim | "none" |
| PASS | [c/es] no em or en dashes in visible text | [] |
| PASS | [c/es] merchant check note present | "ok" |
| PASS | [c/es] 117 places + 50+ claim + data date | "ok" |
| PASS | [c/es] OSM/ODbL, BTC Map and Commons credits in footer | "ok" |
| PASS | [c/es] floating Design switcher: A B C D E, current marked, fixed, in view | {"letters": ["A", "B", "C", "D", "E"], "cur": ["C"], "hrefs": ["../../a/es/", "../../b/es/", "./", "../../d/es/", "../../e/es/", "../../../variants/es/"], "inView": true, "fixed": "fixed"} |
| PASS | [c/es] switcher goes to design B in the same language and remembers it | {"url": "http://127.0.0.1:18431/v/b/es/", "stored": "b"} |
| PASS | [c/es] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [c/es] 1440 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 40, "lowest_ratio": 6.22, "failures": []} |
| PASS | [c/es] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [c/es] no text leaves the screen at 390 | [] |
| PASS | [c/es] no console errors at 390 | [] |
| FAIL | [c/es] brand text does not run into the language switch or menu button at 390 | {"brandRight": 257, "langLeft": 239, "overlapLang": true, "overlapMenu": false} |
| PASS | [c/es] 117 markers at 390 | "ok" |
| PASS | [c/es] switcher fits at 390 | {"right": 382, "vw": 390, "h": 44} |
| PASS | [c/es] mobile menu opens | true |
| PASS | [c/es] menu link scrolls to the merchants section | -0.0 |
| PASS | [c] EN/ES parity: same section ids in same order | ["hero", "lake", "bitcoin", "transport", "community", "tours", "expats", "about"] |
| PASS | [c] EN/ES parity: placeholders, nav targets, h2 and image counts | {"placeholders": ["atm-locations", "contact-email", "expat-contact", "facebook", "meetup-dates", "meetup-venues", "school-list", "tomek-bio-photo", "tour-booking", "tour-booking-details", "whatsapp-invite-url"], "h2": 7, |
| PASS | [c] every nav link targets an existing section | ["#lake", "#bitcoin", "#transport", "#community", "#tours", "#expats", "#about"] |
| PASS | [c] no section dropped (map, merchants, community, tours, expats, boat/tuk tuk, ATM, history) | [] |
| PASS | [c] browser language es: opening EN redirects to /es/ | "http://127.0.0.1:18431/v/c/es/" |
| PASS | [c] EN switch stays in this design and stores the choice | "http://127.0.0.1:18431/v/c/" |
| PASS | [c] ES switch stays in this design | "http://127.0.0.1:18431/v/c/es/" |
| PASS | [c] browser language en: opening /es/ redirects to EN | "http://127.0.0.1:18431/v/c/" |
| PASS | [c] placeholder button shows 'coming soon' toast | "toast" |
| PASS | [c] placeholder badge visible in preview | "\"Placeholder: whatsapp-invite-url\"" |
| PASS | every data-placeholder is listed in HANDOFF.md | {"placeholders": ["atm-locations", "contact-email", "expat-contact", "facebook", "meetup-dates", "meetup-venues", "school-list", "tomek-bio-photo", "tour-booking", "tour-booking-details", "whatsapp-invite-url"], "missing |