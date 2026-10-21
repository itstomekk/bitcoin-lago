# Variants QA report (live)

Base URL: https://itstomekk.github.io/lago-bitcoin-community/
Variants: d, f, g
PASS 290 / FAIL 0

| Result | Gate | Evidence |
|---|---|---|
| PASS | robots.txt Disallow while private | 200 |
| PASS | [d/en] HTTP 200 https://itstomekk.github.io/lago-bitcoin-community/v/d/ | 200 |
| PASS | [d/en] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin on Lake Atitlán, Guatemala", "desc_len": 158} |
| PASS | [d/en] meta robots noindex,nofollow | "present" |
| PASS | [d/en] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/d/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/d/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/d/"]] |
| PASS | [d/en] html lang + data-design | "en" |
| PASS | [d/en] every referenced asset and link returns 200 | {"checked": 123, "bad": []} |
| PASS | [d/en] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [d/en] page weight under 3 MB excluding map tiles | "2355 KB" |
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
| PASS | [d/en] switcher goes to design C in the same language and remembers it | {"url": "https://itstomekk.github.io/lago-bitcoin-community/v/c/", "stored": "c"} |
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
| PASS | [d/es] HTTP 200 https://itstomekk.github.io/lago-bitcoin-community/v/d/es/ | 200 |
| PASS | [d/es] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin en el Lago de Atitlán, Guatemala", "desc_len": 179} |
| PASS | [d/es] meta robots noindex,nofollow | "present" |
| PASS | [d/es] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/d/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/d/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/d/"]] |
| PASS | [d/es] html lang + data-design | "es" |
| PASS | [d/es] every referenced asset and link returns 200 | {"checked": 131, "bad": []} |
| PASS | [d/es] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [d/es] page weight under 3 MB excluding map tiles | "2356 KB" |
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
| PASS | [d/es] switcher goes to design C in the same language and remembers it | {"url": "https://itstomekk.github.io/lago-bitcoin-community/v/c/es/", "stored": "c"} |
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
| PASS | [d] browser language es: opening EN redirects to /es/ | "https://itstomekk.github.io/lago-bitcoin-community/v/d/es/" |
| PASS | [d] EN switch stays in this design and stores the choice | "https://itstomekk.github.io/lago-bitcoin-community/v/d/" |
| PASS | [d] ES switch stays in this design | "https://itstomekk.github.io/lago-bitcoin-community/v/d/es/" |
| PASS | [d] browser language en: opening /es/ redirects to EN | "https://itstomekk.github.io/lago-bitcoin-community/v/d/" |
| PASS | [d] configurable placeholder link shows 'coming soon' toast | "toast" |
| PASS | [d] placeholder badge visible in preview | "\"Placeholder: whatsapp-invite-url\"" |
| PASS | [f/en] HTTP 200 https://itstomekk.github.io/lago-bitcoin-community/v/f/ | 200 |
| PASS | [f/en] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin on Lake Atitlán, Guatemala", "desc_len": 158} |
| PASS | [f/en] meta robots noindex,nofollow | "present" |
| PASS | [f/en] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/f/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/f/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/f/"]] |
| PASS | [f/en] html lang + data-design | "en" |
| PASS | [f/en] every referenced asset and link returns 200 | {"checked": 119, "bad": []} |
| PASS | [f/en] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [f/en] page weight under 3 MB excluding map tiles | "2290 KB" |
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
| PASS | [f/en] switcher goes to design C in the same language and remembers it | {"url": "https://itstomekk.github.io/lago-bitcoin-community/v/c/", "stored": "c"} |
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
| PASS | [f/es] HTTP 200 https://itstomekk.github.io/lago-bitcoin-community/v/f/es/ | 200 |
| PASS | [f/es] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin en el Lago de Atitlán, Guatemala", "desc_len": 179} |
| PASS | [f/es] meta robots noindex,nofollow | "present" |
| PASS | [f/es] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/f/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/f/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/f/"]] |
| PASS | [f/es] html lang + data-design | "es" |
| PASS | [f/es] every referenced asset and link returns 200 | {"checked": 127, "bad": []} |
| PASS | [f/es] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [f/es] page weight under 3 MB excluding map tiles | "2291 KB" |
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
| PASS | [f/es] switcher goes to design C in the same language and remembers it | {"url": "https://itstomekk.github.io/lago-bitcoin-community/v/c/es/", "stored": "c"} |
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
| PASS | [f] browser language es: opening EN redirects to /es/ | "https://itstomekk.github.io/lago-bitcoin-community/v/f/es/" |
| PASS | [f] EN switch stays in this design and stores the choice | "https://itstomekk.github.io/lago-bitcoin-community/v/f/" |
| PASS | [f] ES switch stays in this design | "https://itstomekk.github.io/lago-bitcoin-community/v/f/es/" |
| PASS | [f] browser language en: opening /es/ redirects to EN | "https://itstomekk.github.io/lago-bitcoin-community/v/f/" |
| PASS | [f] configurable placeholder link shows 'coming soon' toast | "toast" |
| PASS | [f] placeholder badge visible in preview | "\"Placeholder: whatsapp-invite-url\"" |
| PASS | [g/en] HTTP 200 https://itstomekk.github.io/lago-bitcoin-community/v/g/ | 200 |
| PASS | [g/en] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin on Lake Atitlán, Guatemala", "desc_len": 158} |
| PASS | [g/en] meta robots noindex,nofollow | "present" |
| PASS | [g/en] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/g/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/g/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/g/"]] |
| PASS | [g/en] html lang + data-design | "en" |
| PASS | [g/en] every referenced asset and link returns 200 | {"checked": 116, "bad": []} |
| PASS | [g/en] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [g/en] page weight under 3 MB excluding map tiles | "2540 KB" |
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
| PASS | [g/en] switcher goes to design C in the same language and remembers it | {"url": "https://itstomekk.github.io/lago-bitcoin-community/v/c/", "stored": "c"} |
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
| PASS | [g/es] HTTP 200 https://itstomekk.github.io/lago-bitcoin-community/v/g/es/ | 200 |
| PASS | [g/es] title + meta description | {"title": "Lago Bitcoin Community / Bitcoin en el Lago de Atitlán, Guatemala", "desc_len": 179} |
| PASS | [g/es] meta robots noindex,nofollow | "present" |
| PASS | [g/es] hreflang en/es/x-default | [["en", "https://itstomekk.github.io/lago-bitcoin-community/v/g/"], ["es", "https://itstomekk.github.io/lago-bitcoin-community/v/g/es/"], ["x-default", "https://itstomekk.github.io/lago-bitcoin-community/v/g/"]] |
| PASS | [g/es] html lang + data-design | "es" |
| PASS | [g/es] every referenced asset and link returns 200 | {"checked": 124, "bad": []} |
| PASS | [g/es] no console errors/warnings, no failed requests | {"console": [], "failed": []} |
| PASS | [g/es] page weight under 3 MB excluding map tiles | "2541 KB" |
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
| PASS | [g/es] switcher goes to design C in the same language and remembers it | {"url": "https://itstomekk.github.io/lago-bitcoin-community/v/c/es/", "stored": "c"} |
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
| PASS | [g] browser language es: opening EN redirects to /es/ | "https://itstomekk.github.io/lago-bitcoin-community/v/g/es/" |
| PASS | [g] EN switch stays in this design and stores the choice | "https://itstomekk.github.io/lago-bitcoin-community/v/g/" |
| PASS | [g] ES switch stays in this design | "https://itstomekk.github.io/lago-bitcoin-community/v/g/es/" |
| PASS | [g] browser language en: opening /es/ redirects to EN | "https://itstomekk.github.io/lago-bitcoin-community/v/g/" |
| PASS | [g] configurable placeholder link shows 'coming soon' toast | "toast" |
| PASS | [g] placeholder badge visible in preview | "\"Placeholder: whatsapp-invite-url\"" |
| PASS | every data-placeholder is listed in HANDOFF.md | {"placeholders": ["atm-locations", "contact-email", "expat-contact", "facebook", "meetup-dates", "meetup-venues", "school-list", "tomek-bio-photo", "tour-booking", "tour-booking-details", "whatsapp-invite-url"], "missing |