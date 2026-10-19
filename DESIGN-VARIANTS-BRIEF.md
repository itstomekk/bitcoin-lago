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

## UPDATE 4 (Tomek, 2026-10-19 evening). FINAL, overrides UPDATE 3 where they differ. Steps 1 and 2 of UPDATE 3 (top bar, press photos + Press section) are DONE and pushed (commits 898e57c, 950ad1f). F and G drafts exist uncommitted: tools/variants/f.html, g.html, v/f.css, v/g.css (continue from them, or restart if weak).

FINAL DESIGN SET: Baseline, A, C, D, AC, AD, CD, F, G, H  (9 designs + baseline).
- REMOVE B and E completely: build config, top bar, /variants/ index, QA runner lists, thumbnails, v/b*, v/e*, tools/variants/b.html, e.html. Update HANDOFF.md.
- Keep A and D as they are, except the logo and the top bar colours below.
- C: KEEP the dark volcano-night concept, make it MUCH MORE MAYA: stepped-pyramid and step-fret geometry, woven textile bands, original glyph-like marks and section numerals, jade/cinnabar/indigo/gold accents, carved-stone feel in panels and cards, still fully readable (WCAG AA). Original abstract motifs only, no copied real glyphs, no fake Maya text, no sacred-symbol misuse.
- NEW "AC": between A and C. A's Maya 1500/2100 minimal structure and light/space with C's dark cinematic mood. Folder v/ac/.
- NEW "AD": merge of A and D (A's restraint and glyph/geometry with D's woven textile colour blocks and arch frames). Folder v/ad/.
- NEW "CD": merge of C and D (C's night drama with D's textile colour blocks and arch frames). Folder v/cd/.
- F, G, H: the three Hallmark designs from UPDATE 3 (structurally different from each other and from all others, Hallmark pre-emit critique stamp, locked tokens, mobile checks 320/375/414/768, no invented metrics).
- LOGO: Tomek's logo is brand/lago-bitcoin-logo-original.jpg (navy wordmark "Lago Bitcoin", the "g" is a green and red quetzal-bird figure, the B of Bitcoin is the bitcoin symbol, white background). Use it in every design's header and footer (and favicon from the quetzal "g" if clean). Make clean web versions: transparent PNG/WebP, plus a light variant with the navy turned white for dark designs (C, AC, CD and any dark one). Keep proportions, do not redraw it. The logo is the Lago Bitcoin brand mark, so keep the page text saying this is an independent community site, and the word "official" stays banned.
- COLOURS borrowed from the logo where they fit the design: navy approx #0a2850 (sampled #002040 to #001848), quetzal green approx #20a060, red approx #d03040. They are close to the jade, cinnabar and indigo already used in A, C, D; unify those tokens to the logo values where the look allows. Contrast AA must still pass.
- SWITCHER / TOP BAR: make it clearly MORE COLOURFUL: navy bar (logo navy), one coloured chip per design using that design's own accent (logo green for A, etc.), active chip filled and with a bright underline, hover glow, the EN/ES toggle in logo red/green. Labels: Base, A, C, D, AC, AD, CD, F, G, H. Still slim, readable (AA), works at 390 px (scrollable chip row is fine, no wrapping into two lines).

ORDER OF WORK, QA + commit + push + live check after EACH:
 1. Remove B and E, add logo assets, colourful top bar, put the logo into the baseline, A, C, D headers. Update /variants/ index.
 2. C more Maya.
 3. AC, then AD, then CD.
 4. F, G, H with Hallmark.
 5. Variants index with all entries and thumbnails, final live QA of everything, HANDOFF.md final.

## UPDATE 5 (Tomek, 2026-10-19 17:20) QUEUE, do after STEP 1B, not during it
- Two photos supplied by Tomek, saved in source-archive/tomek-supplied/: tuktuk-bitcoin-lake-road.jpg (orange tuk tuk with a big white bitcoin logo on the canopy, lake and volcanoes behind; 940x627; Tomek: "especially the tuk tuk one") and pier-to-pier-bitcoin-boat.jpg (orange and blue "PIER TO PIER" bitcoin boat on the lake; 1058x543). Add both to ALL finished designs and the baseline as real imagery (the tuk tuk is a hero-grade image; use it in the boat/tuk tuk section and in at least one big visual per design), optimised WebP+JPG like the press photos. Credit line: "Photo: community archive (source to confirm)" and list in HANDOFF.md under "photo credits to confirm". Do not invent a photographer.
- Photos from the X account https://x.com/LakeBitcoin: Tomek wants them but LATER, after one leading design is picked. Do NOT start this now. Note for later: X needs a login, so it needs Tomek's logged-in browser session or his export, not a logged-out fetch.

## UPDATE 6 (Tomek, 2026-10-19 17:30) QUEUE with UPDATE 5, after STEP 1B
- Embed the YouTube talk "Bitcoin Lake: Bitcoin Adoption in Guatemala - Eliazar, Rudy - AB23 Day 2 - Blink Stage" (Adopting Bitcoin, 2023), video id 79cIKf_T3N0, in every finished design and the baseline, in the History / community section. Use a privacy-friendly facade: show the YouTube thumbnail (https://i.ytimg.com/vi/79cIKf_T3N0/hqdefault.jpg, download and optimise it locally) with a play button, load https://www.youtube-nocookie.com/embed/79cIKf_T3N0 only on click, title + channel credit "Adopting Bitcoin" + link to the video, keyboard accessible, EN/ES labels. Do not add any other third-party script.
- History text may use the facts in source-archive/INVENTORY.md section "YouTube talk read in full", ALWAYS attributed and dated ("as presented at Adopting Bitcoin 2023"), never as current figures. Our own merchant count stays the OSM figure dated 2026-10-19.
