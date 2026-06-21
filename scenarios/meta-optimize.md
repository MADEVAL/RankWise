# Scenario: Meta Optimize

**Use when:** User asks for meta tags only - title, meta description, OG tags. Mode: META-ONLY.

**Pipeline:** extract context → keyword placement → length check → power words → sentiment → deliver

---

## INPUT FORMATS ACCEPTED

### Format 1: Topic description (no existing tags)
```
Topic: [describe the page]
Focus keyword: [keyword]
Language: [language]
Brand: [brand name or "none"]
Page type: [article / product / landing / category]
```

### Format 2: Existing tags to fix
```
Current title: [text]
Current description: [text]
Focus keyword: [keyword]
Language: [language]
```

### Format 3: Full request with context
```
Generate meta tags for [page type] about [topic].
Keyword: [keyword]. Language: [lang]. Brand: [brand].
Target audience: [who]. Key value: [what they get].
```

---

## STEP 1: SEO TITLE GENERATION

### Rules (all languages)
- **Length:** 50–60 characters (EN). Adjust per language in `shared/readability-params.md`.
- **Keyword:** In first 3–5 words
- **Power words:** ≥2 from `shared/power-words.md`
- **Number:** At least 1 (odd preferred)
- **Sentiment:** Clear polarity (not neutral)
- **Brand:** Append " | Brand" or " - Brand" at end if space allows
- **No period at end**
- **No ALL CAPS words** (unless brand convention)
- **No duplicates:** Check word repetition within title - avoid

### Title formulas by page type

| Page Type | Formula | Example |
|-----------|---------|---------|
| Blog/Article | [Number] [Power Word] [Keyword]: [Promise] | "7 Proven SEO Checklist Templates That Actually Work" |
| How-to/Tutorial | How to [Outcome] Using [Keyword] [Time/Result] | "How to Audit Your Website Using This SEO Checklist in 30 Min" |
| Product | [Keyword] - [Primary Benefit] [Proof/Edge] | "SEO Audit Tool - Find & Fix 45+ Ranking Issues in One Click" |
| Landing | [Outcome] with [Keyword]: No [Pain Point] Required | "Rank #1 with SEO Checklists: No Agency Required" |
| Category/Ecom | [Keyword] - [Selection/Range] [Year] | "SEO Tools Compared - Top 12 Picks for 2026" |
| Comparison | [X] vs [Y]: Which [Keyword] Is Best for [Audience]? | "Cloud vs On-Premise: Which SEO Tool Is Best for Enterprise Teams?" |

### Generate 3 variants (when user asks for variants)
1. **Direct/Informational** - "What is [Keyword]? [Definition] + [Benefit]"
2. **Curiosity/Emotional** - "[Power Word]: [Keyword] [Surprising Insight]"
3. **Actionable/Listicle** - "[Number] [Keyword] [Action] for [Audience]"

---

## STEP 2: META DESCRIPTION GENERATION

### Rules (all languages)
- **Length:** 145–158 characters (EN)
- **Keyword:** In first 20 words
- **Active voice:** Concrete verbs, not passive
- **Value proposition:** Specific - what reader gets
- **No fluff:** "Welcome to", "In this article", "We will discuss", "Learn more about"
- **CTA when space:** Specific action verb - "Download the checklist", "Compare tools", "Read the case study"
- **Unique:** Must not duplicate meta title wording

### Description template
```
[Keyword]: [specific value or benefit]. [Evidence/credibility point]. [Action/next step].
```

**Examples:**
- "SEO checklist: audit all 45+ ranking factors in one pass. Includes keyword, content, link, and technical checks. Free template included."
- "SEO checklist for beginners and pros. Step-by-step audit covering titles, meta, headings, images, and links. Fix issues before publishing."

### Per-page-type description patterns

| Page Type | Pattern |
|-----------|---------|
| Blog/Article | [Keyword]: [what reader learns]. [Supporting detail - data/source]. [Specific element in article]. |
| Product | [Keyword] that [primary benefit]. [Key feature]. [Key feature]. [Risk reversal or proof]. |
| Landing | Get [outcome] with [keyword]. [How it's different]. [Proof - numbers/testimonial]. [Start/try CTA]. |
| Category | Browse [number]+ [keyword] for [audience]. [Selection criteria]. Updated [timeframe]. |

### Generate 3 variants (when user asks)
1. **Benefit-focused** - emphasizes what reader gains
2. **Trust-focused** - emphasizes credibility, data, authority
3. **Action-focused** - emphasizes next step, CTA

---

## STEP 3: OG TAG GENERATION

### OG title
- 40–60 characters
- May equal meta title OR be slightly more conversational
- Must still contain keyword
- Social-friendly tone (less formal than meta title acceptable)

### OG description
- 100–200 characters
- Must NOT copy meta description verbatim
- Social media tone: human, intriguing, scroll-stopping
- Can be more emotional/curious than SEO meta description
- No hashtags, no emojis (unless specifically requested)

---

## STEP 4: URL SLUG SUGGESTION

### Rules
- ≤75 characters
- Contains primary keyword
- Remove stop words: the, a, an, in, on, at, to, for, of, with, and, or, but
- Hyphens between words (never underscores)
- No special characters
- No dates (unless intentionally part of strategy)
- Lowercase
- No trailing slash in suggestion

### Generate from keyword
```
"best seo checklist for wordpress beginners" → /seo-checklist-wordpress
"how to increase website traffic with content marketing" → /increase-website-traffic-content-marketing
```

---

## STEP 5: OUTPUT FORMAT

### Single tag set
```
[MODE: meta-only]
[LANG: xx]
[KEYWORD: xxx]

SEO Title (XX chars):
[title text]

Meta Description (XX chars):
[description text]

OG Title (XX chars):
[og title]

OG Description (XX chars):
[og description]

URL Slug:
/suggested-slug
```

### Multiple variants
```
[MODE: meta-only]
[LANG: xx]
[KEYWORD: xxx]

--- Variant 1 (Benefit) ---
Title (XX):
[title]
Description (XX):
[description]

--- Variant 2 (Trust) ---
Title (XX):
[title]
Description (XX):
[description]

--- Variant 3 (Action) ---
Title (XX):
[title]
Description (XX):
[description]

URL Slug:
/suggested-slug
```

### Audit existing tags
```
[MODE: meta-only - audit]
[KEYWORD: xxx]

--- CURRENT TAGS ---
Title (XX chars): [existing]
Issues: [list problems]

Description (XX chars): [existing]
Issues: [list problems]

--- RECOMMENDED TAGS ---
Title (XX chars): [new]
Description (XX chars): [new]
```
