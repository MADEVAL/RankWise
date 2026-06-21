# Scenario: Article Rewrite

**Use when:** User provides URL or pastes text content. Says "rewrite", "optimize", "improve SEO", "fix". Mode: REWRITE.

**Pipeline:** extract → audit → restructure → rewrite → meta → linking → QA

---

## STEP 0: SOURCE EXTRACTION

### If URL provided
**If you have web access (fetch tool available):** fetch the page content.
**If no web access:** ask user to paste the content. Or request the page be saved as text and shared.

When content is available, extract: title, headings (H1-H4), body paragraphs, image descriptions, existing meta tags, existing internal/external links.
Identify the existing focus keyword (from title/H1, or ask user).
Note: word count, heading count, image count, link count.

### If text provided
1. Parse structure: title, headings, paragraphs, images (if included inline as markdown/HTML)
2. Identify focus keyword
3. Note existing metrics

---

## STEP 1: PRE-REWRITE AUDIT

Score the existing content against the 49-factor checklist (`shared/checklist.md`).

**Quick 8-factor scan first:**
- K1: Focus keyword set?
- K2: Keyword in title?
- K4: Keyword in meta description?
- K7: Keyword in body?
- K10: Density %?
- C1: Word count?
- C13: Heading hierarchy?
- L1: Internal links count?

Document the baseline score. This becomes the "before" in your deliverable.

---

## STEP 2: PRESERVATION RULES

**You MUST preserve:**
- Factual claims and data (do not invent, do not alter numbers unless flagged)
- Proper names (people, brands, products, tools)
- Direct quotes (preserve exactly)
- Core message and topic intent
- User's unique insights or proprietary information

**You MAY change:**
- Structure (heading order, paragraph breaks, flow)
- Wording (rewrite sentences, replace weak verbs, add power words)
- Keyword placement and density
- Meta tags (title, description, OG)
- Heading text (preserve topic, optimize for keywords)
- Image alt texts
- Link placement and anchor text
- Factual notes format: flag with `[VERIFY]` / `[ПРОВЕРИТЬ]` etc.

**You must NEVER:**
- Invent facts, statistics, or customer quotes
- Silently change factual claims
- Remove substantive content without noting it

---

## STEP 3: STRUCTURAL REWRITE

### Heading restructure
1. Ensure single H1 (the article title)
2. Break content into logical H2 sections (5–9 total)
3. Add H3 sub-sections where H2 content exceeds 300 words
4. Ensure H2→H3 hierarchy (no H2→H4 skip)
5. Inject keywords into headings:
   - Primary keyword in H1 and ≥1 H2
   - Secondary keywords in other H2s/H3s

### Paragraph restructure
1. Break paragraphs >150 words (120 for non-English)
2. Break paragraphs >3 sentences
3. Create visual rhythm: short–short–long–short
4. Each paragraph: one core idea

### Word count
- If <600: expand thin sections with examples, data, detail
- If adequate (>600): optimize existing without padding
- If >3000 and rambling: condense redundancies, tighten prose

---

## STEP 4: LINE-BY-LINE REWRITE

### Introduction rewrite
- DELETE throat-clearing opener
- ADD pattern-interrupt hook (statistic, question, bold claim, story snippet)
- ENSURE focus keyword in first 100–150 words
- REMOVE: "In this article...", "Today we will...", "Welcome to..."

### Body rewrite
- Remove AI markers: `shared/burned-words.md` (universal + language-specific)
- Replace passive voice with active (target ≤10%)
- Add transition words (target ≥30% of sentences)
- Vary sentence length: no 3 consecutive same-length
- Vary sentence openers: no 3 consecutive same first word
- Add power words to subheadings and key sentences
- Add concrete examples where generic claims exist
- Add data points where claims lack support: flag with [VERIFY]

### Conclusion rewrite
- DELETE regurgitation of introduction
- WRITE one sharp takeaway
- ADD specific CTA: link to next article, tool, or resource

### Keyword optimization
- Adjust keyword density to 0.8%–1.5%
- If <0.8%: add natural keyword instances in thin sections
- If >3%: replace excess with synonyms, pronouns, or restructure
- Ensure keyword appears in: title, meta, URL slug, first 150 words, ≥1 H2, ≥1 image alt

---

## STEP 5: META LAYER REWRITE

### SEO title
- Write new title meeting all criteria from `scenarios/article-generate.md` Step 1
- 50–60 characters (adjust per language)
- Keyword near beginning
- Number + power words
- Clear sentiment

### Meta description
- Write new description: 145–158 characters
- Keyword in first 20 words
- Specific value proposition (not generic "Learn more about...")
- Active voice

### URL slug (flag, don't change in rewrite)
- If current URL >75 characters: suggest shortened version
- If URL doesn't contain keyword: suggest new slug
- Note: changing live URLs requires 301 redirects — flag as recommendation

### OG tags
- Generate OG title + description if not provided

---

## STEP 6: MEDIA & LINKS REWRITE

### Images
- If existing images: rewrite alt texts to include keyword (at least 1) + be descriptive
- If no images: mark K9 and C3 as N/A. Recommend adding ≥1 per 300 words with specific image suggestions.
- Suggest descriptive file names

### Internal links
- Audit existing internal links
- Add contextual internal links if <3 present
- Vary anchor text if >2 exact-match anchors exist
- **Review `shared/checklist.md` → FACTOR INTERDEPENDENCIES** — ensure new links/anchors don't inadvertently change keyword density or break other factors

### External links
- Audit existing external links
- Add authoritative external links if <2 present
- Ensure at least 1 DoFollow
- **If no web access to verify link quality:** flag with "Verify link quality at: [URL]" for the user to check manually

---

## STEP 7: QA — DELIVER

### Deliver format
```
[MODE: rewrite]
[LANG: xx]
[KEYWORD: xxx]
[BEFORE SCORE: XX/49]
[AFTER SCORE: XX/49]

---
[SEO TITLE]
...
---
[META DESCRIPTION]
...
---
[URL SUGGESTION — if changed]
...
---
[REWRITTEN CONTENT]
...
---
[IMAGE ALT TEXTS]
...
---
[CHANGELOG]
- Structural changes made
- Keyword changes: old density X% → new density Y%
- Added X internal links, Y external links
- Meta tags rewritten (before/after)
- Word count: old → new

[RECOMMENDATIONS — items not changed in content but recommended]
- URL slug suggestion (if applicable)
- Image additions (if needed)
- Schema markup to add
```
