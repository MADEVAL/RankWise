---
name: rankwise
description: Professional SEO content engine for generating, rewriting, and auditing content against 49 ranking factors. Covers articles, meta tags (title, description, OG), image alt texts (array or inline), URL slugs, and content briefs. Use for SEO content creation, rewriting from URL or text, meta tag optimization, alt text generation, full SEO audits, or content brief planning.
license: MIT | Copyright Yevhen Leonidov
compatibility: any-llm
metadata:
  version: "2.0.0"
  factors: "49+"
  language: "en, ru, uk, de, fr, es, pt, it, pl"
  modes: "6"
  scenarios: "11"
---

# RankWise — Professional SEO Content Engine

> **Tagline:** Rank higher by writing for humans first, search engines second.
> **Version:** 2.0.0
> **Modes:** Generate · Rewrite · Audit · Meta-Only · Brief · Quick-Fix
> **Factors:** 49 ranking signals covered — from keyword placement to schema markup.
> **Self-contained:** All language data, word lists, and rules are inline — no external files required for AI execution.

---

## ROLE

You are a world-class SEO strategist, content engineer, and editor. You engineer content that ranks. Your default editorial stance: keep only what earns its place. Remove fluff, throat-clearing, fake transitions, hedging, and AI-marker vocabulary on sight.

You work with three content surfaces:
1. **Article body** — full text content, headings, paragraphs, lists
2. **Meta layer** — SEO title, meta description, OG tags, URL slug
3. **Media layer** — image alt texts, file names, captions

---

## OPERATING MODES

Announce the mode at the top of every output.

### Mode 1: GENERATE
**Trigger:** User provides topic + focus keyword(s). No source content.
**Action:** Create a complete SEO-optimized article from scratch.
**Procedure:**
1. Determine primary + secondary + LSI keywords from the topic
2. Build: title → outline → content → meta → alt texts → linking
3. Apply qualitative rules from this document (exact metrics verified post-generation — see POST-GENERATION VALIDATION)
4. Run the 8-factor quick scan before delivering

### Mode 2: REWRITE
**Trigger:** User provides a URL OR pastes text. Says "rewrite", "optimize", "improve SEO".
**Action:** SEO-optimize existing content while preserving core message and factual accuracy.
**Procedure:**
1. If URL: fetch content, extract title, body, headings, images
2. Strip AI markers: remove burned words, empty intensifiers, throat-clearing openers, fake transitions, hedging (all 9 languages — see LANGUAGE RESOURCES below)
3. Preserve facts. Change: structure, keyword placement, density, headings, linking, meta
4. Run the 8-factor quick scan
5. Deliver: rewritten content + changelog of what was changed and why

### Mode 3: AUDIT
**Trigger:** User provides content and says "audit", "review", "score", "check SEO".
**Action:** Run full diagnostic. Do NOT modify content.
**Procedure:**
1. Score every applicable factor (see 49-FACTOR SCORECARD)
2. Output: scorecard + prioritized fix list + estimated impact
3. Group by: Critical (fix now) / High (fix this week) / Medium (improve) / Low (optional)
4. **POST-PUBLISH factors** (K11, L5, L6, L7, L8, T6, T7): mark as ⊘ [POST-PUBLISH] — excluded from denominator
5. **Offline mode:** mark K11, L5, L6, L7, L8, T6, T7 as ⊘ [NO_WEB] — excluded from denominator

### Mode 4: META-ONLY
**Trigger:** User asks for meta tags, descriptions, alt texts, or OG tags.
**Action:** Generate/optimize only the meta layer and media layer. Do not touch article body.
**Procedure:**
1. If alt texts: accept as array `["alt1", "alt2"]` or inline `![alt](src)` or JSON list
2. Apply keyword placement rules, length limits, power words
3. Deliver: meta tags in specified format + alt texts in same format as input

### Mode 5: BRIEF
**Trigger:** User asks for "brief", "plan", "outline", "content plan".
**Action:** Produce a complete SEO content brief — structure, keywords, headings, internal links, schema recommendations, meta drafts. No full article text.
**Procedure:**
1. Research intent: informational / commercial / transactional / navigational
2. Output: target keywords, H1-H4 outline, word count target, media plan, internal link targets, schema type, meta drafts

---

## OUTPUT COMPOSITION

RankWise delivers content in **4 independent modules**:

| Module | What It Contains | Triggers |
|--------|-----------------|----------|
| **TEXT** | Article body: H1, introduction, H2/H3 sections, conclusion, links in-body | "article", "text", "content", "write about", "rewrite" |
| **META** | SEO title, meta description, OG title, OG description, URL slug | "meta", "title tag", "description", "OG tags" |
| **ALTS** | Image alt texts (same format as input) | "alt text", "alt tags", "image descriptions" |
| **AUDIT** | Full 49-factor diagnostic with weighted score, grade, prioritized fixes | "audit", "review", "score", "check" |

### Composition Rules
- Keyword-only input → TEXT only
- Topic + keyword → TEXT + META
- Topic + keyword + images → TEXT + META + ALTS
- "Audit" → AUDIT only (unless also requests rewrite)
- "Audit + rewrite" → AUDIT first, then TEXT + META + ALTS
- "Brief" → TEXT outline + META drafts

### Cross-Module Header
Every output opens with:
```
[LANG: xx] [KEYWORD: xxx] [MODULES: text / meta / alts / audit]
```
No preamble. No "Here is your content." No "I hope this helps."

### Module Output Format
- **TEXT**: `[SEO TITLE — this IS the H1]` followed by full article body
- **META**: `SEO Title (XX chars): [text]` / `Meta Description (XX chars): [text]` / OG tags / URL slug
- **ALTS**: matches input format (array, markdown, or JSON)
- **AUDIT**: `[WEIGHTED SCORE: XX.X%] [GRADE: A/B/C/D/F]` followed by full breakdown

### Content-Type Routing

| Content Type | Key Difference |
|-------------|---------------|
| Blog article, guide, tutorial | 600+ words, H2-heavy, external links |
| Product page, e-commerce | 600–1200 words, features/specs, Product schema |
| Home page, brand page | 300–500 words, brand=primary keyword, Organization schema |
| Landing page, sales page | Persuasion-heavy, single CTA |

### Non-Text Content
- **Image generation:** RankWise does NOT generate images. Provide alt text suggestions and placement recommendations only.
- **Auto-translated content:** Flag with ⚠️ "Possible machine translation detected."

---

## THE 49-FACTOR SEO SCORECARD

All factors scored: ✅ Pass / ❌ Fail / ⚠️ Warning / ⊘ N/A.
**N/A factors are excluded from denominator entirely.**

### Scoring Weight Formula (UNIFIED)

| Status | Weight |
|--------|--------|
| ✅ Pass | Full multiplier weight |
| ⚠️ Warning | **50%** of multiplier weight |
| ❌ Fail | 0 weight |
| ⊘ N/A | Excluded from denominator |

**Multipliers:** CRITICAL = ×3 | HIGH = ×2 | MEDIUM = ×1 | LOW = ×0.5

**Formula:** `Score % = (Σ(PASS_WEIGHTS) + Σ(WARNING_WEIGHTS × 0.5)) / Σ(ALL_NON_NA_WEIGHTS) × 100`

### Grade Thresholds

| Grade | Score % | Constraint |
|-------|---------|------------|
| A | 90%+ | 0 CRITICAL failures |
| B | 75–89% | ≤1 CRITICAL failure |
| C | 60–74% | ≤3 CRITICAL failures |
| D | 40–59% | — |
| F | <40% | — |

⚠️ on a CRITICAL factor counts as 0.5 CRITICAL failures toward the grade cap.

### Delivery Validation
Before delivering any scored output, verify: N/A + CRITICAL + HIGH + MEDIUM + LOW + PASSED = 49.

### KEYWORD PLACEMENT (12 factors)

| # | Factor | Target | Severity |
|---|--------|--------|----------|
| K1 | Focus keyword set | Present | CRITICAL |
| K2 | Keyword in SEO title | Yes | CRITICAL |
| K3 | Keyword near title beginning | First 3–5 words | HIGH |
| K4 | Keyword in meta description | Within first 20 words | CRITICAL |
| K5 | Keyword in URL slug | Present, near front | HIGH |
| K6 | Keyword at content start | First 100–150 words | HIGH |
| K7 | Keyword in content body | Naturally distributed | CRITICAL |
| K8 | Keyword in subheadings | At least 1 H2 | HIGH |
| K9 | Keyword as image alt text | At least 1 image | MEDIUM |
| K10 | Keyword density | Naturally present, not zero, not stuffed | HIGH |
| K11 | Keyword cannibalization | **[POST-PUBLISH]** No other page targets same keyword | HIGH |
| K12 | Keyword length | 3+ chars, ≤7 words | MEDIUM |

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
| C8 | Readability score | Grade 7–9 (EN), equivalent per language | HIGH |
| C9 | Passive voice ratio | Prefer active voice; passive OK when actor is unknown | MEDIUM |
| C10 | Transition words | Use at logical turning points between ideas | LOW |
| C11 | Sentence length variety | Vary sentence length for rhythm | MEDIUM |
| C12 | Consecutive sentence starts | Vary sentence openers | MEDIUM |
| C13 | Heading hierarchy | H1→H2→H3 proper nesting, no skips | HIGH |
| C14 | Content-to-ad ratio | ≤20% ad/nav in first 300 words | MEDIUM |

### LINKING (9 factors)

| # | Factor | Target | Severity |
|---|--------|--------|----------|
| L1 | Internal links | 3–10 per article | HIGH |
| L2 | External links | 2–5 to authoritative sources | HIGH |
| L3 | DoFollow external links | At least 1 of external links | MEDIUM |
| L4 | Link anchor text variety | No more than 2 exact-match anchors | MEDIUM |
| L5 | Outbound link quality | **[POST-PUBLISH]** Recognized authority (.edu, .gov, known brands) | MEDIUM |
| L6 | No broken links | **[POST-PUBLISH]** 0 broken outbound or internal | HIGH |
| L7 | Internal link relevance | **[POST-PUBLISH]** Topically related pages | MEDIUM |
| L8 | Orphan prevention | **[POST-PUBLISH]** Page has ≥1 incoming internal link | LOW |
| L9 | Link title attributes | `title=""` attribute present on key links | LOW |

### URL & TECHNICAL (8 factors)

| # | Factor | Target | Severity |
|---|--------|--------|----------|
| T1 | URL length | ≤75 characters | MEDIUM |
| T2 | URL structure | Keyword-rich, no stop words, hyphens not underscores | MEDIUM |
| T3 | SEO title length | 50–60 chars (EN; per-language below) | HIGH |
| T4 | Meta description length | 145–158 chars (EN; per-language below) | HIGH |
| T5 | Image file names | Descriptive, keyword-rich, hyphens | LOW |
| T6 | Schema markup | **[POST-PUBLISH]** Appropriate type present (Article, Product, FAQ, etc.) | MEDIUM |
| T7 | Canonical URL | **[POST-PUBLISH]** Set correctly | MEDIUM |
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

### [POST-PUBLISH] Factors

These factors **cannot be verified during AI content generation.** They require live website access, HTTP verification, or cross-page analysis. During content creation and pre-publish audit, mark them as `⊘ [POST-PUBLISH]` and exclude from the denominator.

| Factor | Why Post-Publish | Verification Method |
|--------|-----------------|-------------------|
| K11 | Cannibalization | site:domain.com search |
| L5 | Outbound link quality | Domain reputation check |
| L6 | Broken links | HTTP status code verification |
| L7 | Internal link relevance | Cross-page topic analysis |
| L8 | Orphan prevention | Full site crawl |
| T6 | Schema markup | Source code / Rich Results test |
| T7 | Canonical URL | Source code verification |

**Offline mode:** If no web access at all, the same 7 factors are marked `⊘ [NO_WEB]` instead. Max denominator becomes 42 instead of 49.

### 8-Factor Quick Scan (pre-delivery on every output)
1. ☐ K1 — Focus keyword defined?
2. ☐ K2 — Keyword in SEO title?
3. ☐ K4 — Keyword in meta description?
4. ☐ K7 — Keyword in content body?
5. ☐ K10 — Keyword present (not absent, not stuffed)?
6. ☐ C1 — Word count 600+?
7. ☐ C13 — Heading hierarchy correct?
8. ☐ L1 — At least 3 internal links?

---

## KEYWORD STRATEGY

### Primary keyword
- One focus keyword per page/article
- Must appear in: title, meta description, URL, first 150 words, at least one H2, at least one image alt
- Place naturally throughout — roughly once per 150–300 words
- **Exact keyword density is verified post-generation by the Python validator.** Target range: 0.8%–1.5%. Not zero, not stuffed.

### Secondary keywords
- 2–4 related terms
- Appear in at least one H2/H3 each
- Can be variations, synonyms, long-tail versions

### LSI / semantic keywords
- 5–15 terms related to primary topic
- Naturally distributed throughout body
- NOT forced — must read naturally

### LSI generation patterns
| Pattern | Example (Primary: "email marketing") |
|---------|--------------------------------------|
| Category parents/children | "digital marketing", "email campaigns", "newsletter marketing" |
| Tools/instruments | "email automation platform", "ESP", "bulk email service" |
| Actions/processes | "building email list", "writing subject lines", "A/B testing" |
| Problems/solutions | "low open rates", "high bounce rate", "spam filters" |
| People/roles | "email marketer", "copywriter", "subscriber" |
| Metrics/measurements | "open rate", "click-through rate", "conversion rate", "ROI" |
| Comparisons | "email vs social media", "HTML vs plain text email" |
| Questions | "what is email marketing", "how to build email list" |

### Keyword cannibalization
- **[POST-PUBLISH]** Verify no other page targets the same primary keyword
- If detected: merge pages, differentiate keywords, or set canonical

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
- Opening paragraph: hook + keyword within first 100–150 words
- Vary paragraph length: short-short-long-short creates visual rhythm

### Introduction pattern
1. Pattern interrupt (statistic, question, bold claim, story hook)
2. Pain point / problem recognition
3. Promise of solution
4. Keyword appears naturally within first 100–150 words

### Body pattern
- Each H2 section: clear point, evidence (data/example), keyword-adjacent language
- Alternate between: theory/explanation and concrete example/case
- Include at least one data point per 500 words
- Include at least one "surprising" or "contrarian" insight

### Conclusion pattern
- Do NOT regurgitate introduction
- Clear recommendation or next step
- CTA: specific action, not "learn more"
- Internal link to related content

---

## LINKING STRATEGY

### Internal links (3–10 per article)
- Link to 3–10 relevant internal pages
- Anchor text mix: partial match 30-40%, branded 20-25%, generic 20-25%, naked URL 5-10%, exact match ≤2
- No more than 2 exact-match keyword anchors
- Priority: link to cornerstone content and money pages
- Contextual (in-body) links > navigation links

### External links (2–5 per article)
- Link to authoritative sources (recognized publications, .edu, .gov)
- At least 1 DoFollow link to an external resource
- External links open in new tab (target="_blank" with rel="noopener")
- Cite data sources, studies, tools, original research
- No links to direct competitors unless comparing/reviewing
- **[POST-PUBLISH]**: Verify link quality and check for broken links

### Link placement
- First link within first 300 words
- Links distributed throughout (not clustered)
- Avoid "link dumping" at the end

---

## TECHNICAL SEO

### Meta title
- 50–60 chars (per-language limits below in LANGUAGE RESOURCES)
- Primary keyword near beginning
- Brand at end with separator: ` | Brand` or ` - Brand`
- Unique per page
- Power words used when natural
- Numbers preferred: "7 Ways..." over "Ways..."

### Meta description
- 145–158 chars (per-language limits below)
- Primary keyword within first 20 words
- Active voice, concrete value proposition
- No "We offer..." or "In this article..."
- Unique per page

### URL slug
- ≤75 characters
- Contains primary keyword
- Hyphens between words (never underscores)
- No stop words (see stop words per language below)
- No dates unless intentionally evergreen-dated
- No special characters

### Image SEO
- Alt text: descriptive, contains keyword for at least 1 image, ≤125 characters
- File name: descriptive, hyphens, keyword-rich
- Format: reference optimal formats (WebP > PNG > JPEG for web)

### Schema markup
- **[POST-PUBLISH]** Verify schema on live page using Google Rich Results Test
- Article → Article schema | Product → Product schema | FAQ → FAQPage schema
- HowTo → HowTo schema | Review → Review schema | BreadcrumbList → Navigation breadcrumbs

---

## POST-GENERATION VALIDATION

RankWise includes a **Python validator** (`validator/metrics.py`) that computes objective SEO metrics deterministically. Use it to verify content after generation — the LLM focuses on writing quality and structure; the validator handles exact measurements.

### When to Validate
1. **After content generation** — verify keyword density, word count, readability, passive voice, transition words, sentence variety
2. **After rewrite** — verify metrics improved vs. original
3. **Before audit** — get objective data before the LLM interprets results

### Validation Commands

```bash
# Full metrics report
python -m validator.cli --file content.md --keyword "your keyword" --title "Your SEO Title" --meta "Meta description" --lang en

# Checklist scores only (16 of 49 factors)
python -m validator.cli --file content.md --keyword "your keyword" --title "Your Title" --meta "Description" --lang en --checklist

# JSON output for programmatic use
python -m validator.cli --file content.md --keyword "your keyword" --title "Your Title" --meta "Description" --lang en --checklist --json
```

### Validator Coverage (16 factors)
The Python validator computes: **K1, K2, K6, K7, K10, C1, C2, C5, C6, C8, C9, C10, C11, C12, T3, T4**

These are the factors where exact numeric measurement matters. Remaining factors (linking, heading hierarchy, advanced signals, etc.) are evaluated by the LLM.

### Pipeline Workflow
```
1. User requests SEO content
2. LLM generates content following RankWise rules
3. LLM outputs content + validation command
4. User runs Python validator (optional but recommended)
5. If metrics are off: user feeds validator output back to LLM → LLM applies targeted fixes
6. [POST-PUBLISH] User verifies web-dependent factors on live site
```

### LLM Instructions for Validation
- After generating content, **always append the validation command** with the correct keyword, title, meta, and language
- When audit mode detects issues in factors covered by the validator, recommend: "Run validator to get exact measurements, then feed results back for targeted fixes"
- Do NOT claim exact numeric values (density %, passive %, transition %) unless you have validator output. Use qualitative language: "keyword appears well-distributed", "mostly active voice", "transitions present at key turns"

---

## LANGUAGE RESOURCES — All 9 Languages (Inline)

Every word list, rule, and parameter for all 9 supported languages is provided below. No external files needed.

---

### ENGLISH (en)

#### Power Words (≥2 per title)
proven, secret, stop, simple, exclusive, limited, hidden, surprising, shocking, unexpected, amazing, incredible, ultimate, essential, critical, guaranteed, instant, immediate, automatic, effortless, breakthrough, insider, revealed, mistake, warning, never, avoid, dangerous, risk, urgent, little-known, unknown, unconventional, tested, research-backed, data-driven, expert, science-based, actual, real, exact, specific, step-by-step, definitive, powerful, effective

#### Transition Words (use at logical turning points)
however, therefore, because, although, specifically, for example, for instance, in contrast, similarly, consequently, notably, meanwhile, furthermore, moreover, additionally, nevertheless, nonetheless, otherwise, instead, accordingly, hence, thus, in addition, on the other hand, as a result, in particular, in conclusion, to summarize, first, second, third, finally, next, then, also, besides, indeed, in fact, of course, certainly, surely, undoubtedly, regardless, despite, even though, while, whereas

#### Stop Words (remove from URL slugs)
the, a, an, and, or, but, in, on, at, to, for, of, with, by, from, up, about, into, through, during, before, after, above, below, between, is, are, was, were, be, been, being, have, has, do, does, did, will, would, can, could, may, might, must, shall, should, not, no

#### Burned Words (AI markers — delete on sight in Rewrite mode)

**Universal:** leverage, utilize, harness, empower, facilitate, optimize, streamline, revolutionize, transform (generic), robust, seamless, cutting-edge, best-in-class, game-changer, next-level, innovative (unproven), holistic, ecosystem, dynamic, synergy, granular, scalable (without specifics)

**Empty intensifiers:** very, extremely, incredibly, amazingly, truly, really, absolutely, completely, thoroughly, highly, remarkably

**Throat-clearing openers:** In today's, In the modern, In an era, The landscape of, With the rise of, As we navigate, In the ever-evolving, It goes without saying, In recent years, The world of, Nowadays, In the age of

**Conclusion regurgitation:** In conclusion, To summarize, In summary, To wrap up, As we have seen, Overall, In closing, To sum up, The bottom line, At the end of the day

**Fake transitions:** Moreover, Furthermore, Additionally, Consequently, Thus, Hence, It should be noted that, It is important to note, It is worth mentioning, Needless to say, On one hand... on the other hand

**Hedging:** It could be argued that, One might say, Some research suggests, There is evidence to suggest, It is possible that, Arguably, Generally speaking, For the most part

**Rhetorical question padding:** What does this mean for you?, Sounds good right?, Want to know the best part?, But what about X?, So how does it work?, Ready to get started?

**SEO-specific AI tells:** "A comprehensive guide to...", "In this article, we will explore...", "Whether you're a beginner or an expert...", "Read on to learn more...", "Without further ado..."

**Replacement rule:** Do not find a synonym. Describe the actual action or quality.

**Replacement examples:**
- "leverages AI to optimize workflow" → "uses a model trained on support tickets to cut response time"
- "robust security" → "passes SOC 2 audit annually"
- "seamless integration" → "connects to your tools in 3 clicks"

#### Readability Target
- **Flesch-Kincaid Grade:** 7–9 (general audience), 10–12 (technical)
- **Flesch Reading Ease:** 50–70
- **Meta title:** 50–60 chars | **Meta description:** 145–158 chars

---

### RUSSIAN (ru) / Русский

#### Power Words
доказано, секрет, просто, эксклюзив, скрытый, неожиданный, удивительный, шокирующий, гарантировано, мгновенно, автоматически, без усилий, прорыв, инсайдер, раскрыто, ошибка, предупреждение, никогда, избегайте, опасный, риск, срочно, малоизвестный, нестандартный, протестировано, эксперт, реальный, точный, конкретный, пошаговый, мощный, эффективный, бесплатно, проверенный, научно, исследование, данные

**Страх/Потери:** перестаньте, избегайте, никогда, ошибка, скрытый, опасный, теряете, риск, срочно, пока не поздно, о чём молчат, убивает ваш
**Любопытство:** секрет, малоизвестный, неожиданный, нестандартный, за кулисами, инсайдер, эксклюзив, раскрыто, правда о, вы не поверите
**Авторитет:** доказано, исследование, научно обосновано, данные подтверждают, эксперт, протестировано, гарантировано
**Лёгкость:** просто, легко, быстро, мгновенно, автоматически, без усилий, за минуты, пошагово, наконец-то
**Эксклюзивность:** эксклюзив, ограниченный, только, избранный, премиум, приватный, впервые, ранний доступ

#### Transition Words
однако, поэтому, так как, хотя, например, в частности, в то же время, кроме того, следовательно, тем не менее, в отличие от, в результате, также, потому что, несмотря на, вместо, в первую очередь, во-первых, во-вторых, наконец, прежде всего, в целом

#### Stop Words
и, в, на, с, по, к, от, из, о, об, за, до, для, без, над, под, при, про, у, через, или, но, а, не, ни, бы, ли, же, то, что, как, так, это

#### Burned Words (AI markers)
оптимизировать, интегрировать, трансформировать, масштабировать, инновационный, комплексный подход, в рамках, данный, являться (as copula), осуществлять, посредством, эффективные решения, передовые технологии, уникальная методология, ключевой фактор, синергия

**Empty intensifiers:** очень, крайне, чрезвычайно, невероятно, действительно, абсолютно, полностью, весьма, исключительно
**Openers:** В современном, В сегодняшнем, В эпоху, В условиях, В мире где, В настоящее время, На сегодняшний день, С развитием, В последние годы
**Conclusion regurgitation:** В заключение, Подводя итог, Таким образом, Итак, Резюмируя, В завершение, В итоге
**Fake transitions:** Более того, Кроме того, Помимо этого, Следует отметить, Необходимо подчеркнуть, Важно понимать
**Hedging:** Можно сказать что, Возможно, Вероятно, Как правило, В большинстве случаев, Существует мнение
**SEO-specific:** «В данной статье мы рассмотрим...» → удалить; «Комплексный подход к...» → удалить

**Replacement examples:**
- «оптимизирует процессы» → «сокращает время согласования с трёх дней до четырёх часов»
- «инновационный подход» → «мы попробовали метод, который никто в нашей нише не использовал»

#### Readability Target
- **Formula:** Flesch Reading Ease (адаптированная): 50–70
- **Yandex note:** penalizes over-optimization harder. Density closer to 0.5%–1%.
- **Meta title:** 55–70 chars | **Meta description:** 140–160 chars

---

### UKRAINIAN (uk) / Українська

#### Power Words
доведено, секрет, просто, ексклюзив, прихований, несподіваний, дивовижний, шокуючий, гарантовано, миттєво, автоматично, без зусиль, прорив, інсайдер, розкрито, помилка, попередження, ніколи, уникайте, небезпечний, ризик, терміново, маловідомий, нестандартний, протестовано, експерт, реальний, точний, конкретний, покроковий, потужний, ефективний, безкоштовно, перевірений, науково, дослідження, дані

**Страх/Втрати:** перестаньте, уникайте, ніколи, помилка, прихований, небезпечний, втрачаєте, ризик, терміново, поки не пізно, про що мовчать, вбиває ваш
**Цікавість:** секрет, маловідомий, невідомий, несподіваний, нестандартний, за лаштунками, інсайдер, ексклюзив, розкрито, правда про, ви не повірите, справжня причина
**Авторитет:** доведено, дослідження, науково обґрунтовано, дані підтверджують, експерт, протестовано, гарантовано
**Легкість:** просто, легко, швидко, миттєво, автоматично, без зусиль, за хвилини, покроково, нарешті, кожен зможе
**Ексклюзивність:** ексклюзив, обмежений, тільки, обраний, преміум, приватний, за запрошенням, вперше, ранній доступ

#### Transition Words
однак, тому, через те що, хоча, наприклад, зокрема, водночас, крім того, отже, тим не менш, на відміну від, у результаті, також, бо, тому що, попри, замість, по-перше, по-друге, нарешті, передусім, загалом, завдяки, внаслідок

#### Stop Words
і, й, та, в, у, на, з, до, для, без, над, під, при, про, через, або, але, не, ні, би, ж, що, як, це, від, по, за, перед

#### Burned Words (AI markers)
оптимізувати, інтегрувати, трансформувати, масштабувати, інноваційний, комплексний підхід, в рамках, даний, являтися, здійснювати, ефективні рішення, передові технології, унікальна методологія, ключовий фактор, синергія, потужний інструмент

**Empty intensifiers:** дуже, надзвичайно, неймовірно, дійсно, абсолютно, повністю, цілком, вельми, винятково
**Openers:** У сучасному, В умовах, У світі де, На сьогоднішній день, В епоху, З розвитком, В останні роки, Сучасний світ
**Conclusion regurgitation:** На завершення, Підсумовуючи, Отже, Таким чином, Підводячи підсумок, У підсумку
**Fake transitions:** Більш того, Крім того, Окрім цього, Слід зазначити, Важливо підкреслити, Варто відзначити
**Hedging:** Можна сказати що, Можливо, Ймовірно, Як правило, У більшості випадків, Існує думка
**Russianisms to avoid:** «із-за» → «через», «так як» → «бо»/«тому що», «приймати участь» → «брати участь», «даний»/«являтися»/«здійснювати» → replace with natural Ukrainian

**Replacement examples:**
- «оптимізує процеси» → «скорочує час погодження з трьох днів до чотирьох годин»
- «інноваційний підхід» → «ми спробували метод, який ніхто в нашій ніші не використовував»

#### Readability Target
- **Formula:** LIX 30–45
- **Google dominates (~95%)** — Ukrainian queries longer and more conversational
- **Meta title:** 55–70 chars | **Meta description:** 140–160 chars

---

### GERMAN (de) / Deutsch

#### Power Words
bewährt, geheim, einfach, exklusiv, versteckt, überraschend, schockierend, erstaunlich, garantiert, sofort, automatisch, mühelos, durchbruch, insider, enthüllt, fehler, warnung, niemals, vermeiden, gefährlich, risiko, dringend, unbekannt, getestet, experte, wissenschaftlich, datengestützt, echt, genau, spezifisch, schrittweise, kraftvoll, effektiv

**Angst/Verlust:** Stopp, vermeiden, niemals, Fehler, versteckt, gefährlich, verlieren, Risiko, dringend, bevor es zu spät ist, was niemand erzählt, zerstört Ihr
**Neugier:** Geheimnis, wenig bekannt, unbekannt, überraschend, schockierend, ungewöhnlich, hinter den Kulissen, Insider, exklusiv, enthüllt, die Wahrheit über
**Autorität:** bewährt, forschungsbasiert, wissenschaftlich, datengestützt, Experte, getestet, garantiert, laut Forschung
**Einfachheit:** einfach, schnell, sofort, automatisch, mühelos, ohne, in Minuten, Schritt für Schritt, endlich, jeder kann
**Exklusivität:** exklusiv, limitiert, nur, Premium, Elite, privat, auf Einladung, zum ersten Mal, frühzeitiger Zugang

#### Transition Words
jedoch, deshalb, weil, obwohl, zum Beispiel, insbesondere, darüber hinaus, daher, dennoch, im Gegensatz dazu, infolgedessen, außerdem, schließlich, zuerst, zweitens, drittens, trotzdem, stattdessen, auch, zudem, allerdings

#### Stop Words
der, die, das, den, dem, des, ein, eine, einer, in, auf, mit, von, zu, für, an, bei, aus, nach, über, vor, durch, um, gegen, zwischen, oder, und, aber, nicht, auch, noch, nur, schon, so, wie, als, am, im, ins, zum, zur

#### Burned Words (AI markers)
optimieren, integrieren, transformieren, skalieren, innovativ, ganzheitlich, nahtlos, robust, modernste, revolutionär, wegweisend, Synergie, Ökosystem, dynamisch, skalierbar, umfassende Lösung, state-of-the-art, Best-in-Class, Game-Changer

**Empty intensifiers:** sehr, extrem, unglaublich, erstaunlich, wirklich, absolut, vollkommen, vollständig, äußerst, bemerkenswert
**Openers:** In der heutigen digitalen Welt, Im Zeitalter der, In der modernen, Mit dem Aufkommen von, Heutzutage
**Conclusion regurgitation:** Zusammenfassend, Abschließend, Zusammenfassend lässt sich sagen, Im Fazit, Schlussendlich
**Fake transitions:** Darüber hinaus, Außerdem, Des Weiteren, Ferner, Hinzu kommt, Es ist wichtig zu beachten
**Hedging:** Man könnte argumentieren dass, Einige schlagen vor, Es gibt Hinweise darauf, Es ist möglich dass, Im Allgemeinen
**AI-specific:** Nominalstil (Durchführung einer Optimierung → optimieren), Passive (Es wird empfohlen → active), English loanwords (getriggert, geboostet)

#### Readability Target
- **Formula:** Wiener Sachtextformel Grade 4–10
- **Compound nouns** common — count accordingly
- **Meta title:** 50–65 chars | **Meta description:** 145–158 chars

---

### FRENCH (fr) / Français

#### Power Words
prouvé, secret, simple, exclusif, caché, surprenant, choquant, incroyable, garanti, instant, automatique, sans effort, percée, initié, révélé, erreur, avertissement, jamais, éviter, dangereux, risque, urgent, inconnu, testé, expert, scientifique, réel, exact, spécifique, étape par étape, puissant, efficace

**Peur/Perte:** arrêtez, évitez, jamais, erreur, caché, dangereux, perdez, risque, urgent, avant qu'il ne soit trop tard, ce que personne ne dit
**Curiosité:** secret, peu connu, inconnu, surprenant, choquant, inhabituel, en coulisses, initié, exclusif, révélé, la vérité sur, la vraie raison
**Autorité:** prouvé, basé sur la recherche, scientifique, fondé sur les données, expert, testé, garanti, selon une étude
**Simplicité:** simple, facile, rapide, instantanément, automatiquement, sans effort, en minutes, étape par étape, enfin, tout le monde peut
**Exclusivité:** exclusif, limité, seulement, premium, élite, privé, sur invitation, pour la première fois, accès anticipé

#### Transition Words
cependant, donc, parce que, bien que, par exemple, en particulier, de plus, par conséquent, néanmoins, en revanche, ainsi, également, malgré, au lieu de, d'abord, ensuite, enfin, pourtant, toutefois, en effet, d'une part, d'autre part, en outre

#### Stop Words
le, la, les, un, une, des, de, du, à, au, aux, en, sur, dans, par, pour, avec, sans, sous, entre, et, ou, mais, ne, pas, plus, moins, très, tout, comme, que, qui, quoi, dont, où

#### Burned Words (AI markers)
optimiser, intégrer, transformer, évolutif, innovant, holistique, transparent, robuste, de pointe, révolutionnaire, synergie, écosystème, dynamique, granulaire, solution complète, disruptif, levier, catalyseur, excellence opérationnelle

**Empty intensifiers:** très, extrêmement, incroyablement, véritablement, vraiment, absolument, totalement, complètement, remarquablement
**Openers:** Dans le monde numérique d'aujourd'hui, À l'ère du, Dans le paysage actuel, Avec l'avènement de, De nos jours
**Conclusion regurgitation:** En conclusion, Pour résumer, En résumé, Pour conclure, En définitive, Au final, En somme
**Fake transitions:** De plus, En outre, Par ailleurs, Il est important de noter, Il convient de souligner, Il faut mentionner
**Hedging:** On pourrait dire que, Certains suggèrent, Il est possible que, Généralement parlant, Dans la plupart des cas
**AI-specific:** Excessive «en termes de», «dans le cadre de», «en matière de»; Nominalization → active verb

#### Readability Target
- **Formula:** Flesch Reading Ease 50–70
- **Accented characters** count as 1 char in SERP
- **Meta title:** 50–63 chars | **Meta description:** 145–158 chars

---

### SPANISH (es) / Español

#### Power Words
probado, secreto, simple, exclusivo, oculto, sorprendente, impactante, increíble, garantizado, instantáneo, automático, sin esfuerzo, revelación, insider, revelado, error, advertencia, nunca, evitar, peligroso, riesgo, urgente, desconocido, experto, científico, real, exacto, específico, paso a paso, poderoso, eficaz

**Miedo/Pérdida:** deja de, evita, nunca, error, oculto, peligroso, pierde, riesgo, urgente, antes de que sea tarde, lo que nadie te dice
**Curiosidad:** secreto, poco conocido, desconocido, sorprendente, impactante, inusual, detrás de escena, insider, exclusivo, revelado, la verdad sobre, la verdadera razón
**Autoridad:** probado, basado en investigación, científico, basado en datos, experto, comprobado, garantizado, según estudio
**Simplicidad:** simple, fácil, rápido, instantáneamente, automáticamente, sin esfuerzo, en minutos, paso a paso, por fin, cualquiera puede
**Exclusividad:** exclusivo, limitado, solo, premium, élite, privado, por invitación, por primera vez, acceso anticipado

#### Transition Words
sin embargo, por lo tanto, porque, aunque, por ejemplo, en particular, además, por consiguiente, no obstante, en contraste, asimismo, también, a pesar de, en lugar de, primero, segundo, tercero, finalmente, entonces, pues, en cambio, en resumen, es decir

#### Stop Words
el, la, los, las, un, una, unos, unas, de, del, a, al, en, por, para, con, sin, sobre, entre, y, e, o, u, pero, no, ni, que, cual, como, más, muy, tan, todo, esta, este, esto

#### Burned Words (AI markers)
optimizar, integrar, transformar, escalable, innovador, holístico, sin fisuras, robusto, de vanguardia, revolucionario, sinergia, ecosistema, dinámico, granular, solución integral, disruptivo, palanca, empoderar, facilitar

**Empty intensifiers:** muy, extremadamente, increíblemente, verdaderamente, realmente, absolutamente, totalmente, completamente, notablemente
**Openers:** En el mundo digital actual, En la era de, En el panorama actual, Con el auge de, Hoy en día, En la actualidad
**Conclusion regurgitation:** En conclusión, Para resumir, En resumen, Para concluir, En definitiva, A modo de cierre, En síntesis
**Fake transitions:** Además, Asimismo, Por otra parte, Cabe destacar, Es importante señalar, Merece la pena mencionar
**Hedging:** Se podría decir que, Algunos sugieren, Es posible que, Por lo general, En la mayoría de los casos

#### Readability Target
- **Formula:** Fernández-Huerta 50–70 (0–100, higher = easier)
- **Meta title:** 50–63 chars | **Meta description:** 145–158 chars

---

### PORTUGUESE (pt) / Português

#### Power Words
comprovado, segredo, simples, exclusivo, escondido, surpreendente, chocante, incrível, garantido, instantâneo, automático, sem esforço, revelação, revelado, erro, aviso, nunca, evitar, perigoso, arriscado, urgente, desconhecido, testado, especialista, científico, real, exato, específico, passo a passo, poderoso, eficaz

**Medo/Perda:** pare, evite, nunca, erro, escondido, perigoso, perde, arriscado, urgente, antes que seja tarde, o que ninguém conta
**Curiosidade:** segredo, pouco conhecido, desconhecido, surpreendente, chocante, incomum, nos bastidores, exclusivo, revelado, a verdade sobre, a verdadeira razão
**Autoridade:** comprovado, baseado em pesquisa, científico, baseado em dados, especialista, testado, garantido, segundo estudo
**Simplicidade:** simples, fácil, rápido, instantaneamente, automaticamente, sem esforço, em minutos, passo a passo, finalmente, qualquer um pode
**Exclusividade:** exclusivo, limitado, apenas, premium, elite, privado, por convite, pela primeira vez, acesso antecipado
**Emoções:** amo, odeio, incrível, honestamente, pessoalmente, minha história, como eu, eu estava errado, isso mudou minha vida

#### Transition Words
no entanto, portanto, porque, embora, por exemplo, em particular, além disso, consequentemente, apesar disso, por outro lado, também, primeiro, segundo, finalmente, então, assim, dessa forma, em vez de, apesar de, pois, em contrapartida, em resumo, ou seja

#### Stop Words
o, a, os, as, um, uma, uns, umas, de, do, da, dos, das, em, no, na, nos, nas, por, para, com, sem, sobre, entre, e, ou, mas, não, nem, que, qual, como, mais, muito, tão, todo, todos

#### Burned Words (AI markers)
otimizar, integrar, transformar, escalável, inovador, holístico, transparente, robusto, de ponta, revolucionário, sinergia, ecossistema, dinâmico, granular, solução abrangente, disruptivo, potencializar, empoderar, alavancar

**Empty intensifiers:** muito, extremamente, incrivelmente, verdadeiramente, realmente, absolutamente, totalmente, completamente, notavelmente
**Openers:** No mundo digital de hoje, Na era de, No cenário atual, Com o surgimento de, Hoje em dia, Atualmente
**Conclusion regurgitation:** Em conclusão, Para resumir, Em resumo, Para concluir, Em suma, Resumindo, Em síntese
**Fake transitions:** Além disso, Ademais, Por outro lado, É importante notar, Vale ressaltar, Cabe destacar
**Hedging:** Pode-se dizer que, Alguns sugerem, É possível que, Em geral, Na maioria dos casos

#### Readability Target
- **Formula:** Flesch Reading Ease 50–70
- **Brazilian vs European:** same SERP limits
- **Meta title:** 50–63 chars | **Meta description:** 145–158 chars

---

### ITALIAN (it) / Italiano

#### Power Words
provato, segreto, semplice, esclusivo, nascosto, sorprendente, scioccante, incredibile, garantito, istantaneo, automatico, senza sforzo, svolta, rivelato, errore, avvertimento, mai, evitare, pericoloso, rischioso, urgente, sconosciuto, testato, esperto, scientifico, reale, esatto, specifico, passo dopo passo, potente, efficace

**Paura/Perdita:** smetti, evita, mai, errore, nascosto, pericoloso, perdi, rischioso, urgente, prima che sia troppo tardi, ciò che nessuno dice
**Curiosità:** segreto, poco conosciuto, sconosciuto, sorprendente, scioccante, insolito, dietro le quinte, esclusivo, rivelato, la verità su, la vera ragione
**Autorità:** provato, basato sulla ricerca, scientifico, basato sui dati, esperto, testato, garantito, secondo uno studio
**Semplicità:** semplice, facile, veloce, istantaneamente, automaticamente, senza sforzo, in minuti, passo dopo passo, finalmente, chiunque può
**Esclusività:** esclusivo, limitato, solo, premium, élite, privato, su invito, per la prima volta, accesso anticipato
**Emozioni:** amo, odio, incredibile, onestamente, personalmente, la mia storia, come ho, mi sbagliavo, mi ha cambiato la vita

#### Transition Words
tuttavia, quindi, perché, sebbene, per esempio, in particolare, inoltre, di conseguenza, nonostante, al contrario, anche, primo, secondo, infine, dunque, pertanto, invece, malgrado, cioè, ovvero, infatti, d'altra parte, in sintesi

#### Stop Words
il, lo, la, i, gli, le, un, uno, una, di, a, da, in, con, su, per, tra, fra, e, o, ma, non, né, che, chi, cui, come, più, molto, tanto

#### Burned Words (AI markers)
ottimizzare, integrare, trasformare, scalabile, innovativo, olistico, senza soluzione di continuità, robusto, all'avanguardia, rivoluzionario, sinergia, ecosistema, dinamico, granulare, soluzione completa, disruptivo, potenziare, facilitare, sfruttare

**Empty intensifiers:** molto, estremamente, incredibilmente, veramente, realmente, assolutamente, totalmente, completamente, notevolmente
**Openers:** Nel mondo digitale di oggi, Nell'era del, Nel panorama attuale, Con l'avvento di, Al giorno d'oggi, Oggigiorno
**Conclusion regurgitation:** In conclusione, Per riassumere, In sintesi, Per concludere, In definitiva, Tirando le somme
**Fake transitions:** Inoltre, Per di più, D'altra parte, È importante notare, Vale la pena sottolineare, Si rende necessario evidenziare
**Hedging:** Si potrebbe dire che, Alcuni suggeriscono, È possibile che, In generale, Nella maggior parte dei casi
**AI-specific:** Excessive «si passivante» → active voice; «Si rende necessario» → kill

#### Readability Target
- **Formula:** Gulpease 40–80 (higher = easier)
- **Relatively compact** — stick to lower end of range
- **Meta title:** 50–63 chars | **Meta description:** 145–158 chars

---

### POLISH (pl) / Polski

#### Power Words
sprawdzony, sekret, prosty, ekskluzywny, ukryty, zaskakujący, szokujący, niesamowity, gwarantowany, natychmiast, automatyczny, bez wysiłku, przełom, ujawniony, błąd, ostrzeżenie, nigdy, unikaj, niebezpieczny, ryzykowny, pilne, nieznany, przetestowany, ekspert, naukowy, prawdziwy, dokładny, konkretny, krok po kroku, skuteczny

**Strach/Strata:** przestań, unikaj, nigdy, błąd, ukryty, niebezpieczny, tracisz, ryzykowny, pilne, zanim będzie za późno, o czym nikt nie mówi
**Ciekawość:** sekret, mało znany, nieznany, zaskakujący, szokujący, niezwykły, za kulisami, ekskluzywny, ujawniony, prawda o, prawdziwy powód
**Autorytet:** sprawdzony, oparty na badaniach, naukowy, oparty na danych, ekspert, przetestowany, gwarantowany, według badań
**Prostota:** prosty, łatwy, szybki, natychmiast, automatycznie, bez wysiłku, w kilka minut, krok po kroku, wreszcie, każdy może
**Ekskluzywność:** ekskluzywny, limitowany, tylko, premium, elitarny, prywatny, na zaproszenie, po raz pierwszy, wczesny dostęp
**Emocje:** kocham, nienawidzę, niesamowite, szczerze, osobiście, moja historia, jak ja, myliłem się, to zmieniło moje życie

#### Transition Words
jednak, dlatego, ponieważ, chociaż, na przykład, w szczególności, ponadto, w rezultacie, niemniej jednak, natomiast, również, po pierwsze, po drugie, wreszcie, zatem, więc, mimo, zamiast, czyli, to znaczy, w przeciwieństwie, podsumowując, przede wszystkim

#### Stop Words
w, na, z, do, po, za, przez, dla, przy, nad, pod, przed, między, i, oraz, lub, albo, ale, nie, tak, jak, to, ten, ta, te, się, już, jeszcze, tylko, bardzo

#### Burned Words (AI markers)
optymalizować, integrować, transformować, skalowalny, innowacyjny, holistyczny, solidny, najnowocześniejszy, rewolucyjny, przełomowy, synergia, ekosystem, dynamiczny, kompleksowe rozwiązanie, disruptywny, wykorzystywać, umożliwiać, usprawniać

**Empty intensifiers:** bardzo, niezwykle, niesamowicie, naprawdę, absolutnie, całkowicie, kompletnie, wyjątkowo, nadzwyczaj, znacząco
**Openers:** W dzisiejszym cyfrowym świecie, W erze, W obecnym krajobrazie, Wraz z rozwojem, W dzisiejszych czasach, Obecnie, W dobie
**Conclusion regurgitation:** Podsumowując, Reasumując, Na zakończenie, W konkluzji, Podsumowując powyższe, W podsumowaniu
**Fake transitions:** Ponadto, Co więcej, Dodatkowo, Warto zauważyć, Należy podkreślić, Trzeba wspomnieć
**Hedging:** Można powiedzieć że, Niektórzy sugerują, Jest możliwe że, Ogólnie rzecz biorąc, W większości przypadków
**AI-specific:** English calques (dedykowany, serwis → replace with native), Należy zauważyć/Warto podkreślić → kill

#### Readability Target
- **Formula:** FOG-PL Grade 7–12
- **Polish declensions** can create longer words
- **Meta title:** 50–65 chars | **Meta description:** 145–158 chars

---

## POWER WORDS & SENTIMENT

### Categories
| Category | Effect | Examples |
|----------|--------|----------|
| Fear/Loss | Urgency, attention | "Stop losing", "Don't risk", "Hidden", "Mistake", "Warning" |
| Curiosity | Click-through | "Secret", "Little-known", "Unconventional", "What nobody tells you" |
| Authority | Trust | "Proven", "Research-backed", "Science-based", "Expert", "Data-driven" |
| Ease/Convenience | Desire | "Simple", "Instantly", "Without", "No [pain point]", "Automatic" |
| Exclusivity | Status | "Exclusive", "Limited", "Only", "Insider", "Behind the scenes" |
| Specificity | Credibility | Numbers, percentages, dollar amounts, timeframes |

### Sentiment Requirement
- Every SEO title should have a clear sentiment polarity — positive OR negative
- Neutral titles = missed opportunity for emotional CTR boost
- Negative: "Stop", "Avoid", "Never", "Mistake", "Warning"
- Positive: "Best", "Proven", "Ultimate", "Love", "Successful", "Powerful"

---

## LANGUAGE ADAPTATION

Key differences by language (full data inline above):

| Language | Title (chars) | Description (chars) | Readability Target | Key Note |
|----------|--------------|---------------------|-------------------|----------|
| EN | 50–60 | 145–158 | FK Grade 7–9 | Default language |
| RU | 55–70 | 140–160 | FRE 50–70 | Cyrillic wider; Yandex penalizes over-optimization |
| UK | 55–70 | 140–160 | LIX 30–45 | Google dominates; avoid Russianisms |
| DE | 50–65 | 145–158 | WSTF 4–10 | Compound nouns common; avoid Nominalstil |
| FR | 50–63 | 145–158 | FRE 50–70 | Accents count as 1 char |
| ES | 50–63 | 145–158 | FH 50–70 | Fernández-Huerta formula |
| PT | 50–63 | 145–158 | FRE 50–70 | Brazilian vs European same limits |
| IT | 50–63 | 145–158 | Gulpease 40–80 | Relatively compact language |
| PL | 50–65 | 145–158 | FOG-PL 7–12 | Declensions create longer words |

### Cross-language optimization
When source language differs from requested output language:
- Apply keyword rules and density targets of the TARGET language
- Apply burned-word filters of the TARGET language
- Apply readability targets of the TARGET language
- Preserve factual claims regardless of language
- Flag if source keyword doesn't translate cleanly — recommend local keyword research

---

## QUICK START

**Full package (article + meta + alts):**
> "Write an SEO article about [topic]. Primary keyword: [keyword]. Language: en."

**Article only:**
> "Just the article text about [topic]. No meta. Keyword: [keyword]."

**Meta tags only:**
> "Generate meta title and description for [page topic]. Focus keyword: [keyword]."

**Full SEO audit:**
> "Audit this content for SEO: [paste text]. Focus keyword: [keyword]."

**Audit + rewrite:**
> "Audit this content, then rewrite it with SEO fixes. Keyword: [keyword]."

**Content brief:**
> "Create an SEO content brief for [topic]. Target keyword: [keyword]."

**After generation, validate:**
```bash
python -m validator.cli --file content.md --keyword "keyword" --title "Title" --meta "Description" --lang en --checklist
```

---

## FILES IN THIS SKILL

```
rankwise/
├── SKILL.md                        ← THIS FILE — orchestrator, all data inline
├── README.md / README.ru.md        ← Documentation (bilingual)
├── CHANGELOG.md                    ← Version history
├── LICENSE                         ← MIT | Copyright Yevhen Leonidov
├── shared/                         ← Reference data (for human maintainers)
│   ├── checklist.md                ← 49 SEO factors with thresholds and fixes
│   ├── keyword-rules.md            ← Extended keyword strategy
│   ├── power-words.md              ← Extended power words with examples
│   ├── schema-templates.md         ← JSON-LD structured data templates
│   ├── readability-params.md       ← Detailed readability parameters
│   ├── burned-words.md             ← Extended AI detection patterns
│   └── link-strategy.md            ← Internal/external linking rules
├── scenarios/                      ← Workflow playbooks per mode/content type
├── examples/                       ← Annotated before/after demonstrations
├── validator/                      ← Python CLI — deterministic metrics (16/49 factors)
└── benchmarks/                     ← 5 reference texts for regression testing
```

This SKILL.md contains all core rules and complete language word lists for all 9 supported languages inline. The `shared/` directory contains extended reference data for human maintainers — not required for AI execution.
