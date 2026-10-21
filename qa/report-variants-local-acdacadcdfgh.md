# Variants QA report (local-acdacadcdfgh)

Base URL: http://127.0.0.1:18431/
Variants: a, c, d, ac, ad, cd, f, g, h
PASS 899 / FAIL 0

| Result | Gate | Evidence |
|---|---|---|
| PASS | robots.txt Disallow while private | 200 |
| PASS | [a/en] HTTP 200 http://127.0.0.1:18431/v/a/ | 200 |
| PASS | [a/en] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin on Lake Atitlán, Guatemala", "desc_len": 158} |
| PASS | [a/en] meta robots noindex,nofollow | "present" |
| PASS | [a/en] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/a/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/a/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/a/"]] |
| PASS | [a/en] html lang + data-design | "en" |
| PASS | [a/en] every referenced asset and link returns 200 | {"checked": 119, "bad": []} |
| PASS | [a/en] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [a/en] page weight under 3 MB excluding map tiles | "2289 KB" |
| PASS | [a/en] no horizontal overflow at 1440 | {"sw": 1440, "cw": 1440} |
| PASS | [a/en] no text leaves the screen at 1440 | [] |
| PASS | [a/en] every section fills the screen (>=0.95 of viewport height) | [["hero", 1], ["lake", 1.16], ["bitcoin", 1.8], ["transport", 1.44], ["community", 1.59], ["tours", 1], ["expats", 1], ["about", 5.94]] |
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
| PASS | [a/en] every image has alt text | {"images": 51, "bad": []} |
| PASS | [a/en] only local photos, each with a Commons, approved community-archive, or linked press credit | {"photos": 49, "no_credit": [], "other_images": []} |
| PASS | [a/en] all 30 press photos appear once with visible linked credits | {"count": 30, "unique": 30, "missing": [], "bad_credit": []} |
| PASS | [a/en] no broken images | "ok" |
| PASS | [a/en] no 'official'/'oficial' claim | "none" |
| PASS | [a/en] no em or en dashes in visible text | [] |
| PASS | [a/en] merchant check note present | "ok" |
| PASS | [a/en] 117 places + 50+ claim + data date | "ok" |
| PASS | [a/en] OSM/ODbL, BTC Map and Commons credits in footer | "ok" |
| PASS | [a/en] floating Design switcher: all finished designs, current marked, fixed, in view | {"letters": ["A", "C", "D", "AC", "AD", "CD", "F", "G", "H"], "cur": ["A"], "hrefs": ["./", "../c/", "../d/", "../ac/", "../ad/", "../cd/", "../f/", "../g/", "../h/", "../../variants/"], "inView": true, "fixed": "fixed"} |
| PASS | [a/en] switcher goes to design C in the same language and remembers it | {"url": "http://127.0.0.1:18431/v/c/", "stored": "c"} |
| PASS | [a/en] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [a/en] 1440 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 3, "candidates": 3, "lowest_ratio": 6.04, "failures": []} |
| PASS | [a/en] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [a/en] no text leaves the screen at 390 | [] |
| PASS | [a/en] no console errors at 390 | [] |
| PASS | [a/en] brand does not overlap its CTA or menu button at 390 | {"brandRight": 213, "overlapCta": false, "overlapMenu": false} |
| PASS | [a/en] 117 markers at 390 | "ok" |
| PASS | [a/en] switcher fits at 390 | {"right": 382, "vw": 390, "h": 40} |
| PASS | [a/en] mobile menu opens | true |
| PASS | [a/en] navigation link scrolls to the merchants section | -0.0 |
| PASS | [a/en] 390 axe-core WCAG A/AA violations | [] |
| PASS | [a/en] 390 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 3, "candidates": 3, "lowest_ratio": 6.04, "failures": []} |
| PASS | [a/es] HTTP 200 http://127.0.0.1:18431/v/a/es/ | 200 |
| PASS | [a/es] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin en el Lago de Atitlán, Guatemala", "desc_len": 179} |
| PASS | [a/es] meta robots noindex,nofollow | "present" |
| PASS | [a/es] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/a/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/a/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/a/"]] |
| PASS | [a/es] html lang + data-design | "es" |
| PASS | [a/es] every referenced asset and link returns 200 | {"checked": 127, "bad": []} |
| PASS | [a/es] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [a/es] page weight under 3 MB excluding map tiles | "2291 KB" |
| PASS | [a/es] no horizontal overflow at 1440 | {"sw": 1440, "cw": 1440} |
| PASS | [a/es] no text leaves the screen at 1440 | [] |
| PASS | [a/es] every section fills the screen (>=0.95 of viewport height) | [["hero", 1], ["lake", 1.19], ["bitcoin", 1.8], ["transport", 1.48], ["community", 1.54], ["tours", 1], ["expats", 1], ["about", 5.94]] |
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
| PASS | [a/es] every image has alt text | {"images": 51, "bad": []} |
| PASS | [a/es] only local photos, each with a Commons, approved community-archive, or linked press credit | {"photos": 49, "no_credit": [], "other_images": []} |
| PASS | [a/es] all 30 press photos appear once with visible linked credits | {"count": 30, "unique": 30, "missing": [], "bad_credit": []} |
| PASS | [a/es] no broken images | "ok" |
| PASS | [a/es] no 'official'/'oficial' claim | "none" |
| PASS | [a/es] no em or en dashes in visible text | [] |
| PASS | [a/es] merchant check note present | "ok" |
| PASS | [a/es] 117 places + 50+ claim + data date | "ok" |
| PASS | [a/es] OSM/ODbL, BTC Map and Commons credits in footer | "ok" |
| PASS | [a/es] floating Design switcher: all finished designs, current marked, fixed, in view | {"letters": ["A", "C", "D", "AC", "AD", "CD", "F", "G", "H"], "cur": ["A"], "hrefs": ["./", "../../c/es/", "../../d/es/", "../../ac/es/", "../../ad/es/", "../../cd/es/", "../../f/es/", "../../g/es/", "../../h/es/", "../. |
| PASS | [a/es] switcher goes to design C in the same language and remembers it | {"url": "http://127.0.0.1:18431/v/c/es/", "stored": "c"} |
| PASS | [a/es] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [a/es] 1440 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 3, "candidates": 3, "lowest_ratio": 6.04, "failures": []} |
| PASS | [a/es] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [a/es] no text leaves the screen at 390 | [] |
| PASS | [a/es] no console errors at 390 | [] |
| PASS | [a/es] brand does not overlap its CTA or menu button at 390 | {"brandRight": 213, "overlapCta": false, "overlapMenu": false} |
| PASS | [a/es] 117 markers at 390 | "ok" |
| PASS | [a/es] switcher fits at 390 | {"right": 382, "vw": 390, "h": 40} |
| PASS | [a/es] mobile menu opens | true |
| PASS | [a/es] navigation link scrolls to the merchants section | 0 |
| PASS | [a] EN/ES parity: same section ids in same order | ["hero", "lake", "bitcoin", "transport", "community", "tours", "expats", "about"] |
| PASS | [a] EN/ES parity: placeholders, nav targets, h2 and image counts | {"placeholders": ["atm-locations", "contact-email", "expat-contact", "facebook", "meetup-dates", "meetup-venues", "school-list", "tomek-bio-photo", "tour-booking", "tour-booking-details", "whatsapp-invite-url"], "h2": 7, |
| PASS | [a] every nav link targets an existing section | ["#lake", "#bitcoin", "#transport", "#community", "#tours", "#expats", "#about"] |
| PASS | [a] no section dropped (map, merchants, community, tours, expats, boat/tuk tuk, ATM, history) | [] |
| PASS | [a] browser language es: opening EN redirects to /es/ | "http://127.0.0.1:18431/v/a/es/" |
| PASS | [a] EN switch stays in this design and stores the choice | "http://127.0.0.1:18431/v/a/" |
| PASS | [a] ES switch stays in this design | "http://127.0.0.1:18431/v/a/es/" |
| PASS | [a] browser language en: opening /es/ redirects to EN | "http://127.0.0.1:18431/v/a/" |
| PASS | [a] configurable placeholder link shows 'coming soon' toast | "toast" |
| PASS | [a] placeholder badge visible in preview | "\"Placeholder: whatsapp-invite-url\"" |
| PASS | [c/en] HTTP 200 http://127.0.0.1:18431/v/c/ | 200 |
| PASS | [c/en] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin on Lake Atitlán, Guatemala", "desc_len": 158} |
| PASS | [c/en] meta robots noindex,nofollow | "present" |
| PASS | [c/en] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/c/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/c/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/c/"]] |
| PASS | [c/en] html lang + data-design | "en" |
| PASS | [c/en] every referenced asset and link returns 200 | {"checked": 123, "bad": []} |
| PASS | [c/en] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [c/en] page weight under 3 MB excluding map tiles | "2584 KB" |
| PASS | [c/en] no horizontal overflow at 1440 | {"sw": 1440, "cw": 1440} |
| PASS | [c/en] no text leaves the screen at 1440 | [] |
| PASS | [c/en] every section fills the screen (>=0.95 of viewport height) | [["hero", 1], ["lake", 1.12], ["bitcoin", 1.89], ["transport", 1.71], ["community", 1.56], ["tours", 1.13], ["expats", 1], ["about", 6.1]] |
| PASS | [c/en] map ready and renders 117 markers | {"state": "ready", "markers": 117, "tiles": 16} |
| PASS | [c/en] list count == marker count == 117 | {"cards": 117, "markers": 117, "hook": {"m": 117, "c": 117, "v": 117, "p": 117}} |
| PASS | [c/en] count text shows 117 | "Showing 117 of 117 places" |
| PASS | [c/en] markers use the design's own colour token | {"fills": ["#d03040"], "token": "#d03040"} |
| PASS | [c/en] search filters list and map together | {"c": 6, "m": 6, "paths": 6} |
| PASS | [c/en] category chip filters (stay) | {"c": 16, "m": 16, "pressed": "stay"} |
| PASS | [c/en] village filter | {"c": 10, "m": 10} |
| PASS | [c/en] empty state | {"c": 0, "m": 0, "empty": true} |
| PASS | [c/en] reset restores 117 | {"c": 117, "m": 117} |
| PASS | [c/en] ride 'Show on map' opens a popup | "popup" |
| PASS | [c/en] every image has alt text | {"images": 52, "bad": []} |
| PASS | [c/en] only local photos, each with a Commons, approved community-archive, or linked press credit | {"photos": 50, "no_credit": [], "other_images": []} |
| PASS | [c/en] all 30 press photos appear once with visible linked credits | {"count": 30, "unique": 30, "missing": [], "bad_credit": []} |
| PASS | [c/en] no broken images | "ok" |
| PASS | [c/en] no 'official'/'oficial' claim | "none" |
| PASS | [c/en] no em or en dashes in visible text | [] |
| PASS | [c/en] merchant check note present | "ok" |
| PASS | [c/en] 117 places + 50+ claim + data date | "ok" |
| PASS | [c/en] OSM/ODbL, BTC Map and Commons credits in footer | "ok" |
| PASS | [c/en] floating Design switcher: all finished designs, current marked, fixed, in view | {"letters": ["A", "C", "D", "AC", "AD", "CD", "F", "G", "H"], "cur": ["C"], "hrefs": ["../a/", "./", "../d/", "../ac/", "../ad/", "../cd/", "../f/", "../g/", "../h/", "../../variants/"], "inView": true, "fixed": "fixed"} |
| PASS | [c/en] switcher goes to design D in the same language and remembers it | {"url": "http://127.0.0.1:18431/v/d/", "stored": "d"} |
| PASS | [c/en] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [c/en] 1440 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 32, "candidates": 32, "lowest_ratio": 5.03, "failures": []} |
| PASS | [c/en] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [c/en] no text leaves the screen at 390 | [] |
| PASS | [c/en] no console errors at 390 | [] |
| PASS | [c/en] brand does not overlap its CTA or menu button at 390 | {"brandRight": 197, "overlapCta": false, "overlapMenu": false} |
| PASS | [c/en] 117 markers at 390 | "ok" |
| PASS | [c/en] switcher fits at 390 | {"right": 382, "vw": 390, "h": 40} |
| PASS | [c/en] mobile menu opens | true |
| PASS | [c/en] navigation link scrolls to the merchants section | -0.0 |
| PASS | [c/en] 390 axe-core WCAG A/AA violations | [] |
| PASS | [c/en] 390 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 32, "candidates": 32, "lowest_ratio": 5.03, "failures": []} |
| PASS | [c/es] HTTP 200 http://127.0.0.1:18431/v/c/es/ | 200 |
| PASS | [c/es] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin en el Lago de Atitlán, Guatemala", "desc_len": 179} |
| PASS | [c/es] meta robots noindex,nofollow | "present" |
| PASS | [c/es] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/c/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/c/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/c/"]] |
| PASS | [c/es] html lang + data-design | "es" |
| PASS | [c/es] every referenced asset and link returns 200 | {"checked": 131, "bad": []} |
| PASS | [c/es] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [c/es] page weight under 3 MB excluding map tiles | "2585 KB" |
| PASS | [c/es] no horizontal overflow at 1440 | {"sw": 1440, "cw": 1440} |
| PASS | [c/es] no text leaves the screen at 1440 | [] |
| PASS | [c/es] every section fills the screen (>=0.95 of viewport height) | [["hero", 1], ["lake", 1.24], ["bitcoin", 1.89], ["transport", 1.62], ["community", 1.57], ["tours", 1.1], ["expats", 1], ["about", 6.1]] |
| PASS | [c/es] map ready and renders 117 markers | {"state": "ready", "markers": 117, "tiles": 16} |
| PASS | [c/es] list count == marker count == 117 | {"cards": 117, "markers": 117, "hook": {"m": 117, "c": 117, "v": 117, "p": 117}} |
| PASS | [c/es] count text shows 117 | "Mostrando 117 de 117 lugares" |
| PASS | [c/es] markers use the design's own colour token | {"fills": ["#d03040"], "token": "#d03040"} |
| PASS | [c/es] search filters list and map together | {"c": 17, "m": 17, "paths": 17} |
| PASS | [c/es] category chip filters (stay) | {"c": 16, "m": 16, "pressed": "stay"} |
| PASS | [c/es] village filter | {"c": 10, "m": 10} |
| PASS | [c/es] empty state | {"c": 0, "m": 0, "empty": true} |
| PASS | [c/es] reset restores 117 | {"c": 117, "m": 117} |
| PASS | [c/es] ride 'Show on map' opens a popup | "popup" |
| PASS | [c/es] every image has alt text | {"images": 52, "bad": []} |
| PASS | [c/es] only local photos, each with a Commons, approved community-archive, or linked press credit | {"photos": 50, "no_credit": [], "other_images": []} |
| PASS | [c/es] all 30 press photos appear once with visible linked credits | {"count": 30, "unique": 30, "missing": [], "bad_credit": []} |
| PASS | [c/es] no broken images | "ok" |
| PASS | [c/es] no 'official'/'oficial' claim | "none" |
| PASS | [c/es] no em or en dashes in visible text | [] |
| PASS | [c/es] merchant check note present | "ok" |
| PASS | [c/es] 117 places + 50+ claim + data date | "ok" |
| PASS | [c/es] OSM/ODbL, BTC Map and Commons credits in footer | "ok" |
| PASS | [c/es] floating Design switcher: all finished designs, current marked, fixed, in view | {"letters": ["A", "C", "D", "AC", "AD", "CD", "F", "G", "H"], "cur": ["C"], "hrefs": ["../../a/es/", "./", "../../d/es/", "../../ac/es/", "../../ad/es/", "../../cd/es/", "../../f/es/", "../../g/es/", "../../h/es/", "../. |
| PASS | [c/es] switcher goes to design D in the same language and remembers it | {"url": "http://127.0.0.1:18431/v/d/es/", "stored": "d"} |
| PASS | [c/es] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [c/es] 1440 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 32, "candidates": 32, "lowest_ratio": 5.03, "failures": []} |
| PASS | [c/es] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [c/es] no text leaves the screen at 390 | [] |
| PASS | [c/es] no console errors at 390 | [] |
| PASS | [c/es] brand does not overlap its CTA or menu button at 390 | {"brandRight": 197, "overlapCta": false, "overlapMenu": false} |
| PASS | [c/es] 117 markers at 390 | "ok" |
| PASS | [c/es] switcher fits at 390 | {"right": 382, "vw": 390, "h": 40} |
| PASS | [c/es] mobile menu opens | true |
| PASS | [c/es] navigation link scrolls to the merchants section | -0.0 |
| PASS | [c] EN/ES parity: same section ids in same order | ["hero", "lake", "bitcoin", "transport", "community", "tours", "expats", "about"] |
| PASS | [c] EN/ES parity: placeholders, nav targets, h2 and image counts | {"placeholders": ["atm-locations", "contact-email", "expat-contact", "facebook", "meetup-dates", "meetup-venues", "school-list", "tomek-bio-photo", "tour-booking", "tour-booking-details", "whatsapp-invite-url"], "h2": 7, |
| PASS | [c] every nav link targets an existing section | ["#lake", "#bitcoin", "#transport", "#community", "#tours", "#expats", "#about"] |
| PASS | [c] no section dropped (map, merchants, community, tours, expats, boat/tuk tuk, ATM, history) | [] |
| PASS | [c] browser language es: opening EN redirects to /es/ | "http://127.0.0.1:18431/v/c/es/" |
| PASS | [c] EN switch stays in this design and stores the choice | "http://127.0.0.1:18431/v/c/" |
| PASS | [c] ES switch stays in this design | "http://127.0.0.1:18431/v/c/es/" |
| PASS | [c] browser language en: opening /es/ redirects to EN | "http://127.0.0.1:18431/v/c/" |
| PASS | [c] configurable placeholder link shows 'coming soon' toast | "toast" |
| PASS | [c] placeholder badge visible in preview | "\"Placeholder: whatsapp-invite-url\"" |
| PASS | [d/en] HTTP 200 http://127.0.0.1:18431/v/d/ | 200 |
| PASS | [d/en] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin on Lake Atitlán, Guatemala", "desc_len": 158} |
| PASS | [d/en] meta robots noindex,nofollow | "present" |
| PASS | [d/en] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/d/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/d/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/d/"]] |
| PASS | [d/en] html lang + data-design | "en" |
| PASS | [d/en] every referenced asset and link returns 200 | {"checked": 123, "bad": []} |
| PASS | [d/en] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [d/en] page weight under 3 MB excluding map tiles | "2359 KB" |
| PASS | [d/en] no horizontal overflow at 1440 | {"sw": 1440, "cw": 1440} |
| PASS | [d/en] no text leaves the screen at 1440 | [] |
| PASS | [d/en] every section fills the screen (>=0.95 of viewport height) | [["hero", 1], ["lake", 1.29], ["bitcoin", 1.78], ["transport", 1.55], ["community", 1.66], ["tours", 1], ["expats", 1], ["about", 6.12]] |
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
| PASS | [d/en] every image has alt text | {"images": 52, "bad": []} |
| PASS | [d/en] only local photos, each with a Commons, approved community-archive, or linked press credit | {"photos": 50, "no_credit": [], "other_images": []} |
| PASS | [d/en] all 30 press photos appear once with visible linked credits | {"count": 30, "unique": 30, "missing": [], "bad_credit": []} |
| PASS | [d/en] no broken images | "ok" |
| PASS | [d/en] no 'official'/'oficial' claim | "none" |
| PASS | [d/en] no em or en dashes in visible text | [] |
| PASS | [d/en] merchant check note present | "ok" |
| PASS | [d/en] 117 places + 50+ claim + data date | "ok" |
| PASS | [d/en] OSM/ODbL, BTC Map and Commons credits in footer | "ok" |
| PASS | [d/en] floating Design switcher: all finished designs, current marked, fixed, in view | {"letters": ["A", "C", "D", "AC", "AD", "CD", "F", "G", "H"], "cur": ["D"], "hrefs": ["../a/", "../c/", "./", "../ac/", "../ad/", "../cd/", "../f/", "../g/", "../h/", "../../variants/"], "inView": true, "fixed": "fixed"} |
| PASS | [d/en] switcher goes to design C in the same language and remembers it | {"url": "http://127.0.0.1:18431/v/c/", "stored": "c"} |
| PASS | [d/en] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [d/en] 1440 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 8, "candidates": 8, "lowest_ratio": 9.64, "failures": []} |
| PASS | [d/en] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [d/en] no text leaves the screen at 390 | [] |
| PASS | [d/en] no console errors at 390 | [] |
| PASS | [d/en] brand does not overlap its CTA or menu button at 390 | {"brandRight": 221, "overlapCta": false, "overlapMenu": false} |
| PASS | [d/en] 117 markers at 390 | "ok" |
| PASS | [d/en] switcher fits at 390 | {"right": 382, "vw": 390, "h": 40} |
| PASS | [d/en] mobile menu opens | true |
| PASS | [d/en] navigation link scrolls to the merchants section | 84 |
| PASS | [d/en] 390 axe-core WCAG A/AA violations | [] |
| PASS | [d/en] 390 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 8, "candidates": 8, "lowest_ratio": 9.67, "failures": []} |
| PASS | [d/es] HTTP 200 http://127.0.0.1:18431/v/d/es/ | 200 |
| PASS | [d/es] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin en el Lago de Atitlán, Guatemala", "desc_len": 179} |
| PASS | [d/es] meta robots noindex,nofollow | "present" |
| PASS | [d/es] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/d/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/d/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/d/"]] |
| PASS | [d/es] html lang + data-design | "es" |
| PASS | [d/es] every referenced asset and link returns 200 | {"checked": 131, "bad": []} |
| PASS | [d/es] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [d/es] page weight under 3 MB excluding map tiles | "2360 KB" |
| PASS | [d/es] no horizontal overflow at 1440 | {"sw": 1440, "cw": 1440} |
| PASS | [d/es] no text leaves the screen at 1440 | [] |
| PASS | [d/es] every section fills the screen (>=0.95 of viewport height) | [["hero", 1], ["lake", 1.29], ["bitcoin", 1.78], ["transport", 1.55], ["community", 1.67], ["tours", 1], ["expats", 1], ["about", 6.12]] |
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
| PASS | [d/es] every image has alt text | {"images": 52, "bad": []} |
| PASS | [d/es] only local photos, each with a Commons, approved community-archive, or linked press credit | {"photos": 50, "no_credit": [], "other_images": []} |
| PASS | [d/es] all 30 press photos appear once with visible linked credits | {"count": 30, "unique": 30, "missing": [], "bad_credit": []} |
| PASS | [d/es] no broken images | "ok" |
| PASS | [d/es] no 'official'/'oficial' claim | "none" |
| PASS | [d/es] no em or en dashes in visible text | [] |
| PASS | [d/es] merchant check note present | "ok" |
| PASS | [d/es] 117 places + 50+ claim + data date | "ok" |
| PASS | [d/es] OSM/ODbL, BTC Map and Commons credits in footer | "ok" |
| PASS | [d/es] floating Design switcher: all finished designs, current marked, fixed, in view | {"letters": ["A", "C", "D", "AC", "AD", "CD", "F", "G", "H"], "cur": ["D"], "hrefs": ["../../a/es/", "../../c/es/", "./", "../../ac/es/", "../../ad/es/", "../../cd/es/", "../../f/es/", "../../g/es/", "../../h/es/", "../. |
| PASS | [d/es] switcher goes to design C in the same language and remembers it | {"url": "http://127.0.0.1:18431/v/c/es/", "stored": "c"} |
| PASS | [d/es] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [d/es] 1440 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 8, "candidates": 8, "lowest_ratio": 9.67, "failures": []} |
| PASS | [d/es] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [d/es] no text leaves the screen at 390 | [] |
| PASS | [d/es] no console errors at 390 | [] |
| PASS | [d/es] brand does not overlap its CTA or menu button at 390 | {"brandRight": 221, "overlapCta": false, "overlapMenu": false} |
| PASS | [d/es] 117 markers at 390 | "ok" |
| PASS | [d/es] switcher fits at 390 | {"right": 382, "vw": 390, "h": 40} |
| PASS | [d/es] mobile menu opens | true |
| PASS | [d/es] navigation link scrolls to the merchants section | 84 |
| PASS | [d] EN/ES parity: same section ids in same order | ["hero", "lake", "bitcoin", "transport", "community", "tours", "expats", "about"] |
| PASS | [d] EN/ES parity: placeholders, nav targets, h2 and image counts | {"placeholders": ["atm-locations", "contact-email", "expat-contact", "facebook", "meetup-dates", "meetup-venues", "school-list", "tomek-bio-photo", "tour-booking", "tour-booking-details", "whatsapp-invite-url"], "h2": 7, |
| PASS | [d] every nav link targets an existing section | ["#lake", "#bitcoin", "#transport", "#community", "#tours", "#expats", "#about"] |
| PASS | [d] no section dropped (map, merchants, community, tours, expats, boat/tuk tuk, ATM, history) | [] |
| PASS | [d] browser language es: opening EN redirects to /es/ | "http://127.0.0.1:18431/v/d/es/" |
| PASS | [d] EN switch stays in this design and stores the choice | "http://127.0.0.1:18431/v/d/" |
| PASS | [d] ES switch stays in this design | "http://127.0.0.1:18431/v/d/es/" |
| PASS | [d] browser language en: opening /es/ redirects to EN | "http://127.0.0.1:18431/v/d/" |
| PASS | [d] configurable placeholder link shows 'coming soon' toast | "toast" |
| PASS | [d] placeholder badge visible in preview | "\"Placeholder: whatsapp-invite-url\"" |
| PASS | [ac/en] HTTP 200 http://127.0.0.1:18431/v/ac/ | 200 |
| PASS | [ac/en] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin on Lake Atitlán, Guatemala", "desc_len": 158} |
| PASS | [ac/en] meta robots noindex,nofollow | "present" |
| PASS | [ac/en] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/ac/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/ac/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/ac/"]] |
| PASS | [ac/en] html lang + data-design | "en" |
| PASS | [ac/en] every referenced asset and link returns 200 | {"checked": 123, "bad": []} |
| PASS | [ac/en] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [ac/en] page weight under 3 MB excluding map tiles | "2585 KB" |
| PASS | [ac/en] no horizontal overflow at 1440 | {"sw": 1440, "cw": 1440} |
| PASS | [ac/en] no text leaves the screen at 1440 | [] |
| PASS | [ac/en] every section fills the screen (>=0.95 of viewport height) | [["hero", 1], ["lake", 1.12], ["bitcoin", 1.89], ["transport", 1.71], ["community", 1.56], ["tours", 1.13], ["expats", 1], ["about", 6.1]] |
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
| PASS | [ac/en] every image has alt text | {"images": 52, "bad": []} |
| PASS | [ac/en] only local photos, each with a Commons, approved community-archive, or linked press credit | {"photos": 50, "no_credit": [], "other_images": []} |
| PASS | [ac/en] all 30 press photos appear once with visible linked credits | {"count": 30, "unique": 30, "missing": [], "bad_credit": []} |
| PASS | [ac/en] no broken images | "ok" |
| PASS | [ac/en] no 'official'/'oficial' claim | "none" |
| PASS | [ac/en] no em or en dashes in visible text | [] |
| PASS | [ac/en] merchant check note present | "ok" |
| PASS | [ac/en] 117 places + 50+ claim + data date | "ok" |
| PASS | [ac/en] OSM/ODbL, BTC Map and Commons credits in footer | "ok" |
| PASS | [ac/en] floating Design switcher: all finished designs, current marked, fixed, in view | {"letters": ["A", "C", "D", "AC", "AD", "CD", "F", "G", "H"], "cur": ["AC"], "hrefs": ["../a/", "../c/", "../d/", "./", "../ad/", "../cd/", "../f/", "../g/", "../h/", "../../variants/"], "inView": true, "fixed": "fixed"} |
| PASS | [ac/en] switcher goes to design C in the same language and remembers it | {"url": "http://127.0.0.1:18431/v/c/", "stored": "c"} |
| PASS | [ac/en] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [ac/en] 1440 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 29, "candidates": 29, "lowest_ratio": 5.35, "failures": []} |
| PASS | [ac/en] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [ac/en] no text leaves the screen at 390 | [] |
| PASS | [ac/en] no console errors at 390 | [] |
| PASS | [ac/en] brand does not overlap its CTA or menu button at 390 | {"brandRight": 197, "overlapCta": false, "overlapMenu": false} |
| PASS | [ac/en] 117 markers at 390 | "ok" |
| PASS | [ac/en] switcher fits at 390 | {"right": 382, "vw": 390, "h": 40} |
| PASS | [ac/en] mobile menu opens | true |
| PASS | [ac/en] navigation link scrolls to the merchants section | -0.0 |
| PASS | [ac/en] 390 axe-core WCAG A/AA violations | [] |
| PASS | [ac/en] 390 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 29, "candidates": 29, "lowest_ratio": 5.35, "failures": []} |
| PASS | [ac/es] HTTP 200 http://127.0.0.1:18431/v/ac/es/ | 200 |
| PASS | [ac/es] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin en el Lago de Atitlán, Guatemala", "desc_len": 179} |
| PASS | [ac/es] meta robots noindex,nofollow | "present" |
| PASS | [ac/es] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/ac/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/ac/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/ac/"]] |
| PASS | [ac/es] html lang + data-design | "es" |
| PASS | [ac/es] every referenced asset and link returns 200 | {"checked": 131, "bad": []} |
| PASS | [ac/es] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [ac/es] page weight under 3 MB excluding map tiles | "2587 KB" |
| PASS | [ac/es] no horizontal overflow at 1440 | {"sw": 1440, "cw": 1440} |
| PASS | [ac/es] no text leaves the screen at 1440 | [] |
| PASS | [ac/es] every section fills the screen (>=0.95 of viewport height) | [["hero", 1], ["lake", 1.24], ["bitcoin", 1.89], ["transport", 1.62], ["community", 1.57], ["tours", 1.1], ["expats", 1], ["about", 6.1]] |
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
| PASS | [ac/es] every image has alt text | {"images": 52, "bad": []} |
| PASS | [ac/es] only local photos, each with a Commons, approved community-archive, or linked press credit | {"photos": 50, "no_credit": [], "other_images": []} |
| PASS | [ac/es] all 30 press photos appear once with visible linked credits | {"count": 30, "unique": 30, "missing": [], "bad_credit": []} |
| PASS | [ac/es] no broken images | "ok" |
| PASS | [ac/es] no 'official'/'oficial' claim | "none" |
| PASS | [ac/es] no em or en dashes in visible text | [] |
| PASS | [ac/es] merchant check note present | "ok" |
| PASS | [ac/es] 117 places + 50+ claim + data date | "ok" |
| PASS | [ac/es] OSM/ODbL, BTC Map and Commons credits in footer | "ok" |
| PASS | [ac/es] floating Design switcher: all finished designs, current marked, fixed, in view | {"letters": ["A", "C", "D", "AC", "AD", "CD", "F", "G", "H"], "cur": ["AC"], "hrefs": ["../../a/es/", "../../c/es/", "../../d/es/", "./", "../../ad/es/", "../../cd/es/", "../../f/es/", "../../g/es/", "../../h/es/", "../. |
| PASS | [ac/es] switcher goes to design C in the same language and remembers it | {"url": "http://127.0.0.1:18431/v/c/es/", "stored": "c"} |
| PASS | [ac/es] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [ac/es] 1440 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 29, "candidates": 29, "lowest_ratio": 5.35, "failures": []} |
| PASS | [ac/es] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [ac/es] no text leaves the screen at 390 | [] |
| PASS | [ac/es] no console errors at 390 | [] |
| PASS | [ac/es] brand does not overlap its CTA or menu button at 390 | {"brandRight": 197, "overlapCta": false, "overlapMenu": false} |
| PASS | [ac/es] 117 markers at 390 | "ok" |
| PASS | [ac/es] switcher fits at 390 | {"right": 382, "vw": 390, "h": 40} |
| PASS | [ac/es] mobile menu opens | true |
| PASS | [ac/es] navigation link scrolls to the merchants section | -0.0 |
| PASS | [ac] EN/ES parity: same section ids in same order | ["hero", "lake", "bitcoin", "transport", "community", "tours", "expats", "about"] |
| PASS | [ac] EN/ES parity: placeholders, nav targets, h2 and image counts | {"placeholders": ["atm-locations", "contact-email", "expat-contact", "facebook", "meetup-dates", "meetup-venues", "school-list", "tomek-bio-photo", "tour-booking", "tour-booking-details", "whatsapp-invite-url"], "h2": 7, |
| PASS | [ac] every nav link targets an existing section | ["#lake", "#bitcoin", "#transport", "#community", "#tours", "#expats", "#about"] |
| PASS | [ac] no section dropped (map, merchants, community, tours, expats, boat/tuk tuk, ATM, history) | [] |
| PASS | [ac] browser language es: opening EN redirects to /es/ | "http://127.0.0.1:18431/v/ac/es/" |
| PASS | [ac] EN switch stays in this design and stores the choice | "http://127.0.0.1:18431/v/ac/" |
| PASS | [ac] ES switch stays in this design | "http://127.0.0.1:18431/v/ac/es/" |
| PASS | [ac] browser language en: opening /es/ redirects to EN | "http://127.0.0.1:18431/v/ac/" |
| PASS | [ac] configurable placeholder link shows 'coming soon' toast | "toast" |
| PASS | [ac] placeholder badge visible in preview | "\"Placeholder: whatsapp-invite-url\"" |
| PASS | [ad/en] HTTP 200 http://127.0.0.1:18431/v/ad/ | 200 |
| PASS | [ad/en] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin on Lake Atitlán, Guatemala", "desc_len": 158} |
| PASS | [ad/en] meta robots noindex,nofollow | "present" |
| PASS | [ad/en] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/ad/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/ad/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/ad/"]] |
| PASS | [ad/en] html lang + data-design | "en" |
| PASS | [ad/en] every referenced asset and link returns 200 | {"checked": 123, "bad": []} |
| PASS | [ad/en] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [ad/en] page weight under 3 MB excluding map tiles | "2361 KB" |
| PASS | [ad/en] no horizontal overflow at 1440 | {"sw": 1440, "cw": 1440} |
| PASS | [ad/en] no text leaves the screen at 1440 | [] |
| PASS | [ad/en] every section fills the screen (>=0.95 of viewport height) | [["hero", 1], ["lake", 1.3], ["bitcoin", 1.78], ["transport", 1.55], ["community", 1.66], ["tours", 1], ["expats", 1], ["about", 6.12]] |
| PASS | [ad/en] map ready and renders 117 markers | {"state": "ready", "markers": 117, "tiles": 16} |
| PASS | [ad/en] list count == marker count == 117 | {"cards": 117, "markers": 117, "hook": {"m": 117, "c": 117, "v": 117, "p": 117}} |
| PASS | [ad/en] count text shows 117 | "Showing 117 of 117 places" |
| PASS | [ad/en] markers use the design's own colour token | {"fills": ["#20a060"], "token": "#20a060"} |
| PASS | [ad/en] search filters list and map together | {"c": 6, "m": 6, "paths": 6} |
| PASS | [ad/en] category chip filters (stay) | {"c": 16, "m": 16, "pressed": "stay"} |
| PASS | [ad/en] village filter | {"c": 10, "m": 10} |
| PASS | [ad/en] empty state | {"c": 0, "m": 0, "empty": true} |
| PASS | [ad/en] reset restores 117 | {"c": 117, "m": 117} |
| PASS | [ad/en] ride 'Show on map' opens a popup | "popup" |
| PASS | [ad/en] every image has alt text | {"images": 52, "bad": []} |
| PASS | [ad/en] only local photos, each with a Commons, approved community-archive, or linked press credit | {"photos": 50, "no_credit": [], "other_images": []} |
| PASS | [ad/en] all 30 press photos appear once with visible linked credits | {"count": 30, "unique": 30, "missing": [], "bad_credit": []} |
| PASS | [ad/en] no broken images | "ok" |
| PASS | [ad/en] no 'official'/'oficial' claim | "none" |
| PASS | [ad/en] no em or en dashes in visible text | [] |
| PASS | [ad/en] merchant check note present | "ok" |
| PASS | [ad/en] 117 places + 50+ claim + data date | "ok" |
| PASS | [ad/en] OSM/ODbL, BTC Map and Commons credits in footer | "ok" |
| PASS | [ad/en] floating Design switcher: all finished designs, current marked, fixed, in view | {"letters": ["A", "C", "D", "AC", "AD", "CD", "F", "G", "H"], "cur": ["AD"], "hrefs": ["../a/", "../c/", "../d/", "../ac/", "./", "../cd/", "../f/", "../g/", "../h/", "../../variants/"], "inView": true, "fixed": "fixed"} |
| PASS | [ad/en] switcher goes to design C in the same language and remembers it | {"url": "http://127.0.0.1:18431/v/c/", "stored": "c"} |
| PASS | [ad/en] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [ad/en] 1440 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 8, "candidates": 8, "lowest_ratio": 9.98, "failures": []} |
| PASS | [ad/en] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [ad/en] no text leaves the screen at 390 | [] |
| PASS | [ad/en] no console errors at 390 | [] |
| PASS | [ad/en] brand does not overlap its CTA or menu button at 390 | {"brandRight": 221, "overlapCta": false, "overlapMenu": false} |
| PASS | [ad/en] 117 markers at 390 | "ok" |
| PASS | [ad/en] switcher fits at 390 | {"right": 382, "vw": 390, "h": 40} |
| PASS | [ad/en] mobile menu opens | true |
| PASS | [ad/en] navigation link scrolls to the merchants section | 84 |
| PASS | [ad/en] 390 axe-core WCAG A/AA violations | [] |
| PASS | [ad/en] 390 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 8, "candidates": 8, "lowest_ratio": 9.98, "failures": []} |
| PASS | [ad/es] HTTP 200 http://127.0.0.1:18431/v/ad/es/ | 200 |
| PASS | [ad/es] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin en el Lago de Atitlán, Guatemala", "desc_len": 179} |
| PASS | [ad/es] meta robots noindex,nofollow | "present" |
| PASS | [ad/es] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/ad/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/ad/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/ad/"]] |
| PASS | [ad/es] html lang + data-design | "es" |
| PASS | [ad/es] every referenced asset and link returns 200 | {"checked": 131, "bad": []} |
| PASS | [ad/es] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [ad/es] page weight under 3 MB excluding map tiles | "2362 KB" |
| PASS | [ad/es] no horizontal overflow at 1440 | {"sw": 1440, "cw": 1440} |
| PASS | [ad/es] no text leaves the screen at 1440 | [] |
| PASS | [ad/es] every section fills the screen (>=0.95 of viewport height) | [["hero", 1], ["lake", 1.3], ["bitcoin", 1.78], ["transport", 1.55], ["community", 1.67], ["tours", 1], ["expats", 1], ["about", 6.12]] |
| PASS | [ad/es] map ready and renders 117 markers | {"state": "ready", "markers": 117, "tiles": 16} |
| PASS | [ad/es] list count == marker count == 117 | {"cards": 117, "markers": 117, "hook": {"m": 117, "c": 117, "v": 117, "p": 117}} |
| PASS | [ad/es] count text shows 117 | "Mostrando 117 de 117 lugares" |
| PASS | [ad/es] markers use the design's own colour token | {"fills": ["#20a060"], "token": "#20a060"} |
| PASS | [ad/es] search filters list and map together | {"c": 17, "m": 17, "paths": 17} |
| PASS | [ad/es] category chip filters (stay) | {"c": 16, "m": 16, "pressed": "stay"} |
| PASS | [ad/es] village filter | {"c": 10, "m": 10} |
| PASS | [ad/es] empty state | {"c": 0, "m": 0, "empty": true} |
| PASS | [ad/es] reset restores 117 | {"c": 117, "m": 117} |
| PASS | [ad/es] ride 'Show on map' opens a popup | "popup" |
| PASS | [ad/es] every image has alt text | {"images": 52, "bad": []} |
| PASS | [ad/es] only local photos, each with a Commons, approved community-archive, or linked press credit | {"photos": 50, "no_credit": [], "other_images": []} |
| PASS | [ad/es] all 30 press photos appear once with visible linked credits | {"count": 30, "unique": 30, "missing": [], "bad_credit": []} |
| PASS | [ad/es] no broken images | "ok" |
| PASS | [ad/es] no 'official'/'oficial' claim | "none" |
| PASS | [ad/es] no em or en dashes in visible text | [] |
| PASS | [ad/es] merchant check note present | "ok" |
| PASS | [ad/es] 117 places + 50+ claim + data date | "ok" |
| PASS | [ad/es] OSM/ODbL, BTC Map and Commons credits in footer | "ok" |
| PASS | [ad/es] floating Design switcher: all finished designs, current marked, fixed, in view | {"letters": ["A", "C", "D", "AC", "AD", "CD", "F", "G", "H"], "cur": ["AD"], "hrefs": ["../../a/es/", "../../c/es/", "../../d/es/", "../../ac/es/", "./", "../../cd/es/", "../../f/es/", "../../g/es/", "../../h/es/", "../. |
| PASS | [ad/es] switcher goes to design C in the same language and remembers it | {"url": "http://127.0.0.1:18431/v/c/es/", "stored": "c"} |
| PASS | [ad/es] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [ad/es] 1440 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 8, "candidates": 8, "lowest_ratio": 9.98, "failures": []} |
| PASS | [ad/es] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [ad/es] no text leaves the screen at 390 | [] |
| PASS | [ad/es] no console errors at 390 | [] |
| PASS | [ad/es] brand does not overlap its CTA or menu button at 390 | {"brandRight": 221, "overlapCta": false, "overlapMenu": false} |
| PASS | [ad/es] 117 markers at 390 | "ok" |
| PASS | [ad/es] switcher fits at 390 | {"right": 382, "vw": 390, "h": 40} |
| PASS | [ad/es] mobile menu opens | true |
| PASS | [ad/es] navigation link scrolls to the merchants section | 84 |
| PASS | [ad] EN/ES parity: same section ids in same order | ["hero", "lake", "bitcoin", "transport", "community", "tours", "expats", "about"] |
| PASS | [ad] EN/ES parity: placeholders, nav targets, h2 and image counts | {"placeholders": ["atm-locations", "contact-email", "expat-contact", "facebook", "meetup-dates", "meetup-venues", "school-list", "tomek-bio-photo", "tour-booking", "tour-booking-details", "whatsapp-invite-url"], "h2": 7, |
| PASS | [ad] every nav link targets an existing section | ["#lake", "#bitcoin", "#transport", "#community", "#tours", "#expats", "#about"] |
| PASS | [ad] no section dropped (map, merchants, community, tours, expats, boat/tuk tuk, ATM, history) | [] |
| PASS | [ad] browser language es: opening EN redirects to /es/ | "http://127.0.0.1:18431/v/ad/es/" |
| PASS | [ad] EN switch stays in this design and stores the choice | "http://127.0.0.1:18431/v/ad/" |
| PASS | [ad] ES switch stays in this design | "http://127.0.0.1:18431/v/ad/es/" |
| PASS | [ad] browser language en: opening /es/ redirects to EN | "http://127.0.0.1:18431/v/ad/" |
| PASS | [ad] configurable placeholder link shows 'coming soon' toast | "toast" |
| PASS | [ad] placeholder badge visible in preview | "\"Placeholder: whatsapp-invite-url\"" |
| PASS | [cd/en] HTTP 200 http://127.0.0.1:18431/v/cd/ | 200 |
| PASS | [cd/en] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin on Lake Atitlán, Guatemala", "desc_len": 158} |
| PASS | [cd/en] meta robots noindex,nofollow | "present" |
| PASS | [cd/en] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/cd/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/cd/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/cd/"]] |
| PASS | [cd/en] html lang + data-design | "en" |
| PASS | [cd/en] every referenced asset and link returns 200 | {"checked": 123, "bad": []} |
| PASS | [cd/en] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [cd/en] page weight under 3 MB excluding map tiles | "2585 KB" |
| PASS | [cd/en] no horizontal overflow at 1440 | {"sw": 1440, "cw": 1440} |
| PASS | [cd/en] no text leaves the screen at 1440 | [] |
| PASS | [cd/en] every section fills the screen (>=0.95 of viewport height) | [["hero", 1], ["lake", 1.12], ["bitcoin", 1.89], ["transport", 1.71], ["community", 1.56], ["tours", 1.13], ["expats", 1], ["about", 6.1]] |
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
| PASS | [cd/en] every image has alt text | {"images": 52, "bad": []} |
| PASS | [cd/en] only local photos, each with a Commons, approved community-archive, or linked press credit | {"photos": 50, "no_credit": [], "other_images": []} |
| PASS | [cd/en] all 30 press photos appear once with visible linked credits | {"count": 30, "unique": 30, "missing": [], "bad_credit": []} |
| PASS | [cd/en] no broken images | "ok" |
| PASS | [cd/en] no 'official'/'oficial' claim | "none" |
| PASS | [cd/en] no em or en dashes in visible text | [] |
| PASS | [cd/en] merchant check note present | "ok" |
| PASS | [cd/en] 117 places + 50+ claim + data date | "ok" |
| PASS | [cd/en] OSM/ODbL, BTC Map and Commons credits in footer | "ok" |
| PASS | [cd/en] floating Design switcher: all finished designs, current marked, fixed, in view | {"letters": ["A", "C", "D", "AC", "AD", "CD", "F", "G", "H"], "cur": ["CD"], "hrefs": ["../a/", "../c/", "../d/", "../ac/", "../ad/", "./", "../f/", "../g/", "../h/", "../../variants/"], "inView": true, "fixed": "fixed"} |
| PASS | [cd/en] switcher goes to design C in the same language and remembers it | {"url": "http://127.0.0.1:18431/v/c/", "stored": "c"} |
| PASS | [cd/en] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [cd/en] 1440 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 32, "candidates": 32, "lowest_ratio": 5.03, "failures": []} |
| PASS | [cd/en] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [cd/en] no text leaves the screen at 390 | [] |
| PASS | [cd/en] no console errors at 390 | [] |
| PASS | [cd/en] brand does not overlap its CTA or menu button at 390 | {"brandRight": 197, "overlapCta": false, "overlapMenu": false} |
| PASS | [cd/en] 117 markers at 390 | "ok" |
| PASS | [cd/en] switcher fits at 390 | {"right": 382, "vw": 390, "h": 40} |
| PASS | [cd/en] mobile menu opens | true |
| PASS | [cd/en] navigation link scrolls to the merchants section | -0.0 |
| PASS | [cd/en] 390 axe-core WCAG A/AA violations | [] |
| PASS | [cd/en] 390 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 32, "candidates": 32, "lowest_ratio": 5.03, "failures": []} |
| PASS | [cd/es] HTTP 200 http://127.0.0.1:18431/v/cd/es/ | 200 |
| PASS | [cd/es] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin en el Lago de Atitlán, Guatemala", "desc_len": 179} |
| PASS | [cd/es] meta robots noindex,nofollow | "present" |
| PASS | [cd/es] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/cd/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/cd/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/cd/"]] |
| PASS | [cd/es] html lang + data-design | "es" |
| PASS | [cd/es] every referenced asset and link returns 200 | {"checked": 131, "bad": []} |
| PASS | [cd/es] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [cd/es] page weight under 3 MB excluding map tiles | "2586 KB" |
| PASS | [cd/es] no horizontal overflow at 1440 | {"sw": 1440, "cw": 1440} |
| PASS | [cd/es] no text leaves the screen at 1440 | [] |
| PASS | [cd/es] every section fills the screen (>=0.95 of viewport height) | [["hero", 1], ["lake", 1.24], ["bitcoin", 1.89], ["transport", 1.62], ["community", 1.57], ["tours", 1.1], ["expats", 1], ["about", 6.1]] |
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
| PASS | [cd/es] every image has alt text | {"images": 52, "bad": []} |
| PASS | [cd/es] only local photos, each with a Commons, approved community-archive, or linked press credit | {"photos": 50, "no_credit": [], "other_images": []} |
| PASS | [cd/es] all 30 press photos appear once with visible linked credits | {"count": 30, "unique": 30, "missing": [], "bad_credit": []} |
| PASS | [cd/es] no broken images | "ok" |
| PASS | [cd/es] no 'official'/'oficial' claim | "none" |
| PASS | [cd/es] no em or en dashes in visible text | [] |
| PASS | [cd/es] merchant check note present | "ok" |
| PASS | [cd/es] 117 places + 50+ claim + data date | "ok" |
| PASS | [cd/es] OSM/ODbL, BTC Map and Commons credits in footer | "ok" |
| PASS | [cd/es] floating Design switcher: all finished designs, current marked, fixed, in view | {"letters": ["A", "C", "D", "AC", "AD", "CD", "F", "G", "H"], "cur": ["CD"], "hrefs": ["../../a/es/", "../../c/es/", "../../d/es/", "../../ac/es/", "../../ad/es/", "./", "../../f/es/", "../../g/es/", "../../h/es/", "../. |
| PASS | [cd/es] switcher goes to design C in the same language and remembers it | {"url": "http://127.0.0.1:18431/v/c/es/", "stored": "c"} |
| PASS | [cd/es] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [cd/es] 1440 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 32, "candidates": 32, "lowest_ratio": 5.03, "failures": []} |
| PASS | [cd/es] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [cd/es] no text leaves the screen at 390 | [] |
| PASS | [cd/es] no console errors at 390 | [] |
| PASS | [cd/es] brand does not overlap its CTA or menu button at 390 | {"brandRight": 197, "overlapCta": false, "overlapMenu": false} |
| PASS | [cd/es] 117 markers at 390 | "ok" |
| PASS | [cd/es] switcher fits at 390 | {"right": 382, "vw": 390, "h": 40} |
| PASS | [cd/es] mobile menu opens | true |
| PASS | [cd/es] navigation link scrolls to the merchants section | -0.0 |
| PASS | [cd] EN/ES parity: same section ids in same order | ["hero", "lake", "bitcoin", "transport", "community", "tours", "expats", "about"] |
| PASS | [cd] EN/ES parity: placeholders, nav targets, h2 and image counts | {"placeholders": ["atm-locations", "contact-email", "expat-contact", "facebook", "meetup-dates", "meetup-venues", "school-list", "tomek-bio-photo", "tour-booking", "tour-booking-details", "whatsapp-invite-url"], "h2": 7, |
| PASS | [cd] every nav link targets an existing section | ["#lake", "#bitcoin", "#transport", "#community", "#tours", "#expats", "#about"] |
| PASS | [cd] no section dropped (map, merchants, community, tours, expats, boat/tuk tuk, ATM, history) | [] |
| PASS | [cd] browser language es: opening EN redirects to /es/ | "http://127.0.0.1:18431/v/cd/es/" |
| PASS | [cd] EN switch stays in this design and stores the choice | "http://127.0.0.1:18431/v/cd/" |
| PASS | [cd] ES switch stays in this design | "http://127.0.0.1:18431/v/cd/es/" |
| PASS | [cd] browser language en: opening /es/ redirects to EN | "http://127.0.0.1:18431/v/cd/" |
| PASS | [cd] configurable placeholder link shows 'coming soon' toast | "toast" |
| PASS | [cd] placeholder badge visible in preview | "\"Placeholder: whatsapp-invite-url\"" |
| PASS | [f/en] HTTP 200 http://127.0.0.1:18431/v/f/ | 200 |
| PASS | [f/en] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin on Lake Atitlán, Guatemala", "desc_len": 158} |
| PASS | [f/en] meta robots noindex,nofollow | "present" |
| PASS | [f/en] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/f/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/f/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/f/"]] |
| PASS | [f/en] html lang + data-design | "en" |
| PASS | [f/en] every referenced asset and link returns 200 | {"checked": 119, "bad": []} |
| PASS | [f/en] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [f/en] page weight under 3 MB excluding map tiles | "2294 KB" |
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
| PASS | [f/en] floating Design switcher: all finished designs, current marked, fixed, in view | {"letters": ["A", "C", "D", "AC", "AD", "CD", "F", "G", "H"], "cur": ["F"], "hrefs": ["../a/", "../c/", "../d/", "../ac/", "../ad/", "../cd/", "./", "../g/", "../h/", "../../variants/"], "inView": true, "fixed": "fixed"} |
| PASS | [f/en] switcher goes to design C in the same language and remembers it | {"url": "http://127.0.0.1:18431/v/c/", "stored": "c"} |
| PASS | [f/en] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [f/en] 1440 text over photos/gradients: contrast | "no overlay text found" |
| PASS | [f/en] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [f/en] no text leaves the screen at 390 | [] |
| PASS | [f/en] no console errors at 390 | [] |
| PASS | [f/en] brand does not overlap its CTA or menu button at 390 | {"brandRight": 129, "overlapCta": false, "overlapMenu": false} |
| PASS | [f/en] 117 markers at 390 | "ok" |
| PASS | [f/en] switcher fits at 390 | {"right": 378, "vw": 390, "h": 52} |
| PASS | [f/en] mobile menu opens | true |
| PASS | [f/en] navigation link scrolls to the merchants section | -0.0 |
| PASS | [f/en] 390 axe-core WCAG A/AA violations | [] |
| PASS | [f/en] 390 text over photos/gradients: contrast | "no overlay text found" |
| PASS | [f/es] HTTP 200 http://127.0.0.1:18431/v/f/es/ | 200 |
| PASS | [f/es] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin en el Lago de Atitlán, Guatemala", "desc_len": 179} |
| PASS | [f/es] meta robots noindex,nofollow | "present" |
| PASS | [f/es] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/f/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/f/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/f/"]] |
| PASS | [f/es] html lang + data-design | "es" |
| PASS | [f/es] every referenced asset and link returns 200 | {"checked": 127, "bad": []} |
| PASS | [f/es] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [f/es] page weight under 3 MB excluding map tiles | "2295 KB" |
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
| PASS | [f/es] floating Design switcher: all finished designs, current marked, fixed, in view | {"letters": ["A", "C", "D", "AC", "AD", "CD", "F", "G", "H"], "cur": ["F"], "hrefs": ["../../a/es/", "../../c/es/", "../../d/es/", "../../ac/es/", "../../ad/es/", "../../cd/es/", "./", "../../g/es/", "../../h/es/", "../. |
| PASS | [f/es] switcher goes to design C in the same language and remembers it | {"url": "http://127.0.0.1:18431/v/c/es/", "stored": "c"} |
| PASS | [f/es] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [f/es] 1440 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 1, "candidates": 1, "lowest_ratio": 16.89, "failures": []} |
| PASS | [f/es] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [f/es] no text leaves the screen at 390 | [] |
| PASS | [f/es] no console errors at 390 | [] |
| PASS | [f/es] brand does not overlap its CTA or menu button at 390 | {"brandRight": 129, "overlapCta": false, "overlapMenu": false} |
| PASS | [f/es] 117 markers at 390 | "ok" |
| PASS | [f/es] switcher fits at 390 | {"right": 378, "vw": 390, "h": 52} |
| PASS | [f/es] mobile menu opens | true |
| PASS | [f/es] navigation link scrolls to the merchants section | 0 |
| PASS | [f] EN/ES parity: same section ids in same order | ["hero", "lake", "bitcoin", "transport", "community", "tours", "expats", "about"] |
| PASS | [f] EN/ES parity: placeholders, nav targets, h2 and image counts | {"placeholders": ["atm-locations", "contact-email", "expat-contact", "facebook", "meetup-dates", "meetup-venues", "school-list", "tomek-bio-photo", "tour-booking", "tour-booking-details", "whatsapp-invite-url"], "h2": 7, |
| PASS | [f] every nav link targets an existing section | ["#lake", "#bitcoin", "#transport", "#community", "#about"] |
| PASS | [f] no section dropped (map, merchants, community, tours, expats, boat/tuk tuk, ATM, history) | [] |
| PASS | [f] browser language es: opening EN redirects to /es/ | "http://127.0.0.1:18431/v/f/es/" |
| PASS | [f] EN switch stays in this design and stores the choice | "http://127.0.0.1:18431/v/f/" |
| PASS | [f] ES switch stays in this design | "http://127.0.0.1:18431/v/f/es/" |
| PASS | [f] browser language en: opening /es/ redirects to EN | "http://127.0.0.1:18431/v/f/" |
| PASS | [f] configurable placeholder link shows 'coming soon' toast | "toast" |
| PASS | [f] placeholder badge visible in preview | "\"Placeholder: whatsapp-invite-url\"" |
| PASS | [g/en] HTTP 200 http://127.0.0.1:18431/v/g/ | 200 |
| PASS | [g/en] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin on Lake Atitlán, Guatemala", "desc_len": 158} |
| PASS | [g/en] meta robots noindex,nofollow | "present" |
| PASS | [g/en] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/g/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/g/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/g/"]] |
| PASS | [g/en] html lang + data-design | "en" |
| PASS | [g/en] every referenced asset and link returns 200 | {"checked": 116, "bad": []} |
| PASS | [g/en] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [g/en] page weight under 3 MB excluding map tiles | "2543 KB" |
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
| PASS | [g/en] floating Design switcher: all finished designs, current marked, fixed, in view | {"letters": ["A", "C", "D", "AC", "AD", "CD", "F", "G", "H"], "cur": ["G"], "hrefs": ["../a/", "../c/", "../d/", "../ac/", "../ad/", "../cd/", "../f/", "./", "../h/", "../../variants/"], "inView": true, "fixed": "fixed"} |
| PASS | [g/en] switcher goes to design C in the same language and remembers it | {"url": "http://127.0.0.1:18431/v/c/", "stored": "c"} |
| PASS | [g/en] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [g/en] 1440 text over photos/gradients: contrast | "no overlay text found" |
| PASS | [g/en] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [g/en] no text leaves the screen at 390 | [] |
| PASS | [g/en] no console errors at 390 | [] |
| PASS | [g/en] brand does not overlap its CTA or menu button at 390 | {"brandRight": 311, "overlapCta": false, "overlapMenu": false} |
| PASS | [g/en] 117 markers at 390 | "ok" |
| PASS | [g/en] switcher fits at 390 | {"right": 382, "vw": 390, "h": 40} |
| PASS | [g/en] mobile menu opens | true |
| PASS | [g/en] navigation link scrolls to the merchants section | 0 |
| PASS | [g/en] 390 axe-core WCAG A/AA violations | [] |
| PASS | [g/en] 390 text over photos/gradients: contrast | "no overlay text found" |
| PASS | [g/es] HTTP 200 http://127.0.0.1:18431/v/g/es/ | 200 |
| PASS | [g/es] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin en el Lago de Atitlán, Guatemala", "desc_len": 179} |
| PASS | [g/es] meta robots noindex,nofollow | "present" |
| PASS | [g/es] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/g/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/g/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/g/"]] |
| PASS | [g/es] html lang + data-design | "es" |
| PASS | [g/es] every referenced asset and link returns 200 | {"checked": 124, "bad": []} |
| PASS | [g/es] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [g/es] page weight under 3 MB excluding map tiles | "2545 KB" |
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
| PASS | [g/es] floating Design switcher: all finished designs, current marked, fixed, in view | {"letters": ["A", "C", "D", "AC", "AD", "CD", "F", "G", "H"], "cur": ["G"], "hrefs": ["../../a/es/", "../../c/es/", "../../d/es/", "../../ac/es/", "../../ad/es/", "../../cd/es/", "../../f/es/", "./", "../../h/es/", "../. |
| PASS | [g/es] switcher goes to design C in the same language and remembers it | {"url": "http://127.0.0.1:18431/v/c/es/", "stored": "c"} |
| PASS | [g/es] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [g/es] 1440 text over photos/gradients: contrast | "no overlay text found" |
| PASS | [g/es] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [g/es] no text leaves the screen at 390 | [] |
| PASS | [g/es] no console errors at 390 | [] |
| PASS | [g/es] brand does not overlap its CTA or menu button at 390 | {"brandRight": 311, "overlapCta": false, "overlapMenu": false} |
| PASS | [g/es] 117 markers at 390 | "ok" |
| PASS | [g/es] switcher fits at 390 | {"right": 382, "vw": 390, "h": 40} |
| PASS | [g/es] mobile menu opens | true |
| PASS | [g/es] navigation link scrolls to the merchants section | 0 |
| PASS | [g] EN/ES parity: same section ids in same order | ["hero", "lake", "bitcoin", "transport", "community", "tours", "expats", "about"] |
| PASS | [g] EN/ES parity: placeholders, nav targets, h2 and image counts | {"placeholders": ["atm-locations", "contact-email", "expat-contact", "facebook", "meetup-dates", "meetup-venues", "school-list", "tomek-bio-photo", "tour-booking", "tour-booking-details", "whatsapp-invite-url"], "h2": 7, |
| PASS | [g] every nav link targets an existing section | ["#lake", "#bitcoin", "#transport", "#community", "#tours", "#expats", "#about"] |
| PASS | [g] no section dropped (map, merchants, community, tours, expats, boat/tuk tuk, ATM, history) | [] |
| PASS | [g] browser language es: opening EN redirects to /es/ | "http://127.0.0.1:18431/v/g/es/" |
| PASS | [g] EN switch stays in this design and stores the choice | "http://127.0.0.1:18431/v/g/" |
| PASS | [g] ES switch stays in this design | "http://127.0.0.1:18431/v/g/es/" |
| PASS | [g] browser language en: opening /es/ redirects to EN | "http://127.0.0.1:18431/v/g/" |
| PASS | [g] configurable placeholder link shows 'coming soon' toast | "toast" |
| PASS | [g] placeholder badge visible in preview | "\"Placeholder: whatsapp-invite-url\"" |
| PASS | [h/en] HTTP 200 http://127.0.0.1:18431/v/h/ | 200 |
| PASS | [h/en] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin on Lake Atitlán, Guatemala", "desc_len": 158} |
| PASS | [h/en] meta robots noindex,nofollow | "present" |
| PASS | [h/en] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/h/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/h/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/h/"]] |
| PASS | [h/en] html lang + data-design | "en" |
| PASS | [h/en] every referenced asset and link returns 200 | {"checked": 116, "bad": []} |
| PASS | [h/en] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [h/en] page weight under 3 MB excluding map tiles | "2164 KB" |
| PASS | [h/en] no horizontal overflow at 1440 | {"sw": 1440, "cw": 1440} |
| PASS | [h/en] no text leaves the screen at 1440 | [] |
| PASS | [h/en] every section fills the screen (>=0.95 of viewport height) | [["hero", 0.95], ["lake", 2.56], ["bitcoin", 1.75], ["transport", 1.97], ["community", 2.64], ["tours", 1.85], ["expats", 0.95], ["about", 6.65]] |
| PASS | [h/en] map ready and renders 117 markers | {"state": "ready", "markers": 117, "tiles": 16} |
| PASS | [h/en] list count == marker count == 117 | {"cards": 117, "markers": 117, "hook": {"m": 117, "c": 117, "v": 117, "p": 117}} |
| PASS | [h/en] count text shows 117 | "Showing 117 of 117 places" |
| PASS | [h/en] markers use the design's own colour token | {"fills": ["oklch(45% 0.19 264)"], "token": "oklch(45% 0.19 264)"} |
| PASS | [h/en] search filters list and map together | {"c": 6, "m": 6, "paths": 6} |
| PASS | [h/en] category chip filters (stay) | {"c": 16, "m": 16, "pressed": "stay"} |
| PASS | [h/en] village filter | {"c": 10, "m": 10} |
| PASS | [h/en] empty state | {"c": 0, "m": 0, "empty": true} |
| PASS | [h/en] reset restores 117 | {"c": 117, "m": 117} |
| PASS | [h/en] ride 'Show on map' opens a popup | "popup" |
| PASS | [h/en] every image has alt text | {"images": 49, "bad": []} |
| PASS | [h/en] only local photos, each with a Commons, approved community-archive, or linked press credit | {"photos": 48, "no_credit": [], "other_images": []} |
| PASS | [h/en] all 30 press photos appear once with visible linked credits | {"count": 30, "unique": 30, "missing": [], "bad_credit": []} |
| PASS | [h/en] no broken images | "ok" |
| PASS | [h/en] no 'official'/'oficial' claim | "none" |
| PASS | [h/en] no em or en dashes in visible text | [] |
| PASS | [h/en] merchant check note present | "ok" |
| PASS | [h/en] 117 places + 50+ claim + data date | "ok" |
| PASS | [h/en] OSM/ODbL, BTC Map and Commons credits in footer | "ok" |
| PASS | [h/en] floating Design switcher: all finished designs, current marked, fixed, in view | {"letters": ["A", "C", "D", "AC", "AD", "CD", "F", "G", "H"], "cur": ["H"], "hrefs": ["../a/", "../c/", "../d/", "../ac/", "../ad/", "../cd/", "../f/", "../g/", "./", "../../variants/"], "inView": true, "fixed": "fixed"} |
| PASS | [h/en] switcher goes to design C in the same language and remembers it | {"url": "http://127.0.0.1:18431/v/c/", "stored": "c"} |
| PASS | [h/en] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [h/en] 1440 text over photos/gradients: contrast | "no overlay text found" |
| PASS | [h/en] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [h/en] no text leaves the screen at 390 | [] |
| PASS | [h/en] no console errors at 390 | [] |
| PASS | [h/en] brand does not overlap its CTA or menu button at 390 | {"brandRight": 92, "overlapCta": false, "overlapMenu": false} |
| PASS | [h/en] 117 markers at 390 | "ok" |
| PASS | [h/en] switcher fits at 390 | {"right": 382, "vw": 390, "h": 40} |
| PASS | [h/en] mobile section map has seven links | true |
| PASS | [h/en] navigation link scrolls to the merchants section | 52 |
| PASS | [h/en] 390 axe-core WCAG A/AA violations | [] |
| PASS | [h/en] 390 text over photos/gradients: contrast | "no overlay text found" |
| PASS | [h/es] HTTP 200 http://127.0.0.1:18431/v/h/es/ | 200 |
| PASS | [h/es] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin en el Lago de Atitlán, Guatemala", "desc_len": 179} |
| PASS | [h/es] meta robots noindex,nofollow | "present" |
| PASS | [h/es] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/h/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/h/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/h/"]] |
| PASS | [h/es] html lang + data-design | "es" |
| PASS | [h/es] every referenced asset and link returns 200 | {"checked": 124, "bad": []} |
| PASS | [h/es] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [h/es] page weight under 3 MB excluding map tiles | "2166 KB" |
| PASS | [h/es] no horizontal overflow at 1440 | {"sw": 1440, "cw": 1440} |
| PASS | [h/es] no text leaves the screen at 1440 | [] |
| PASS | [h/es] every section fills the screen (>=0.95 of viewport height) | [["hero", 0.95], ["lake", 2.44], ["bitcoin", 1.77], ["transport", 1.97], ["community", 2.82], ["tours", 1.69], ["expats", 1], ["about", 6.65]] |
| PASS | [h/es] map ready and renders 117 markers | {"state": "ready", "markers": 117, "tiles": 16} |
| PASS | [h/es] list count == marker count == 117 | {"cards": 117, "markers": 117, "hook": {"m": 117, "c": 117, "v": 117, "p": 117}} |
| PASS | [h/es] count text shows 117 | "Mostrando 117 de 117 lugares" |
| PASS | [h/es] markers use the design's own colour token | {"fills": ["oklch(45% 0.19 264)"], "token": "oklch(45% 0.19 264)"} |
| PASS | [h/es] search filters list and map together | {"c": 17, "m": 17, "paths": 17} |
| PASS | [h/es] category chip filters (stay) | {"c": 16, "m": 16, "pressed": "stay"} |
| PASS | [h/es] village filter | {"c": 10, "m": 10} |
| PASS | [h/es] empty state | {"c": 0, "m": 0, "empty": true} |
| PASS | [h/es] reset restores 117 | {"c": 117, "m": 117} |
| PASS | [h/es] ride 'Show on map' opens a popup | "popup" |
| PASS | [h/es] every image has alt text | {"images": 49, "bad": []} |
| PASS | [h/es] only local photos, each with a Commons, approved community-archive, or linked press credit | {"photos": 48, "no_credit": [], "other_images": []} |
| PASS | [h/es] all 30 press photos appear once with visible linked credits | {"count": 30, "unique": 30, "missing": [], "bad_credit": []} |
| PASS | [h/es] no broken images | "ok" |
| PASS | [h/es] no 'official'/'oficial' claim | "none" |
| PASS | [h/es] no em or en dashes in visible text | [] |
| PASS | [h/es] merchant check note present | "ok" |
| PASS | [h/es] 117 places + 50+ claim + data date | "ok" |
| PASS | [h/es] OSM/ODbL, BTC Map and Commons credits in footer | "ok" |
| PASS | [h/es] floating Design switcher: all finished designs, current marked, fixed, in view | {"letters": ["A", "C", "D", "AC", "AD", "CD", "F", "G", "H"], "cur": ["H"], "hrefs": ["../../a/es/", "../../c/es/", "../../d/es/", "../../ac/es/", "../../ad/es/", "../../cd/es/", "../../f/es/", "../../g/es/", "./", "../. |
| PASS | [h/es] switcher goes to design C in the same language and remembers it | {"url": "http://127.0.0.1:18431/v/c/es/", "stored": "c"} |
| PASS | [h/es] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [h/es] 1440 text over photos/gradients: contrast | "no overlay text found" |
| PASS | [h/es] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [h/es] no text leaves the screen at 390 | [] |
| PASS | [h/es] no console errors at 390 | [] |
| PASS | [h/es] brand does not overlap its CTA or menu button at 390 | {"brandRight": 92, "overlapCta": false, "overlapMenu": false} |
| PASS | [h/es] 117 markers at 390 | "ok" |
| PASS | [h/es] switcher fits at 390 | {"right": 382, "vw": 390, "h": 40} |
| PASS | [h/es] mobile section map has seven links | true |
| PASS | [h/es] navigation link scrolls to the merchants section | 52 |
| PASS | [h] EN/ES parity: same section ids in same order | ["hero", "lake", "bitcoin", "transport", "community", "tours", "expats", "about"] |
| PASS | [h] EN/ES parity: placeholders, nav targets, h2 and image counts | {"placeholders": ["atm-locations", "contact-email", "expat-contact", "facebook", "meetup-dates", "meetup-venues", "school-list", "tomek-bio-photo", "tour-booking", "tour-booking-details", "whatsapp-invite-url"], "h2": 7, |
| PASS | [h] every nav link targets an existing section | ["#lake", "#community", "#bitcoin", "#transport", "#about", "#expats", "#tours", "#bitcoin"] |
| PASS | [h] no section dropped (map, merchants, community, tours, expats, boat/tuk tuk, ATM, history) | [] |
| PASS | [h] browser language es: opening EN redirects to /es/ | "http://127.0.0.1:18431/v/h/es/" |
| PASS | [h] EN switch stays in this design and stores the choice | "http://127.0.0.1:18431/v/h/" |
| PASS | [h] ES switch stays in this design | "http://127.0.0.1:18431/v/h/es/" |
| PASS | [h] browser language en: opening /es/ redirects to EN | "http://127.0.0.1:18431/v/h/" |
| PASS | [h] configurable placeholder link shows 'coming soon' toast | "toast" |
| PASS | [h] placeholder badge visible in preview | "\"Placeholder: atm-locations\"" |
| PASS | [index/en] HTTP 200 http://127.0.0.1:18431/variants/ | 200 |
| PASS | [index/en] noindex,nofollow | "present" |
| PASS | [index/en] every referenced asset and link returns 200 | {"checked": 34, "bad": []} |
| PASS | [index/en] 1440: 10 cards and loaded thumbnails, no console errors or overflow | {"info": {"cards": 10, "thumbs": 10}, "errs": [], "ov": {"sw": 1440, "cw": 1440}} |
| PASS | [index/en] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [index/en] 390: 10 cards and loaded thumbnails, no console errors or overflow | {"info": {"cards": 10, "thumbs": 10}, "errs": [], "ov": {"sw": 390, "cw": 390}} |
| PASS | [index/en] 390 axe-core WCAG A/AA violations | [] |
| PASS | [index/en] card A opens /v/a/ in en | "http://127.0.0.1:18431/v/a/" |
| PASS | [index/en] card C opens /v/c/ in en | "http://127.0.0.1:18431/v/c/" |
| PASS | [index/en] card D opens /v/d/ in en | "http://127.0.0.1:18431/v/d/" |
| PASS | [index/en] card AC opens /v/ac/ in en | "http://127.0.0.1:18431/v/ac/" |
| PASS | [index/en] card AD opens /v/ad/ in en | "http://127.0.0.1:18431/v/ad/" |
| PASS | [index/en] card CD opens /v/cd/ in en | "http://127.0.0.1:18431/v/cd/" |
| PASS | [index/en] card F opens /v/f/ in en | "http://127.0.0.1:18431/v/f/" |
| PASS | [index/en] card G opens /v/g/ in en | "http://127.0.0.1:18431/v/g/" |
| PASS | [index/en] card H opens /v/h/ in en | "http://127.0.0.1:18431/v/h/" |
| PASS | [index/es] HTTP 200 http://127.0.0.1:18431/variants/es/ | 200 |
| PASS | [index/es] noindex,nofollow | "present" |
| PASS | [index/es] every referenced asset and link returns 200 | {"checked": 35, "bad": []} |
| PASS | [index/es] 1440: 10 cards and loaded thumbnails, no console errors or overflow | {"info": {"cards": 10, "thumbs": 10}, "errs": [], "ov": {"sw": 1440, "cw": 1440}} |
| PASS | [index/es] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [index/es] 390: 10 cards and loaded thumbnails, no console errors or overflow | {"info": {"cards": 10, "thumbs": 10}, "errs": [], "ov": {"sw": 390, "cw": 390}} |
| PASS | [index/es] 390 axe-core WCAG A/AA violations | [] |
| PASS | [index/es] card A opens /v/a/ in es | "http://127.0.0.1:18431/v/a/es/" |
| PASS | [index/es] card C opens /v/c/ in es | "http://127.0.0.1:18431/v/c/es/" |
| PASS | [index/es] card D opens /v/d/ in es | "http://127.0.0.1:18431/v/d/es/" |
| PASS | [index/es] card AC opens /v/ac/ in es | "http://127.0.0.1:18431/v/ac/es/" |
| PASS | [index/es] card AD opens /v/ad/ in es | "http://127.0.0.1:18431/v/ad/es/" |
| PASS | [index/es] card CD opens /v/cd/ in es | "http://127.0.0.1:18431/v/cd/es/" |
| PASS | [index/es] card F opens /v/f/ in es | "http://127.0.0.1:18431/v/f/es/" |
| PASS | [index/es] card G opens /v/g/ in es | "http://127.0.0.1:18431/v/g/es/" |
| PASS | [index/es] card H opens /v/h/ in es | "http://127.0.0.1:18431/v/h/es/" |
| PASS | HTTP 200 http://127.0.0.1:18431/v/ | 200 |
| PASS | every data-placeholder is listed in HANDOFF.md | {"placeholders": ["atm-locations", "contact-email", "expat-contact", "facebook", "meetup-dates", "meetup-venues", "school-list", "tomek-bio-photo", "tour-booking", "tour-booking-details", "whatsapp-invite-url"], "missing |