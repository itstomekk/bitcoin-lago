# Variants QA report (local-ac)

Base URL: http://127.0.0.1:18432/
Variants: ac
PASS 96 / FAIL 0

| Result | Gate | Evidence |
|---|---|---|
| PASS | robots.txt Disallow while private | 200 |
| PASS | [ac/en] HTTP 200 http://127.0.0.1:18432/v/ac/ | 200 |
| PASS | [ac/en] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin on Lake Atitlán, Guatemala", "desc_len": 158} |
| PASS | [ac/en] meta robots noindex,nofollow | "present" |
| PASS | [ac/en] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/ac/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/ac/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/ac/"]] |
| PASS | [ac/en] html lang + data-design | "en" |
| PASS | [ac/en] every referenced asset and link returns 200 | {"checked": 60, "bad": []} |
| PASS | [ac/en] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [ac/en] page weight under 3 MB excluding map tiles | "1132 KB" |
| PASS | [ac/en] no horizontal overflow at 1440 | {"sw": 1440, "cw": 1440} |
| PASS | [ac/en] no text leaves the screen at 1440 | [] |
| PASS | [ac/en] every section fills the screen (>=0.95 of viewport height) | [["hero", 1], ["lake", 1.12], ["bitcoin", 1.89], ["transport", 1.71], ["community", 1], ["tours", 1.13], ["expats", 1], ["about", 2.73]] |
| PASS | [ac/en] map ready and renders 117 markers | {"state": "ready", "markers": 117, "tiles": 16} |
| PASS | [ac/en] list count == marker count == 117 | {"cards": 117, "markers": 117, "hook": {"m": 117, "c": 117, "v": 117, "p": 117}} |
| PASS | [ac/en] count text shows 117 | "Showing 117 of 117 places" |
| PASS | [ac/en] markers use the design's own colour token | {"fills": ["#20a060"], "token": "#20a060"} |
| PASS | [ac/en] search filters list and map together | {"c": 6, "m": 6, "paths": 6} |
| PASS | [ac/en] category chip filters (stay) | {"c": 16, "m": 16, "pressed": "stay"} |
| PASS | [ac/en] village filter | {"c": 10, "m": 10} |
| PASS | [ac/en] empty state | {"c": 0, "m": 0, "empty": true} |
| PASS | [ac/en] reset restores 117 | {"c": 117, "m": 117} |
| PASS | [ac/en] ride 'Show on map' opens a popup | "popup" |
| PASS | [ac/en] every image has alt text | {"images": 13, "bad": []} |
| PASS | [ac/en] only local photos, each with a Commons or approved community-archive credit | {"photos": 11, "no_credit": [], "other_images": []} |
| PASS | [ac/en] no broken images | "ok" |
| PASS | [ac/en] no 'official'/'oficial' claim | "none" |
| PASS | [ac/en] no em or en dashes in visible text | [] |
| PASS | [ac/en] merchant check note present | "ok" |
| PASS | [ac/en] 117 places + 50+ claim + data date | "ok" |
| PASS | [ac/en] OSM/ODbL, BTC Map and Commons credits in footer | "ok" |
| PASS | [ac/en] floating Design switcher: all finished designs, current marked, fixed, in view | {"letters": ["A", "C", "D", "AC", "AD", "CD"], "cur": ["AC"], "hrefs": ["../a/", "../c/", "../d/", "./", "../ad/", "../cd/", "../../variants/"], "inView": true, "fixed": "fixed"} |
| PASS | [ac/en] switcher goes to design C in the same language and remembers it | {"url": "http://127.0.0.1:18432/v/c/", "stored": "c"} |
| PASS | [ac/en] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [ac/en] 1440 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 29, "lowest_ratio": 5.35, "failures": []} |
| PASS | [ac/en] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [ac/en] no text leaves the screen at 390 | [] |
| PASS | [ac/en] no console errors at 390 | [] |
| PASS | [ac/en] brand text does not run into the language switch or menu button at 390 | {"brandRight": 197, "langLeft": 240, "overlapLang": false, "overlapMenu": false} |
| PASS | [ac/en] 117 markers at 390 | "ok" |
| PASS | [ac/en] switcher fits at 390 | {"right": 382, "vw": 390, "h": 44} |
| PASS | [ac/en] mobile menu opens | true |
| PASS | [ac/en] menu link scrolls to the merchants section | -0.0 |
| PASS | [ac/en] 390 axe-core WCAG A/AA violations | [] |
| PASS | [ac/en] 390 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 29, "lowest_ratio": 5.35, "failures": []} |
| PASS | [ac/es] HTTP 200 http://127.0.0.1:18432/v/ac/es/ | 200 |
| PASS | [ac/es] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin en el Lago de Atitlán, Guatemala", "desc_len": 179} |
| PASS | [ac/es] meta robots noindex,nofollow | "present" |
| PASS | [ac/es] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/ac/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/ac/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/ac/"]] |
| PASS | [ac/es] html lang + data-design | "es" |
| PASS | [ac/es] every referenced asset and link returns 200 | {"checked": 65, "bad": []} |
| PASS | [ac/es] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [ac/es] page weight under 3 MB excluding map tiles | "1133 KB" |
| PASS | [ac/es] no horizontal overflow at 1440 | {"sw": 1440, "cw": 1440} |
| PASS | [ac/es] no text leaves the screen at 1440 | [] |
| PASS | [ac/es] every section fills the screen (>=0.95 of viewport height) | [["hero", 1], ["lake", 1.24], ["bitcoin", 1.89], ["transport", 1.62], ["community", 1], ["tours", 1.1], ["expats", 1], ["about", 2.73]] |
| PASS | [ac/es] map ready and renders 117 markers | {"state": "ready", "markers": 117, "tiles": 16} |
| PASS | [ac/es] list count == marker count == 117 | {"cards": 117, "markers": 117, "hook": {"m": 117, "c": 117, "v": 117, "p": 117}} |
| PASS | [ac/es] count text shows 117 | "Mostrando 117 de 117 lugares" |
| PASS | [ac/es] markers use the design's own colour token | {"fills": ["#20a060"], "token": "#20a060"} |
| PASS | [ac/es] search filters list and map together | {"c": 17, "m": 17, "paths": 17} |
| PASS | [ac/es] category chip filters (stay) | {"c": 16, "m": 16, "pressed": "stay"} |
| PASS | [ac/es] village filter | {"c": 10, "m": 10} |
| PASS | [ac/es] empty state | {"c": 0, "m": 0, "empty": true} |
| PASS | [ac/es] reset restores 117 | {"c": 117, "m": 117} |
| PASS | [ac/es] ride 'Show on map' opens a popup | "popup" |
| PASS | [ac/es] every image has alt text | {"images": 13, "bad": []} |
| PASS | [ac/es] only local photos, each with a Commons or approved community-archive credit | {"photos": 11, "no_credit": [], "other_images": []} |
| PASS | [ac/es] no broken images | "ok" |
| PASS | [ac/es] no 'official'/'oficial' claim | "none" |
| PASS | [ac/es] no em or en dashes in visible text | [] |
| PASS | [ac/es] merchant check note present | "ok" |
| PASS | [ac/es] 117 places + 50+ claim + data date | "ok" |
| PASS | [ac/es] OSM/ODbL, BTC Map and Commons credits in footer | "ok" |
| PASS | [ac/es] floating Design switcher: all finished designs, current marked, fixed, in view | {"letters": ["A", "C", "D", "AC", "AD", "CD"], "cur": ["AC"], "hrefs": ["../../a/es/", "../../c/es/", "../../d/es/", "./", "../../ad/es/", "../../cd/es/", "../../../variants/es/"], "inView": true, "fixed": "fixed"} |
| PASS | [ac/es] switcher goes to design C in the same language and remembers it | {"url": "http://127.0.0.1:18432/v/c/es/", "stored": "c"} |
| PASS | [ac/es] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [ac/es] 1440 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 29, "lowest_ratio": 5.35, "failures": []} |
| PASS | [ac/es] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [ac/es] no text leaves the screen at 390 | [] |
| PASS | [ac/es] no console errors at 390 | [] |
| PASS | [ac/es] brand text does not run into the language switch or menu button at 390 | {"brandRight": 197, "langLeft": 240, "overlapLang": false, "overlapMenu": false} |
| PASS | [ac/es] 117 markers at 390 | "ok" |
| PASS | [ac/es] switcher fits at 390 | {"right": 382, "vw": 390, "h": 44} |
| PASS | [ac/es] mobile menu opens | true |
| PASS | [ac/es] menu link scrolls to the merchants section | -0.0 |
| PASS | [ac] EN/ES parity: same section ids in same order | ["hero", "lake", "bitcoin", "transport", "community", "tours", "expats", "about"] |
| PASS | [ac] EN/ES parity: placeholders, nav targets, h2 and image counts | {"placeholders": ["atm-locations", "contact-email", "expat-contact", "facebook", "meetup-dates", "meetup-venues", "school-list", "tomek-bio-photo", "tour-booking", "tour-booking-details", "whatsapp-invite-url"], "h2": 7, |
| PASS | [ac] every nav link targets an existing section | ["#lake", "#bitcoin", "#transport", "#community", "#tours", "#expats", "#about"] |
| PASS | [ac] no section dropped (map, merchants, community, tours, expats, boat/tuk tuk, ATM, history) | [] |
| PASS | [ac] browser language es: opening EN redirects to /es/ | "http://127.0.0.1:18432/v/ac/es/" |
| PASS | [ac] EN switch stays in this design and stores the choice | "http://127.0.0.1:18432/v/ac/" |
| PASS | [ac] ES switch stays in this design | "http://127.0.0.1:18432/v/ac/es/" |
| PASS | [ac] browser language en: opening /es/ redirects to EN | "http://127.0.0.1:18432/v/ac/" |
| PASS | [ac] placeholder button shows 'coming soon' toast | "toast" |
| PASS | [ac] placeholder badge visible in preview | "\"Placeholder: whatsapp-invite-url\"" |
| PASS | every data-placeholder is listed in HANDOFF.md | {"placeholders": ["atm-locations", "contact-email", "expat-contact", "facebook", "meetup-dates", "meetup-venues", "school-list", "tomek-bio-photo", "tour-booking", "tour-booking-details", "whatsapp-invite-url"], "missing |