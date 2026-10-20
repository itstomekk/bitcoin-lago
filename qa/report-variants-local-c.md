# Variants QA report (local-c)

Base URL: http://127.0.0.1:18433/
Variants: c
PASS 111 / FAIL 2

| Result | Gate | Evidence |
|---|---|---|
| PASS | robots.txt Disallow while private | 200 |
| PASS | [c/en] HTTP 200 http://127.0.0.1:18433/v/c/ | 200 |
| PASS | [c/en] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin on Lake Atitlán, Guatemala", "desc_len": 158} |
| PASS | [c/en] meta robots noindex,nofollow | "present" |
| PASS | [c/en] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/c/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/c/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/c/"]] |
| PASS | [c/en] html lang + data-design | "en" |
| PASS | [c/en] every referenced asset and link returns 200 | {"checked": 48, "bad": []} |
| PASS | [c/en] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [c/en] page weight under 3 MB excluding map tiles | "1023 KB" |
| PASS | [c/en] no horizontal overflow at 1440 | {"sw": 1440, "cw": 1440} |
| PASS | [c/en] no text leaves the screen at 1440 | [] |
| PASS | [c/en] every section fills the screen (>=0.95 of viewport height) | [["hero", 1], ["lake", 1.12], ["bitcoin", 1.89], ["transport", 1.26], ["community", 1], ["tours", 1.13], ["expats", 1], ["about", 1.99]] |
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
| PASS | [c/en] every image has alt text | {"images": 10, "bad": []} |
| PASS | [c/en] only local Commons photos, each with Commons + licence credit | {"photos": 8, "no_credit": [], "other_images": []} |
| PASS | [c/en] no broken images | "ok" |
| PASS | [c/en] no 'official'/'oficial' claim | "none" |
| PASS | [c/en] no em or en dashes in visible text | [] |
| PASS | [c/en] merchant check note present | "ok" |
| PASS | [c/en] 117 places + 50+ claim + data date | "ok" |
| PASS | [c/en] OSM/ODbL, BTC Map and Commons credits in footer | "ok" |
| PASS | [c/en] floating Design switcher: A C D, current marked, fixed, in view | {"letters": ["A", "C", "D"], "cur": ["C"], "hrefs": ["../a/", "./", "../d/", "../../variants/"], "inView": true, "fixed": "fixed"} |
| PASS | [c/en] switcher goes to design D in the same language and remembers it | {"url": "http://127.0.0.1:18433/v/d/", "stored": "d"} |
| PASS | [c/en] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [c/en] 1440 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 32, "lowest_ratio": 6.22, "failures": []} |
| PASS | [c/en] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [c/en] no text leaves the screen at 390 | [] |
| PASS | [c/en] no console errors at 390 | [] |
| PASS | [c/en] brand text does not run into the language switch or menu button at 390 | {"brandRight": 200, "langLeft": 240, "overlapLang": false, "overlapMenu": false} |
| PASS | [c/en] 117 markers at 390 | "ok" |
| PASS | [c/en] switcher fits at 390 | {"right": 382, "vw": 390, "h": 44} |
| PASS | [c/en] mobile menu opens | true |
| PASS | [c/en] menu link scrolls to the merchants section | -0.0 |
| PASS | [c/en] 390 axe-core WCAG A/AA violations | [] |
| PASS | [c/en] 390 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 32, "lowest_ratio": 6.22, "failures": []} |
| PASS | [c/es] HTTP 200 http://127.0.0.1:18433/v/c/es/ | 200 |
| PASS | [c/es] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin en el Lago de Atitlán, Guatemala", "desc_len": 179} |
| PASS | [c/es] meta robots noindex,nofollow | "present" |
| PASS | [c/es] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/c/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/c/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/c/"]] |
| PASS | [c/es] html lang + data-design | "es" |
| PASS | [c/es] every referenced asset and link returns 200 | {"checked": 50, "bad": []} |
| PASS | [c/es] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [c/es] page weight under 3 MB excluding map tiles | "1024 KB" |
| PASS | [c/es] no horizontal overflow at 1440 | {"sw": 1440, "cw": 1440} |
| PASS | [c/es] no text leaves the screen at 1440 | [] |
| PASS | [c/es] every section fills the screen (>=0.95 of viewport height) | [["hero", 1], ["lake", 1.24], ["bitcoin", 1.89], ["transport", 1.17], ["community", 1], ["tours", 1.1], ["expats", 1], ["about", 1.99]] |
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
| PASS | [c/es] every image has alt text | {"images": 10, "bad": []} |
| PASS | [c/es] only local Commons photos, each with Commons + licence credit | {"photos": 8, "no_credit": [], "other_images": []} |
| PASS | [c/es] no broken images | "ok" |
| PASS | [c/es] no 'official'/'oficial' claim | "none" |
| PASS | [c/es] no em or en dashes in visible text | [] |
| PASS | [c/es] merchant check note present | "ok" |
| PASS | [c/es] 117 places + 50+ claim + data date | "ok" |
| PASS | [c/es] OSM/ODbL, BTC Map and Commons credits in footer | "ok" |
| PASS | [c/es] floating Design switcher: A C D, current marked, fixed, in view | {"letters": ["A", "C", "D"], "cur": ["C"], "hrefs": ["../../a/es/", "./", "../../d/es/", "../../../variants/es/"], "inView": true, "fixed": "fixed"} |
| PASS | [c/es] switcher goes to design D in the same language and remembers it | {"url": "http://127.0.0.1:18433/v/d/es/", "stored": "d"} |
| PASS | [c/es] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [c/es] 1440 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 32, "lowest_ratio": 6.22, "failures": []} |
| PASS | [c/es] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [c/es] no text leaves the screen at 390 | [] |
| PASS | [c/es] no console errors at 390 | [] |
| PASS | [c/es] brand text does not run into the language switch or menu button at 390 | {"brandRight": 200, "langLeft": 240, "overlapLang": false, "overlapMenu": false} |
| PASS | [c/es] 117 markers at 390 | "ok" |
| PASS | [c/es] switcher fits at 390 | {"right": 382, "vw": 390, "h": 44} |
| PASS | [c/es] mobile menu opens | true |
| PASS | [c/es] menu link scrolls to the merchants section | -0.0 |
| PASS | [c] EN/ES parity: same section ids in same order | ["hero", "lake", "bitcoin", "transport", "community", "tours", "expats", "about"] |
| PASS | [c] EN/ES parity: placeholders, nav targets, h2 and image counts | {"placeholders": ["atm-locations", "contact-email", "expat-contact", "facebook", "meetup-dates", "meetup-venues", "school-list", "tomek-bio-photo", "tour-booking", "tour-booking-details", "whatsapp-invite-url"], "h2": 7, |
| PASS | [c] every nav link targets an existing section | ["#lake", "#bitcoin", "#transport", "#community", "#tours", "#expats", "#about"] |
| PASS | [c] no section dropped (map, merchants, community, tours, expats, boat/tuk tuk, ATM, history) | [] |
| PASS | [c] browser language es: opening EN redirects to /es/ | "http://127.0.0.1:18433/v/c/es/" |
| PASS | [c] EN switch stays in this design and stores the choice | "http://127.0.0.1:18433/v/c/" |
| PASS | [c] ES switch stays in this design | "http://127.0.0.1:18433/v/c/es/" |
| PASS | [c] browser language en: opening /es/ redirects to EN | "http://127.0.0.1:18433/v/c/" |
| PASS | [c] placeholder button shows 'coming soon' toast | "toast" |
| PASS | [c] placeholder badge visible in preview | "\"Placeholder: whatsapp-invite-url\"" |
| PASS | [index/en] HTTP 200 http://127.0.0.1:18433/variants/ | 200 |
| PASS | [index/en] noindex,nofollow | "present" |
| PASS | [index/en] every referenced asset and link returns 200 | {"checked": 16, "bad": []} |
| PASS | [index/en] 1440: four cards, four loaded thumbnails, no console errors, no overflow | {"info": {"cards": 4, "thumbs": 4}, "errs": [], "ov": {"sw": 1440, "cw": 1440}} |
| PASS | [index/en] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [index/en] 390: four cards, four loaded thumbnails, no console errors, no overflow | {"info": {"cards": 4, "thumbs": 4}, "errs": [], "ov": {"sw": 390, "cw": 390}} |
| PASS | [index/en] 390 axe-core WCAG A/AA violations | [] |
| PASS | [index/en] card C opens /v/c/ in en | "http://127.0.0.1:18433/v/c/" |
| PASS | [index/es] HTTP 200 http://127.0.0.1:18433/variants/es/ | 200 |
| PASS | [index/es] noindex,nofollow | "present" |
| PASS | [index/es] every referenced asset and link returns 200 | {"checked": 17, "bad": []} |
| PASS | [index/es] 1440: four cards, four loaded thumbnails, no console errors, no overflow | {"info": {"cards": 4, "thumbs": 4}, "errs": [], "ov": {"sw": 1440, "cw": 1440}} |
| FAIL | [index/es] 1440 axe-core WCAG A/AA violations | [{"id": "color-contrast", "impact": "serious", "n": 1, "sample": ["a[href=\"../\"][data-lang=\"en\"][title=\"English\"] :: Element has insufficient color contrast of 3.51 (foreground color: #d03040, background color: #00 |
| PASS | [index/es] 390: four cards, four loaded thumbnails, no console errors, no overflow | {"info": {"cards": 4, "thumbs": 4}, "errs": [], "ov": {"sw": 390, "cw": 390}} |
| FAIL | [index/es] 390 axe-core WCAG A/AA violations | [{"id": "color-contrast", "impact": "serious", "n": 1, "sample": ["a[href=\"../\"][data-lang=\"en\"][title=\"English\"] :: Element has insufficient color contrast of 3.51 (foreground color: #d03040, background color: #00 |
| PASS | [index/es] card C opens /v/c/ in es | "http://127.0.0.1:18433/v/c/es/" |
| PASS | HTTP 200 http://127.0.0.1:18433/v/ | 200 |
| PASS | every data-placeholder is listed in HANDOFF.md | {"placeholders": ["atm-locations", "contact-email", "expat-contact", "facebook", "meetup-dates", "meetup-venues", "school-list", "tomek-bio-photo", "tour-booking", "tour-booking-details", "whatsapp-invite-url"], "missing |