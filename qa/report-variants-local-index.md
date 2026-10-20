# Variants QA report (local-index)

Base URL: http://127.0.0.1:18435/
Variants: a, c, d, ac, ad, cd, f, g
PASS 33 / FAIL 0

| Result | Gate | Evidence |
|---|---|---|
| PASS | robots.txt Disallow while private | 200 |
| PASS | [index/en] HTTP 200 http://127.0.0.1:18435/variants/ | 200 |
| PASS | [index/en] noindex,nofollow | "present" |
| PASS | [index/en] every referenced asset and link returns 200 | {"checked": 31, "bad": []} |
| PASS | [index/en] 1440: 9 cards and loaded thumbnails, no console errors or overflow | {"info": {"cards": 9, "thumbs": 9}, "errs": [], "ov": {"sw": 1440, "cw": 1440}} |
| PASS | [index/en] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [index/en] 390: 9 cards and loaded thumbnails, no console errors or overflow | {"info": {"cards": 9, "thumbs": 9}, "errs": [], "ov": {"sw": 390, "cw": 390}} |
| PASS | [index/en] 390 axe-core WCAG A/AA violations | [] |
| PASS | [index/en] card A opens /v/a/ in en | "http://127.0.0.1:18435/v/a/" |
| PASS | [index/en] card C opens /v/c/ in en | "http://127.0.0.1:18435/v/c/" |
| PASS | [index/en] card D opens /v/d/ in en | "http://127.0.0.1:18435/v/d/" |
| PASS | [index/en] card AC opens /v/ac/ in en | "http://127.0.0.1:18435/v/ac/" |
| PASS | [index/en] card AD opens /v/ad/ in en | "http://127.0.0.1:18435/v/ad/" |
| PASS | [index/en] card CD opens /v/cd/ in en | "http://127.0.0.1:18435/v/cd/" |
| PASS | [index/en] card F opens /v/f/ in en | "http://127.0.0.1:18435/v/f/" |
| PASS | [index/en] card G opens /v/g/ in en | "http://127.0.0.1:18435/v/g/" |
| PASS | [index/es] HTTP 200 http://127.0.0.1:18435/variants/es/ | 200 |
| PASS | [index/es] noindex,nofollow | "present" |
| PASS | [index/es] every referenced asset and link returns 200 | {"checked": 32, "bad": []} |
| PASS | [index/es] 1440: 9 cards and loaded thumbnails, no console errors or overflow | {"info": {"cards": 9, "thumbs": 9}, "errs": [], "ov": {"sw": 1440, "cw": 1440}} |
| PASS | [index/es] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [index/es] 390: 9 cards and loaded thumbnails, no console errors or overflow | {"info": {"cards": 9, "thumbs": 9}, "errs": [], "ov": {"sw": 390, "cw": 390}} |
| PASS | [index/es] 390 axe-core WCAG A/AA violations | [] |
| PASS | [index/es] card A opens /v/a/ in es | "http://127.0.0.1:18435/v/a/es/" |
| PASS | [index/es] card C opens /v/c/ in es | "http://127.0.0.1:18435/v/c/es/" |
| PASS | [index/es] card D opens /v/d/ in es | "http://127.0.0.1:18435/v/d/es/" |
| PASS | [index/es] card AC opens /v/ac/ in es | "http://127.0.0.1:18435/v/ac/es/" |
| PASS | [index/es] card AD opens /v/ad/ in es | "http://127.0.0.1:18435/v/ad/es/" |
| PASS | [index/es] card CD opens /v/cd/ in es | "http://127.0.0.1:18435/v/cd/es/" |
| PASS | [index/es] card F opens /v/f/ in es | "http://127.0.0.1:18435/v/f/es/" |
| PASS | [index/es] card G opens /v/g/ in es | "http://127.0.0.1:18435/v/g/es/" |
| PASS | HTTP 200 http://127.0.0.1:18435/v/ | 200 |
| PASS | every data-placeholder is listed in HANDOFF.md | {"placeholders": [], "missing": []} |