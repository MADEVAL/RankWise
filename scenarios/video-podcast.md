# Scenario: Video & Podcast SEO
> **Version:** 1.2.2

**Use when:** User asks to optimize YouTube video descriptions, podcast show notes, timestamps, or video metadata. Mode: GENERATE (video page) or META-ONLY (metadata).

**Pipeline:** extract topic → keyword mapping → title → description → timestamps → schema → deliver

---

## STEP 0: PLATFORM DETECTION

| Platform | Focus | Schema Type |
|----------|-------|-------------|
| **YouTube** | Title (100 chars max), description (5000 chars), tags, thumbnail alt, timestamps | VideoObject |
| **Podcast (Spotify/Apple)** | Episode title, show notes, timestamps, guest bio | Episode + PodcastSeries |
| **Vimeo / Wistia** | Title, description, tags | VideoObject |
| **Self-hosted / Web** | Title, description, transcript, schema | VideoObject + SeekToAction |

---

## STEP 1: TITLE OPTIMIZATION

### YouTube titles (max 100 chars, display ~60)
```
[Pattern]: [Number] + [Power Word] + [Keyword] + [Curiosity/Result]
```

**Examples:**
- "7 SEO Mistakes Killing Your Rankings (Fix Them in 5 Minutes)"
- "How We 3× Our Organic Traffic in 90 Days — Exact Workflow"
- "I Audited 100 SaaS Landing Pages. Here's What Crushes Conversions"

### Podcast episode titles
```
[Pattern]: [Guest Name on Topic] or [#Episode — Keyword: Hook]
```
- 50–70 characters
- Guest name (if applicable) + topic keyword
- Avoid: "Episode 47" as primary title element (bury number at end)

### Title checklist
- Primary keyword in first 5-8 words
- ≥1 power word
- ≥1 number (odd preferred)
- Clear sentiment (not neutral)
- No ALL CAPS (exception: acronyms)
- No clickbait that isn't delivered

---

## STEP 2: DESCRIPTION OPTIMIZATION

### YouTube description structure

```
[FIRST 2-3 LINES — ABOVE THE FOLD]
Hook line + what viewer learns + keyword.
These 3 lines appear before "SHOW MORE" — 157 chars max.

────────────────────────────

[BODY — EXPANDED]
What this video covers:
- Point 1 (keyword-rich)
- Point 2
- Point 3

[LINKS & RESOURCES]
- Tool/resource name: URL
- Related video: Title — URL
- Article version: URL

[TIMESTAMPS / CHAPTERS]
0:00 — Intro
0:45 — Section 1 Title
3:20 — Section 2 Title
...

[HASHTAGS]
#keyword1 #keyword2 #keyword3 (3-5 relevant)
```

### Podcast show notes structure

```
[EPISODE SUMMARY — 3-4 sentences]
Episode topic + guest name + credentials + what listener gains.
Keyword in first 2 sentences.

[WHAT YOU'LL LEARN]
- Key takeaway 1
- Key takeaway 2
- Key takeaway 3 (5-7 bullets)

[GUEST BIO]
Name, role, company, 1-line credibility highlight.

[TIMESTAMPS / CHAPTERS]
00:00 — Intro & guest background
05:30 — Topic deep dive
22:00 — Practical steps
38:00 — Key takeaways

[RESOURCES MENTIONED]
- Resource: URL (context why mentioned)

[CONNECT]
- Guest Twitter/LinkedIn
- Host info
- Subscribe link
```

### Description SEO rules
- Primary keyword in first 157 characters
- 2-4 secondary keywords naturally placed in body
- External links: DO follow, authoritative sources
- Internal links: to related videos/episodes (YouTube cards/end screens)
- Hashtags: 3-5 relevant, no more — over-hashtagging hurts

---

## STEP 3: TIMESTAMPS / CHAPTERS

### Format
```
HH:MM:SS — Chapter Title
0:00 — Introduction
1:30 — Why [Topic] Matters in 2026
5:45 — The [Number] Biggest Mistakes
12:00 — Step-by-Step: How to [Action]
22:30 — Real Examples & Results
35:00 — Your Next Steps
```

### Chapter SEO
- Each chapter title = mini-headline with keyword potential
- 5-12 chapters total
- First chapter = introduction (NOT "Intro" — use descriptive title)
- Middle chapters = core value (place keywords here)
- Final chapter = CTA / next steps

### YouTube chapters
- First timestamp MUST be 0:00
- Min 3 chapters, each ≥10 seconds
- Chapter titles appear in SERP as rich snippets — write them for click-through

---

## STEP 4: TAGS & HASHTAGS

### YouTube tags (comma-separated, 300-500 chars total)
```
Primary keyword, secondary keyword 1, secondary keyword 2, broad category, specific sub-topic, competitor channel name (if relevant), long-tail variation 1, long-tail variation 2
```

**Tag strategy:**
1. Exact primary keyword first
2. 2-3 phrase-match variations
3. Broad topic tag
4. 1-2 competitor channel names (only if truly relevant)
5. 3-4 long-tail question-form keywords

### Hashtags (for description top/bottom)
- YouTube displays top 3 above title — make them count
- Max 15, but 3-5 recommended
- Format: `#KeywordPhrase` (PascalCase or lowercase)

---

## STEP 5: THUMBNAIL ALT TEXT

If thumbnail image available:
```
[Descriptive alt text, ≤125 chars, keyword included naturally]
"Thumbnail showing 7 SEO mistakes chart with red X marks and ranking arrow going down"
```

---

## STEP 6: SCHEMA MARKUP

### VideoObject (for web-hosted video pages)
See `shared/schema-templates.md` → VideoObject pattern:

```json
{
  "@context": "https://schema.org",
  "@type": "VideoObject",
  "name": "{{VIDEO_TITLE}}",
  "description": "{{VIDEO_DESCRIPTION}}",
  "thumbnailUrl": "{{THUMBNAIL_URL}}",
  "uploadDate": "{{PUBLISH_DATE}}",
  "duration": "{{DURATION_ISO8601}}",
  "contentUrl": "{{VIDEO_URL}}",
  "embedUrl": "{{EMBED_URL}}",
  "interactionStatistic": {
    "@type": "InteractionCounter",
    "interactionType": { "@type": "WatchAction" },
    "userInteractionCount": "{{VIEW_COUNT}}"
  }
}
```

### SeekToAction (for YouTube chapters)
When using VideoObject on web: include `potentialAction` → `SeekToAction` with timestamps for rich results.

---

## STEP 7: FACTOR ADAPTATION

| Factor | Adaptation for Video/Podcast |
|--------|------------------------------|
| K1-K8 | Keyword placement applies to title, description, timestamps |
| K10 | Density 0.5-1.0% in description (shorter content) |
| C1 | Description word count: 150-300 words minimum |
| C4 | ⊘ N/A — TOC not applicable (use timestamps instead) |
| C5 | Number in title: mandatory for list-style videos |
| C6 | Power words in title: ≥2 (critical for CTR) |
| L1 | Internal links: to other videos/episodes (YouTube cards/end screens) |
| L2 | External links: to tools, studies, guest websites |
| T3 | Title length: ≤100 chars YouTube, 50-70 podcast |
| T4 | Description first 157 chars for YouTube SERP preview |
| T6 | Schema: VideoObject (web), YouTube handles schema natively |
| A1 | Featured snippet: first 2-3 description lines = featured snippet text |
| A4 | Freshness: publish date in description (YouTube auto-adds) |

---

## STEP 8: DELIVERY FORMAT

```
[MODE: meta-only / generate — video/podcast]
[LANG: xx]
[KEYWORD: xxx]
[PLATFORM: youtube / podcast / web]

====================================
TITLE (XX chars)
====================================
[Optimized title]

====================================
DESCRIPTION
====================================
[Full description as structured above]

====================================
TIMESTAMPS
====================================
[Chapter list with timestamps]

====================================
TAGS
====================================
[Comma-separated tags]

====================================
HASHTAGS
====================================
[3-5 hashtags]

====================================
SCHEMA
====================================
Type: VideoObject
(see shared/schema-templates.md)
```
