# Variants QA report (local-cd)

Base URL: http://127.0.0.1:18432/
Variants: cd
PASS 96 / FAIL 0

| Result | Gate | Evidence |
|---|---|---|
| PASS | robots.txt Disallow while private | 200 |
| PASS | [cd/en] HTTP 200 http://127.0.0.1:18432/v/cd/ | 200 |
| PASS | [cd/en] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin on Lake Atitlán, Guatemala", "desc_len": 158} |
| PASS | [cd/en] meta robots noindex,nofollow | "present" |
| PASS | [cd/en] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/cd/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/cd/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/cd/"]] |
| PASS | [cd/en] html lang + data-design | "en" |
| PASS | [cd/en] every referenced asset and link returns 200 | {"checked": 60, "bad": []} |
| PASS | [cd/en] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [cd/en] page weight under 3 MB excluding map tiles | "1132 KB" |
| PASS | [cd/en] no horizontal overflow at 1440 | {"sw": 1440, "cw": 1440} |
| PASS | [cd/en] no text leaves the screen at 1440 | [] |
| PASS | [cd/en] every section fills the screen (>=0.95 of viewport height) | [["hero", 1], ["lake", 1.12], ["bitcoin", 1.89], ["transport", 1.71], ["community", 1], ["tours", 1.13], ["expats", 1], ["about", 2.73]] |
| PASS | [cd/en] map ready and renders 117 markers | {"state": "ready", "markers": 117, "tiles": 16} |
| PASS | [cd/en] list count == marker count == 117 | {"cards": 117, "markers": 117, "hook": {"m": 117, "c": 117, "v": 117, "p": 117}} |
| PASS | [cd/en] count text shows 117 | "Showing 117 of 117 places" |
| PASS | [cd/en] markers use the design's own colour token | {"fills": ["#d03040"], "token": "#d03040"} |
| PASS | [cd/en] search filters list and map together | {"c": 6, "m": 6, "paths": 6} |
| PASS | [cd/en] category chip filters (stay) | {"c": 16, "m": 16, "pressed": "stay"} |
| PASS | [cd/en] village filter | {"c": 10, "m": 10} |
| PASS | [cd/en] empty state | {"c": 0, "m": 0, "empty": true} |
| PASS | [cd/en] reset restores 117 | {"c": 117, "m": 117} |
| PASS | [cd/en] ride 'Show on map' opens a popup | "popup" |
| PASS | [cd/en] every image has alt text | {"images": 13, "bad": []} |
| PASS | [cd/en] only local photos, each with a Commons or approved community-archive credit | {"photos": 11, "no_credit": [], "other_images": []} |
| PASS | [cd/en] no broken images | "ok" |
| PASS | [cd/en] no 'official'/'oficial' claim | "none" |
| PASS | [cd/en] no em or en dashes in visible text | [] |
| PASS | [cd/en] merchant check note present | "ok" |
| PASS | [cd/en] 117 places + 50+ claim + data date | "ok" |
| PASS | [cd/en] OSM/ODbL, BTC Map and Commons credits in footer | "ok" |
| PASS | [cd/en] floating Design switcher: all finished designs, current marked, fixed, in view | {"letters": ["A", "C", "D", "AC", "AD", "CD"], "cur": ["CD"], "hrefs": ["../a/", "../c/", "../d/", "../ac/", "../ad/", "./", "../../variants/"], "inView": true, "fixed": "fixed"} |
| PASS | [cd/en] switcher goes to design C in the same language and remembers it | {"url": "http://127.0.0.1:18432/v/c/", "stored": "c"} |
| PASS | [cd/en] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [cd/en] 1440 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 32, "lowest_ratio": 5.03, "failures": []} |
| PASS | [cd/en] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [cd/en] no text leaves the screen at 390 | [] |
| PASS | [cd/en] no console errors at 390 | [] |
| PASS | [cd/en] brand text does not run into the language switch or menu button at 390 | {"brandRight": 197, "langLeft": 240, "overlapLang": false, "overlapMenu": false} |
| PASS | [cd/en] 117 markers at 390 | "ok" |
| PASS | [cd/en] switcher fits at 390 | {"right": 382, "vw": 390, "h": 44} |
| PASS | [cd/en] mobile menu opens | true |
| PASS | [cd/en] menu link scrolls to the merchants section | -0.0 |
| PASS | [cd/en] 390 axe-core WCAG A/AA violations | [] |
| PASS | [cd/en] 390 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 32, "lowest_ratio": 5.03, "failures": []} |
| PASS | [cd/es] HTTP 200 http://127.0.0.1:18432/v/cd/es/ | 200 |
| PASS | [cd/es] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin en el Lago de Atitlán, Guatemala", "desc_len": 179} |
| PASS | [cd/es] meta robots noindex,nofollow | "present" |
| PASS | [cd/es] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/cd/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/cd/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/cd/"]] |
| PASS | [cd/es] html lang + data-design | "es" |
| PASS | [cd/es] every referenced asset and link returns 200 | {"checked": 65, "bad": []} |
| PASS | [cd/es] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [cd/es] page weight under 3 MB excluding map tiles | "1133 KB" |
| PASS | [cd/es] no horizontal overflow at 1440 | {"sw": 1440, "cw": 1440} |
| PASS | [cd/es] no text leaves the screen at 1440 | [] |
| PASS | [cd/es] every section fills the screen (>=0.95 of viewport height) | [["hero", 1], ["lake", 1.24], ["bitcoin", 1.89], ["transport", 1.62], ["community", 1], ["tours", 1.1], ["expats", 1], ["about", 2.73]] |
| PASS | [cd/es] map ready and renders 117 markers | {"state": "ready", "markers": 117, "tiles": 16} |
| PASS | [cd/es] list count == marker count == 117 | {"cards": 117, "markers": 117, "hook": {"m": 117, "c": 117, "v": 117, "p": 117}} |
| PASS | [cd/es] count text shows 117 | "Mostrando 117 de 117 lugares" |
| PASS | [cd/es] markers use the design's own colour token | {"fills": ["#d03040"], "token": "#d03040"} |
| PASS | [cd/es] search filters list and map together | {"c": 17, "m": 17, "paths": 17} |
| PASS | [cd/es] category chip filters (stay) | {"c": 16, "m": 16, "pressed": "stay"} |
| PASS | [cd/es] village filter | {"c": 10, "m": 10} |
| PASS | [cd/es] empty state | {"c": 0, "m": 0, "empty": true} |
| PASS | [cd/es] reset restores 117 | {"c": 117, "m": 117} |
| PASS | [cd/es] ride 'Show on map' opens a popup | "popup" |
| PASS | [cd/es] every image has alt text | {"images": 13, "bad": []} |
| PASS | [cd/es] only local photos, each with a Commons or approved community-archive credit | {"photos": 11, "no_credit": [], "other_images": []} |
| PASS | [cd/es] no broken images | "ok" |
| PASS | [cd/es] no 'official'/'oficial' claim | "none" |
| PASS | [cd/es] no em or en dashes in visible text | [] |
| PASS | [cd/es] merchant check note present | "ok" |
| PASS | [cd/es] 117 places + 50+ claim + data date | "ok" |
| PASS | [cd/es] OSM/ODbL, BTC Map and Commons credits in footer | "ok" |
| PASS | [cd/es] floating Design switcher: all finished designs, current marked, fixed, in view | {"letters": ["A", "C", "D", "AC", "AD", "CD"], "cur": ["CD"], "hrefs": ["../../a/es/", "../../c/es/", "../../d/es/", "../../ac/es/", "../../ad/es/", "./", "../../../variants/es/"], "inView": true, "fixed": "fixed"} |
| PASS | [cd/es] switcher goes to design C in the same language and remembers it | {"url": "http://127.0.0.1:18432/v/c/es/", "stored": "c"} |
| PASS | [cd/es] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [cd/es] 1440 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 32, "lowest_ratio": 5.03, "failures": []} |
| PASS | [cd/es] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [cd/es] no text leaves the screen at 390 | [] |
| PASS | [cd/es] no console errors at 390 | [] |
| PASS | [cd/es] brand text does not run into the language switch or menu button at 390 | {"brandRight": 197, "langLeft": 240, "overlapLang": false, "overlapMenu": false} |
| PASS | [cd/es] 117 markers at 390 | "ok" |
| PASS | [cd/es] switcher fits at 390 | {"right": 382, "vw": 390, "h": 44} |
| PASS | [cd/es] mobile menu opens | true |
| PASS | [cd/es] menu link scrolls to the merchants section | -0.0 |
| PASS | [cd] EN/ES parity: same section ids in same order | ["hero", "lake", "bitcoin", "transport", "community", "tours", "expats", "about"] |
| PASS | [cd] EN/ES parity: placeholders, nav targets, h2 and image counts | {"placeholders": ["atm-locations", "contact-email", "expat-contact", "facebook", "meetup-dates", "meetup-venues", "school-list", "tomek-bio-photo", "tour-booking", "tour-booking-details", "whatsapp-invite-url"], "h2": 7, |
| PASS | [cd] every nav link targets an existing section | ["#lake", "#bitcoin", "#transport", "#community", "#tours", "#expats", "#about"] |
| PASS | [cd] no section dropped (map, merchants, community, tours, expats, boat/tuk tuk, ATM, history) | [] |
| PASS | [cd] browser language es: opening EN redirects to /es/ | "http://127.0.0.1:18432/v/cd/es/" |
| PASS | [cd] EN switch stays in this design and stores the choice | "http://127.0.0.1:18432/v/cd/" |
| PASS | [cd] ES switch stays in this design | "http://127.0.0.1:18432/v/cd/es/" |
| PASS | [cd] browser language en: opening /es/ redirects to EN | "http://127.0.0.1:18432/v/cd/" |
| PASS | [cd] placeholder button shows 'coming soon' toast | "toast" |
| PASS | [cd] placeholder badge visible in preview | "\"Placeholder: whatsapp-invite-url\"" |
| PASS | every data-placeholder is listed in HANDOFF.md | {"placeholders": ["atm-locations", "contact-email", "expat-contact", "facebook", "meetup-dates", "meetup-venues", "school-list", "tomek-bio-photo", "tour-booking", "tour-booking-details", "whatsapp-invite-url"], "missing |