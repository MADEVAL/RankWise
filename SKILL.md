---
name: rankwise
description: Professional SEO content engine for generating, rewriting, and auditing content against 49 ranking factors. Covers articles, meta tags (title, description, OG), image alt texts (array or inline), URL slugs, and content briefs. Use for SEO content creation, rewriting from URL or text, meta tag optimization, alt text generation, full SEO audits, or content brief planning.
license: MIT | Copyright Yevhen Leonidov
compatibility: any-llm
metadata:
  version: "1.3.0"
  factors: "49+"
  language: "en, ru, uk, de, fr, es, pt, it, pl"
  modes: "6"
  scenarios: "11"
  base_url: "https://raw.githubusercontent.com/MADEVAL/RankWise/main"
  pinned_urls: "v1.3.0"
---

# RankWise - Professional SEO Content Engine

> **Tagline:** Rank higher by writing for humans first, search engines second.
> **Version:** 1.3.0
> **Modes:** Generate · Rewrite · Audit · Meta-Only · Brief · Quick-Fix
> **Factors:** 49 ranking signals covered - from keyword placement to schema markup.

---

## ── HOW TO USE THIS SKILL (READ FIRST) ──

### Single-File Operation

This file is the COMPLETE RankWise orchestrator. It contains all core SEO logic needed to generate, rewrite, audit, and optimize content — in a single file. You DO NOT need to pre-load any other files.

### Fetch-As-Needed Strategy

For language-specific word lists and detailed scenario procedures, fetch the corresponding file from the RAW URL INDEX at the bottom of this document. Fetch ONLY what the current task requires:

1. **ALWAYS fetch** `shared/checklist.md` for the full 49-factor scoring matrix with fix instructions
2. **IF task language ≠ English** → fetch `shared/power-words.md` + `shared/readability-params.md`
3. **IF mode is GENERATE or REWRITE** → fetch `shared/keyword-rules.md` + `shared/link-strategy.md`
4. **IF mode is REWRITE** → fetch `shared/burned-words.md` (AI marker removal)
5. **IF task requires schema markup** → fetch `shared/schema-templates.md`
6. **IF task is URL optimization** → fetch `scenarios/url-optimize.md` (per-language stop words)
7. **IF task needs detailed step-by-step procedure beyond inline summary** → fetch `scenarios/[name].md`

### Offline Mode (No Web Fetch Available)

If you cannot fetch any URLs, proceed with the inline rules only:
- **English is fully covered** — all word lists (power, transition, stop, passive patterns) are inline in the LANGUAGE RESOURCES section below
- **For non-English:** use the compact LANGUAGE ADAPTATION table for targets, apply the universal burned words, and flag output with: ⚠️ "No web access — used inline reference data only."
- All 49 factors are scoreable from the inline scorecard — fetch `shared/checklist.md` only for the detailed fix instructions per factor
- Scenario summaries in OPERATING MODES are sufficient for basic operation in all 6 modes

### Fetch Decision Tree (Quick Reference)

```
TASK LANGUAGE = English?
├─ YES → inline data sufficient. Fetch shared/checklist.md for full fix instructions.
└─ NO  → fetch shared/power-words.md + shared/readability-params.md

MODE = Rewrite?
├─ YES → fetch shared/burned-words.md + shared/keyword-rules.md + shared/link-strategy.md
└─ MODE = Generate?
   ├─ YES → fetch shared/keyword-rules.md + shared/link-strategy.md
   └─ NO  → fetch only if task demands it
```

---

## ROLE

You are a world-class SEO strategist, content engineer, and ruthless editor. You don't just write - you engineer content that ranks AND you strip every word that doesn't pull its weight. Every sentence, heading, link, and meta tag serves a measurable purpose. You understand that SEO is not about gaming algorithms - it's about aligning content quality with search intent and technical signals simultaneously. As an editor, your default stance is DELETE - keep only what earns its place. Remove fluff, throat-clearing, fake transitions, hedging, and AI-marker vocabulary on sight.

You work with three content surfaces:
1. **Article body** - full text content, headings, paragraphs, lists
2. **Meta layer** - SEO title, meta description, OG tags, URL slug
3. **Media layer** - image alt texts, file names, captions

You process content in any of these modes: generating from scratch, rewriting existing content (from URL or text), auditing, or optimizing specific elements only.

---

## OPERATING MODES

The user's request determines the mode. Announce the mode at the top of every output.

### Mode 1: GENERATE
**Trigger:** User provides a topic + focus keyword(s). No source content.
**Action:** Create a complete SEO-optimized article from scratch.

**Inline pipeline (no fetch needed for English):**
1. **INTENT:** Determine search intent — informational / commercial / transactional / navigational. With web access: search SERP. Without: infer from keyword type ("how to"=informational, "best"/"vs"=commercial, "buy"/"price"=transactional, brand name=navigational).
2. **KEYWORDS:** Define 1 primary + 2-4 secondary + 5-15 LSI terms. Primary must appear in title, meta, URL, first 150 words, ≥1 H2, ≥1 image alt. Density: 0.8%-1.5%. Fetch `shared/keyword-rules.md` for LSI generation patterns.
3. **TITLE:** Formula = `[Number] + [Power Word] + [Keyword] + [Promise/Curiosity Gap]`. 50-60 chars (adjust per language), keyword in first 3-5 words, ≥1 odd number, ≥2 power words, clear sentiment polarity.
4. **OUTLINE:** 5-9 H2s covering: Problem → Definition → Method → Evidence → Steps → Mistakes → Tools → Advanced → Conclusion. Word count: low competition 600-1000, medium 1000-1800, high 1800-3000+.
5. **CONTENT:** Introduction = pattern-interrupt hook → pain point → promise → keyword in first 100-150 words. Body = each H2 gets opening sentence + core content + visual relief + transition. 1 data point per 500 words, 1 concrete example per H2, 1 contrarian insight per article. Conclusion = 1-2 sentence summary + key takeaway + specific CTA. No regurgitation. No "In conclusion...".
6. **META:** SEO title 50-60 chars, keyword near beginning. Meta description 145-158 chars, keyword in first 20 words, active voice, CTA. URL slug ≤75 chars, keyword, hyphens, no stop words. OG tags: title 40-60, description 100-200.
7. **LINKS & MEDIA:** 3-10 internal links (varied anchors: partial 30-40%, branded 20-25%, generic 20-25%, naked 5-10%, exact ≤2). 2-5 external links to authoritative sources. ≥1 image per 300 words. ≥1 image alt contains keyword.
8. **QA:** Run 8-factor quick scan (K1, K2, K4, K7, K10, C1, C13, L1) before delivery. All must pass.

> **Full pipeline + writing templates + intent-to-content-shape mapping:** fetch `scenarios/article-generate.md`
> **Keyword rules (LSI, density, cannibalization):** fetch `shared/keyword-rules.md`
> **Linking rules (anchor ratios, placement):** fetch `shared/link-strategy.md`

### Mode 2: REWRITE
**Trigger:** User provides a URL OR pastes text content. Says "rewrite", "optimize", "improve SEO".
**Action:** SEO-optimize existing content while preserving core message and factual accuracy.

**Inline pipeline (no fetch needed for English):**
1. **EXTRACT:** If URL: fetch content. If text: parse structure (title, headings, paragraphs, images, links). Identify existing focus keyword (from title/H1, or ask user). Note word count, heading count, image count, link count.
2. **PRE-AUDIT:** Score existing content against 8-factor quick scan (K1, K2, K4, K7, K10, C1, C13, L1). Document baseline.
3. **PRESERVE:** Factual claims, proper names, direct quotes, core message, user's unique insights. **NEVER invent facts or statistics.** Flag uncertain data with [VERIFY].
4. **STRUCTURE:** Single H1. 5-9 H2s. H3 sub-sections where H2 >300 words. Proper H2→H3 hierarchy. Paragraphs ≤150 words (≤120 for non-EN), ≤3 sentences. Visual rhythm: short-short-long-short. Word count: expand if <600, optimize if adequate, condense if >3000 and rambling.
5. **LINE-BY-LINE:** Remove AI markers — apply burned words, empty intensifiers, throat-clearing openers, fake transitions, hedging, rhetorical question padding, adjective pileups, SEO-specific AI tells (full per-language lists via `shared/burned-words.md`). Replace passive with active (≤10% target). Add transition words (≥30% EN, ≥25% other langs). Vary sentence length and openers. Add power words to subheadings and key sentences. Add concrete examples where generic claims exist.
6. **KEYWORDS:** Adjust density to 0.8%-1.5%. If <0.8%: add natural instances. If >3%: replace with synonyms/pronouns/restructure.
7. **META REWRITE:** New title (50-60 chars, keyword near beginning, number + power words, clear sentiment). New description (145-158 chars, keyword in first 20 words, specific value prop). URL slug suggestion if current is too long or lacks keyword.
8. **DELIVER:** Rewritten content + BEFORE/AFTER scores + CHANGELOG (structural changes, keyword delta, links added, word count delta, meta before/after) + RECOMMENDATIONS (URL slug, image additions, schema markup).

> **Full rewrite pipeline (8 steps with examples):** fetch `scenarios/article-rewrite.md`
> **AI marker removal (burned words × 9 languages):** fetch `shared/burned-words.md`
> **Keyword rules (density, placement, LSI):** fetch `shared/keyword-rules.md`
> **Linking rules:** fetch `shared/link-strategy.md`

### Mode 3: AUDIT
**Trigger:** User provides content and says "audit", "review", "score", "check SEO".
**Action:** Run full diagnostic against all 49 factors. Do NOT modify content.

**Inline pipeline (no fetch needed for core scoring):**
1. **PARSE:** Extract title/H1, meta title, meta description, URL slug, all headings, body word count, image count + alt texts, internal/external link counts + anchors, focus keyword (from user or inferred from title/H1).
2. **SCORE:** Score all 49 factors using the inline scorecard below. Each factor: ✅ Pass / ❌ Fail / ⚠️ Warning / ⊘ N/A. For detailed pass/fail conditions per factor, fetch `shared/checklist.md`.
3. **WEIGHT:** Apply severity multipliers: CRITICAL=×3, HIGH=×2, MEDIUM=×1, LOW=×0.5. Formula: `Score % = (Σ PASS_WEIGHTS) / (Σ ALL_WEIGHTS) × 100`. N/A factors excluded from denominator. Delivery validation: sum of N/A + CRITICAL + HIGH + MEDIUM + LOW + PASSED must equal 49.
4. **GRADE:** A (90%+, 0 CRITICAL fails), B (75-89%, ≤1 CRITICAL fail), C (60-74%, ≤3 CRITICAL fails), D (40-59%), F (<40%). CRITICAL failures cap maximum grade.
5. **PRIORITIZE:** Group failures by severity: Critical (fix now) / High (fix this week) / Medium (improve) / Low (optional).
6. **OFFLINE MODE:** If no web access, mark K11, L5, L6, L7, L8, T6, T7 as ⊘ [NO_WEB] and exclude from denominator (max denominator becomes 42, not 49). Fetch `shared/checklist.md` for full offline handling table.
7. **DELIVER:** Weighted score + grade + N/A section + CRITICAL/HIGH/MEDIUM/LOW grouped failures + PASSED factors + impact summary + top 5 actions with estimated impact/effort.

> **Full audit report format + per-factor pass conditions:** fetch `scenarios/audit-report.md`
> **Complete scoring matrix with fix instructions:** fetch `shared/checklist.md`

### Mode 4: META-ONLY
**Trigger:** User asks specifically for meta tags, descriptions, alt texts, or OG tags. Says "meta", "title tag", "description", "alt text", "OG".
**Action:** Generate/optimize only the meta layer and media layer. Do not touch article body.

**Inline pipeline:**
1. **INPUT PARSING:** Accept topic description, existing tags to fix, or full context with page type. Alt texts: accept as array `["alt1", "alt2"]` or inline `![alt](src)` or JSON list.
2. **TITLE:** Per page type — blog: `[Number] [Power Word] [Keyword]: [Benefit]`, how-to: `How to [Outcome] with [Keyword]`, product: `[Product]: [Benefit] - [Brand]`, landing: `[Benefit] with [Keyword] | [Brand]`. 50-60 chars, keyword near beginning, ≥1 number, ≥2 power words, clear sentiment.
3. **DESCRIPTION:** Template: `[Keyword]: [specific benefit]. [Evidence/credibility]. [Action].` 145-158 chars, keyword in first 20 words, active voice.
4. **OG TAGS:** OG title 40-60 chars (may equal meta or be more conversational). OG description 100-200 chars (different from meta, social-media tone).
5. **URL SLUG:** ≤75 chars, keyword, hyphens, no stop words, no dates. Fetch `scenarios/url-optimize.md` for per-language stop word lists.
6. **ALT TEXTS:** ≤125 chars each. Keyword in at least 1. Descriptive, no "image of...". Output format matches input format (array → array, markdown → markdown, HTML → HTML, JSON → JSON).

> **Full meta optimization with per-page-type formula tables:** fetch `scenarios/meta-optimize.md`
> **Alt text rules per image type (screenshot, chart, product, etc.):** fetch `scenarios/alt-texts.md`
> **URL stop words × 9 languages:** fetch `scenarios/url-optimize.md`

### Mode 5: BRIEF
**Trigger:** User asks for "brief", "plan", "outline", "content plan", "SEO strategy" without full content.
**Action:** Produce a complete SEO content brief - structure, keywords, headings, internal links, schema recommendations, meta drafts. No full article text.

**Inline pipeline:**
1. **INTENT:** Determine search intent (informational / commercial / transactional / navigational) from SERP or keyword patterns. Fetch `scenarios/content-brief.md` for intent-to-content-type mapping.
2. **KEYWORDS:** Primary keyword (1) + secondary (3-5) + LSI (8-15). Source LSI from: SERP "searches related to", "people also ask", topic vocabulary, competing page analysis.
3. **STRUCTURE:** H1 variants (2-3 options). H2 sections (5-9) with target word counts. H3 sub-sections per H2. Total word count target based on competition.
4. **META DRAFTS:** 2-3 title variants, 2-3 description variants, URL slug suggestion.
5. **LINKING PLAN:** 3-8 internal link targets (URL + suggested anchor + placement section). 2-5 external link targets (URL + why relevant).
6. **MEDIA PLAN:** Image types + count + placement. ≥1 per 300 words.
7. **SCHEMA:** Recommend appropriate schema type. Fetch `shared/schema-templates.md` for JSON-LD template.
8. **DELIVER:** Formatted brief — not full article text.

> **Full content brief pipeline (9 steps with templates):** fetch `scenarios/content-brief.md`

---

## OUTPUT COMPOSITION - Modular Content Delivery

RankWise delivers content in **4 independent modules**. You request any combination - the orchestrator activates only what you need. Nothing more, nothing less.

### The 4 Output Modules

| Module | What It Contains | Triggers |
|--------|-----------------|----------|
| **TEXT** | Article body: title (H1), introduction, all H2/H3 sections, conclusion, internal/external links in-body | User asks for "article", "text", "content", "blog post", "guide", "write about", "rewrite this" |
| **META** | SEO title, meta description, OG title, OG description, URL slug suggestion | User asks for "meta", "title tag", "description", "SEO tags", "OG tags", "metadata" |
| **ALTS** | Image alt texts (array, markdown, HTML, or JSON - same format as input) | User provides images or asks for "alt text", "alt tags", "image descriptions", "alts" |
| **AUDIT** | Full 49-factor diagnostic report with weighted score, grade, prioritized fixes | User asks for "audit", "review", "score", "check", "analyze" |

### Composition Rules

**You deliver ONLY the modules the user requested.** Default rules:

1. **Keyword-only input** (user provides keyword, no topic description, no URL, no images) → **TEXT only** - article body optimized for that keyword. Meta and alts require more context.
2. **Topic + keyword** (has context, no modules specified) → TEXT + META
3. **Full context** (topic + keyword + images or image descriptions) → TEXT + META + ALTS
4. **Explicit minimal** - "Just the article" / "Only text" / "Content only" → TEXT only (overrides rule #2/3)
5. **"With meta" / "+ meta tags"** → TEXT + META
6. **"With images" / "+ alt texts"** → TEXT + ALTS
7. **"Meta only" / "Just the tags"** → META only
8. **"Alt texts only" / "Just image descriptions"** → ALTS only
9. **"Full package" / "Everything" / "All"** → TEXT + META + ALTS (always honored)
10. **"Audit"** → AUDIT only (unless user also requests TEXT)
11. **"Audit + rewrite"** → AUDIT first, then TEXT + META + ALTS
12. **"Brief" / "Plan"** → TEXT outline + META drafts (no full body)
13. **"Audit + brief"** → AUDIT first, then TEXT outline + META drafts
14. **Sub-selection supported** - "just the H2s" → TEXT (headings only), "only the intro" → TEXT (first 200 words), "just internal links" → TEXT (links list), "rewrite only the meta" → META only, "audit only headings" → AUDIT (C13 + K8 factors only)

### Content-Type Routing

When generating/rewriting, detect content type and route to the correct scenario:

| Content Type | Scenario | Key Difference |
|-------------|----------|---------------|
| Blog article, guide, tutorial | `scenarios/article-generate.md` | 600+ words, H2-heavy, external links |
| Product page, e-commerce | `scenarios/product-page.md` | 600–1200 words, features/specs, Product schema |
| Home page, brand page | `scenarios/home-page.md` | 300–500 words, brand=primary keyword, Organization schema |
| Landing page, sales page | `scenarios/article-generate.md` + persuasion psychology layer | Persuasion-heavy, single CTA |
| Category/archive page | `scenarios/product-page.md` (adapted) | Multiple products, filtering, short descriptions |

> **Full specialized scenario procedures:** fetch `scenarios/home-page.md`, `scenarios/product-page.md`, `scenarios/video-podcast.md` from the RAW URL INDEX

### Multi-Keyword Pages

Some pages legitimately target multiple keywords (home pages, pillar pages, category pages):
- Designate ONE primary keyword for the 49-factor scorecard
- List secondary keywords as "co-targets" - each gets a dedicated H2 section with its own density
- For audit: score K1–K12 against the primary keyword. Flag secondary coverage as bonus, not requirement.
- Cannibalization check (K11) applies to the primary keyword only.

### Non-Text Content Handling

**JavaScript-heavy / SPA pages:** Content rendered client-side may be invisible to text-only analysis. Flag all content-dependent factors as ⚠️ "Verify on rendered page". Request rendered HTML or screenshot if available.

**Auto-translated content:** Watch for literal translations, preserved source-language idioms, untranslated cultural references. Flag with: ⚠️ "Possible machine translation detected - verify with native speaker." Burned-word lists apply to target language, but also check for source-language residues.

**Code-heavy technical content:** Readability targets (C8) adjust to Grade 10–12. Passive voice (C9) may be necessary for technical accuracy - flag as ⚠️ rather than ❌ if >10% but contextually justified. Sentence length max extends to 30 words for code explanations.

**Image generation:** RankWise does NOT generate images, illustrations, or graphics. This skill optimizes text content, meta tags, alt texts, and URLs. For image creation, use a dedicated image-generation tool (DALL-E, Midjourney, Stable Diffusion). RankWise can provide alt text suggestions and image placement recommendations, but actual image generation is out of scope.

### Flexible Request Examples

| User Request | Modules Activated |
|-------------|-------------------|
| "Write an SEO article about email marketing. Keyword: email strategy." | TEXT + META (topic + keyword context) |
| "SEO article. Keyword: email marketing." | TEXT only (keyword only, no topic context) |
| "Just the article text. No meta. Keyword: content marketing." | TEXT only (explicit) |
| "Give me meta tags for this landing page. Keyword: project tool." | META only |
| "I have 5 images. Generate alt texts. Keyword: fitness tracker." | ALTS only |
| "Audit this blog post. Keyword: SaaS metrics." | AUDIT only |
| "SEO article + alt texts. Skip the meta. Keyword: remote work." | TEXT + ALTS |
| "Generate article with meta only - no images." | TEXT + META |
| "Full package: article + meta + alts. Keyword: email automation." | TEXT + META + ALTS |
| "Audit this content, then rewrite it with SEO fixes." | AUDIT → TEXT + META + ALTS |
| "Content brief for a pillar page. Keyword: growth marketing." | TEXT outline + META drafts |

### Module Output Format

Each module outputs independently. When combined, modules appear in order: TEXT → META → ALTS → AUDIT.

**TEXT output:**
```
[SEO TITLE - this IS the H1]
[Full article body with H2/H3 structure, internal links inline, external links inline]
```

**META output:**
```
SEO Title (XX chars):
[title text]

Meta Description (XX chars):
[description text]

OG Title (XX chars):
[og title text]

OG Description (XX chars):
[og description text]

URL Slug:
/suggested-slug
```

**ALTS output (matches input format):**
```
# If input was array:
1. [alt text 1]
2. [alt text 2]

# If input was markdown:
![alt text 1](image1.jpg)
![alt text 2](image2.png)
```

**AUDIT output:**
```
[MODE: audit]
[WEIGHTED SCORE: XX.X%]
[GRADE: A/B/C/D/F]
...full report format: fetch scenarios/audit-report.md
```

### Cross-Module Header

Every output opens with a single context line:

```
[LANG: xx] [KEYWORD: xxx] [MODULES: text / meta / alts / audit]
```

No other preamble. No "Here is your content." No "I hope this helps."

---

## THE 49-FACTOR SEO SCORECARD

Every piece of content is scored against these factors.
> **Full scoring matrix with fix instructions per factor:** fetch `shared/checklist.md`
> **Full audit report format:** fetch `scenarios/audit-report.md`

### KEYWORD PLACEMENT (12 factors)

| # | Factor | Target | Severity |
|---|--------|--------|----------|
| K1 | Focus keyword set | Present | CRITICAL |
| K2 | Keyword in SEO title | Yes | CRITICAL |
| K3 | Keyword near title beginning | First 3-5 words | HIGH |
| K4 | Keyword in meta description | Within first 20 words | CRITICAL |
| K5 | Keyword in URL slug | Present, near front | HIGH |
| K6 | Keyword at content start | First 100-150 words | HIGH |
| K7 | Keyword in content body | Naturally distributed | CRITICAL |
| K8 | Keyword in subheadings | At least 1 H2 | HIGH |
| K9 | Keyword as image alt text | At least 1 image | MEDIUM |
| K10 | Keyword density | 0.8%–1.5% (not 0%, not >3%) | HIGH |
| K11 | Keyword cannibalization | No other page targets same primary keyword | HIGH |
| K12 | Keyword length | 3+ characters, not excessively long (≤7 words) | MEDIUM |

### CONTENT QUALITY (14 factors)

| # | Factor | Target | Severity |
|---|--------|--------|----------|
| C1 | Word count | 600+ (competitive: 1500+) | HIGH |
| C2 | Short paragraphs | ≤3 sentences, ≤150 words each | MEDIUM |
| C3 | Images and/or videos | ≥1 per 300 words | MEDIUM |
| C4 | Table of Contents | For articles >800 words | LOW |
| C5 | Numbers in title | At least 1 (odd numbers preferred) | MEDIUM |
| C6 | Power words in title | ≥2 emotionally charged words | MEDIUM |
| C7 | Sentiment signal | Clear positive or negative (not neutral) | LOW |
| C8 | Readability score | Grade 7-9 (EN), equivalent per language — see LANGUAGE ADAPTATION table below | HIGH |
| C9 | Passive voice ratio | ≤10% of sentences | MEDIUM |
| C10 | Transition words | ≥30% of sentences (EN); ≥25% other languages | LOW |
| C11 | Sentence length variety | No 3 consecutive same-length (±2 words) | MEDIUM |
| C12 | Consecutive sentence starts | No 3 consecutive same first word | MEDIUM |
| C13 | Heading hierarchy | H1→H2→H3 proper nesting, no skips | HIGH |
| C14 | Content-to-ad ratio | Main content dominates above-fold: ≤20% ad/nav in first 300 words | MEDIUM |

### LINKING (9 factors)

| # | Factor | Target | Severity |
|---|--------|--------|----------|
| L1 | Internal links | 3–10 per article | HIGH |
| L2 | External links | 2–5 to authoritative sources | HIGH |
| L3 | DoFollow external links | At least 1 of external links | MEDIUM |
| L4 | Link anchor text variety | No more than 2 exact-match anchors | MEDIUM |
| L5 | Outbound link quality | Recognized authority (.edu, .gov, known brands) | MEDIUM |
| L6 | No broken links | 0 broken | HIGH |
| L7 | Internal link relevance | Topically related pages | MEDIUM |
| L8 | Orphan prevention | Page has at least 1 incoming internal link | LOW |
| L9 | Link title attributes | `title=""` attribute present on key links | LOW |

### URL & TECHNICAL (8 factors)

| # | Factor | Target | Severity |
|---|--------|--------|----------|
| T1 | URL length | ≤75 characters | MEDIUM |
| T2 | URL structure | Keyword-rich, no stop words, hyphens not underscores | MEDIUM |
| T3 | SEO title length | Per-language limits — see LANGUAGE ADAPTATION table below | HIGH |
| T4 | Meta description length | Per-language limits — see LANGUAGE ADAPTATION table below | HIGH |
| T5 | Image file names | Descriptive, keyword-rich, hyphens | LOW |
| T6 | Schema markup | Appropriate type present (Article, Product, FAQ, etc.) | MEDIUM |
| T7 | Canonical URL | Set correctly | MEDIUM |
| T8 | OG / Twitter Card tags | Open Graph and/or Twitter Card meta tags present | LOW |

### ADVANCED SIGNALS (6 factors)

| # | Factor | Target | Severity |
|---|--------|--------|----------|
| A1 | Featured snippet potential | Concise 40–60 word answer for target query | MEDIUM |
| A2 | E-E-A-T signals | ≥3 of 5 signals: author bio, publication date, citation, about page, contact/privacy | HIGH |
| A3 | LSI / semantic keywords | 5–15 related terms naturally present | MEDIUM |
| A4 | Content freshness | Date visible, updated within reasonable window | LOW |
| A5 | Mobile readability | Scannable on mobile: short paragraphs, clear headings | MEDIUM |
| A6 | Breadcrumb structure | Logical breadcrumb path | LOW |

Total: **49 factors**. All factors scored: ✅ Pass / ❌ Fail / ⚠️ Warning / ⊘ N/A.

### Scoring weights
Factors carry different weights based on severity:
- **CRITICAL** = ×3 multiplier. Any CRITICAL failure caps maximum grade at B.
- **HIGH** = ×2 multiplier
- **MEDIUM** = ×1 multiplier
- **LOW** = ×0.5 multiplier
- ⊘ **N/A** factors are excluded from denominator entirely (does not penalize score)

**Formula:** `Score % = (Σ PASS_WEIGHTS) / (Σ ALL_WEIGHTS) × 100`

**Grade thresholds (applied AFTER weighted calculation):**

| Grade | Score % | Meaning | Constraint |
|-------|---------|---------|------------|
| A | 90%+ | Excellent. Minor tweaks only. | 0 CRITICAL failures |
| B | 75–89% | Good. Several improvements available. | ≤1 CRITICAL failure |
| C | 60–74% | Average. Significant gaps to fix. | ≤3 CRITICAL failures |
| D | 40–59% | Poor. Major overhaul needed. | - |
| F | <40% | Failing. Start over or fully restructure. | - |

**Delivery validation rule:** Before delivering any scored output, verify: N/A + CRITICAL + HIGH + MEDIUM + LOW + PASSED = 49. If sum ≠ 49, re-scan.

**8-Factor Quick Scan (pre-delivery on every output):**
1. ☐ K1 - Focus keyword defined?
2. ☐ K2 - Keyword in SEO title?
3. ☐ K4 - Keyword in meta description?
4. ☐ K7 - Keyword in content body?
5. ☐ K10 - Density 0.8–1.5%?
6. ☐ C1 - Word count 600+?
7. ☐ C13 - Heading hierarchy correct?
8. ☐ L1 - At least 3 internal links?

**Offline mode (no web access):** Mark K11, L5, L6, L7, L8, T6, T7 as ⊘ [NO_WEB] — exclude from denominator (max 42 instead of 49).

---

## KEYWORD STRATEGY

> **Full rules (LSI generation, cannibalization, density-by-length):** fetch `shared/keyword-rules.md`

### Primary keyword
- One focus keyword per page/article
- Must appear in: title, meta description, URL, first 150 words, at least one H2, at least one image alt
- Density: 0.8%–1.5% (not zero, not stuffed). Calculation: `(exact_matches / total_words) × 100`

### Secondary keywords
- 2–4 related terms
- Appear in at least one H2/H3 each
- Can be variations, synonyms, long-tail versions

### LSI / semantic keywords
- 5–15 terms related to primary topic
- Naturally distributed throughout body — NOT forced
- Source from: SERP "searches related to", "people also ask", topic vocabulary, competing page analysis, internal site search data, keyword research tools

### Keyword cannibalization check
- Verify no other page on the same site targets the exact same primary keyword
- If detected: recommend merge pages, differentiate keywords, or set canonical
- With web access: run `site:yoursite.com "keyword"` check

---

## CONTENT ARCHITECTURE

### Title formula
```
[Number] + [Power Word] + [Keyword] + [Promise/Curiosity Gap]
```
Examples:
- "7 Proven Ways to Fix Slow Website Load Times (No Developer Needed)"
- "How We Cut Customer Churn by 40% in 30 Days: The Exact Playbook"

### Heading structure
- **H1:** The article title. Contains primary keyword. One per page.
- **H2:** Major sections. At least one H2 contains primary keyword. Use power words.
- **H3:** Sub-sections under H2. Contain secondary keywords.
- **H4:** Detail points under H3 (rare, only for deep content)

### Paragraph rules
- Max 3 sentences per paragraph (mobile optimization)
- Max 150 words per paragraph (120 for non-English)
- Opening paragraph: hook + keyword within first 100-150 words
- Vary paragraph length: short-short-long-short creates visual rhythm

### Introduction pattern
1. Pattern interrupt (statistic, question, bold claim, story hook)
2. Pain point / problem recognition
3. Promise of solution
4. Keyword appears naturally within first 100-150 words

### Body pattern
- Each H2 section: clear point, evidence (data/example), keyword-adjacent language
- Alternate between: theory/explanation and concrete example/case
- Include at least one data point per 500 words
- Include at least one "surprising" or "contrarian" insight to trigger engagement

### Conclusion pattern
- Do NOT regurgitate introduction
- Clear recommendation or next step
- CTA: specific action, not "learn more"
- Internal link to related content

---

## LINKING STRATEGY

> **Full rules (anchor ratios, topic clusters, audit checklist):** fetch `shared/link-strategy.md`

### Internal links (3–10 per article)
- Link to 3–10 relevant internal pages
- Anchor text mix: partial match 30-40%, branded 20-25%, generic 20-25%, naked URL 5-10%, exact match ≤2
- Priority: link to cornerstone content and money pages
- Contextual (in-body) links > navigation links

### External links (2–5 per article)
- Link to authoritative sources: .edu, .gov, recognized publications, known trusted brands
- At least 1 DoFollow link to an external resource
- External links open in new tab (target="_blank" with rel="noopener")
- Cite data sources, studies, tools, original research
- No links to direct competitors unless comparing/reviewing

### Link placement
- First link within first 300 words
- Links distributed throughout (not clustered)
- Avoid "link dumping" at the end

---

## TECHNICAL SEO

### Meta title
- 50–60 characters (adjust per language — see LANGUAGE ADAPTATION table)
- Primary keyword near beginning
- Brand at end with separator: ` | Brand` or ` - Brand`
- Unique per page (no duplicates across site)
- Power words used when natural
- Numbers preferred: "7 Ways..." over "Ways..."

### Meta description
- 145–158 characters (adjust per language)
- Primary keyword within first 20 words
- Active voice, concrete value proposition
- No "We offer..." or "In this article..."
- Unique per page
- CTA when appropriate: specific verb, not "click here"

### URL slug
- ≤75 characters
- Contains primary keyword
- Hyphens between words (never underscores)
- No stop words: the, a, an, and, or, but, in, on, at, to, for, of, with
- No dates unless intentionally evergreen-dated
- No special characters
- > **Full stop-word lists for all 9 languages:** fetch `scenarios/url-optimize.md`

### Image SEO
- Alt text: descriptive, contains keyword for at least 1 image, ≤125 characters
- File name: descriptive, hyphens, keyword-rich
- Caption: optional but beneficial (captions are read 300% more than body text)
- Format: reference optimal formats (WebP > PNG > JPEG for web)

### Schema markup
> **Full JSON-LD templates (13 types):** fetch `shared/schema-templates.md`
- Article → Article schema
- Product → Product schema with price, availability, reviews
- FAQ → FAQPage schema (for search engine FAQ rich results)
- HowTo → HowTo schema (for step-by-step content)
- Recipe → Recipe schema
- Review → Review schema
- BreadcrumbList → Navigation breadcrumbs

---

## POWER WORDS & SENTIMENT

> **Full power word lists × 9 languages:** fetch `shared/power-words.md`

Power words are emotionally charged terms that trigger psychological responses. They increase CTR and engagement.

### Categories
| Category | Effect | Examples (EN) |
|----------|--------|----------|
| Fear/Loss | Urgency, attention | "Stop losing", "Don't risk", "Hidden", "Mistake", "Warning" |
| Curiosity | Click-through | "Secret", "Little-known", "Unconventional", "What nobody tells you" |
| Authority | Trust | "Proven", "Research-backed", "Science-based", "Expert", "Data-driven" |
| Ease/Convenience | Desire | "Simple", "Instantly", "Without", "No [pain point]", "Automatic" |
| Exclusivity | Status | "Exclusive", "Limited", "Only", "Insider", "Behind the scenes" |
| Specificity | Credibility | Numbers, percentages, dollar amounts, timeframes |

### English power words (inline — full list)
proven, secret, stop, simple, exclusive, limited, hidden, surprising, shocking, unexpected, amazing, incredible, ultimate, essential, critical, guaranteed, instant, immediate, automatic, effortless, breakthrough, insider, revealed, mistake, warning, never, avoid, dangerous, risk, urgent, little-known, unknown, unconventional, tested, research-backed, data-driven, expert, science-based, actual, real, exact, specific, step-by-step, definitive, powerful, effective

> **For non-English power words:** fetch `shared/power-words.md`

### Sentiment requirement
- Every SEO title should have a clear sentiment polarity - positive OR negative
- Neutral titles = missed opportunity for emotional CTR boost
- Negative titles often outperform positive on social, positive often better in SERP

---

## LANGUAGE ADAPTATION

All rules adapt to the content language. Inline quick reference:

| Lang | Title (chars) | Desc (chars) | Readability Target | Formula | Transition ≥% | Passive ≤% |
|------|--------------|--------------|--------------------|--------|----------------|------------|
| EN | 50–60 | 145–158 | Grade 7–9 | FK Grade | 30% | 10% |
| RU | 55–70 | 140–160 | FRE 50–70 | FRE | 25% | 8% |
| UK | 55–70 | 140–160 | LIX 30–45 | LIX | 25% | 10% |
| DE | 50–65 | 145–158 | WSTF 4–10 | WSTF | 25% | 10% |
| FR | 50–63 | 145–158 | FRE 50–70 | FRE | 25% | 10% |
| ES | 50–63 | 145–158 | FH 50–70 | FH | 25% | 10% |
| PT | 50–63 | 145–158 | FRE 50–70 | FRE | 25% | 10% |
| IT | 50–63 | 145–158 | Gulpease 50–60 | Gulpease | 25% | 10% |
| PL | 50–65 | 145–158 | FOG-PL 7–12 | FOG-PL | 25% | 10% |

### Per-language notes

**Russian / Русский:** Avoid канцеляризмы: «осуществлять», «являться», «данный». Yandex (~35% share) penalizes over-optimization harder.

**Ukrainian / Українська:** Google dominates (~95% share). Avoid Russianisms in keyword selection and content phrasing.

**German / Deutsch:** Compound nouns common — count characters accordingly. Avoid Nominalstil in content body.

**French / Español / Português / Italiano / Polski:** Character limits as above. Full per-language sentence length limits, readability nuances, and OG tag limits: fetch `shared/readability-params.md`.

### Cross-language optimization
When source content language differs from requested output language:
- Apply keyword rules and density targets of the TARGET language
- Apply burned-word filters of the TARGET language (rewrite removes source-language AI markers)
- Apply readability params of the TARGET language
- Preserve factual claims regardless of language
- Flag if source keyword doesn't translate cleanly - recommend local keyword research

---

## ── LANGUAGE RESOURCES (English — inline) ──

English is the default language. All word lists below are sufficient for offline English operation.
For non-English word lists, fetch the corresponding file from the RAW URL INDEX.

### English Power Words (for titles/headings — target ≥2)
proven, secret, stop, simple, exclusive, limited, hidden, surprising, shocking, unexpected, amazing, incredible, ultimate, essential, critical, guaranteed, instant, immediate, automatic, effortless, breakthrough, insider, revealed, mistake, warning, never, avoid, dangerous, risk, urgent, little-known, unknown, unconventional, tested, research-backed, data-driven, expert, science-based, actual, real, exact, specific, step-by-step, definitive, powerful, effective

### English Transition Words (for body — target ≥30% of sentences)
however, therefore, because, although, specifically, for example, for instance, in contrast, similarly, consequently, notably, meanwhile, furthermore, moreover, additionally, nevertheless, nonetheless, otherwise, instead, accordingly, hence, thus, in addition, on the other hand, as a result, in particular, in conclusion, to summarize, first, second, third, finally, next, then, also, besides, indeed, in fact, of course, certainly, surely, undoubtedly, regardless, despite, even though, while, whereas

### English Stop Words (for URL slugs — remove these)
the, a, an, and, or, but, in, on, at, to, for, of, with, by, from, up, about, into, through, during, before, after, above, below, between, is, are, was, were, be, been, being, have, has, do, does, did, will, would, can, could, may, might, must, shall, should, not, no

### English Passive Voice Detection Patterns
- `(am|is|are|was|were|be|been|being) + [optional adverb] + [past participle verb ending in -ed/-en/-t]`
- `(has|have|had|will have) + been + [past participle]`
- Examples: "was written", "were analyzed", "has been shown", "can be improved"

### English Burned Words (AI markers — delete on sight in Rewrite mode)
**Universal:** leverage, utilize, harness, empower, facilitate, optimize, streamline, revolutionize, transform (generic), robust, seamless, cutting-edge, best-in-class, game-changer, next-level, innovative (unproven), holistic, ecosystem, dynamic, synergy, granular, scalable (without specifics)

**Empty intensifiers:** very, extremely, incredibly, amazingly, truly, really, absolutely, completely, thoroughly, highly, remarkably

**Throat-clearing openers:** In today's, In the modern, In an era, The landscape of, With the rise of, As we navigate, In the ever-evolving, It goes without saying, In recent years, The world of, Nowadays, In the age of

**Conclusion regurgitation:** In conclusion, To summarize, In summary, To wrap up, As we have seen, Overall, In closing, To sum up, The bottom line, At the end of the day

**Fake transitions (delete unless structural):** Moreover, Furthermore, Additionally, Consequently, Thus, Hence, It should be noted that, It is important to note, It is worth mentioning, Needless to say

**Hedging language:** It could be argued that, One might say, Some research suggests, There is evidence to suggest, It is possible that, Arguably, Generally speaking, For the most part

**Rhetorical question padding:** What does this mean for you?, Sounds good right?, Want to know the best part?, But what about X?, So how does it work?, Ready to get started?

**SEO-specific AI tells:** "A comprehensive guide to...", "In this article, we will explore...", "Whether you're a beginner or an expert...", "Read on to learn more...", "Without further ado..."

**Replacement rule:** Do not find a synonym. Describe the actual action or quality.

> **Full burned words × 9 languages:** fetch `shared/burned-words.md`

---

## INTEGRATION WITH OTHER SKILLS

RankWise is designed as a **modular SEO engine** - it can work alongside any other AI skill without conflict. RankWise handles SEO structure, keywords, linking, and meta signals. Other skills handle their domain. The goal: compose, don't compete.

### General Integration Protocol

**Recommended pipeline for multi-skill workflows:**
1. **RankWise Brief or Generate** → establish SEO structure, keyword placement, heading hierarchy, meta drafts
2. **Other skill(s)** → apply their domain expertise (tone, persuasion, formatting, translation, etc.) within the SEO framework
3. **RankWise Audit** → verify that SEO signals survived all downstream transformations

### Integration Rules for Other Skills

When combining RankWise with any other skill, communicate these guardrails:

1. **Keyword placement is load-bearing.** Other skills may rewrite sentences but must preserve keyword positions in: title, first 150 words, at least one H2, meta description. If a skill automatically cleans up or paraphrases, instruct it: "Preserve all keyword placements from the RankWise output."
2. **Heading hierarchy is structural.** H1→H2→H3 nesting must survive any rewrite. If another skill restructures content, instruct it: "Keep heading hierarchy intact - only rewrite content under headings."
3. **Density stays in range.** Text expansions or contractions by other skills can drift keyword density below 0.8% or above 3%. Re-check density after any downstream pass.
4. **Link integrity.** Other skills may remove inline links during rewriting. Instruct them to preserve all hyperlinks, or re-add them after the pass.
5. **Meta tags are separate.** If another skill generates its own meta tags, instruct it to skip the SEO meta layer and leave it to RankWise.
6. **Language consistency.** If another skill translates or localizes content, re-apply readability targets and power-word lists for the target language.

### Conflict Awareness

| Transformation | Risk | Guardrail |
|---------------|------|-----------|
| Text cleanup / deduplication | May remove keyword instances | Re-check density after pass; instruct skill to skip keyword-bearing sentences |
| Tone adjustment | May strip power words or sentiment signals | Cross-reference power-word list; cap power word density at ~2 per 300 words |
| Content shortening | May drop below 600-word threshold or cut H2 sections | Set minimum word count before pass; lock heading structure |
| Content expansion | May over-stuff keywords or dilute structure | Cap keyword density at 1.5%; maintain heading count |
| Translation | Source-language idioms may not map to target | Apply burned-words and readability params of target language |

### Multi-Skill Joint Prompt Pattern

```
"1) RankWise SEO [brief/generate/rewrite] for [topic]. Keyword: [kw].
 2) [Skill Name] [action] from that output. [Additional instructions if needed].
 3) RankWise audit the final result. [LANG: xx]."
```

This pattern works with any skill - humanization, persuasion, translation, formatting, summarization, or any other downstream processor.

---

## OUTPUT FORMATS - Quick Reference

Full format details: see **OUTPUT COMPOSITION** above (Module Output Format + Cross-Module Header). Brief summary:

| Mode | Output |
|------|--------|
| **Generate / Rewrite** | Cross-module header → TEXT (H1 + body + links) → META (title/desc/OG/slug) → ALTS → [Rewrite: + CHANGELOG] → Schema recommendation |
| **Audit** | Cross-module header → Weighted Score + Grade → N/A → CRITICAL → HIGH → MEDIUM → LOW → PASSED → Impact → Top 5 Actions (full spec: fetch `scenarios/audit-report.md`) |
| **Brief** | Cross-module header → Intent → Keywords → H1 Options → H2 Outline → Meta Drafts → Link Plan → Media Plan → Schema (full spec: fetch `scenarios/content-brief.md`) |
| **Any combination** | Only requested modules, in order: TEXT → META → ALTS → AUDIT |

---

## MODULE ACTIVATION LOGIC

Before processing any request, determine which modules to activate using these ordered rules:

**Step 1: Parse user intent for modules**
Scan the request for module triggers (see OUTPUT COMPOSITION table above).

**Step 2: Determine content source**
- Topic + keyword (no existing content) → **GENERATE** pipeline for TEXT
- URL or pasted text → **REWRITE** pipeline for TEXT
- No TEXT requested → skip content generation

**Step 3: Activate only requested modules, in order: TEXT → META → ALTS → AUDIT**

**Special routing rules (first match wins):**

1. **Quick-Fix detected** - "fix my [element]", "too long/short", "add keyword to", "remove" → Activate only the relevant module with fix instructions (fetch `scenarios/quick-fix.md`)
2. **Scoped audit** - "audit this title", "audit my meta", "review my tags", "check my alt texts", "audit only headings" → META or ALTS module with audit annotations (NOT full AUDIT). If user says "audit this meta + rewrite it" → META with audit annotations first, then META rewrite.
3. **Sub-selection** - "just the headings", "only the intro", "just internal links", "only the meta", "rewrite only H2s" → activate the requested subset of the appropriate module
4. **Audit-only detected** - "audit", "review", "score", "check", "analyze" without "and rewrite/fix" and without narrow scope → AUDIT only
5. **Audit + Rewrite** - "audit and rewrite/fix/optimize" → AUDIT first, then TEXT + META + ALTS
6. **Audit + Brief** - "audit and plan/brief" → AUDIT first, then TEXT(outline) + META(drafts)
7. **Brief requested** - "brief", "plan", "outline", "content plan" → TEXT(outline) + META(drafts)
8. **No modules specified** → context-aware default:
   - Keyword only (no topic/images/URL) → TEXT only
   - Topic + keyword → TEXT + META
   - Topic + keyword + images → TEXT + META + ALTS
9. **Ambiguous** → ask: "Just the article text? Full package with meta and alt texts? Or something else?"

**Module activation is independent of mode.** The mode (Generate/Rewrite/Audit) determines HOW content is produced. Modules determine WHAT is delivered.

**Offline mode detection:** Before audit operations, determine if web access is available (fetch tool, search capability). If NO web access → activate OFFLINE scoring (K11, L5, L6, L7, L8, T6, T7 → ⊘ [NO_WEB], exclude from denominator). If YES → score all factors normally.

### Handling Incomplete Input

When the user's request is missing critical information, do NOT guess silently. Ask precisely what's needed:

| Missing | Ask |
|---------|-----|
| No keyword | "What's the focus keyword for this content?" |
| No language | "Which language should I write in? (en/ru/uk/de/fr/es/pt/it/pl)" |
| No content (for rewrite/audit) | "Please paste the content or share the URL." |
| Ambiguous mode | "Should I generate new content, rewrite existing content, run an SEO audit, or create a content brief?" |
| Ambiguous modules | "Just the article text? With meta tags? Full package (article + meta + alt texts)?" |
| URL provided, no keyword | Extract keyword from page title/H1 and ask: "I see '[inferred keyword]' as the likely focus keyword. Confirm?" |

If 2+ items are missing, ask about all of them in a single response. Do not ask one at a time.

---

## ── SCENARIO SUMMARIES (Quick Reference) ──

Each scenario has a 5-10 line summary sufficient for basic execution. Fetch the full file for edge cases, detailed templates, and examples.

| Scenario | Mode | Core Pipeline | Fetch |
|----------|------|---------------|-------|
| **article-generate** | Generate | intent → keywords → title → outline → write → meta → links → QA | `scenarios/article-generate.md` |
| **article-rewrite** | Rewrite | extract → pre-audit → preserve → restructure → rewrite → meta → links → deliver | `scenarios/article-rewrite.md` |
| **audit-report** | Audit | parse → score 49 → weight → grade → prioritize → report format | `scenarios/audit-report.md` |
| **content-brief** | Brief | intent → keywords → structure → meta drafts → linking plan → media plan → schema → deliver | `scenarios/content-brief.md` |
| **meta-optimize** | Meta-Only | title (per page type formula) → description → OG tags → URL slug → output format | `scenarios/meta-optimize.md` |
| **alt-texts** | Meta-Only | extract images → identify type → generate (≤125 chars, keyword in ≥1, no "image of") → same format output | `scenarios/alt-texts.md` |
| **url-optimize** | Meta-Only | parse URL → identify keyword → strip stop words → shorten → validate (≤75 chars, hyphens, lowercase) | `scenarios/url-optimize.md` |
| **quick-fix** | Quick-Fix | trigger detection (33 phrases → factor mapping) → apply fix per factor → before/after → deliver | `scenarios/quick-fix.md` |
| **home-page** | Generate | multi-keyword (brand=primary, 3-5 total) → hero structure → Organization schema → adapted factors (C1: 300-500, L2: 0-2) | `scenarios/home-page.md` |
| **product-page** | Generate | product keyword → features/specs → Product+Offer schema → ≥5 images → breadcrumb → adapted factors (C1: 600-1200) | `scenarios/product-page.md` |
| **video-podcast** | Generate/Meta | platform detection → title (YT ≤100) → description above-fold → timestamps (5-12) → tags → VideoObject+SeekToAction schema | `scenarios/video-podcast.md` |

---

## ── RAW URL INDEX ──

Base URL: `https://raw.githubusercontent.com/MADEVAL/RankWise/main/`

> **Stable reference:** Replace `main` with a pinned tag for guaranteed version stability:
> `https://raw.githubusercontent.com/MADEVAL/RankWise/v1.3.0/shared/checklist.md`

### Always-needed references
- 49-factor checklist + fix instructions: [shared/checklist.md](https://raw.githubusercontent.com/MADEVAL/RankWise/main/shared/checklist.md)
- Keyword rules (density, placement, LSI, cannibalization): [shared/keyword-rules.md](https://raw.githubusercontent.com/MADEVAL/RankWise/main/shared/keyword-rules.md)

### Language-specific references
- Power words × 9 languages: [shared/power-words.md](https://raw.githubusercontent.com/MADEVAL/RankWise/main/shared/power-words.md)
- Burned words (AI markers) × 9 languages: [shared/burned-words.md](https://raw.githubusercontent.com/MADEVAL/RankWise/main/shared/burned-words.md)
- Readability params per language: [shared/readability-params.md](https://raw.githubusercontent.com/MADEVAL/RankWise/main/shared/readability-params.md)

### Strategy references
- Internal/external linking rules: [shared/link-strategy.md](https://raw.githubusercontent.com/MADEVAL/RankWise/main/shared/link-strategy.md)
- JSON-LD schema templates (13 types): [shared/schema-templates.md](https://raw.githubusercontent.com/MADEVAL/RankWise/main/shared/schema-templates.md)

### Scenario procedures (full step-by-step)
- Article generation: [scenarios/article-generate.md](https://raw.githubusercontent.com/MADEVAL/RankWise/main/scenarios/article-generate.md)
- Article rewrite: [scenarios/article-rewrite.md](https://raw.githubusercontent.com/MADEVAL/RankWise/main/scenarios/article-rewrite.md)
- Audit report format: [scenarios/audit-report.md](https://raw.githubusercontent.com/MADEVAL/RankWise/main/scenarios/audit-report.md)
- Content brief/plan: [scenarios/content-brief.md](https://raw.githubusercontent.com/MADEVAL/RankWise/main/scenarios/content-brief.md)
- Meta tag optimization: [scenarios/meta-optimize.md](https://raw.githubusercontent.com/MADEVAL/RankWise/main/scenarios/meta-optimize.md)
- Alt texts: [scenarios/alt-texts.md](https://raw.githubusercontent.com/MADEVAL/RankWise/main/scenarios/alt-texts.md)
- URL slug optimization: [scenarios/url-optimize.md](https://raw.githubusercontent.com/MADEVAL/RankWise/main/scenarios/url-optimize.md)
- Quick-fix (all 49 factors): [scenarios/quick-fix.md](https://raw.githubusercontent.com/MADEVAL/RankWise/main/scenarios/quick-fix.md)
- Home page / brand SEO: [scenarios/home-page.md](https://raw.githubusercontent.com/MADEVAL/RankWise/main/scenarios/home-page.md)
- Product / e-commerce SEO: [scenarios/product-page.md](https://raw.githubusercontent.com/MADEVAL/RankWise/main/scenarios/product-page.md)
- Video / podcast SEO: [scenarios/video-podcast.md](https://raw.githubusercontent.com/MADEVAL/RankWise/main/scenarios/video-podcast.md)

### Annotated examples
- Full rewrite before/after: [examples/before-after-article.md](https://raw.githubusercontent.com/MADEVAL/RankWise/main/examples/before-after-article.md)
- Meta tag examples: [examples/meta-examples.md](https://raw.githubusercontent.com/MADEVAL/RankWise/main/examples/meta-examples.md)
- Audit report example: [examples/audit-example.md](https://raw.githubusercontent.com/MADEVAL/RankWise/main/examples/audit-example.md)
- Integration pipeline example: [examples/integration-pipeline.md](https://raw.githubusercontent.com/MADEVAL/RankWise/main/examples/integration-pipeline.md)

### Validator (for CI/CD or programmatic use)
- CLI entry point: run `pip install rankwise-validator && rankwise-validator --help`
- All sources: [validator/](https://github.com/MADEVAL/RankWise/tree/main/validator/)
- Tests: [tests/](https://github.com/MADEVAL/RankWise/tree/main/tests/)
- Benchmarks: [benchmarks/](https://github.com/MADEVAL/RankWise/tree/main/benchmarks/)

---

## POST-GENERATION VALIDATION (Orchestrator)

RankWise includes a **Python validator + orchestrator** (`validator/`) that computes objective SEO metrics deterministically and generates targeted LLM fix prompts. Use it to verify content after generation — the LLM focuses on writing quality and structure; the orchestrator handles exact measurements and automated re-validation.

### Validation + Fix Pipeline

```bash
# 1. Full metrics report
python -m validator.cli --file content.md --keyword "your keyword" --title "Your SEO Title" --meta "Description" --lang en

# 2. Checklist scores (16 of 49 factors)
python -m validator.cli --file content.md --keyword "your keyword" --title "Your Title" --meta "Description" --lang en --checklist

# 3. Orchestrator — build fix plan with LLM-ready prompts
python -m validator.cli --file content.md --keyword "your keyword" --title "Your Title" --orchestrate

# 4. Consolidated LLM fix prompt (ready to paste into the LLM)
python -m validator.cli --file content.md --keyword "your keyword" --title "Your Title" --fix-prompt

# 5. After LLM applies fixes — re-validate and diff
python -m validator.cli --file content.md --keyword "keyword" --title "Title" --orchestrate --revalidate-file fixed.md

# 6. JSON output for programmatic use
python -m validator.cli --file content.md --keyword "keyword" --title "Title" --orchestrate --json
```

### Orchestrator Coverage (16 factors)

The Python orchestrator computes: **K1, K2, K6, K7, K10, C1, C2, C5, C6, C8, C9, C10, C11, C12, T3, T4**

These are the factors where exact numeric measurement matters. Remaining factors (linking, heading hierarchy, advanced signals, etc.) are evaluated by the LLM.

### Pipeline Workflow

```
1. User requests SEO content
2. LLM generates content following RankWise rules
3. User runs: python -m validator.cli --file content.md --keyword "kw" --fix-prompt
4. LLM receives a consolidated fix prompt with exact values and target locations
5. LLM applies targeted fixes
6. User runs: python -m validator.cli --file content.md ... --orchestrate --revalidate-file fixed.md
7. Repeat until all 16 factors pass → [ALL CLEAR]
```

> **Requirements:** Python 3.10+ + `pip install readsight`

---

## QUICK START

**Full package (article + meta + alts):**
> "Write an SEO article about [topic]. Primary keyword: [keyword]. Language: en."

**Article only (no meta, no alts):**
> "Just the article text about [topic]. No meta. Keyword: [keyword]."

**Article + meta (no images):**
> "SEO article with meta tags only. Skip the alt texts. Keyword: [keyword]."

**Meta tags only:**
> "Generate meta title and description for [page topic]. Focus keyword: [keyword]."

**Image alt texts only:**
> "Generate SEO alt texts for these images: [array]. Focus keyword: [keyword]."

**Full SEO audit:**
> "Audit this content for SEO: [paste text]. Focus keyword: [keyword]."

**Audit + rewrite:**
> "Audit this content, then rewrite it with SEO fixes. Keyword: [keyword]."

**Rewrite from URL:**
> "Rewrite this article for better SEO: [URL]. Focus keyword: [keyword]."

**Content brief:**
> "Create an SEO content brief for [topic]. Target keyword: [keyword]."

**Joint with another skill:**
> "RankWise SEO brief for [topic], then [other skill] from that brief. EN. Keyword: [kw]."

---

## FILES IN THIS SKILL

```
rankwise/
├── SKILL.md                        ← THIS FILE — complete single-file orchestrator
├── README.md / README.ru.md        ← Documentation (bilingual)
├── CHANGELOG.md                    ← Version history
├── LICENSE                         ← MIT | Copyright Yevhen Leonidov
├── IMPROVEMENT-PLAN.md             ← v1.3.0 improvement plan (this version)
├── .gitignore
├── shared/
│   ├── checklist.md                ← 49 SEO factors with thresholds, severity, fixes
│   ├── keyword-rules.md            ← Density, placement, LSI, cannibalization rules
│   ├── power-words.md              ← Power words × languages for sentiment & CTR
│   ├── schema-templates.md         ← JSON-LD structured data templates
│   ├── readability-params.md       ← Readability targets per language
│   ├── burned-words.md             ← AI detection patterns × 9 languages
│   └── link-strategy.md            ← Internal/external linking rules
├── scenarios/
│   ├── article-generate.md         ← Full article generation from topic + keywords
│   ├── article-rewrite.md          ← Rewrite pipeline (URL or pasted text)
│   ├── meta-optimize.md            ← Meta titles, descriptions, OG tags
│   ├── alt-texts.md                ← Image alt text optimization (array/inline)
│   ├── audit-report.md             ← Full SEO audit with scoring
│   ├── content-brief.md            ← Content brief / plan generation
│   ├── url-optimize.md             ← URL slug optimization
│   ├── quick-fix.md                ← Single-factor quick fixes (all 49)
│   ├── home-page.md                ← Home page / brand page optimization
│   ├── product-page.md             ← Product / e-commerce page optimization
│   └── video-podcast.md            ← YouTube / podcast SEO
├── examples/
│   ├── before-after-article.md     ← Full article rewrite example
│   ├── meta-examples.md            ← Meta tag before/after examples
│   ├── audit-example.md            ← Complete audit report example
│   └── integration-pipeline.md     ← Multi-skill integration example
├── validator/                      ← Python CLI + Orchestrator — deterministic metrics (16/49 factors) + automated fix prompts
│   ├── __init__.py                  ← Module exports
│   ├── cli.py                       ← CLI entry point (validate, orchestrate, revalidate)
│   ├── metrics.py                   ← Core analysis engine
│   └── orchestrator.py             ← Automated fix plan generation + LLM prompt builder
├── tests/
│   ├── test_metrics.py              ← Validator unit tests
│   ├── test_languages.py            ← Multi-language tests (9 languages)
│   ├── test_benchmarks.py           ← Benchmark regression tests
│   └── test_orchestrator.py         ← Orchestrator pipeline tests
└── benchmarks/                     ← 5 reference texts for regression testing
```

**How files relate to each other:**
- `SKILL.md` is the **single-file orchestrator** — it contains all core rules inline and provides raw GitHub URLs for every reference file
- `shared/` files are **data references** — fetch them via RAW URL INDEX when the task requires per-language word lists or full scoring matrices
- `scenarios/` files are **procedural playbooks** — fetch them via RAW URL INDEX when the inline procedure summary is insufficient
- `examples/` files are **annotated demonstrations** — fetch them for reference on expected output quality
- `validator/orchestrator.py` is the **automated fix pipeline** — validates content, generates LLM-ready fix prompts, supports iterative re-validation
- `validator/metrics.py` is the **deterministic computation layer** — computes 16 of 49 factors via ReadSightPy (independent from this skill prompt)
