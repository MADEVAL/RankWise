# SEO Checklist - 49 Ranking Factors
> **Version:** 1.2.1

> Complete scoring matrix with thresholds, severity levels, and fix instructions.
> Used by RankWise in Generate, Rewrite, and Audit modes.

---

## KEYWORD PLACEMENT (K1–K12)

| # | Factor | Target | Severity | Fix If Failing |
|---|--------|--------|----------|----------------|
| K1 | Focus keyword set | Must be present | CRITICAL | Define one primary keyword for the page. One page = one keyword. |
| K2 | Keyword in SEO title | Must appear | CRITICAL | Edit the SEO title to include the keyword. Keep it near the beginning. |
| K3 | Keyword near title beginning | First 3–5 words | HIGH | Move keyword closer to start. Swap with filler words. |
| K4 | Keyword in meta description | Within first 20 words | CRITICAL | Rewrite description, placing keyword in the opening clause. |
| K5 | Keyword in URL slug | Present, near front | HIGH | Edit slug: remove stop words, place keyword at or near the beginning. |
| K6 | Keyword at content start | First 100–150 words | HIGH | Rewrite opening paragraph to naturally include keyword. |
| K7 | Keyword in content body | Naturally distributed (4-8 times per 1000 words) | CRITICAL | Add keyword instances where they fit naturally. Vary with synonyms. |
| K8 | Keyword in subheadings | At least 1 H2 or H3 | HIGH | Find the most relevant H2 - add keyword if it fits the section topic. |
| K9 | Keyword as image alt text | At least 1 image | MEDIUM | Choose the most relevant image - add keyword to its alt text naturally. |
| K10 | Keyword density | 0.8%–1.5%, not 0%, not >3% | HIGH | Below 0.8%: add keyword instances. Above 3%: replace some with synonyms/pronouns. |
| K11 | Keyword cannibalization | No other page targets same primary keyword | HIGH | Check `site:yoursite.com "keyword"`. If multiple pages: merge, differentiate, or canonicalize. See `shared/keyword-rules.md` Cannibalization section. |
| K12 | Keyword length | 3+ characters, ≤7 words | MEDIUM | Too short (<3 chars): too generic. Too long (>7 words): unnatural. Pick a 2–5 word keyword phrase. |

---

## CONTENT QUALITY (C1–C14)

| # | Factor | Target | Severity | Fix If Failing |
|---|--------|--------|----------|----------------|
| C1 | Word count | 600+ minimum, 1500+ competitive | HIGH | Expand thin sections. Add examples, data, step-by-step detail, FAQ. |
| C2 | Short paragraphs | ≤3 sentences, ≤150 words each | MEDIUM | Break long paragraphs at logical transition points. |
| C3 | Images and/or videos | ≥1 per 300 words | MEDIUM | Add relevant images: screenshots, charts, infographics, photos. Embed videos where useful. |
| C4 | Table of Contents | For articles >800 words | LOW | Add TOC at top with anchor links to each H2. |
| C5 | Numbers in title | At least 1 number (odd preferred) | MEDIUM | Add a specific number: "7 Ways...", "How I Increased X by 40%", "3 Mistakes..." |
| C6 | Power words in title | ≥2 emotionally charged words | MEDIUM | Add power words from `shared/power-words.md`. Example: "Proven", "Stop", "Secret", "Simple". |
| C7 | Sentiment signal | Clear positive or negative polarity | LOW | Ensure title conveys emotion. Neutral = missed CTR opportunity. |
| C8 | Readability score | Grade 7–9 (EN) / equivalent per language | HIGH | Shorten long sentences. Replace complex words. Break dense paragraphs. |
| C9 | Passive voice ratio | ≤10% of sentences | MEDIUM | Convert passive to active: "was written by" → "wrote". |
| C10 | Transition words | ≥30% of sentences (EN); ≥25% other languages - see `shared/readability-params.md` | LOW | Add: "however", "because", "therefore", "for example", "specifically", "in contrast". |
| C11 | Sentence length variety | No 3 consecutive same-length (±2 words) | MEDIUM | Vary sentence length. Mix: short (2-5 words), medium (10-15), long (18-25). |
| C12 | Consecutive sentence starts | No 3 consecutive same first word | MEDIUM | Rewrite to vary openers: "The", "It", "This", "You", "When", "If", "Because", etc. |
| C13 | Heading hierarchy | H1→H2→H3 proper, no H2→H4 skip | HIGH | Fix hierarchy: insert missing H3 between H2 and H4. Ensure single H1. |
| C14 | Content-to-ad ratio | Main content dominates above-fold: first ~300 words contain ≤20% navigational/boilerplate content. Heuristic: count sentences that are ads, nav menus, sidebar widgets, or cookie banners vs. main content sentences. If ad/nav ratio >20% of first 300 words → ❌ Fail. If text-only view is unavailable → ⚠️ "Verify on rendered page." | MEDIUM | Push main content higher. Reduce ad density in first screen. |

---

## LINKING (L1–L9)

| # | Factor | Target | Severity | Fix If Failing |
|---|--------|--------|----------|----------------|
| L1 | Internal links | 3–10 links to own site | HIGH | Add contextual links to relevant pages. Aim for in-body links, not just nav. |
| L2 | External links | 2–5 links to authoritative sources | HIGH | Link to sources: studies, data, tools, recognized publications. Cite specific pages. |
| L3 | DoFollow external links | At least 1 of external links | MEDIUM | Ensure at least one external link has no `rel="nofollow"`. |
| L4 | Link anchor text variety | ≤2 exact-match anchors | MEDIUM | Vary anchor text. Mix: branded, partial match, generic ("read more"), naked URL. |
| L5 | Outbound link quality | Recognized authority: .edu, .gov, Wikipedia, HBR, major industry publications, or known trusted brands. If domain is unknown → score ⚠️ Warning (not ❌ Fail) unless it's a known spam/low-quality domain. Do not use arbitrary DA scores - verify by domain reputation instead. | MEDIUM | Check domain for .edu/.gov or known authority brands. If unknown → ⚠️ flag for manual verification. |
| L6 | No broken links | 0 broken outbound or internal links | HIGH | Check all links. Remove or replace broken ones. |
| L7 | Internal link relevance | Linked pages are topically related | MEDIUM | Ensure internal links point to context-relevant content. Heuristic: linked page title/H1 shares topic words with linking paragraph. |
| L8 | Orphan prevention | Page has ≥1 incoming internal link | LOW | Add a link from at least one other page on the site to this page. |
| L9 | Link title attributes | `title=""` attribute present on key in-body links | LOW | Add descriptive `title` attribute to internal and key external links. Screen readers + SEO bonus. |

---

## URL & TECHNICAL (T1–T8)

| # | Factor | Target | Severity | Fix If Failing |
|---|--------|--------|----------|----------------|
| T1 | URL length | ≤75 characters | MEDIUM | Shorten slug: remove stop words, unnecessary path segments. |
| T2 | URL structure | Keyword, hyphens, no underscores, no stop words | MEDIUM | Edit slug: replace underscores with hyphens, remove "the/a/an/in/on/at/for/of". |
| T3 | SEO title length | Per-language limits - see `shared/readability-params.md` Meta Length table | HIGH | Trim or expand title to fit. Cut filler words. Add brand at end if space. |
| T4 | Meta description length | Per-language limits - see `shared/readability-params.md` Meta Length table | HIGH | Trim to fit. Remove fluff. Ensure keyword + value proposition fit the window. |
| T5 | Image file names | Descriptive, keyword-rich, hyphens | LOW | Rename: "IMG_4521.jpg" → "seo-checklist-ranking-factors.jpg". |
| T6 | Schema markup | Appropriate type present | MEDIUM | Add JSON-LD schema. See `shared/schema-templates.md` for templates. Validate with search engine rich results testing tools if web access available. |
| T7 | Canonical URL | Correct canonical set | MEDIUM | Set canonical to preferred URL version. Resolve www/non-www, http/https, trailing slash. |
| T8 | OG / Twitter Card tags | Open Graph and/or Twitter Card meta tags present | LOW | Add `og:title`, `og:description`, `og:image`, and `twitter:card` meta tags. See `scenarios/meta-optimize.md` Step 3. |

---

## ADVANCED SIGNALS (A1–A6)

| # | Factor | Target | Severity | Fix If Failing |
|---|--------|--------|----------|----------------|
| A1 | Featured snippet potential | 40–60 word concise answer to target query | MEDIUM | Add a clear, direct answer paragraph. Use definition format or list format. |
| A2 | E-E-A-T signals | Experience, Expertise, Authoritativeness, Trustworthiness: ≥3 of 5 must be present - (1) author name + bio with credentials, (2) publication/modified date visible, (3) at least 1 credible external citation/source, (4) about/site-info page reference, (5) contact info or privacy policy link. 3+ = ✅ Pass, 2 = ⚠️ Warning, 0–1 = ❌ Fail. See also HCU notes below. | HIGH | Add: author bio with credentials, publication date, citations, about page link, privacy policy. |
| A3 | LSI / semantic keywords | 5–15 related terms naturally present | MEDIUM | Add: related terms, synonyms, category words. Use SERP "Searches related to" for ideas. |
| A4 | Content freshness | Date visible, updated within reasonable period | LOW | Add "Last updated" date. Update annually for evergreen, within weeks for news-sensitive. |
| A5 | Mobile readability | Short paragraphs, clear headings, adequate font size equivalent | MEDIUM | Test: can you scan the page on a phone? Break long sections. Ensure heading contrast. |
| A6 | Breadcrumb structure | Logical breadcrumb path: Home > Category > Page | LOW | Add breadcrumb markup: see `shared/schema-templates.md` → BreadcrumbList. |

---

## SCORING METHODOLOGY

Each factor receives one of:
- ✅ **Pass** - meets or exceeds target
- ❌ **Fail** - below target, fix required
- ⚠️ **Warning** - borderline or partially met
- ⊘ **N/A** - not applicable to this content type

### Weighted scoring
Not all factors carry equal weight. Score is calculated with multipliers:

- **CRITICAL** = ×3 | **HIGH** = ×2 | **MEDIUM** = ×1 | **LOW** = ×0.5

**Formula:** `Score % = (Σ(PASS_WEIGHTS) / Σ(ALL_WEIGHTS)) × 100`

Where PASS_WEIGHTS sums the multipliers of all ✅ factors, and ALL_WEIGHTS sums multipliers of all applicable (non-N/A) factors.

**N/A handling:** ⊘ factors are excluded from both numerator and denominator. They do not penalize the score. Example: a product page with no images → K9, C3 are N/A → excluded. A blog post with images → K9, C3 are scored.

### Grade thresholds (applied AFTER weighted calculation)

| Grade | Score % | Meaning | Constraint |
|-------|---------|---------|------------|
| A | 90%+ | Excellent. Minor tweaks only. | 0 CRITICAL failures |
| B | 75–89% | Good. Several improvements available. | ≤1 CRITICAL failure |
| C | 60–74% | Average. Significant gaps to fix. | ≤3 CRITICAL failures |
| D | 40–59% | Poor. Major overhaul needed. | - |
| F | <40% | Failing. Start over or fully restructure. | - |

**Constraint enforcement:** A page with 95% raw score but 1 CRITICAL failure → capped at B. A page with 80% and 4 CRITICAL failures → capped at C. ⚠️ Warning on a CRITICAL factor counts as 0.5 CRITICAL failures for cap purposes (e.g., K1⚠️ = probably defined but not explicit → 0.5 toward the cap).

### Priority levels
- **CRITICAL** - Fix immediately. These factors alone can prevent ranking. Impact: Very High.
- **HIGH** - Fix this week. Major ranking impact. Impact: High.
- **MEDIUM** - Improve. Noticeable ranking impact over time. Impact: Medium.
- **LOW** - Optional. Marginal improvements, competitive differentiators. Impact: Low.

> **Note:** Impact labels are qualitative, not derived from rank-correlation studies. They express consensus SEO prioritization, not guaranteed ranking deltas.

### Delivery validation rule
Before delivering any scored output, verify: N/A + CRITICAL + HIGH + MEDIUM + LOW + PASSED = 49. If sum ≠ 49, re-scan the content - a factor was missed. This guarantees 100% coverage on every audit.

---

## MODE-SPECIFIC FACTOR WEIGHTS

### Audit Mode: Score all applicable factors. Exclude N/A from denominator.
### Generate Mode: Pass all factors by design (target score 46+/49 weighted). Mark image factors N/A if no images available - note in output.
### Rewrite Mode: Score existing content, then score rewritten content. Report delta. Mark image factors N/A if original had no images.
### Meta-Only Mode: Score K1, K2, K3, K4, K5, T1, T2, T3, T4, T8, C5, C6, C7 (13 factors relevant to meta/URL/alt layer). Body-level factors are N/A.
### Brief Mode: Recommend targets for all factors (no scoring - planning phase)

---

## FACTOR INTERDEPENDENCIES

Some factors interact. Fixing one may affect another:

- **C1 (word count) ↑** may **K10 (density) ↓** - longer content needs more keyword instances
- **C11 (sentence variety) ↑** may **C8 (readability) ↓** if long sentences are too complex
- **L1 (internal links) ↑** may **K10 (density) ↓** if anchors use exact-match keywords excessively
- **T3/T4 (title/desc length) ↑** may **K2/K4 (keyword placement) ↓** if keyword gets pushed out by length
- **C13 (heading hierarchy) ↑** may **K8 (keyword in H2) ↑** - restructuring provides natural keyword placement

When delivering fixes, account for these dependencies. Group related fixes together.

---

## CHECKLIST QUICK-SCAN (60-second pre-delivery)

Before delivering ANY output, scan these 8 highest-impact factors:

1. ☐ K1 - Focus keyword defined?
2. ☐ K2 - Keyword in SEO title?
3. ☐ K4 - Keyword in meta description?
4. ☐ K7 - Keyword in content body?
5. ☐ K10 - Density 0.8–1.5%?
6. ☐ C1 - Word count 600+?
7. ☐ C13 - Heading hierarchy correct?
8. ☐ L1 - At least 3 internal links?

If any of these 8 fail, fix before delivery.

---

## HCU / HELPFUL CONTENT COMPLIANCE

Google's Helpful Content Update (HCU) rewards **people-first** content — original, satisfying, and demonstrating first-hand experience. RankWise aligns via:

- **Burned words** (`shared/burned-words.md`): removes AI-marker vocabulary that signals low-effort content
- **E-E-A-T signals** (A2): author expertise, citations, transparency — all core HCU signals
- **Originality gate** (article-generate.md Step 3): 1 data point per 500 words, 1 concrete example per H2, 1 contrarian insight per article
- **Ruthless editor** persona: default stance is DELETE — content must earn its place

> **HCU risk note:** AI-generated content that lacks original examples, unique data, or first-hand experience is at risk of HCU classifier demotion. RankWise's content quality rules are designed to surface these gaps — but the final responsibility for originality rests with the human author/editor.

---

## OFFLINE MODE — WEB-ACCESS FACTORS

When operating **without web access** (no fetch/crawl capability), the following factors cannot be reliably scored. Instead of penalizing with ⚠️ marks, mark them as `⊘ [NO_WEB]` and **exclude from denominator**:

| Factor | Offline handling |
|--------|-----------------|
| K11 | ⊘ [NO_WEB] — Cannibalization check requires `site:` search |
| L5 | ⊘ [NO_WEB] — Outbound link quality requires domain lookup |
| L6 | ⊘ [NO_WEB] — Broken link check requires HTTP verification |
| L7 | ⊘ [NO_WEB] — Internal link relevance requires cross-page analysis |
| L8 | ⊘ [NO_WEB] — Orphan check requires full-site crawl |
| T6 | ⊘ [NO_WEB] — Schema validation requires source access |
| T7 | ⊘ [NO_WEB] — Canonical URL check requires source access |
| A3 | Scored offline — Use topic vocabulary diversity as proxy for LSI |

**With web access:** score all factors normally. **Without web access:** exclude these 7 from denominator (denominator becomes 42 max, not 49). Mark clearly in report: `⊘ K11 [NO_WEB]: Requires site search — skipped.`
