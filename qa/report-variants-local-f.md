# Variants QA report (local-f)

Base URL: http://127.0.0.1:18435/
Variants: f
PASS 98 / FAIL 0

| Result | Gate | Evidence |
|---|---|---|
| PASS | robots.txt Disallow while private | 200 |
| PASS | [f/en] HTTP 200 http://127.0.0.1:18435/v/f/ | 200 |
| PASS | [f/en] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin on Lake Atitlán, Guatemala", "desc_len": 158} |
| PASS | [f/en] meta robots noindex,nofollow | "present" |
| PASS | [f/en] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/f/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/f/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/f/"]] |
| PASS | [f/en] html lang + data-design | "en" |
| PASS | [f/en] every referenced asset and link returns 200 | {"checked": 117, "bad": []} |
| PASS | [f/en] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [f/en] page weight under 3 MB excluding map tiles | "2292 KB" |
| PASS | [f/en] no horizontal overflow at 1440 | {"sw": 1440, "cw": 1440} |
| PASS | [f/en] no text leaves the screen at 1440 | [] |
| PASS | [f/en] every section fills the screen (>=0.95 of viewport height) | [["hero", 0.95], ["lake", 1.2], ["bitcoin", 1.5], ["transport", 2.29], ["community", 1.99], ["tours", 0.95], ["expats", 0.95], ["about", 6.03]] |
| PASS | [f/en] map ready and renders 117 markers | {"state": "ready", "markers": 117, "tiles": 15} |
| PASS | [f/en] list count == marker count == 117 | {"cards": 117, "markers": 117, "hook": {"m": 117, "c": 117, "v": 117, "p": 117}} |
| PASS | [f/en] count text shows 117 | "Showing 117 of 117 places" |
| PASS | [f/en] markers use the design's own colour token | {"fills": ["oklch(48% 0.16 25)"], "token": "oklch(48% 0.16 25)"} |
| PASS | [f/en] search filters list and map together | {"c": 6, "m": 6, "paths": 6} |
| PASS | [f/en] category chip filters (stay) | {"c": 16, "m": 16, "pressed": "stay"} |
| PASS | [f/en] village filter | {"c": 10, "m": 10} |
| PASS | [f/en] empty state | {"c": 0, "m": 0, "empty": true} |
| PASS | [f/en] reset restores 117 | {"c": 117, "m": 117} |
| PASS | [f/en] ride 'Show on map' opens a popup | "popup" |
| PASS | [f/en] every image has alt text | {"images": 52, "bad": []} |
| PASS | [f/en] only local photos, each with a Commons, approved community-archive, or linked press credit | {"photos": 50, "no_credit": [], "other_images": []} |
| PASS | [f/en] all 30 press photos appear once with visible linked credits | {"count": 30, "unique": 30, "missing": [], "bad_credit": []} |
| PASS | [f/en] no broken images | "ok" |
| PASS | [f/en] no 'official'/'oficial' claim | "none" |
| PASS | [f/en] no em or en dashes in visible text | [] |
| PASS | [f/en] merchant check note present | "ok" |
| PASS | [f/en] 117 places + 50+ claim + data date | "ok" |
| PASS | [f/en] OSM/ODbL, BTC Map and Commons credits in footer | "ok" |
| PASS | [f/en] floating Design switcher: all finished designs, current marked, fixed, in view | {"letters": ["A", "C", "D", "AC", "AD", "CD", "F"], "cur": ["F"], "hrefs": ["../a/", "../c/", "../d/", "../ac/", "../ad/", "../cd/", "./", "../../variants/"], "inView": true, "fixed": "fixed"} |
| PASS | [f/en] switcher goes to design C in the same language and remembers it | {"url": "http://127.0.0.1:18435/v/c/", "stored": "c"} |
| PASS | [f/en] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [f/en] 1440 text over photos/gradients: contrast | "no overlay text found" |
| PASS | [f/en] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [f/en] no text leaves the screen at 390 | [] |
| PASS | [f/en] no console errors at 390 | [] |
| PASS | [f/en] brand does not overlap its CTA or menu button at 390 | {"brandRight": 129, "overlapCta": false, "overlapMenu": false} |
| PASS | [f/en] 117 markers at 390 | "ok" |
| PASS | [f/en] switcher fits at 390 | {"right": 375, "vw": 390, "h": 52} |
| PASS | [f/en] mobile menu opens | true |
| PASS | [f/en] menu link scrolls to the merchants section | -0.0 |
| PASS | [f/en] 390 axe-core WCAG A/AA violations | [] |
| PASS | [f/en] 390 text over photos/gradients: contrast | "no overlay text found" |
| PASS | [f/es] HTTP 200 http://127.0.0.1:18435/v/f/es/ | 200 |
| PASS | [f/es] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin en el Lago de Atitlán, Guatemala", "desc_len": 179} |
| PASS | [f/es] meta robots noindex,nofollow | "present" |
| PASS | [f/es] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/f/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/f/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/f/"]] |
| PASS | [f/es] html lang + data-design | "es" |
| PASS | [f/es] every referenced asset and link returns 200 | {"checked": 123, "bad": []} |
| PASS | [f/es] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [f/es] page weight under 3 MB excluding map tiles | "2293 KB" |
| PASS | [f/es] no horizontal overflow at 1440 | {"sw": 1440, "cw": 1440} |
| PASS | [f/es] no text leaves the screen at 1440 | [] |
| PASS | [f/es] every section fills the screen (>=0.95 of viewport height) | [["hero", 0.95], ["lake", 1.19], ["bitcoin", 1.56], ["transport", 2.33], ["community", 1.99], ["tours", 0.95], ["expats", 0.95], ["about", 6.03]] |
| PASS | [f/es] map ready and renders 117 markers | {"state": "ready", "markers": 117, "tiles": 15} |
| PASS | [f/es] list count == marker count == 117 | {"cards": 117, "markers": 117, "hook": {"m": 117, "c": 117, "v": 117, "p": 117}} |
| PASS | [f/es] count text shows 117 | "Mostrando 117 de 117 lugares" |
| PASS | [f/es] markers use the design's own colour token | {"fills": ["oklch(48% 0.16 25)"], "token": "oklch(48% 0.16 25)"} |
| PASS | [f/es] search filters list and map together | {"c": 17, "m": 17, "paths": 17} |
| PASS | [f/es] category chip filters (stay) | {"c": 16, "m": 16, "pressed": "stay"} |
| PASS | [f/es] village filter | {"c": 10, "m": 10} |
| PASS | [f/es] empty state | {"c": 0, "m": 0, "empty": true} |
| PASS | [f/es] reset restores 117 | {"c": 117, "m": 117} |
| PASS | [f/es] ride 'Show on map' opens a popup | "popup" |
| PASS | [f/es] every image has alt text | {"images": 52, "bad": []} |
| PASS | [f/es] only local photos, each with a Commons, approved community-archive, or linked press credit | {"photos": 50, "no_credit": [], "other_images": []} |
| PASS | [f/es] all 30 press photos appear once with visible linked credits | {"count": 30, "unique": 30, "missing": [], "bad_credit": []} |
| PASS | [f/es] no broken images | "ok" |
| PASS | [f/es] no 'official'/'oficial' claim | "none" |
| PASS | [f/es] no em or en dashes in visible text | [] |
| PASS | [f/es] merchant check note present | "ok" |
| PASS | [f/es] 117 places + 50+ claim + data date | "ok" |
| PASS | [f/es] OSM/ODbL, BTC Map and Commons credits in footer | "ok" |
| PASS | [f/es] floating Design switcher: all finished designs, current marked, fixed, in view | {"letters": ["A", "C", "D", "AC", "AD", "CD", "F"], "cur": ["F"], "hrefs": ["../../a/es/", "../../c/es/", "../../d/es/", "../../ac/es/", "../../ad/es/", "../../cd/es/", "./", "../../../variants/es/"], "inView": true, "fi |
| PASS | [f/es] switcher goes to design C in the same language and remembers it | {"url": "http://127.0.0.1:18435/v/c/es/", "stored": "c"} |
| PASS | [f/es] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [f/es] 1440 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 1, "lowest_ratio": 19.08, "failures": []} |
| PASS | [f/es] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [f/es] no text leaves the screen at 390 | [] |
| PASS | [f/es] no console errors at 390 | [] |
| PASS | [f/es] brand does not overlap its CTA or menu button at 390 | {"brandRight": 129, "overlapCta": false, "overlapMenu": false} |
| PASS | [f/es] 117 markers at 390 | "ok" |
| PASS | [f/es] switcher fits at 390 | {"right": 378, "vw": 390, "h": 52} |
| PASS | [f/es] mobile menu opens | true |
| PASS | [f/es] menu link scrolls to the merchants section | 0 |
| PASS | [f] EN/ES parity: same section ids in same order | ["hero", "lake", "bitcoin", "transport", "community", "tours", "expats", "about"] |
| PASS | [f] EN/ES parity: placeholders, nav targets, h2 and image counts | {"placeholders": ["atm-locations", "contact-email", "expat-contact", "facebook", "meetup-dates", "meetup-venues", "school-list", "tomek-bio-photo", "tour-booking", "tour-booking-details", "whatsapp-invite-url"], "h2": 7, |
| PASS | [f] every nav link targets an existing section | ["#lake", "#bitcoin", "#transport", "#community", "#about"] |
| PASS | [f] no section dropped (map, merchants, community, tours, expats, boat/tuk tuk, ATM, history) | [] |
| PASS | [f] browser language es: opening EN redirects to /es/ | "http://127.0.0.1:18435/v/f/es/" |
| PASS | [f] EN switch stays in this design and stores the choice | "http://127.0.0.1:18435/v/f/" |
| PASS | [f] ES switch stays in this design | "http://127.0.0.1:18435/v/f/es/" |
| PASS | [f] browser language en: opening /es/ redirects to EN | "http://127.0.0.1:18435/v/f/" |
| PASS | [f] placeholder button shows 'coming soon' toast | "toast" |
| PASS | [f] placeholder badge visible in preview | "\"Placeholder: whatsapp-invite-url\"" |
| PASS | every data-placeholder is listed in HANDOFF.md | {"placeholders": ["atm-locations", "contact-email", "expat-contact", "facebook", "meetup-dates", "meetup-venues", "school-list", "tomek-bio-photo", "tour-booking", "tour-booking-details", "whatsapp-invite-url"], "missing |