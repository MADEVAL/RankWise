# Scenario: Audit Report

**Use when:** User asks to audit, review, score, or check SEO. Mode: AUDIT.

**Pipeline:** parse content → score all factors → prioritize → report → recommend

---

## STEP 0: PARSE CONTENT

Extract from provided content:
- Title / H1
- Meta title (if provided separately)
- Meta description (if provided)
- URL slug (if provided)
- All headings (H1, H2, H3, H4)
- Body word count
- Image count + existing alt texts
- Internal links count + anchors
- External links count + anchors
- Keyword (from user, or inferred from title/H1)

If keyword not provided, flag K1 as FAIL and note: "No focus keyword specified. Recommend: [best guess from title]."

---

## STEP 1: SCORE ALL FACTORS

Score all 49 factors from `shared/checklist.md`:

- ✅ **Pass** — meets or exceeds target
- ❌ **Fail** — below target, needs fix
- ⚠️ **Warning** — borderline or partially met
- ⊘ **N/A** — not applicable to this content type

**N/A handling:** Exclude N/A factors from denominator. Example: content with no images → K9, C3 → N/A → denominator is 47, not 49. Product pages → C4 (TOC) → N/A. Always explain why a factor was marked N/A in the report.

**Weighted score formula:**
```
Raw Score (%) = (Σ(PASS_WEIGHTS) / Σ(ALL_WEIGHTS)) × 100
```
Where PASS_WEIGHTS sum the multipliers (CRITICAL=×3, HIGH=×2, MEDIUM=×1, LOW=×0.5) of all ✅ and ⚠️ factors, and ALL_WEIGHTS sums multipliers of all non-N/A factors. ⚠️ counts as 50% pass (half weight).

**Grade constraints:**
- A (90%+) requires 0 CRITICAL failures
- B (75–89%) requires ≤1 CRITICAL failure
- C (60–74%) requires ≤3 CRITICAL failures
- D/F: no constraint beyond raw score

### Scoring reference

| Factor | Check | Pass Condition |
|--------|-------|---------------|
| K1 | Keyword defined | User provided or clearly inferable from title |
| K2 | Keyword in SEO title | Case-insensitive match in title string |
| K3 | Keyword near title start | Keyword appears within first 5 words of title |
| K4 | Keyword in meta description | Case-insensitive match in description |
| K5 | Keyword in URL | Case-insensitive match in slug |
| K6 | Keyword at content start | Match in first ~150 words of body |
| K7 | Keyword in body | Any match in body content |
| K8 | Keyword in subheading | Match in any H2 or H3 |
| K9 | Keyword as alt text | Match in any image alt attribute |
| K10 | Keyword density | Count occurrences / total words × 100. 0.8%–1.5% = pass |
| K11 | Cannibalization check | If site access: search site for keyword. If no access: flag ⚠️ "Verify manually: site:domain.com keyword" |
| K12 | Keyword length | 3+ chars AND ≤7 words |
| C1 | Word count | Total words ≥600 |
| C2 | Short paragraphs | Avg paragraph ≤150 words AND ≤3 sentences |
| C3 | Images/videos | Count. ≥1 per 300 words. If no images present, mark ⊘ N/A and note recommendation. |
| C4 | Table of Contents | Present (for articles >800 words). For product/landing pages <800 words: ⊘ N/A. |
| C5 | Number in title | Regex digit found in title |
| C6 | Power words in title | ≥2 from `shared/power-words.md` found |
| C7 | Sentiment | Title has positive or negative polarity (not neutral) |
| C8 | Readability | Approximate: avg sentence length 12–20 words = Grade 7–9. >22 words avg = Grade 12+. See `shared/readability-params.md`. |
| C9 | Passive voice | Count passive / total sentences × 100 ≤10% |
| C10 | Transition words | Count sentences with transitions / total × 100. EN: ≥30%, non-EN: ≥25% (see `shared/readability-params.md`) |
| C11 | Sentence variety | Check 3-consecutive rule violation |
| C12 | Sentence starts | Check 3-consecutive same first word |
| C13 | Heading hierarchy | H1→H2→H3 proper, no skips |
| C14 | Content-to-ad ratio | Proxy: first ~300 words of content — count sentences that are ads, nav, sidebar, or boilerplate vs. main content. >20% ad/nav = ❌ Fail. Text-only view unavailable → ⚠️ "Verify on rendered page." |
| L1 | Internal links | Count ≥3 |
| L2 | External links | Count ≥2 |
| L3 | DoFollow external | Count DoFollow ≥1 |
| L4 | Anchor variety | Count exact-match anchors ≤2 |
| L5 | Outbound quality | Proxy: check domain for .edu, .gov, Wikipedia, HBR, major publications, or known trusted brands. If domain is unknown → ⚠️ Warning (not ❌ Fail) unless obviously spam/low-quality. No arbitrary DA threshold required. |
| L6 | Broken links | If web access: verify. If no access: flag ⚠️ "Verify links manually." |
| L7 | Internal relevance | Proxy: linked page title/H1 shares topic words with linking paragraph. If no access to linked pages: ⚠️ Warning. |
| L8 | Orphan check | If site access: check incoming links. If no access: mark ⊘ N/A |
| L9 | Link title attributes | Check for `title=""` attribute on ≥2 in-body links |
| T1 | URL length | Characters ≤75 |
| T2 | URL structure | Hyphens, keyword present, no stop words |
| T3 | Title length | Characters within per-language range (see `shared/readability-params.md` Meta Length table). Default EN: 50–60. |
| T4 | Description length | Characters within per-language range. Default EN: 145–158. |
| T5 | Image file names | Descriptive, hyphenated (if visible in content) |
| T6 | Schema markup | Appropriate schema present (if visible in source). If no source access: flag ⚠️ "Verify schema with search engine rich results testing tools" |
| T7 | Canonical URL | Set (if visible in source). If no source access: ⊘ N/A |
| T8 | OG / Twitter Card tags | OG title + description present, and/or twitter:card present. Pass if either OG tags (title+desc) OR twitter:card meta tags are present. |
| A1 | Featured snippet | 40–60 word concise answer paragraph present |
| A2 | E-E-A-T signals | ≥3 of 5 present: (1) author name + bio with credentials, (2) publication/modified date visible, (3) at least 1 credible external citation/source, (4) about/site-info page reference, (5) contact info or privacy policy link. 3+ = ✅ Pass, 2 = ⚠️ Warning, 0–1 = ❌ Fail. |
| A3 | LSI keywords | 5–15 related terms present. If web access: cross-reference "Searches related to". If no access: check for natural topic vocabulary diversity. |
| A4 | Freshness | Date visible |
| A5 | Mobile readability | Proxy: all paragraphs ≤150 words AND headings spaced every 200–350 words |
| A6 | Breadcrumb | Breadcrumb markup or visible breadcrumb navigation (if visible)

---

## STEP 2: PRIORITIZE FAILURES

Group all ❌ and ⚠️ by severity:

### CRITICAL — Fix Now (blocks ranking)
- K1: No keyword
- K2: Keyword missing from title
- K4: Keyword missing from meta description
- K7: Keyword missing from body

### HIGH — Fix This Week (major ranking impact)
- K3, K5, K6, K8, K10, K11, K12 — remaining keyword factors
- C1 — word count below 600
- C8 — poor readability
- C13 — broken heading hierarchy
- L1 — too few internal links
- L2 — too few external links
- L6 — broken links
- T3, T4 — title/description length off
- A2 — missing E-E-A-T signals

### MEDIUM — Improve (noticeable impact over time)
- K9 — keyword in alt text
- C2, C3, C5, C6, C9, C11, C12, C14 — content quality
- L3, L4, L5, L7 — linking quality
- T1, T2, T6 — technical
- A1, A3, A5 — advanced signals

### LOW — Optional (marginal)
- C4, C7, C10 — content polish
- L8, L9 — link polish
- T5, T7, T8 — minor technical
- A4, A6 — minor signals

---

## STEP 3: ESTIMATE IMPACT

Per fix category:
- Fixing CRITICAL factors: +30–50% ranking improvement potential
- Adding HIGH fixes: +20–30% additional
- Adding MEDIUM fixes: +10–20% additional
- Adding LOW fixes: +5–10% additional

---

## STEP 4: REPORT FORMAT

**Pre-delivery validation:** Before outputting the final report, verify: N/A_COUNT + CRITICAL_COUNT + HIGH_COUNT + MEDIUM_COUNT + LOW_COUNT + PASSED_COUNT = 49. If the sum is not 49, a factor was missed — re-scan until all 49 are accounted for.

```
[MODE: audit]
[LANG: xx]
[KEYWORD: xxx or "NOT SET"]
[WEIGHTED SCORE: XX.X% (XX.X/XX.X weighted points)]
[RAW SCORE: XX/XX applicable factors]
[GRADE: A/B/C/D/F] [Constraint: X CRITICAL failures → capped at X]

====================================
NOT APPLICABLE (excluded from score)
====================================
⊘ [Factor ID]: [Reason for exclusion]
...

====================================
CRITICAL FAILURES — Fix Now (×3 weight)
====================================
❌ [Factor ID]: [Factor name] — [Current state] → [Target]
   Fix: [1-2 sentence instruction]
...

====================================
HIGH PRIORITY — Fix This Week (×2 weight)
====================================
❌ [Factor ID]: ...
⚠️ [Factor ID]: ...
...

====================================
MEDIUM PRIORITY — Improve (×1 weight)
====================================
❌ [Factor ID]: ...
⚠️ [Factor ID]: ...
...

====================================
LOW PRIORITY — Optional (×0.5 weight)
====================================
⚠️ [Factor ID]: ...
...

====================================
PASSED FACTORS (XX/XX applicable)
====================================
✅ K2, K7, C2, ... (list all passing)

====================================
ESTIMATED IMPACT
====================================
Fixing Critical only:     +XX% ranking potential
Fixing Critical + High:   +XX% ranking potential
Fixing all:               +XX% ranking potential

====================================
TOP 5 ACTIONS (Do These First)
====================================
1. [Action] — [Impact: Critical/High/Medium] — [Effort: Low/Med/High]
2. ...
```
