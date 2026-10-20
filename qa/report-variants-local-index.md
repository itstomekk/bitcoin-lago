# Variants QA report (local-index)

Base URL: http://127.0.0.1:18432/
Variants: a
PASS 19 / FAIL 0

| Result | Gate | Evidence |
|---|---|---|
| PASS | robots.txt Disallow while private | 200 |
| PASS | [index/en] HTTP 200 http://127.0.0.1:18432/variants/ | 200 |
| PASS | [index/en] noindex,nofollow | "present" |
| PASS | [index/en] every referenced asset and link returns 200 | {"checked": 25, "bad": []} |
| PASS | [index/en] 1440: 7 cards and loaded thumbnails, no console errors or overflow | {"info": {"cards": 7, "thumbs": 7}, "errs": [], "ov": {"sw": 1440, "cw": 1440}} |
| PASS | [index/en] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [index/en] 390: 7 cards and loaded thumbnails, no console errors or overflow | {"info": {"cards": 7, "thumbs": 7}, "errs": [], "ov": {"sw": 390, "cw": 390}} |
| PASS | [index/en] 390 axe-core WCAG A/AA violations | [] |
| PASS | [index/en] card A opens /v/a/ in en | "http://127.0.0.1:18432/v/a/" |
| PASS | [index/es] HTTP 200 http://127.0.0.1:18432/variants/es/ | 200 |
| PASS | [index/es] noindex,nofollow | "present" |
| PASS | [index/es] every referenced asset and link returns 200 | {"checked": 26, "bad": []} |
| PASS | [index/es] 1440: 7 cards and loaded thumbnails, no console errors or overflow | {"info": {"cards": 7, "thumbs": 7}, "errs": [], "ov": {"sw": 1440, "cw": 1440}} |
| PASS | [index/es] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [index/es] 390: 7 cards and loaded thumbnails, no console errors or overflow | {"info": {"cards": 7, "thumbs": 7}, "errs": [], "ov": {"sw": 390, "cw": 390}} |
| PASS | [index/es] 390 axe-core WCAG A/AA violations | [] |
| PASS | [index/es] card A opens /v/a/ in es | "http://127.0.0.1:18432/v/a/es/" |
| PASS | HTTP 200 http://127.0.0.1:18432/v/ | 200 |
| PASS | every data-placeholder is listed in HANDOFF.md | {"placeholders": [], "missing": []} |