# Variants QA report (local-index)

Base URL: http://127.0.0.1:18431/
Variants: a
PASS 19 / FAIL 0

| Result | Gate | Evidence |
|---|---|---|
| PASS | robots.txt Disallow while private | 200 |
| PASS | [index/en] HTTP 200 http://127.0.0.1:18431/variants/ | 200 |
| PASS | [index/en] noindex,nofollow | "present" |
| PASS | [index/en] every referenced asset and link returns 200 | {"checked": 22, "bad": []} |
| PASS | [index/en] 1440: six cards, six loaded thumbnails, no console errors, no overflow | {"info": {"cards": 6, "thumbs": 6}, "errs": [], "ov": {"sw": 1440, "cw": 1440}} |
| PASS | [index/en] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [index/en] 390: six cards, six loaded thumbnails, no console errors, no overflow | {"info": {"cards": 6, "thumbs": 6}, "errs": [], "ov": {"sw": 390, "cw": 390}} |
| PASS | [index/en] 390 axe-core WCAG A/AA violations | [] |
| PASS | [index/en] card A opens /v/a/ in en | "http://127.0.0.1:18431/v/a/" |
| PASS | [index/es] HTTP 200 http://127.0.0.1:18431/variants/es/ | 200 |
| PASS | [index/es] noindex,nofollow | "present" |
| PASS | [index/es] every referenced asset and link returns 200 | {"checked": 23, "bad": []} |
| PASS | [index/es] 1440: six cards, six loaded thumbnails, no console errors, no overflow | {"info": {"cards": 6, "thumbs": 6}, "errs": [], "ov": {"sw": 1440, "cw": 1440}} |
| PASS | [index/es] 1440 axe-core WCAG A/AA violations | [] |
| PASS | [index/es] 390: six cards, six loaded thumbnails, no console errors, no overflow | {"info": {"cards": 6, "thumbs": 6}, "errs": [], "ov": {"sw": 390, "cw": 390}} |
| PASS | [index/es] 390 axe-core WCAG A/AA violations | [] |
| PASS | [index/es] card A opens /v/a/ in es | "http://127.0.0.1:18431/v/a/es/" |
| PASS | HTTP 200 http://127.0.0.1:18431/v/ | 200 |
| PASS | every data-placeholder is listed in HANDOFF.md | {"placeholders": [], "missing": []} |