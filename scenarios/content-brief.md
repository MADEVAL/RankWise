# Scenario: Content Brief
> **Version:** 1.2.1

**Use when:** User asks for SEO content brief, plan, outline, or strategy. No full content required. Mode: BRIEF.

**Pipeline:** intent analysis → keyword research → structure design → meta drafts → linking plan → media plan → deliver

---

## STEP 0: SEARCH INTENT DETERMINATION

**If web access available:** search the primary keyword in SERP (or analyze SERP data if provided).

**If no web access:** Infer intent from keyword patterns:
- "how to", "what is", "guide", "why", "learn" → **Informational**
- "best", "vs", "comparison", "review", "top X", "alternatives" → **Commercial**
- "buy", "price", "cheap", "discount", "download", "sign up", "order" → **Transactional**
- Brand/company name only → **Navigational**
- If ambiguous, default to **Informational**.

### Identify intent
| Intent | Signal | Content Type |
|--------|--------|-------------|
| **Informational** | SERP has guides, how-tos, definitions | Guide, tutorial, explainer |
| **Commercial** | SERP has comparisons, reviews, "best X" | Comparison, review, buying guide |
| **Transactional** | SERP has product pages, landing pages, sign-up pages | Product, landing, sales page |
| **Navigational** | SERP has brand homepages, about pages | About, brand page |

### Note SERP features (if web access available)
- Featured snippet → target with concise answer
- People Also Ask → extract as H2/H3 questions
- Video carousel → consider video content
- Image pack → plan infographics/screenshots
- Knowledge panel → note entity relationships
- Related searches → LSI keyword source

**If no web access:** infer likely features from content type. How-to keywords typically trigger video carousels and featured snippets. Definition keywords trigger knowledge panels.

---

## STEP 1: KEYWORD PLAN

### Primary keyword
- The main target keyword
- Search volume (if known, or flag "[VOLUME UNKNOWN]")
- Difficulty estimation: Low / Medium / High (based on SERP competitors)

### Secondary keywords (3–5)
- Longer-tail variations
- Question-form keywords
- Related intent keywords

### LSI / semantic keywords (8–15)
Source from:
- SERP "Searches related to"
- SERP "People also ask"
- Wikipedia sub-topics
- Competitor headings (scan top 3 SERP results)

### Keyword map (draft)
```
Primary:  [keyword]              → H1, meta, URL, ≥1 H2
Secondary 1: [kw2]               → H2 section
Secondary 2: [kw3]               → H2 section
...
LSI terms: [term1, term2, ...]   → body, H3s, alt texts
```

---

## STEP 2: STRUCTURE BLUEPRINT

### H1 (Title)
Suggest 3 title variants meeting all criteria:
- 50–60 characters
- Primary keyword near beginning
- Number + power words
- Clear sentiment

### H2 Sections (5–9 suggested)
For each H2:
- Section title (SEO-optimized, includes keyword where appropriate)
- Target word count for this section
- Key points to cover (3–5 bullet points)
- Which secondary keyword or LSI term to target

### H3 Sub-sections
List under each H2 where content justifies depth (>300 words per H2).

### Structure template
```
H1: [Title]
  ├── Introduction (~150 words)
  │   [Hook idea], [Pain point], [Keyword placement]
  │
  ├── H2: [Section 1] (~250 words) - Keyword: [secondary kw]
  │   ├── H3: [Sub-point]
  │   └── H3: [Sub-point]
  │
  ├── H2: [Section 2] (~300 words) - Keyword: [primary kw]
  │   ├── H3: [Sub-point]
  │   └── H3: [Sub-point]
  │
  ... (continue for all sections)
  │
  └── Conclusion + CTA (~100 words)
```

### Total target word count
Based on SERP competition:
- Top 3 avg word count: [X] → Your target: [X + 20%]
- Or manual: specify

---

## STEP 3: META DRAFTS

### SEO Title (2–3 variants)
```
1. [Variant 1]
2. [Variant 2]
3. [Variant 3]
```

### Meta Description (2–3 variants)
```
1. [Variant 1]
2. [Variant 2]
```

### URL Slug
```
/suggested-slug
```

---

## STEP 4: LINKING PLAN

### Internal links (suggest 3–8)
```
Target URL | Suggested anchor text | Placement (which section)
---------|----------------------|----------
/page-1   | "anchor text"        | Introduction
/page-2   | "anchor text"        | H2 Section 3
...
```

### External links (suggest 2–5)
```
Target URL | Authority | Why link | Placement
---------|-----------|----------|----------
source.com | DA 65    | Data cite | H2 Section 4
...
```

---

## STEP 5: MEDIA PLAN

### Images needed (≥1 per 300 words)
```
Count: [X] images
Types: [infographic / screenshot / chart / photo / illustration / diagram]
Suggestions:
1. [Image idea] - placement: [section] - possible alt text: "[draft]"
2. ...
```

### Video (optional)
```
If SERP shows video carousel: Consider embedding a [X-minute] video on [topic]
```

---

## STEP 6: SCHEMA RECOMMENDATION

```
Schema type: [Article / Product / FAQPage / HowTo / Review]
Reason: [based on content type and SERP features]
Template: see shared/schema-templates.md
```

---

## STEP 7: COMPETITOR GAP NOTES

Scan top 3 SERP results. Note:
- What they cover well
- What they miss or cover weakly
- Your angle: what you'll do differently/better
- Unique data, examples, or insights you can add

---

## STEP 8: DELIVERY FORMAT

```
[MODE: brief]
[LANG: xx]
[INTENT: informational/commercial/transactional/navigational]
[TARGET WORD COUNT: X words]

====================================
KEYWORD PLAN
====================================
Primary: [keyword]
Secondary: [kw1, kw2, kw3, ...]
LSI: [term1, term2, ...]

====================================
STRUCTURE BLUEPRINT
====================================
H1 Options:
1. [title variant 1]
2. [title variant 2]
3. [title variant 3]

H2 Sections:
1. [H2 title] (~X words) - Keyword: [kw]
   - [key point]
   - [key point]
2. [H2 title] (~X words) - Keyword: [kw]
   ...

====================================
META DRAFTS
====================================
Title:
1. [variant]
2. [variant]

Description:
1. [variant]
2. [variant]

URL: /suggested-slug

====================================
LINKING PLAN
====================================
Internal:
- [URL] → anchor: "[text]" → placement: [section]
External:
- [URL] (DA XX) → cite: [reason] → placement: [section]

====================================
MEDIA PLAN
====================================
[X] images needed:
1. [type]: [idea] → section: [name]

====================================
SCHEMA
====================================
Type: [schema type]
Reason: [why]

====================================
COMPETITOR GAP
====================================
Top 3 competitors cover: [summary]
They miss: [gaps]
Your angle: [differentiation]
Your unique additions: [data, examples, insights]
```
