# Variants QA report (local)

Base URL: http://127.0.0.1:18500/
Variants: ac, ad, cd
PASS 290 / FAIL 0

| Result | Gate | Evidence |
|---|---|---|
| PASS | robots.txt Disallow while private | 200 |
| PASS | [ac/en] HTTP 200 http://127.0.0.1:18500/v/ac/ | 200 |
| PASS | [ac/en] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin on Lake Atitlán, Guatemala", "desc_len": 158} |
| PASS | [ac/en] meta robots noindex,nofollow | "present" |
| PASS | [ac/en] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/ac/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/ac/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/ac/"]] |
| PASS | [ac/en] html lang + data-design | "en" |
| PASS | [ac/en] every referenced asset and link returns 200 | {"checked": 123, "bad": []} |
| PASS | [ac/en] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [ac/en] page weight under 3 MB excluding map tiles | "2584 KB" |
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
| PASS | [ac/en] switcher goes to design C in the same language and remembers it | {"url": "http://127.0.0.1:18500/v/c/", "stored": "c"} |
| PASS | [ac/en] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [ac/en] 1440 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 29, "lowest_ratio": 5.35, "failures": []} |
| PASS | [ac/en] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [ac/en] no text leaves the screen at 390 | [] |
| PASS | [ac/en] no console errors at 390 | [] |
| PASS | [ac/en] brand does not overlap its CTA or menu button at 390 | {"brandRight": 197, "overlapCta": false, "overlapMenu": false} |
| PASS | [ac/en] 117 markers at 390 | "ok" |
| PASS | [ac/en] switcher fits at 390 | {"right": 382, "vw": 390, "h": 40} |
| PASS | [ac/en] mobile menu opens | true |
| PASS | [ac/en] navigation link scrolls to the merchants section | -0.0 |
| PASS | [ac/en] 390 axe-core WCAG A/AA violations | [] |
| PASS | [ac/en] 390 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 29, "lowest_ratio": 5.35, "failures": []} |
| PASS | [ac/es] HTTP 200 http://127.0.0.1:18500/v/ac/es/ | 200 |
| PASS | [ac/es] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin en el Lago de Atitlán, Guatemala", "desc_len": 179} |
| PASS | [ac/es] meta robots noindex,nofollow | "present" |
| PASS | [ac/es] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/ac/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/ac/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/ac/"]] |
| PASS | [ac/es] html lang + data-design | "es" |
| PASS | [ac/es] every referenced asset and link returns 200 | {"checked": 131, "bad": []} |
| PASS | [ac/es] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [ac/es] page weight under 3 MB excluding map tiles | "2586 KB" |
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
| PASS | [ac/es] switcher goes to design C in the same language and remembers it | {"url": "http://127.0.0.1:18500/v/c/es/", "stored": "c"} |
| PASS | [ac/es] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [ac/es] 1440 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 29, "lowest_ratio": 5.35, "failures": []} |
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
| PASS | [ac] browser language es: opening EN redirects to /es/ | "http://127.0.0.1:18500/v/ac/es/" |
| PASS | [ac] EN switch stays in this design and stores the choice | "http://127.0.0.1:18500/v/ac/" |
| PASS | [ac] ES switch stays in this design | "http://127.0.0.1:18500/v/ac/es/" |
| PASS | [ac] browser language en: opening /es/ redirects to EN | "http://127.0.0.1:18500/v/ac/" |
| PASS | [ac] placeholder button shows 'coming soon' toast | "toast" |
| PASS | [ac] placeholder badge visible in preview | "\"Placeholder: whatsapp-invite-url\"" |
| PASS | [ad/en] HTTP 200 http://127.0.0.1:18500/v/ad/ | 200 |
| PASS | [ad/en] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin on Lake Atitlán, Guatemala", "desc_len": 158} |
| PASS | [ad/en] meta robots noindex,nofollow | "present" |
| PASS | [ad/en] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/ad/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/ad/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/ad/"]] |
| PASS | [ad/en] html lang + data-design | "en" |
| PASS | [ad/en] every referenced asset and link returns 200 | {"checked": 123, "bad": []} |
| PASS | [ad/en] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [ad/en] page weight under 3 MB excluding map tiles | "2359 KB" |
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
| PASS | [ad/en] switcher goes to design C in the same language and remembers it | {"url": "http://127.0.0.1:18500/v/c/", "stored": "c"} |
| PASS | [ad/en] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [ad/en] 1440 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 8, "lowest_ratio": 9.98, "failures": []} |
| PASS | [ad/en] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [ad/en] no text leaves the screen at 390 | [] |
| PASS | [ad/en] no console errors at 390 | [] |
| PASS | [ad/en] brand does not overlap its CTA or menu button at 390 | {"brandRight": 221, "overlapCta": false, "overlapMenu": false} |
| PASS | [ad/en] 117 markers at 390 | "ok" |
| PASS | [ad/en] switcher fits at 390 | {"right": 382, "vw": 390, "h": 40} |
| PASS | [ad/en] mobile menu opens | true |
| PASS | [ad/en] navigation link scrolls to the merchants section | 84 |
| PASS | [ad/en] 390 axe-core WCAG A/AA violations | [] |
| PASS | [ad/en] 390 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 8, "lowest_ratio": 9.98, "failures": []} |
| PASS | [ad/es] HTTP 200 http://127.0.0.1:18500/v/ad/es/ | 200 |
| PASS | [ad/es] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin en el Lago de Atitlán, Guatemala", "desc_len": 179} |
| PASS | [ad/es] meta robots noindex,nofollow | "present" |
| PASS | [ad/es] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/ad/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/ad/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/ad/"]] |
| PASS | [ad/es] html lang + data-design | "es" |
| PASS | [ad/es] every referenced asset and link returns 200 | {"checked": 131, "bad": []} |
| PASS | [ad/es] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [ad/es] page weight under 3 MB excluding map tiles | "2361 KB" |
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
| PASS | [ad/es] switcher goes to design C in the same language and remembers it | {"url": "http://127.0.0.1:18500/v/c/es/", "stored": "c"} |
| PASS | [ad/es] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [ad/es] 1440 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 8, "lowest_ratio": 9.98, "failures": []} |
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
| PASS | [ad] browser language es: opening EN redirects to /es/ | "http://127.0.0.1:18500/v/ad/es/" |
| PASS | [ad] EN switch stays in this design and stores the choice | "http://127.0.0.1:18500/v/ad/" |
| PASS | [ad] ES switch stays in this design | "http://127.0.0.1:18500/v/ad/es/" |
| PASS | [ad] browser language en: opening /es/ redirects to EN | "http://127.0.0.1:18500/v/ad/" |
| PASS | [ad] placeholder button shows 'coming soon' toast | "toast" |
| PASS | [ad] placeholder badge visible in preview | "\"Placeholder: whatsapp-invite-url\"" |
| PASS | [cd/en] HTTP 200 http://127.0.0.1:18500/v/cd/ | 200 |
| PASS | [cd/en] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin on Lake Atitlán, Guatemala", "desc_len": 158} |
| PASS | [cd/en] meta robots noindex,nofollow | "present" |
| PASS | [cd/en] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/cd/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/cd/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/cd/"]] |
| PASS | [cd/en] html lang + data-design | "en" |
| PASS | [cd/en] every referenced asset and link returns 200 | {"checked": 123, "bad": []} |
| PASS | [cd/en] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [cd/en] page weight under 3 MB excluding map tiles | "2584 KB" |
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
| PASS | [cd/en] switcher goes to design C in the same language and remembers it | {"url": "http://127.0.0.1:18500/v/c/", "stored": "c"} |
| PASS | [cd/en] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [cd/en] 1440 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 32, "lowest_ratio": 5.03, "failures": []} |
| PASS | [cd/en] no horizontal overflow at 390 | {"sw": 390, "cw": 390} |
| PASS | [cd/en] no text leaves the screen at 390 | [] |
| PASS | [cd/en] no console errors at 390 | [] |
| PASS | [cd/en] brand does not overlap its CTA or menu button at 390 | {"brandRight": 197, "overlapCta": false, "overlapMenu": false} |
| PASS | [cd/en] 117 markers at 390 | "ok" |
| PASS | [cd/en] switcher fits at 390 | {"right": 382, "vw": 390, "h": 40} |
| PASS | [cd/en] mobile menu opens | true |
| PASS | [cd/en] navigation link scrolls to the merchants section | -0.0 |
| PASS | [cd/en] 390 axe-core WCAG A/AA violations | [] |
| PASS | [cd/en] 390 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 32, "lowest_ratio": 5.03, "failures": []} |
| PASS | [cd/es] HTTP 200 http://127.0.0.1:18500/v/cd/es/ | 200 |
| PASS | [cd/es] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin en el Lago de Atitlán, Guatemala", "desc_len": 179} |
| PASS | [cd/es] meta robots noindex,nofollow | "present" |
| PASS | [cd/es] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/cd/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/cd/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/cd/"]] |
| PASS | [cd/es] html lang + data-design | "es" |
| PASS | [cd/es] every referenced asset and link returns 200 | {"checked": 131, "bad": []} |
| PASS | [cd/es] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [cd/es] page weight under 3 MB excluding map tiles | "2585 KB" |
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
| PASS | [cd/es] switcher goes to design C in the same language and remembers it | {"url": "http://127.0.0.1:18500/v/c/es/", "stored": "c"} |
| PASS | [cd/es] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [cd/es] 1440 text over photos/gradients: contrast >= AA (pixel check) | {"checked": 32, "lowest_ratio": 5.03, "failures": []} |
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
| PASS | [cd] browser language es: opening EN redirects to /es/ | "http://127.0.0.1:18500/v/cd/es/" |
| PASS | [cd] EN switch stays in this design and stores the choice | "http://127.0.0.1:18500/v/cd/" |
| PASS | [cd] ES switch stays in this design | "http://127.0.0.1:18500/v/cd/es/" |
| PASS | [cd] browser language en: opening /es/ redirects to EN | "http://127.0.0.1:18500/v/cd/" |
| PASS | [cd] placeholder button shows 'coming soon' toast | "toast" |
| PASS | [cd] placeholder badge visible in preview | "\"Placeholder: whatsapp-invite-url\"" |
| PASS | every data-placeholder is listed in HANDOFF.md | {"placeholders": ["atm-locations", "contact-email", "expat-contact", "facebook", "meetup-dates", "meetup-venues", "school-list", "tomek-bio-photo", "tour-booking", "tour-booking-details", "whatsapp-invite-url"], "missing |