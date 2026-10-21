# Variants QA report (live-g)

Base URL: https://itstomekk.github.io/lago-bitcoin-community/
Variants: g
PASS 115 / FAIL 0

| Result | Gate | Evidence |
|---|---|---|
| PASS | robots.txt Disallow while private | 200 |
| PASS | [g/en] HTTP 200 https://itstomekk.github.io/lago-bitcoin-community/v/g/ | 200 |
| PASS | [g/en] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin on Lake Atitlán, Guatemala", "desc_len": 158} |
| PASS | [g/en] meta robots noindex,nofollow | "present" |
| PASS | [g/en] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/g/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/g/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/g/"]] |
| PASS | [g/en] html lang + data-design | "en" |
| PASS | [g/en] every referenced asset and link returns 200 | {"checked": 115, "bad": []} |
| PASS | [g/en] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [g/en] page weight under 3 MB excluding map tiles | "2538 KB" |
| PASS | [g/en] no horizontal overflow at 1440 | {"sw": 1440, "cw": 1440} |
| PASS | [g/en] no text leaves the screen at 1440 | [] |
| PASS | [g/en] every section fills the screen (>=0.95 of viewport height) | [["hero", 1.44], ["lake", 2.54], ["bitcoin", 1.65], ["transport", 2.28], ["community", 3.46], ["tours", 1.82], ["expats", 1.23], ["about", 6.96]] |
| PASS | [g/en] map ready and renders 117 markers | {"state": "ready", "markers": 117, "tiles": 16} |
| PASS | [g/en] list count == marker count == 117 | {"cards": 117, "markers": 117, "hook": {"m": 117, "c": 117, "v": 117, "p": 117}} |
| PASS | [g/en] count text shows 117 | "Showing 117 of 117 places" |
| PASS | [g/en] markers use the design's own colour token | {"fills": ["oklch(40% 0.12 145)"], "token": "oklch(40% 0.12 145)"} |
| PASS | [g/en] search filters list and map together | {"c": 6, "m": 6, "paths": 6} |
| PASS | [g/en] category chip filters (stay) | {"c": 16, "m": 16, "pressed": "stay"} |
| PASS | [g/en] village filter | {"c": 10, "m": 10} |
| PASS | [g/en] empty state | {"c": 0, "m": 0, "empty": true} |
| PASS | [g/en] reset restores 117 | {"c": 117, "m": 117} |
| PASS | [g/en] ride 'Show on map' opens a popup | "popup" |
| PASS | [g/en] every image has alt text | {"images": 51, "bad": []} |
| PASS | [g/en] only local photos, each with a Commons, approved community-archive, or linked press credit | {"photos": 49, "no_credit": [], "other_images": []} |
| PASS | [g/en] all 30 press photos appear once with visible linked credits | {"count": 30, "unique": 30, "missing": [], "bad_credit": []} |
| PASS | [g/en] no broken images | "ok" |
| PASS | [g/en] no 'official'/'oficial' claim | "none" |
| PASS | [g/en] no em or en dashes in visible text | [] |
| PASS | [g/en] merchant check note present | "ok" |
| PASS | [g/en] 117 places + 50+ claim + data date | "ok" |
| PASS | [g/en] OSM/ODbL, BTC Map and Commons credits in footer | "ok" |
| PASS | [g/en] floating Design switcher: all finished designs, current marked, fixed, in view | {"letters": ["A", "C", "D", "AC", "AD", "CD", "F", "G"], "cur": ["G"], "hrefs": ["../a/", "../c/", "../d/", "../ac/", "../ad/", "../cd/", "../f/", "./", "../../variants/"], "inView": true, "fixed": "fixed"} |
| PASS | [g/en] switcher goes to design C in the same language and remembers it | {"url": "https://itstomekk.github.io/lago-bitcoin-community/v/c/", "stored": "c"} |
| PASS | [g/en] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [g/en] 1440 text over photos/gradients: contrast | "no overlay text found" |
| PASS | [g/en] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [g/en] no text leaves the screen at 390 | [] |
| PASS | [g/en] no console errors at 390 | [] |
| PASS | [g/en] brand does not overlap its CTA or menu button at 390 | {"brandRight": 311, "overlapCta": false, "overlapMenu": false} |
| PASS | [g/en] 117 markers at 390 | "ok" |
| PASS | [g/en] switcher fits at 390 | {"right": 382, "vw": 390, "h": 44} |
| PASS | [g/en] mobile menu opens | true |
| PASS | [g/en] menu link scrolls to the merchants section | 0 |
| PASS | [g/en] 390 axe-core WCAG A/AA violations | [] |
| PASS | [g/en] 390 text over photos/gradients: contrast | "no overlay text found" |
| PASS | [g/es] HTTP 200 https://itstomekk.github.io/lago-bitcoin-community/v/g/es/ | 200 |
| PASS | [g/es] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin en el Lago de Atitlán, Guatemala", "desc_len": 179} |
| PASS | [g/es] meta robots noindex,nofollow | "present" |
| PASS | [g/es] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/g/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/g/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/g/"]] |
| PASS | [g/es] html lang + data-design | "es" |
| PASS | [g/es] every referenced asset and link returns 200 | {"checked": 122, "bad": []} |
| PASS | [g/es] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [g/es] page weight under 3 MB excluding map tiles | "2539 KB" |
| PASS | [g/es] no horizontal overflow at 1440 | {"sw": 1440, "cw": 1440} |
| PASS | [g/es] no text leaves the screen at 1440 | [] |
| PASS | [g/es] every section fills the screen (>=0.95 of viewport height) | [["hero", 1.44], ["lake", 2.57], ["bitcoin", 1.65], ["transport", 2.31], ["community", 3.49], ["tours", 1.82], ["expats", 1.23], ["about", 7.01]] |
| PASS | [g/es] map ready and renders 117 markers | {"state": "ready", "markers": 117, "tiles": 16} |
| PASS | [g/es] list count == marker count == 117 | {"cards": 117, "markers": 117, "hook": {"m": 117, "c": 117, "v": 117, "p": 117}} |
| PASS | [g/es] count text shows 117 | "Mostrando 117 de 117 lugares" |
| PASS | [g/es] markers use the design's own colour token | {"fills": ["oklch(40% 0.12 145)"], "token": "oklch(40% 0.12 145)"} |
| PASS | [g/es] search filters list and map together | {"c": 17, "m": 17, "paths": 17} |
| PASS | [g/es] category chip filters (stay) | {"c": 16, "m": 16, "pressed": "stay"} |
| PASS | [g/es] village filter | {"c": 10, "m": 10} |
| PASS | [g/es] empty state | {"c": 0, "m": 0, "empty": true} |
| PASS | [g/es] reset restores 117 | {"c": 117, "m": 117} |
| PASS | [g/es] ride 'Show on map' opens a popup | "popup" |
| PASS | [g/es] every image has alt text | {"images": 51, "bad": []} |
| PASS | [g/es] only local photos, each with a Commons, approved community-archive, or linked press credit | {"photos": 49, "no_credit": [], "other_images": []} |
| PASS | [g/es] all 30 press photos appear once with visible linked credits | {"count": 30, "unique": 30, "missing": [], "bad_credit": []} |
| PASS | [g/es] no broken images | "ok" |
| PASS | [g/es] no 'official'/'oficial' claim | "none" |
| PASS | [g/es] no em or en dashes in visible text | [] |
| PASS | [g/es] merchant check note present | "ok" |
| PASS | [g/es] 117 places + 50+ claim + data date | "ok" |
| PASS | [g/es] OSM/ODbL, BTC Map and Commons credits in footer | "ok" |
| PASS | [g/es] floating Design switcher: all finished designs, current marked, fixed, in view | {"letters": ["A", "C", "D", "AC", "AD", "CD", "F", "G"], "cur": ["G"], "hrefs": ["../../a/es/", "../../c/es/", "../../d/es/", "../../ac/es/", "../../ad/es/", "../../cd/es/", "../../f/es/", "./", "../../../variants/es/"], |
| PASS | [g/es] switcher goes to design C in the same language and remembers it | {"url": "https://itstomekk.github.io/lago-bitcoin-community/v/c/es/", "stored": "c"} |
| PASS | [g/es] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [g/es] 1440 text over photos/gradients: contrast | "no overlay text found" |
| PASS | [g/es] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [g/es] no text leaves the screen at 390 | [] |
| PASS | [g/es] no console errors at 390 | [] |
| PASS | [g/es] brand does not overlap its CTA or menu button at 390 | {"brandRight": 311, "overlapCta": false, "overlapMenu": false} |
| PASS | [g/es] 117 markers at 390 | "ok" |
| PASS | [g/es] switcher fits at 390 | {"right": 382, "vw": 390, "h": 44} |
| PASS | [g/es] mobile menu opens | true |
| PASS | [g/es] menu link scrolls to the merchants section | 0 |
| PASS | [g] EN/ES parity: same section ids in same order | ["hero", "lake", "bitcoin", "transport", "community", "tours", "expats", "about"] |
| PASS | [g] EN/ES parity: placeholders, nav targets, h2 and image counts | {"placeholders": ["atm-locations", "contact-email", "expat-contact", "facebook", "meetup-dates", "meetup-venues", "school-list", "tomek-bio-photo", "tour-booking", "tour-booking-details", "whatsapp-invite-url"], "h2": 7, |
| PASS | [g] every nav link targets an existing section | ["#lake", "#bitcoin", "#transport", "#community", "#tours", "#expats", "#about"] |
| PASS | [g] no section dropped (map, merchants, community, tours, expats, boat/tuk tuk, ATM, history) | [] |
| PASS | [g] browser language es: opening EN redirects to /es/ | "https://itstomekk.github.io/lago-bitcoin-community/v/g/es/" |
| PASS | [g] EN switch stays in this design and stores the choice | "https://itstomekk.github.io/lago-bitcoin-community/v/g/" |
| PASS | [g] ES switch stays in this design | "https://itstomekk.github.io/lago-bitcoin-community/v/g/es/" |
| PASS | [g] browser language en: opening /es/ redirects to EN | "https://itstomekk.github.io/lago-bitcoin-community/v/g/" |
| PASS | [g] placeholder button shows 'coming soon' toast | "toast" |
| PASS | [g] placeholder badge visible in preview | "\"Placeholder: whatsapp-invite-url\"" |
| PASS | [index/en] HTTP 200 https://itstomekk.github.io/lago-bitcoin-community/variants/ | 200 |
| PASS | [index/en] noindex,nofollow | "present" |
| PASS | [index/en] every referenced asset and link returns 200 | {"checked": 31, "bad": []} |
| PASS | [index/en] 1440: 9 cards and loaded thumbnails, no console errors or overflow | {"info": {"cards": 9, "thumbs": 9}, "errs": [], "ov": {"sw": 1440, "cw": 1440}} |
| PASS | [index/en] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [index/en] 390: 9 cards and loaded thumbnails, no console errors or overflow | {"info": {"cards": 9, "thumbs": 9}, "errs": [], "ov": {"sw": 390, "cw": 390}} |
| PASS | [index/en] 390 axe-core WCAG A/AA violations | [] |
| PASS | [index/en] card G opens /v/g/ in en | "https://itstomekk.github.io/lago-bitcoin-community/v/g/" |
| PASS | [index/es] HTTP 200 https://itstomekk.github.io/lago-bitcoin-community/variants/es/ | 200 |
| PASS | [index/es] noindex,nofollow | "present" |
| PASS | [index/es] every referenced asset and link returns 200 | {"checked": 32, "bad": []} |
| PASS | [index/es] 1440: 9 cards and loaded thumbnails, no console errors or overflow | {"info": {"cards": 9, "thumbs": 9}, "errs": [], "ov": {"sw": 1440, "cw": 1440}} |
| PASS | [index/es] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [index/es] 390: 9 cards and loaded thumbnails, no console errors or overflow | {"info": {"cards": 9, "thumbs": 9}, "errs": [], "ov": {"sw": 390, "cw": 390}} |
| PASS | [index/es] 390 axe-core WCAG A/AA violations | [] |
| PASS | [index/es] card G opens /v/g/ in es | "https://itstomekk.github.io/lago-bitcoin-community/v/g/es/" |
| PASS | HTTP 200 https://itstomekk.github.io/lago-bitcoin-community/v/ | 200 |
| PASS | every data-placeholder is listed in HANDOFF.md | {"placeholders": ["atm-locations", "contact-email", "expat-contact", "facebook", "meetup-dates", "meetup-venues", "school-list", "tomek-bio-photo", "tour-booking", "tour-booking-details", "whatsapp-invite-url"], "missing |