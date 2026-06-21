# Example: Complete Audit Report (v1.1 — Weighted Scoring)

**Mode:** AUDIT
**Language:** en
**Keyword:** "project management software"
**Content:** 520-word product page

---

```
[MODE: audit]
[LANG: en]
[KEYWORD: project management software]
[WEIGHTED SCORE: 11.9% (8.0/67.5 weighted points)]
[RAW SCORE: 7/46 applicable factors]
[GRADE: F] [Constraint: 4 CRITICAL failures → grade capped at F regardless of weighted %]

====================================
NOT APPLICABLE (excluded from score)
====================================
⊘ C4: Table of Contents — not applicable to product page (<800 words)
⊘ L4: Anchor variety — only 1 link, cannot assess variety
⊘ L8: Orphan check — cannot verify without site access

====================================
CRITICAL FAILURES — Fix Now (×3 weight each)
====================================
❌ K1: Focus keyword set — Provided by user, but NOT present in any on-page element
❌ K2: Keyword in SEO title — Title is "TaskPro" (brand only, no keyword)
   Fix: Change to "TaskPro: Project Management Software for Remote Teams"
❌ K4: Keyword in meta description — Description missing entirely
   Fix: Add: "Project management software built for remote teams. Task tracking, time estimates, and team chat in one tool. Start free."
❌ K7: Keyword in body — Only appears once (in footer text)
   Fix: Add keyword to hero section and first feature description block

====================================
HIGH PRIORITY — Fix This Week (×2 weight each)
====================================
❌ K3: Keyword near title beginning — Brand-first title pushes keyword out
❌ K5: Keyword in URL — URL is /products/taskpro
   Fix: Change to /project-management-software
❌ K6: Keyword at content start — First 150 words don't contain keyword
❌ K8: Keyword in subheadings — No H2s contain keyword
❌ K10: Keyword density — 0.1% (1 instance in 520 words)
❌ K11: Cannibalization — Cannot verify without site access. ⚠️ Verify manually: site:taskpro.com "project management software"
⚠️ K12: Keyword length — "project management software" is 3 words (acceptable range)
❌ C1: Word count — 520 words (below 600 minimum)
❌ C8: Readability — Grade 13 (avg sentence ~24 words; target Grade 7–9)
⚠️ C9: Passive voice — 18% of sentences (target ≤10%)
❌ C13: Heading hierarchy — H1 present, then H3 (skips H2 entirely)
❌ L1: Internal links — Only 1 link (target 3–10)
❌ L2: External links — 0 links (target 2–5)
⚠️ T3: Title length — 7 chars (target 50–60 for EN)
❌ T4: Description length — Missing entirely (target 145–158 for EN)
⚠️ A2: E-E-A-T signals — No author bio, no publication date, no citations

====================================
MEDIUM PRIORITY — Improve (×1 weight each)
====================================
⚠️ C2: Short paragraphs — 3 paragraphs exceed 150 words
⚠️ C3: Images — 2 images for 520 words (need ~2; borderline pass)
⚠️ C5: Number in title — No number present
⚠️ C6: Power words in title — 0 power words (target ≥2)
⚠️ C11: Sentence variety — 5 consecutive sentences within ±2 words of each other
⚠️ L5: Outbound quality — No external links to assess → ⚠️ Warning
⚠️ T1: URL length — 16 chars (under 75, but lacks keyword)
⚠️ T6: Schema markup — No JSON-LD found. Add Product schema.
⚠️ A1: Featured snippet — No concise answer paragraph
⚠️ A3: LSI keywords — Only 2 related terms found (need 5–15)
⚠️ A5: Mobile readability — Paragraphs render as 7+ lines on mobile (proxy: multiple paragraphs >120 words)
⚠️ C12: Consecutive sentence starts — 4 consecutive sentences start with "The" — variety needed

====================================
LOW PRIORITY — Optional (×0.5 weight each)
====================================
⚠️ C7: Sentiment — Neutral title (missed CTR opportunity)
⚠️ C10: Transition words — 22% of sentences (target ≥30% EN)
⚠️ L9: Link title attributes — No title="" attributes on links
⚠️ T5: Image file names — "screenshot1.png", "hero.jpg" (not descriptive)
⚠️ T8: OG / Twitter Card tags — Not present
⚠️ A4: Content freshness — No date visible
⚠️ A6: Breadcrumb — No breadcrumb markup or navigation visible

====================================
PASSED FACTORS (7/46 applicable)
====================================
✅ K9: Keyword in alt text (screenshot alt text contains keyword)
✅ C14: Content-to-ad ratio (clean — no ads, main content above fold)
✅ L3: DoFollow external (the 1 internal link is DoFollow — 1 of 1)
✅ L6: No broken links (1 link verified)
✅ L7: Internal relevance (link points to related feature page)
✅ T2: URL structure (hyphens used, lowercase)
✅ T7: Canonical URL (default self-canonical — acceptable for single page)

====================================
WEIGHTED SCORE BREAKDOWN
====================================
PASSED weights:    7 PASS × multipliers = 8.0
TOTAL weights:    46 applicable × multipliers = 67.5
Score:             8.0 / 67.5 = 11.9%
Constraint:        4 CRITICAL failures → grade F

====================================
ESTIMATED IMPACT
====================================
Fixing Critical only (4 factors):         +45% ranking potential
Fixing Critical + High (18 factors):      +65% ranking potential
Fixing all (33 factors):                  +80% ranking potential

====================================
TOP 5 ACTIONS (Do These First)
====================================
1. Rewrite SEO title to: "TaskPro: Project Management Software for Remote Teams"
   Impact: Critical (×3) | Effort: Low (5 min)

2. Add meta description with keyword in first 20 words
   Impact: Critical (×3) | Effort: Low (5 min)

3. Add keyword naturally to hero section + 2 H2 headings
   Impact: High (×2 each for K6, K7, K8) | Effort: Medium (30 min)

4. Change URL slug to include keyword (/project-management-software)
   Impact: High (×2 for K5) | Effort: Medium (needs 301 redirect)

5. Expand content from 520 to 800+ words with feature details + proper H2 structure
   Impact: High (×2 for C1) + fixes C13 | Effort: High (2–3 hrs)
```
