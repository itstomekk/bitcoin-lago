# Variants QA report (local)

Base URL: http://127.0.0.1:18432/
Variants: a, c, d
PASS 305 / FAIL 0

| Result | Gate | Evidence |
|---|---|---|
| PASS | robots.txt Disallow while private | 200 |
| PASS | [a/en] HTTP 200 http://127.0.0.1:18432/v/a/ | 200 |
| PASS | [a/en] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin on Lake Atitlán, Guatemala", "desc_len": 158} |
| PASS | [a/en] meta robots noindex,nofollow | "present" |
| PASS | [a/en] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/a/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/a/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/a/"]] |
| PASS | [a/en] html lang + data-design | "en" |
| PASS | [a/en] every referenced asset and link returns 200 | {"checked": 53, "bad": []} |
| PASS | [a/en] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [a/en] page weight under 3 MB excluding map tiles | "835 KB" |
| PASS | [a/en] no horizontal overflow at 1440 | {"sw": 1440, "cw": 1440} |
| PASS | [a/en] no text leaves the screen at 1440 | [] |
| PASS | [a/en] every section fills the screen (>=0.95 of viewport height) | [["hero", 1], ["lake", 1.16], ["bitcoin", 1.8], ["transport", 1.44], ["community", 1], ["tours", 1], ["expats", 1], ["about", 2.54]] |
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
| PASS | [a/en] every image has alt text | {"images": 12, "bad": []} |
| PASS | [a/en] only local photos, each with a Commons or approved community-archive credit | {"photos": 10, "no_credit": [], "other_images": []} |
| PASS | [a/en] no broken images | "ok" |
| PASS | [a/en] no 'official'/'oficial' claim | "none" |
| PASS | [a/en] no em or en dashes in visible text | [] |
| PASS | [a/en] merchant check note present | "ok" |
| PASS | [a/en] 117 places + 50+ claim + data date | "ok" |
| PASS | [a/en] OSM/ODbL, BTC Map and Commons credits in footer | "ok" |
| PASS | [a/en] floating Design switcher: A C D, current marked, fixed, in view | {"letters": ["A", "C", "D"], "cur": ["A"], "hrefs": ["./", "../c/", "../d/", "../../variants/"], "inView": true, "fixed": "fixed"} |
| PASS | [a/en] switcher goes to design C in the same language and remembers it | {"url": "http://127.0.0.1:18432/v/c/", "stored": "c"} |
| PASS | [a/en] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [a/en] 1440 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 3, "lowest_ratio": 6.04, "failures": []} |
| PASS | [a/en] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [a/en] no text leaves the screen at 390 | [] |
| PASS | [a/en] no console errors at 390 | [] |
| PASS | [a/en] brand text does not run into the language switch or menu button at 390 | {"brandRight": 213, "langLeft": 235, "overlapLang": false, "overlapMenu": false} |
| PASS | [a/en] 117 markers at 390 | "ok" |
| PASS | [a/en] switcher fits at 390 | {"right": 382, "vw": 390, "h": 44} |
| PASS | [a/en] mobile menu opens | true |
| PASS | [a/en] menu link scrolls to the merchants section | -0.0 |
| PASS | [a/en] 390 axe-core WCAG A/AA violations | [] |
| PASS | [a/en] 390 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 3, "lowest_ratio": 6.04, "failures": []} |
| PASS | [a/es] HTTP 200 http://127.0.0.1:18432/v/a/es/ | 200 |
| PASS | [a/es] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin en el Lago de Atitlán, Guatemala", "desc_len": 179} |
| PASS | [a/es] meta robots noindex,nofollow | "present" |
| PASS | [a/es] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/a/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/a/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/a/"]] |
| PASS | [a/es] html lang + data-design | "es" |
| PASS | [a/es] every referenced asset and link returns 200 | {"checked": 55, "bad": []} |
| PASS | [a/es] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [a/es] page weight under 3 MB excluding map tiles | "837 KB" |
| PASS | [a/es] no horizontal overflow at 1440 | {"sw": 1440, "cw": 1440} |
| PASS | [a/es] no text leaves the screen at 1440 | [] |
| PASS | [a/es] every section fills the screen (>=0.95 of viewport height) | [["hero", 1], ["lake", 1.19], ["bitcoin", 1.8], ["transport", 1.48], ["community", 1], ["tours", 1], ["expats", 1], ["about", 2.54]] |
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
| PASS | [a/es] every image has alt text | {"images": 12, "bad": []} |
| PASS | [a/es] only local photos, each with a Commons or approved community-archive credit | {"photos": 10, "no_credit": [], "other_images": []} |
| PASS | [a/es] no broken images | "ok" |
| PASS | [a/es] no 'official'/'oficial' claim | "none" |
| PASS | [a/es] no em or en dashes in visible text | [] |
| PASS | [a/es] merchant check note present | "ok" |
| PASS | [a/es] 117 places + 50+ claim + data date | "ok" |
| PASS | [a/es] OSM/ODbL, BTC Map and Commons credits in footer | "ok" |
| PASS | [a/es] floating Design switcher: A C D, current marked, fixed, in view | {"letters": ["A", "C", "D"], "cur": ["A"], "hrefs": ["./", "../../c/es/", "../../d/es/", "../../../variants/es/"], "inView": true, "fixed": "fixed"} |
| PASS | [a/es] switcher goes to design C in the same language and remembers it | {"url": "http://127.0.0.1:18432/v/c/es/", "stored": "c"} |
| PASS | [a/es] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [a/es] 1440 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 3, "lowest_ratio": 6.04, "failures": []} |
| PASS | [a/es] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [a/es] no text leaves the screen at 390 | [] |
| PASS | [a/es] no console errors at 390 | [] |
| PASS | [a/es] brand text does not run into the language switch or menu button at 390 | {"brandRight": 213, "langLeft": 235, "overlapLang": false, "overlapMenu": false} |
| PASS | [a/es] 117 markers at 390 | "ok" |
| PASS | [a/es] switcher fits at 390 | {"right": 382, "vw": 390, "h": 44} |
| PASS | [a/es] mobile menu opens | true |
| PASS | [a/es] menu link scrolls to the merchants section | 0 |
| PASS | [a] EN/ES parity: same section ids in same order | ["hero", "lake", "bitcoin", "transport", "community", "tours", "expats", "about"] |
| PASS | [a] EN/ES parity: placeholders, nav targets, h2 and image counts | {"placeholders": ["atm-locations", "contact-email", "expat-contact", "facebook", "meetup-dates", "meetup-venues", "school-list", "tomek-bio-photo", "tour-booking", "tour-booking-details", "whatsapp-invite-url"], "h2": 7, |
| PASS | [a] every nav link targets an existing section | ["#lake", "#bitcoin", "#transport", "#community", "#tours", "#expats", "#about"] |
| PASS | [a] no section dropped (map, merchants, community, tours, expats, boat/tuk tuk, ATM, history) | [] |
| PASS | [a] browser language es: opening EN redirects to /es/ | "http://127.0.0.1:18432/v/a/es/" |
| PASS | [a] EN switch stays in this design and stores the choice | "http://127.0.0.1:18432/v/a/" |
| PASS | [a] ES switch stays in this design | "http://127.0.0.1:18432/v/a/es/" |
| PASS | [a] browser language en: opening /es/ redirects to EN | "http://127.0.0.1:18432/v/a/" |
| PASS | [a] placeholder button shows 'coming soon' toast | "toast" |
| PASS | [a] placeholder badge visible in preview | "\"Placeholder: whatsapp-invite-url\"" |
| PASS | [c/en] HTTP 200 http://127.0.0.1:18432/v/c/ | 200 |
| PASS | [c/en] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin on Lake Atitlán, Guatemala", "desc_len": 158} |
| PASS | [c/en] meta robots noindex,nofollow | "present" |
| PASS | [c/en] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/c/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/c/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/c/"]] |
| PASS | [c/en] html lang + data-design | "en" |
| PASS | [c/en] every referenced asset and link returns 200 | {"checked": 57, "bad": []} |
| PASS | [c/en] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [c/en] page weight under 3 MB excluding map tiles | "1129 KB" |
| PASS | [c/en] no horizontal overflow at 1440 | {"sw": 1440, "cw": 1440} |
| PASS | [c/en] no text leaves the screen at 1440 | [] |
| PASS | [c/en] every section fills the screen (>=0.95 of viewport height) | [["hero", 1], ["lake", 1.12], ["bitcoin", 1.89], ["transport", 1.71], ["community", 1], ["tours", 1.13], ["expats", 1], ["about", 2.73]] |
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
| PASS | [c/en] every image has alt text | {"images": 13, "bad": []} |
| PASS | [c/en] only local photos, each with a Commons or approved community-archive credit | {"photos": 11, "no_credit": [], "other_images": []} |
| PASS | [c/en] no broken images | "ok" |
| PASS | [c/en] no 'official'/'oficial' claim | "none" |
| PASS | [c/en] no em or en dashes in visible text | [] |
| PASS | [c/en] merchant check note present | "ok" |
| PASS | [c/en] 117 places + 50+ claim + data date | "ok" |
| PASS | [c/en] OSM/ODbL, BTC Map and Commons credits in footer | "ok" |
| PASS | [c/en] floating Design switcher: A C D, current marked, fixed, in view | {"letters": ["A", "C", "D"], "cur": ["C"], "hrefs": ["../a/", "./", "../d/", "../../variants/"], "inView": true, "fixed": "fixed"} |
| PASS | [c/en] switcher goes to design D in the same language and remembers it | {"url": "http://127.0.0.1:18432/v/d/", "stored": "d"} |
| PASS | [c/en] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [c/en] 1440 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 32, "lowest_ratio": 6.22, "failures": []} |
| PASS | [c/en] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [c/en] no text leaves the screen at 390 | [] |
| PASS | [c/en] no console errors at 390 | [] |
| PASS | [c/en] brand text does not run into the language switch or menu button at 390 | {"brandRight": 197, "langLeft": 240, "overlapLang": false, "overlapMenu": false} |
| PASS | [c/en] 117 markers at 390 | "ok" |
| PASS | [c/en] switcher fits at 390 | {"right": 382, "vw": 390, "h": 44} |
| PASS | [c/en] mobile menu opens | true |
| PASS | [c/en] menu link scrolls to the merchants section | -0.0 |
| PASS | [c/en] 390 axe-core WCAG A/AA violations | [] |
| PASS | [c/en] 390 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 32, "lowest_ratio": 6.22, "failures": []} |
| PASS | [c/es] HTTP 200 http://127.0.0.1:18432/v/c/es/ | 200 |
| PASS | [c/es] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin en el Lago de Atitlán, Guatemala", "desc_len": 179} |
| PASS | [c/es] meta robots noindex,nofollow | "present" |
| PASS | [c/es] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/c/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/c/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/c/"]] |
| PASS | [c/es] html lang + data-design | "es" |
| PASS | [c/es] every referenced asset and link returns 200 | {"checked": 59, "bad": []} |
| PASS | [c/es] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [c/es] page weight under 3 MB excluding map tiles | "1130 KB" |
| PASS | [c/es] no horizontal overflow at 1440 | {"sw": 1440, "cw": 1440} |
| PASS | [c/es] no text leaves the screen at 1440 | [] |
| PASS | [c/es] every section fills the screen (>=0.95 of viewport height) | [["hero", 1], ["lake", 1.24], ["bitcoin", 1.89], ["transport", 1.62], ["community", 1], ["tours", 1.1], ["expats", 1], ["about", 2.73]] |
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
| PASS | [c/es] every image has alt text | {"images": 13, "bad": []} |
| PASS | [c/es] only local photos, each with a Commons or approved community-archive credit | {"photos": 11, "no_credit": [], "other_images": []} |
| PASS | [c/es] no broken images | "ok" |
| PASS | [c/es] no 'official'/'oficial' claim | "none" |
| PASS | [c/es] no em or en dashes in visible text | [] |
| PASS | [c/es] merchant check note present | "ok" |
| PASS | [c/es] 117 places + 50+ claim + data date | "ok" |
| PASS | [c/es] OSM/ODbL, BTC Map and Commons credits in footer | "ok" |
| PASS | [c/es] floating Design switcher: A C D, current marked, fixed, in view | {"letters": ["A", "C", "D"], "cur": ["C"], "hrefs": ["../../a/es/", "./", "../../d/es/", "../../../variants/es/"], "inView": true, "fixed": "fixed"} |
| PASS | [c/es] switcher goes to design D in the same language and remembers it | {"url": "http://127.0.0.1:18432/v/d/es/", "stored": "d"} |
| PASS | [c/es] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [c/es] 1440 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 32, "lowest_ratio": 6.22, "failures": []} |
| PASS | [c/es] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [c/es] no text leaves the screen at 390 | [] |
| PASS | [c/es] no console errors at 390 | [] |
| PASS | [c/es] brand text does not run into the language switch or menu button at 390 | {"brandRight": 197, "langLeft": 240, "overlapLang": false, "overlapMenu": false} |
| PASS | [c/es] 117 markers at 390 | "ok" |
| PASS | [c/es] switcher fits at 390 | {"right": 382, "vw": 390, "h": 44} |
| PASS | [c/es] mobile menu opens | true |
| PASS | [c/es] menu link scrolls to the merchants section | -0.0 |
| PASS | [c] EN/ES parity: same section ids in same order | ["hero", "lake", "bitcoin", "transport", "community", "tours", "expats", "about"] |
| PASS | [c] EN/ES parity: placeholders, nav targets, h2 and image counts | {"placeholders": ["atm-locations", "contact-email", "expat-contact", "facebook", "meetup-dates", "meetup-venues", "school-list", "tomek-bio-photo", "tour-booking", "tour-booking-details", "whatsapp-invite-url"], "h2": 7, |
| PASS | [c] every nav link targets an existing section | ["#lake", "#bitcoin", "#transport", "#community", "#tours", "#expats", "#about"] |
| PASS | [c] no section dropped (map, merchants, community, tours, expats, boat/tuk tuk, ATM, history) | [] |
| PASS | [c] browser language es: opening EN redirects to /es/ | "http://127.0.0.1:18432/v/c/es/" |
| PASS | [c] EN switch stays in this design and stores the choice | "http://127.0.0.1:18432/v/c/" |
| PASS | [c] ES switch stays in this design | "http://127.0.0.1:18432/v/c/es/" |
| PASS | [c] browser language en: opening /es/ redirects to EN | "http://127.0.0.1:18432/v/c/" |
| PASS | [c] placeholder button shows 'coming soon' toast | "toast" |
| PASS | [c] placeholder badge visible in preview | "\"Placeholder: whatsapp-invite-url\"" |
| PASS | [d/en] HTTP 200 http://127.0.0.1:18432/v/d/ | 200 |
| PASS | [d/en] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin on Lake Atitlán, Guatemala", "desc_len": 158} |
| PASS | [d/en] meta robots noindex,nofollow | "present" |
| PASS | [d/en] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/d/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/d/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/d/"]] |
| PASS | [d/en] html lang + data-design | "en" |
| PASS | [d/en] every referenced asset and link returns 200 | {"checked": 57, "bad": []} |
| PASS | [d/en] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [d/en] page weight under 3 MB excluding map tiles | "905 KB" |
| PASS | [d/en] no horizontal overflow at 1440 | {"sw": 1440, "cw": 1440} |
| PASS | [d/en] no text leaves the screen at 1440 | [] |
| PASS | [d/en] every section fills the screen (>=0.95 of viewport height) | [["hero", 1], ["lake", 1.29], ["bitcoin", 1.78], ["transport", 1.55], ["community", 1.06], ["tours", 1], ["expats", 1], ["about", 2.72]] |
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
| PASS | [d/en] every image has alt text | {"images": 13, "bad": []} |
| PASS | [d/en] only local photos, each with a Commons or approved community-archive credit | {"photos": 11, "no_credit": [], "other_images": []} |
| PASS | [d/en] no broken images | "ok" |
| PASS | [d/en] no 'official'/'oficial' claim | "none" |
| PASS | [d/en] no em or en dashes in visible text | [] |
| PASS | [d/en] merchant check note present | "ok" |
| PASS | [d/en] 117 places + 50+ claim + data date | "ok" |
| PASS | [d/en] OSM/ODbL, BTC Map and Commons credits in footer | "ok" |
| PASS | [d/en] floating Design switcher: A C D, current marked, fixed, in view | {"letters": ["A", "C", "D"], "cur": ["D"], "hrefs": ["../a/", "../c/", "./", "../../variants/"], "inView": true, "fixed": "fixed"} |
| PASS | [d/en] switcher goes to design C in the same language and remembers it | {"url": "http://127.0.0.1:18432/v/c/", "stored": "c"} |
| PASS | [d/en] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [d/en] 1440 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 8, "lowest_ratio": 9.64, "failures": []} |
| PASS | [d/en] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [d/en] no text leaves the screen at 390 | [] |
| PASS | [d/en] no console errors at 390 | [] |
| PASS | [d/en] brand text does not run into the language switch or menu button at 390 | {"brandRight": 221, "langLeft": 246, "overlapLang": false, "overlapMenu": false} |
| PASS | [d/en] 117 markers at 390 | "ok" |
| PASS | [d/en] switcher fits at 390 | {"right": 382, "vw": 390, "h": 44} |
| PASS | [d/en] mobile menu opens | true |
| PASS | [d/en] menu link scrolls to the merchants section | 84 |
| PASS | [d/en] 390 axe-core WCAG A/AA violations | [] |
| PASS | [d/en] 390 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 8, "lowest_ratio": 9.67, "failures": []} |
| PASS | [d/es] HTTP 200 http://127.0.0.1:18432/v/d/es/ | 200 |
| PASS | [d/es] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin en el Lago de Atitlán, Guatemala", "desc_len": 179} |
| PASS | [d/es] meta robots noindex,nofollow | "present" |
| PASS | [d/es] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/d/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/d/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/d/"]] |
| PASS | [d/es] html lang + data-design | "es" |
| PASS | [d/es] every referenced asset and link returns 200 | {"checked": 59, "bad": []} |
| PASS | [d/es] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [d/es] page weight under 3 MB excluding map tiles | "906 KB" |
| PASS | [d/es] no horizontal overflow at 1440 | {"sw": 1440, "cw": 1440} |
| PASS | [d/es] no text leaves the screen at 1440 | [] |
| PASS | [d/es] every section fills the screen (>=0.95 of viewport height) | [["hero", 1], ["lake", 1.29], ["bitcoin", 1.78], ["transport", 1.55], ["community", 1.07], ["tours", 1], ["expats", 1], ["about", 2.72]] |
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
| PASS | [d/es] every image has alt text | {"images": 13, "bad": []} |
| PASS | [d/es] only local photos, each with a Commons or approved community-archive credit | {"photos": 11, "no_credit": [], "other_images": []} |
| PASS | [d/es] no broken images | "ok" |
| PASS | [d/es] no 'official'/'oficial' claim | "none" |
| PASS | [d/es] no em or en dashes in visible text | [] |
| PASS | [d/es] merchant check note present | "ok" |
| PASS | [d/es] 117 places + 50+ claim + data date | "ok" |
| PASS | [d/es] OSM/ODbL, BTC Map and Commons credits in footer | "ok" |
| PASS | [d/es] floating Design switcher: A C D, current marked, fixed, in view | {"letters": ["A", "C", "D"], "cur": ["D"], "hrefs": ["../../a/es/", "../../c/es/", "./", "../../../variants/es/"], "inView": true, "fixed": "fixed"} |
| PASS | [d/es] switcher goes to design C in the same language and remembers it | {"url": "http://127.0.0.1:18432/v/c/es/", "stored": "c"} |
| PASS | [d/es] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [d/es] 1440 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 8, "lowest_ratio": 9.67, "failures": []} |
| PASS | [d/es] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [d/es] no text leaves the screen at 390 | [] |
| PASS | [d/es] no console errors at 390 | [] |
| PASS | [d/es] brand text does not run into the language switch or menu button at 390 | {"brandRight": 221, "langLeft": 246, "overlapLang": false, "overlapMenu": false} |
| PASS | [d/es] 117 markers at 390 | "ok" |
| PASS | [d/es] switcher fits at 390 | {"right": 382, "vw": 390, "h": 44} |
| PASS | [d/es] mobile menu opens | true |
| PASS | [d/es] menu link scrolls to the merchants section | 84 |
| PASS | [d] EN/ES parity: same section ids in same order | ["hero", "lake", "bitcoin", "transport", "community", "tours", "expats", "about"] |
| PASS | [d] EN/ES parity: placeholders, nav targets, h2 and image counts | {"placeholders": ["atm-locations", "contact-email", "expat-contact", "facebook", "meetup-dates", "meetup-venues", "school-list", "tomek-bio-photo", "tour-booking", "tour-booking-details", "whatsapp-invite-url"], "h2": 7, |
| PASS | [d] every nav link targets an existing section | ["#lake", "#bitcoin", "#transport", "#community", "#tours", "#expats", "#about"] |
| PASS | [d] no section dropped (map, merchants, community, tours, expats, boat/tuk tuk, ATM, history) | [] |
| PASS | [d] browser language es: opening EN redirects to /es/ | "http://127.0.0.1:18432/v/d/es/" |
| PASS | [d] EN switch stays in this design and stores the choice | "http://127.0.0.1:18432/v/d/" |
| PASS | [d] ES switch stays in this design | "http://127.0.0.1:18432/v/d/es/" |
| PASS | [d] browser language en: opening /es/ redirects to EN | "http://127.0.0.1:18432/v/d/" |
| PASS | [d] placeholder button shows 'coming soon' toast | "toast" |
| PASS | [d] placeholder badge visible in preview | "\"Placeholder: whatsapp-invite-url\"" |
| PASS | [index/en] HTTP 200 http://127.0.0.1:18432/variants/ | 200 |
| PASS | [index/en] noindex,nofollow | "present" |
| PASS | [index/en] every referenced asset and link returns 200 | {"checked": 16, "bad": []} |
| PASS | [index/en] 1440: four cards, four loaded thumbnails, no console errors, no overflow | {"info": {"cards": 4, "thumbs": 4}, "errs": [], "ov": {"sw": 1440, "cw": 1440}} |
| PASS | [index/en] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [index/en] 390: four cards, four loaded thumbnails, no console errors, no overflow | {"info": {"cards": 4, "thumbs": 4}, "errs": [], "ov": {"sw": 390, "cw": 390}} |
| PASS | [index/en] 390 axe-core WCAG A/AA violations | [] |
| PASS | [index/en] card A opens /v/a/ in en | "http://127.0.0.1:18432/v/a/" |
| PASS | [index/en] card C opens /v/c/ in en | "http://127.0.0.1:18432/v/c/" |
| PASS | [index/en] card D opens /v/d/ in en | "http://127.0.0.1:18432/v/d/" |
| PASS | [index/es] HTTP 200 http://127.0.0.1:18432/variants/es/ | 200 |
| PASS | [index/es] noindex,nofollow | "present" |
| PASS | [index/es] every referenced asset and link returns 200 | {"checked": 17, "bad": []} |
| PASS | [index/es] 1440: four cards, four loaded thumbnails, no console errors, no overflow | {"info": {"cards": 4, "thumbs": 4}, "errs": [], "ov": {"sw": 1440, "cw": 1440}} |
| PASS | [index/es] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [index/es] 390: four cards, four loaded thumbnails, no console errors, no overflow | {"info": {"cards": 4, "thumbs": 4}, "errs": [], "ov": {"sw": 390, "cw": 390}} |
| PASS | [index/es] 390 axe-core WCAG A/AA violations | [] |
| PASS | [index/es] card A opens /v/a/ in es | "http://127.0.0.1:18432/v/a/es/" |
| PASS | [index/es] card C opens /v/c/ in es | "http://127.0.0.1:18432/v/c/es/" |
| PASS | [index/es] card D opens /v/d/ in es | "http://127.0.0.1:18432/v/d/es/" |
| PASS | HTTP 200 http://127.0.0.1:18432/v/ | 200 |
| PASS | every data-placeholder is listed in HANDOFF.md | {"placeholders": ["atm-locations", "contact-email", "expat-contact", "facebook", "meetup-dates", "meetup-venues", "school-list", "tomek-bio-photo", "tour-booking", "tour-booking-details", "whatsapp-invite-url"], "missing |