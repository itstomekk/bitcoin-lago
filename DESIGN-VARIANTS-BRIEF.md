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
