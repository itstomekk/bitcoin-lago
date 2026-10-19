# DESIGN VARIANTS BRIEF (Tomek voice note, 2026-10-19, transcribed from Polish, garbled; intent below)

Tomek wants FIVE distinct design variants of the same site (same content, same data, same EN/ES), previewable on GitHub Pages and switchable between each other.

1. Variant A: "Maya minimal". Minimalist, few colours, very restrained, only a hint of Maya (geometry, textile/glyph rhythm, not clip-art, not exoticising). Natural but elegant.
2. Variants B to E: four other clearly different directions, each innovative, using real imagery (Commons photos) as a design driver. Suggested spread: B editorial/magazine, C dark and cinematic volcano, D warm textile/cooperative craft, E bright modern fintech-meets-lake. Builder may swap directions if the design skills suggest better ones, but all five must look unmistakably different, not recoloured copies.
3. Switch mechanism: `/v/a/`, `/v/b/` ... `/v/e/` (each with EN and `/es/`), plus a small floating "Design A B C D E" switcher on every page, remembers last choice, and an index at `/variants/` with a thumbnail of each. Root `/` = the variant Tomek picks later (default A until then).
4. All variants share one content source (`tools/content.py`) and one data set; differences live in CSS/layout/templates only. noindex,nofollow on all.
5. Use the webdev profile design skills: design-taste-frontend, high-end-visual-design, minimalist-ui, industrial-brutalist-ui, stitch-design-taste, gpt-taste, imagegen-frontend-web, hallmark as fits each variant. Always informative: no variant may drop sections (map, merchant list, community, tours, expats, boat, ATM, history, placeholders).
6. Before building variants: give Tomek a short status of what is already built (current single design = treat it as a candidate variant, not a throwaway).
7. Verify every variant: 200, no console errors, no overflow at 1440 and 390, map shows all markers, list count == marker count, ES parity, switcher works. Screenshots per variant in qa/screenshots/<variant>/.

## UPDATE from Tomek's voice note 2 (2026-10-19), overrides softer wording above
- "Awesome, give me the website": ship working variants fast, deploy them, give the address.
- More modern, FULL-SCREEN: immersive full-viewport sections, big imagery, minimal chrome.
- The page should feel like year 2100 and year 1500 at the same time: ancient AND ultra-modern. Think codex/stone/textile heritage fused with a futuristic interface (precise grids, luminous lines, motion, depth), not a theme-park Maya.
- Maya hint comes through THREE channels: geometry, textile (woven rhythm, step-fret patterns), and COLOUR (earth, jade, cinnabar, indigo, cacao), PLUS glyph-like decorative elements (original abstract glyph-inspired marks, section numerals, dividers). Do NOT copy real Maya glyphs as claims of meaning, do not write fake Maya text, no sacred-symbol misuse. Original, abstract, respectful.
- Readability first: all body copy and merchant data stay fully legible (WCAG AA), glyphs are decoration or numbering only.
- Variant A = this Maya 1500/2100 minimal direction (Tomek's first choice). B to E: four other directions, each also full-screen and modern.
- Deliver at the same GitHub Pages site: /v/a/ ... /v/e/ (+ /es/), floating switcher, /variants/ index. Root stays the current baseline until Tomek picks.
- Report the live URLs, verified from the live site, with screenshots.

## UPDATE 2 from Tomek (voice note 3, 2026-10-19). These CHANGE earlier rules. Read before continuing.
1. NO URLs list needed. Add a FIXED TOP BAR on every page of every variant AND on the root baseline, with the variant switcher (Baseline, A, B, C, D, E) and the EN/ES toggle. It is a testing bar: slim, always visible, must not cover content (push the page down or use a sticky offset) and must work on 390px. Keep it visually separate from each variant's own design (neutral dark strip, small type).
2. Press articles and photos are NOT private any more. Tomek instructed: use all scraped photos as normal site imagery. The curated set is ready: `images/press/` (30 raw files, 28 MB, too heavy) with credits in `data/press-photos.json` (publisher, article title, article URL, rights note). Reference-only logos/avatars/ads/charts/stock are NOT included and stay out.
   - Resize/convert them with tools/optimize_images.py to WebP + JPG (800 and 1600 px), keep originals out of the deployed pages.
   - Every press photo used on a page must show a visible credit line "Photo: <publisher>, via <article title>" linking to the article URL. alt text required. Keep the rights note in HANDOFF.md.
   - Use them as real imagery in the variants (people, merchants, tuk tuk, mining, school shirts), not only in the press section. Faces: use group/event shots as supplied, do not crop to single identifiable faces for marketing.
   - Update .gitignore so images/press (optimised versions) and data/press-photos.json are committed. source-archive/ stays ignored (raw research). Update HANDOFF.md "private material" section accordingly.
3. Add a Press section (all variants) with headline, publisher, date if known, and a short quote of at most one sentence per article, each linking to the original. Articles to cover: see data/press-photos.json plus source-archive/articles/*.txt (read-only reference).
4. USE THE HALLMARK SKILL (webdev profile skills/hallmark/SKILL.md and its references) for at least two of the variants, with its pre-emit critique stamp, locked tokens, structural variety, no fabricated metrics, mobile checks at 320/375/414/768. Say in HANDOFF.md which variants used Hallmark.
5. Do not invent facts from the press articles. Quotes must be verbatim from source-archive/articles/*.txt.

## UPDATE 3 (Tomek, 2026-10-19, FINAL PLAN, overrides UPDATE 2 step list where they differ)
- Total designs: A to E (existing, live) PLUS three NEW designs F, G, H, each built with the HALLMARK skill (profile skills/hallmark/SKILL.md + references: catalog theme, structural variety, locked tokens, pre-emit critique stamp, mobile checks at 320/375/414/768, no invented metrics). F, G, H must be structurally different from each other and from A to E (different section rhythm, not recolours). Keep the Maya hint option available for one of them only if it fits; do not repeat A.
- Do NOT retrofit Hallmark onto A to E.
- Press photos: add them (all 30 in images/press with credits in data/press-photos.json), used as real imagery in ALL designs (baseline, A to H) plus a Press section with one short verbatim quote per article from source-archive/articles/*.txt, each credit line visible and linked.
- Fixed top bar on every page (baseline and A to H, EN and ES): Baseline / A / B / C / D / E / F / G / H + EN/ES toggle.
- No framework needed (no Astro): the site is plain HTML/CSS/JS generated by the Python build in tools/. Keep it that way.
- ORDER OF WORK, commit and push after EACH step, run the QA runner for the pages touched:
  1. Top bar on baseline + A to E.
  2. Press photos optimised + used + Press section on baseline + A to E.
  3. Design F (Hallmark), then G, then H, each: build, QA, commit, push, check live.
  4. /variants/ index and top bar list updated to all 9 entries, thumbnails.
  5. Final live QA of everything, HANDOFF.md updated.
