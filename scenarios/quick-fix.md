# Scenario: Quick Fix

**Use when:** User asks to fix a specific SEO element without full article rewrite. Mode: auto-detect based on what user mentions.

**Pipeline:** identify target → apply fix → verify → deliver

---

## TRIGGER DETECTION

| User says | Fix target | Scenario reference |
|-----------|-----------|-------------------|
| "keyword density too high", "keyword stuffing" | K10 - Keyword density | Below |
| "add keyword to headings", "keyword in H2" | K8 - Keyword in H2 | Below |
| "add keyword to title" | K2 - Keyword in title | Below |
| "add keyword to description" | K4 - Keyword in description | Below |
| "add keyword to URL" | K5 - Keyword in URL | Below |
| "cannibalization", "duplicate keyword" | K11 - Cannibalization | Below |
| "keyword too short", "keyword too long" | K12 - Keyword length | Below |
| "add internal links" | L1 - Internal links | Below |
| "add external links" | L2 - External links | Below |
| "URL too long" | T1 - URL length | `scenarios/url-optimize.md` |
| "passive voice too much" | C9 - Passive voice | Below |
| "paragraphs too long" | C2 - Short paragraphs | Below |
| "add power words" | C6 - Power words in title | `shared/power-words.md` |
| "add alt text" | K9 - Alt text | `scenarios/alt-texts.md` |
| "content too short", "word count low" | C1 - Word count | Below |
| "title too long/short" | T3 - Title length | Below |
| "description too long/short" | T4 - Description length | Below |
| "readability poor", "hard to read" | C8 - Readability | Below |
| "heading hierarchy broken" | C13 - Heading hierarchy | Below |
| "no schema", "add schema" | T6 - Schema markup | Below |
| "no OG tags", "add open graph" | T8 - OG tags | Below |
| "no date", "add freshness" | A4 - Content freshness | Below |
| "no author", "E-E-A-T missing" | A2 - E-E-A-T | Below |
| "no number in title" | C5 - Number in title | Below |
| "transition words low" | C10 - Transition words | Below |
| "sentence length same" | C11 - Sentence variety | Below |
| "repeated sentence starts" | C12 - Sentence starts | Below |
| "broken link" | L6 - Broken links | Below |
| "no dofollow links" | L3 - DoFollow | Below |
| "too many exact anchors" | L4 - Anchor variety | Below |
| "no featured snippet" | A1 - Featured snippet | Below |
| "LSI keywords missing" | A3 - LSI keywords | Below |
| "mobile readability poor" | A5 - Mobile readability | Below |
| "no breadcrumb" | A6 - Breadcrumb | Below |
| "image filenames bad" | T5 - Image file names | Below |
| "no TOC", "add table of contents" | C4 - Table of Contents | Below |
| "sentiment neutral" | C7 - Sentiment | Below |
| "keyword not at start" | K6 - Keyword at start | Below |
| "keyword not in first 100 words" | K6 - Keyword at start | Below |

---

## FIX: T3 - TITLE LENGTH

### Too long (>60 chars)
1. Remove filler words: "the", "a", "very", "really", "just"
2. Remove brand if title >60 without brand - suggest separate title + brand format
3. Condense phrases: "How to" → keep, "A Complete Guide to" → "Guide to"
4. Remove year if not essential

### Too short (<50 chars)
1. Add power word
2. Add number
3. Add specificity: "SEO Checklist" → "7-Step SEO Checklist for Higher Rankings"
4. Add benefit: "[Topic]" → "[Topic]: [Benefit]"

### Deliver
```
Original (XX chars): [title]
Issue: Too long/short - target 50–60 chars
Fixed (XX chars): [new title]
```

---

## FIX: T4 - DESCRIPTION LENGTH

### Too long (>158 chars)
1. Remove redundant phrases
2. Cut to one value proposition (not multiple)
3. Remove filler: "We offer", "You will learn", "In this article"
4. Tighten CTA

### Too short (<145 chars)
1. Add supporting detail: fact, stat, feature
2. Add credibility element: "Based on X study", "Used by Y companies"
3. Add CTA if space: "Download the template", "Compare plans"

### Deliver
```
Original (XX chars): [description]
Issue: Too long/short - target 145–158 chars
Fixed (XX chars): [new description]
```

---

## FIX: K2 / K4 - KEYWORD MISSING FROM TITLE / DESCRIPTION

1. Identify where to insert keyword naturally
2. Title: place in first 3–5 words
3. Description: place in first 20 words
4. If insertion breaks grammar, restructure the sentence

### Deliver
```
Original: [title/description]
Issue: Focus keyword "[keyword]" not present
Fixed: [new title/description]
```

---

## FIX: K10 - KEYWORD DENSITY

### Too low (<0.8%)
1. Find sections that discuss the keyword topic without using the term
2. Add 1–2 natural instances where the keyword fits
3. Check: does it still read naturally?

### Too high (>3%)
1. Replace some exact-match instances with:
   - Synonyms ("SEO checklist" → "search optimization checklist", "ranking factors checklist")
   - Pronouns ("it", "this", "the checklist")
   - Stemmed forms ("checklisting", "checklist-based")
2. Restructure sentences to avoid forced keyword placement

### Deliver
```
Original density: X.X% (X instances in Y words)
Issue: Too low/high - target 0.8%–1.5%
New density: X.X% (X instances in Y words)
Changed: [list specific changes: "line X - changed '...' to '...'"]
```

---

## FIX: K8 - KEYWORD IN SUBHEADINGS

1. Scan all H2s
2. Find the H2 most topically aligned with the primary keyword
3. If keyword fits naturally: insert it
4. If keyword doesn't fit any H2: restructure one H2 to cover the keyword topic directly

### Deliver
```
Current H2s:
- [h2 text 1]
- [h2 text 2]  ← keyword candidate
- [h2 text 3]

Suggested H2 change:
- [h2 text 2] → "[h2 with keyword]"
```

---

## FIX: L1 - INTERNAL LINKS

1. Suggest 3–8 internal pages to link to
2. Provide: target URL, suggested anchor text, placement (which section)
3. Anchor text must be varied (≤2 exact-match)

### Deliver
```
Current internal links: X
Need: 3–10 (suggested: Y)

Suggested additions:
1. /page-url - anchor: "[natural text]" - place in: [section name]
2. /page-url - anchor: "[different text]" - place in: [section name]
...
```

---

## FIX: L2 - EXTERNAL LINKS

1. Suggest 2–5 authoritative external sources
2. Provide: target URL, domain authority (if known), why relevant, suggested anchor text

### Deliver
```
Current external links: X
Need: 2–5 (suggested: Y)

Suggested additions:
1. https://source.com/page - (DA: XX) - relevance: [reason] - anchor: "[text]"
2. ...
```

---

## FIX: C9 - PASSIVE VOICE

1. Identify sentences with passive voice
2. Convert to active: agent + active verb + object
3. Exception: passive is acceptable when agent is unknown or irrelevant

### Passive voice patterns to catch
- "was [verb]ed by"
- "has been [verb]ed"
- "will be [verb]ed"
- "is being [verb]ed"
- "can be [verb]ed"

### Deliver
```
Passive sentences found: X of Y total (XX%) - target ≤10%

Conversions:
1. "The report was written by the team" → "The team wrote the report"
2. "Mistakes can be made by beginners" → "Beginners can make mistakes"
3. ...
```

---

## FIX: C2 - SHORT PARAGRAPHS

1. Identify paragraphs >150 words or >3 sentences
2. Break at logical transition points
3. Ensure each new paragraph has one clear idea

### Deliver
```
Paragraphs too long: X of Y

Break suggestions:
1. Paragraph #3 (X words, Y sentences):
   - Break after: "[last sentence before break]"
   - New paragraph starts: "[first sentence after break]"
...
```

---

## FIX: ALL REMAINING FACTORS (K1–A6)

### K1 - Focus Keyword Missing
- Best guess from title/H1. Example: title "How to Grow Your Email List" → keyword "grow email list"
- Deliver: keyword suggestion. Ask user to confirm.

### K3 - Keyword Not at Title Beginning
- Move keyword to first 3-5 words. "The Ultimate Guide to Email Marketing Strategy" → "Email Marketing Strategy: The Ultimate Guide"

### K5 - Keyword Missing from URL
- Insert keyword into slug near beginning. Remove stop words. See `scenarios/url-optimize.md`.

### K6 - Keyword Not in First 150 Words
- Rewrite opening paragraph to naturally include keyword. Do NOT force: "In this article about [keyword]" - use it in context.

### K7 - Keyword Missing from Body
- Identify the H2 section most relevant to the keyword topic. Add 1-2 natural instances there.

### K9 - Keyword Missing from Alt Text
- If images exist: pick the most relevant image. Add keyword to alt text naturally. If no images: mark N/A.

### K11 - Cannibalization Detected
- Recommend: merge pages, differentiate keywords, or set canonical. Flag "[VERIFY] search site for keyword".

### K12 - Keyword Too Short/Long
- Too short (<3 chars): pick a longer, more specific phrase. Too long (>7 words): condense to 2-5 core words.

### C1 - Word Count Too Low
- Identify the 2-3 thinnest sections. For each, add: 1 example, 1 data point, 1 actionable step. Target +200 words per section.

### C3 - Too Few Images
- If article >600 words: suggest 2-3 image types (screenshot, chart, photo, diagram) with placement locations. If no images available: mark N/A.

### C4 - Missing Table of Contents
- Only for articles >800 words. Extract all H2s. Generate anchor links. Place TOC after introduction, before first H2.

### C5 - No Number in Title
- Add a specific number: "X Ways", "X Steps", "How X [group] Can", "Increase by X%". Prefer odd numbers.

### C7 - Neutral Sentiment
- Steer title to positive ("Boost", "Achieve", "Master") or negative ("Avoid", "Stop", "Fix"). Which fits the content better?

### C8 - Poor Readability
- Shorten sentences >25 words. Split complex sentences. Replace jargon. Target: average 12-20 words per sentence.

### C10 - Too Few Transition Words
- Scan paragraphs. Add transitions at logical turning points: "However", "For example", "In contrast", "Therefore", "Specifically".

### C11 - Sentence Length Monotony
- Find 3+ consecutive same-length sentences. Split one long, merge two short, add a single-word fragment.

### C12 - Repeated Sentence Starts
- Find 3+ consecutive sentences starting identically. Rewrite 2 of them: change subject, start with preposition/conjunction, use a question.

### C14 - Content Below Ads
- If text-only view shows heavy ad/nav density in first 300 words: suggest moving main content higher. Flag "[VERIFY on live page]".

### L3 - No DoFollow External Links
- Choose 1 existing external link. Remove `rel="nofollow"`. If no external links: add 1 with DoFollow.

### L4 - Too Many Exact-Match Anchors
- Replace excess exact-match anchors with: branded variant, partial match, "read more about [topic]", or naked URL.

### L5 - Low-Quality Outbound Links
- Flag: "[VERIFY] check domain authority of [URL]. Replace with .edu, .gov, or recognized authority source."

### L6 - Broken Link Detected
- Flag: "[VERIFY] check URL [link]. Remove or replace with live alternative."

### L7 - Irrelevant Internal Links
- Flag: "[VERIFY] link to [URL] may not be topically related. Consider replacing with [suggested relevant page]."

### T5 - Non-Descriptive Image File Names
- Suggest rename: "IMG_4521.jpg" → "[keyword]-[description].jpg". Use hyphens, lowercase.

### T6 - No Schema Markup
- Recommend appropriate schema type. Provide JSON-LD template from `shared/schema-templates.md`.

### T7 - Incorrect Canonical
- Flag: "[VERIFY] canonical URL is [current]. Should point to preferred version. Resolve www/non-www, http/https."

### T8 - No OG/Twitter Cards
- Generate og:title, og:description, og:image, twitter:card. Use meta title/description as base. See `scenarios/meta-optimize.md` Step 3.

### A1 - No Featured Snippet Paragraph
- Add 40-60 word concise answer to the primary keyword query. Place after introduction. Use definition or list format.

### A2 - Missing E-E-A-T Signals
- Add: author bio (name + credentials), publication date, 1 citation, link to about page. Any 2 of 4 = pass.

### A3 - Too Few LSI Keywords
- Add 5-10 related terms. Source: SERP "Searches related to", "People also ask", topic vocabulary. Distribute naturally.

### A4 - No Freshness Date
- Add "Published: [date]" or "Last updated: [date]" near title or in footer.

### A5 - Poor Mobile Readability
- Break paragraphs >120 words. Ensure headings are clearly separated. Flag: "[VERIFY] test on mobile viewport."

### A6 - No Breadcrumb
- Add BreadcrumbList schema (see `shared/schema-templates.md`). Or implement visible breadcrumb: Home > Category > Page.

---

## GENERAL QUICK FIX DELIVERY FORMAT

```
[MODE: quick-fix]
[LANG: xx]
[KEYWORD: xxx]
[FIX TARGET: factor ID - factor name]

Issue:
[what's wrong]

Fix:
[what to change, with before/after]

Before:
[original text]

After:
[fixed text]

[If applicable: additional notes, trade-offs, dependencies on other factors]
```
