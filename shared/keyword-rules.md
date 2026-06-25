# Keyword Rules - Placement, Density, LSI, Cannibalization
> **Version:** 1.2.1

> Full keyword strategy: from selection to distribution.

---

## KEYWORD HIERARCHY

### Primary Keyword (1 per page)
- The main topic target
- Appears in: title, meta description, URL, first 150 words, ≥1 H2, ≥1 image alt, body
- Density: 0.8%–1.5% of total word count
- Exact match: use 1-2 times. Partial match: 2-4 times. Synonyms: 2-4 times.

### Secondary Keywords (2–4 per page)
- Support the primary topic
- Often: longer-tail variations, related angles, question-form keywords
- Appear in: ≥1 H2/H3 each, body naturally
- Density: 0.3%–0.7% each

### LSI / Semantic Keywords (5–15 per page)
- Terms search engines associate with the primary topic
- Source: SERP "Searches related to", "People also ask", Wikipedia sub-topics, competitor content
- Appear: naturally throughout body - not forced
- No density target - presence is the signal

---

## DENSITY CALCULATION

```
Keyword Density (%) = (Keyword Occurrences × 100) / Total Word Count
```

### Exact match
- "SEO checklist" appearing exactly as-is

### Partial match
- "SEO ranking checklist", "the checklist for SEO" - contains the keyword but not in exact order

### Stem variations
- "checklists", "checklist-driven", "checklist-based"

### Combined density
- Exact + partial + stem variations = total effective density
- Target: 0.8%–1.5% combined

### Density by content length
| Content Length | Exact Matches | Partial/Stem | Total Instances |
|---------------|---------------|--------------|-----------------|
| 600 words | 1-2 | 2-3 | 3-5 |
| 1000 words | 2-3 | 3-5 | 5-8 |
| 1500 words | 3-4 | 4-6 | 7-10 |
| 2000 words | 4-5 | 5-8 | 9-13 |
| 3000+ words | 5-8 | 8-12 | 13-20 |

---

## PLACEMENT RULES

### Rule 1: Title
- Keyword in SEO title
- Near the beginning (first 3-5 words ideal)
- Only once in title (don't stuff)

### Rule 2: Meta Description
- Keyword in first 20 words of description
- Acts as bold trigger in SERP
- Natural - must read like a human sentence

### Rule 3: URL
- Keyword in URL slug
- Near the beginning
- Remove stop words from slug

### Rule 4: First 100–150 Words
- Keyword appears once in the opening paragraph
- Establishes topic relevance immediately
- Must read naturally - not "Today we will discuss [keyword]"

### Rule 5: Headings
- At least one H2 contains the primary keyword
- Secondary keywords in other H2s or H3s
- Keyword in heading = strong relevance signal

### Rule 6: Image Alt Text
- At least one image has keyword in alt text
- Descriptive + keyword: "SEO checklist ranking factors table" not just "SEO"

### Rule 7: Body Distribution
- Keyword appears every 150–300 words throughout
- NOT clustered at start only
- NOT "keyword stuffing" - every instance must read naturally

---

## LSI KEYWORD GENERATION PATTERNS

Use these patterns to generate LSI keywords for any primary keyword:

| Pattern | Example (Primary: "email marketing") |
|---------|--------------------------------------|
| Category parents/children | "digital marketing", "email campaigns", "newsletter marketing" |
| Tools/instruments | "email automation platform", "ESP", "bulk email service" |
| Actions/processes | "building email list", "writing subject lines", "A/B testing" |
| Problems/solutions | "low open rates", "high bounce rate", "spam filters" |
| People/roles | "email marketer", "copywriter", "subscriber" |
| Metrics/measurements | "open rate", "click-through rate", "conversion rate", "ROI" |
| Time/sequence | "email sequence", "welcome email", "drip campaign" |
| Comparisons | "email vs social media", "HTML vs plain text email" |
| Questions | "what is email marketing", "how to build email list", "best time to send emails" |

### LSI source methods
1. SERP "Searches related to [keyword]" - bottom of search results
2. SERP "People also ask" - mid-SERP feature
3. Search autocomplete - type keyword, note suggestions
4. Wikipedia - sub-topics in article structure
5. Competitor content - terms they target in headings
6. Keyword research tools - "Also rank for" feature

---

## KEYWORD CANNIBALIZATION CHECK

### What it is
Two or more pages on the same site targeting the same primary keyword. Search engines don't know which to rank - both suffer.

### Detection
1. Search `site:yoursite.com "primary keyword"`
2. If multiple pages appear in results → possible cannibalization
3. Check if those pages target the exact same keyword in titles

### Fix options (ranked by recommendation)
1. **Merge** - Combine pages into one comprehensive resource. 301 redirect the weaker page.
2. **Differentiate** - Change keyword target on one page to a related but distinct term
3. **Canonicalize** - Set canonical on the weaker page pointing to the stronger page
4. **De-optimize** - Remove keyword from title/headings on the weaker page, target a different angle

### Prevention
- Maintain a keyword map: each primary keyword → exactly one URL
- Before creating new content: search your own site for the keyword
- Use RankWise Audit on new content drafts before publishing

---

## LANGUAGE-SPECIFIC KEYWORD NOTES

### English
- Search engines understand synonyms, stemming, entities
- Long-tail keywords often outperform short-head due to intent clarity
- Question keywords growing (voice search trend)

### Russian / Русский
- Yandex: morphological analysis is strong. Different word forms (падежи) are recognized.
- Yandex penalizes over-optimization harder. Density closer to 0.5%–1%.
- Word order is flexible - keyword can appear anywhere and still match.
- Question keywords: 40%+ of queries in Yandex are questions.

### Ukrainian / Українська
- Google dominates (~95% market share). Ukrainian queries are longer and more conversational.
- Avoid Russian SEO patterns leaking into Ukrainian content.
- Morphological analysis works - different cases (відмінки) are recognized as related.
- Natural conversational density: 0.8%–1.2%. Do not over-optimize.
- Question-form keywords are very common (voice search and conversational queries).
- Watch for Russianisms in keyword lists: use Ukrainian equivalents, not calques.

### German / Deutsch
- Compound nouns: "SEO-Optimierung" and "SEO Optimierung" may be different keywords.
- Umlauts matter: ä ≠ ae, ö ≠ oe, ü ≠ ue in keyword matching.
- Case matters less (search engines understand declensions).

### French / Español / Português / Italiano
- Accented characters: é vs e may or may not be treated as equivalent - check.
- Gendered variations: search engines understand masculine/feminine as related.
- Plural/singular: typically treated as related.

### Multi-language sites
- Use hreflang tags to specify language/region targeting
- Each language version targets keywords in that language
- Don't translate keywords directly - research local search behavior
