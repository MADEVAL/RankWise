# Scenario: Article Generate

**Use when:** User provides topic + focus keyword. No source content. Mode: GENERATE.

**Pipeline:** keyword audit → SERP intent analysis → title crafting → outline → content writing → meta generation → linking → QA check

---

## STEP 0: INTENT ANALYSIS

Before writing, determine the search intent.

**If you have web access:** search the primary keyword in SERP. Note what type of content ranks in top 5 positions. Note SERP features present (featured snippet, video carousel, people also ask, etc.).

**If no web access:** Infer intent from keyword type:
- "how to", "what is", "guide", "why" → Informational
- "best", "vs", "comparison", "review", "top" → Commercial
- "buy", "price", "cheap", "discount", "order" → Transactional
- Brand names only → Navigational
- If unclear, default to Informational.

| Intent Type | Content Shape | Title Pattern |
|------------|---------------|---------------|
| **Informational** | Guide, explainer, tutorial, listicle | "How to...", "What is...", "X Ways...", "Complete Guide to..." |
| **Commercial** | Comparison, review, best-of list | "Best X for Y", "X vs Y", "Top X [Product] in 2026" |
| **Transactional** | Product page, service page, landing | "[Product]: [Benefit]", "Buy [Product] — [Value Prop]" |
| **Navigational** | Brand page, about page | "[Brand]: [One-liner]" |

**How to determine intent:**
1. Search the primary keyword in SERP (if web access available)
2. Note what type of content ranks in top 5 positions
3. Note SERP features present (featured snippet, video carousel, people also ask, etc.)
4. Match your content to the dominant content type
5. **If no web access:** infer from keyword type as described above

---

## STEP 1: TITLE CRAFTING

### Formula
```
[Number] + [Power Word] + [Focus Keyword] + [Specific Promise or Curiosity Hook]
```

### Variations
- **How-to:** "How to [Achieve Outcome] Using [Keyword]: [Timeframe/Result]"
- **Listicle:** "[Odd Number] [Power Word] [Keyword] Strategies That Actually Work"
- **Question:** "[Bold Question Related to Keyword]? Here's What [Number] Studies Say"
- **Contrarian:** "Stop [Common Mistake About Keyword]. Do This Instead."
- **Case study:** "How We [Achieved X] Using [Keyword] in [Timeframe]"

### Title checklist
- 50–60 characters (adjust per language: `shared/readability-params.md`)
- Focus keyword in first 3–5 words
- At least 1 number (odd preferred)
- At least 2 power words from `shared/power-words.md`
- Clear sentiment polarity (not neutral)
- No clickbait — promise must be deliverable
- Unique (search to verify no duplicate on same site)

---

## STEP 2: OUTLINE STRUCTURE

### Content length decision
| Competition Level | Target Word Count |
|-------------------|-------------------|
| Low (easy keyword) | 600–1000 |
| Medium | 1000–1800 |
| High (hard keyword) | 1800–3000+ |

### H2 section blueprint
Generate 5–9 H2s covering:

1. **Problem/Pain** — Why this matters, what goes wrong without it
2. **Definition/Context** — What is [keyword], why it exists
3. **Core Method/Approach** — The main how-to or explanation
4. **Evidence/Data** — Statistics, studies, results
5. **Practical Steps** — Step-by-step implementation
6. **Common Mistakes** — What people get wrong
7. **Tools/Resources** — What helps
8. **Advanced/Evolved** — Next-level applications
9. **Conclusion/Next Steps** — What to do now

Each H2 gets 2–4 H3 sub-sections as needed.

### Heading keyword placement
- H1: Primary keyword (the title)
- At least 1 H2: Primary keyword
- Other H2s: Secondary keywords
- H3s: Secondary keywords + LSI terms

---

## STEP 3: CONTENT WRITING

### Introduction (first 100–150 words)
1. **Hook** — Pattern interrupt. Statistic, question, bold claim, or story.
2. **Pain point** — Why the reader should care RIGHT NOW.
3. **Promise** — What they'll get from reading.
4. **Keyword** — Naturally within first 100–150 words.
5. **Transition** — Bridge to first H2.

**DO NOT use:**
- "In today's digital landscape..."
- "Welcome to our comprehensive guide..."
- "In this article, we will explore..."
- Throat-clearing preamble — go straight to value.

### Body sections
Each H2 section:
1. **Opening sentence** — Clear, direct. States what this section covers.
2. **Core content** — Mix of explanation, data, examples.
3. **Visual relief** — List, table, or image reference.
4. **Transition** — Bridge to next H2 (or let heading do the work).

### Content rules
- 1 data point/statistic per 500 words
- 1 concrete example per H2 section
- 1 "surprising" or "contrarian" insight per article
- Keyword density: 0.8%–1.5% (see `shared/keyword-rules.md`)
- Passive voice: ≤10% of sentences (`shared/readability-params.md`)
- Transition words: ≥30% of sentences
- Sentence length: varied — no 3 consecutive same-length

### Conclusion
1. **Summary** — 1-2 sentences, no regurgitation.
2. **Key takeaway** — The ONE thing reader should remember.
3. **CTA** — Specific next action. "Try [tool]", "Download [template]", "Read [related article]".
4. **No** "In conclusion..." / "To summarize..." / "We hope you enjoyed..."

---

## STEP 4: META LAYER

### SEO title
- 50–60 characters
- Keyword near beginning
- Brand at end if space: ` | Brand`

### Meta description
- 145–158 characters
- Keyword in first 20 words
- Active voice, value proposition, CTA
- Template: "[[Keyword]]: [specific benefit]. [Evidence/credibility]. [Action]."

### URL slug
- Remove stop words
- Hyphens not underscores
- ≤75 characters
- Example: "best-email-marketing-tools" not "best_tools_for_email_marketing_2026"

### OG tags
- OG title: 40–60 chars, may equal meta title or be slightly more conversational
- OG description: 100–200 chars, different from meta description, social-media tone

---

## STEP 5: MEDIA & LINKS

### Image plan
- ≥1 image per 300 words
- At least 1 image: focus keyword in alt text
- File names: descriptive, keyword-rich, hyphens
- Alt texts: ≤125 characters, descriptive + keyword where natural
- **If no images available:** Mark K9 and C3 as N/A. Include specific image recommendations: type (screenshot/chart/photo/infographic), suggested content, and placement section. Do NOT generate alt texts for non-existent images.

### Internal links
- 3–10 contextual in-body links
- Anchor text variety: `shared/link-strategy.md`

### External links
- 2–5 authoritative outbound links
- At least 1 DoFollow
- `shared/link-strategy.md`

---

## STEP 6: QA — THE 8-FACTOR QUICK SCAN

Before delivering, verify these 8 critical factors:
1. ☐ K1: Focus keyword set
2. ☐ K2: Keyword in SEO title
3. ☐ K4: Keyword in meta description
4. ☐ K7: Keyword in body
5. ☐ K10: Density 0.8–1.5%
6. ☐ C1: Word count ≥600
7. ☐ C13: Heading hierarchy correct
8. ☐ L1: ≥3 internal links

If all pass, deliver.
