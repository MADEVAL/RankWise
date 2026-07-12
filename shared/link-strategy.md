# Link Strategy - Internal & External Linking Rules
> **Version:** 1.3.0

> Every link should have a purpose. Internal for structure. External for credibility.

---

## INTERNAL LINKS (3–10 per article)

### Why internal links matter
- Pass PageRank/link equity between pages
- Help search engines understand site structure and topic clusters
- Reduce bounce rate (users click through to more content)
- Convert informational traffic to commercial pages

### Anchor text strategy (per article)

| Type | Mix % | Example |
|------|-------|---------|
| **Partial match** | 30–40% | "SEO checklist for beginners" |
| **Branded** | 20–25% | "RankWise SEO tool" |
| **Generic / natural** | 20–25% | "as we covered earlier", "read more about" |
| **Naked URL** | 5–10% | "example.com/seo-guide" |
| **Exact match** | ≤2 total | "SEO checklist" (limit: 2 max per article) |

### Link placement rules
1. **First link within 300 words** - signals relevance early
2. **Distributed throughout** - not clustered at start or end
3. **Contextual (in-body)** - inside paragraphs, not just navigation or sidebar
4. **Natural flow** - link text reads naturally in the sentence
5. **No link farms** - each internal page linked only once (unless different context)

### What to link to
1. **Cornerstone content** - your most comprehensive pages on the topic
2. **Money pages** - product, service, pricing pages
3. **Related articles** - topic cluster pages
4. **Category/archive pages** - topic hubs
5. **About/author pages** - for E-E-A-T signals

### Link placement pattern
```
Introduction → link to cornerstone content (topic authority)
H2 Section 1 → link to related article (depth)
H2 Section 2 → link to money page (commercial intent)
H2 Section 3 → link to related article (depth)
H2 Section 4 → link to case study / example (social proof)
Conclusion → link to next-step content (funnel)
```

### Internal link DON'Ts
- Do NOT use exact same anchor text for 3+ links
- Do NOT link to irrelevant pages just to hit count
- Do NOT link every instance of a keyword
- Do NOT put all links in the last paragraph
- Do NOT use footer links as substitute for body links

---

## EXTERNAL LINKS (2–5 per article)

### Why external links matter
- Signal to search engines: you cite sources, you're thorough
- Build topical authority through association
- Users trust content with verifiable citations
- Potential for backlinks in return (ego bait)

### Authority criteria
Link to sources that are:
- **Domain Authority 40+** (or recognized authority in niche)
- **Original source** - not a blog that reposted a study
- **Recent** - studies from last 2–3 years (unless citing seminal work)
- **Non-competitor** - informational sources, tools, data, not direct business competitors

### External link types

| Type | Example | Best for |
|------|---------|----------|
| **Research/Data** | Original study, government data, survey results | Backing claims |
| **Tools/Calculators** | Free tools readers can use | Utility value |
| **Definitions** | Wikipedia, official documentation | Clarifying terms |
| **Case Studies** | Other companies' published results (not competitors) | Inspiration |
| **News/Publications** | Reputable industry publications | Timeliness |
| **Expert Opinions** | Recognized expert blog posts (not self-promotion) | Authority |

### DoFollow vs NoFollow
- **At least 1 DoFollow external link** - signal of confidence
- **NoFollow** - for sponsored, affiliate, user-generated, or untrusted links
- **Default:** DoFollow unless there's a reason to NoFollow
- Never NoFollow ALL external links - looks unnatural

### External link attributes
```html
<a href="https://example.com" target="_blank" rel="noopener noreferrer">Anchor Text</a>
```
- `target="_blank"` - opens in new tab (standard for external links)
- `rel="noopener noreferrer"` - security best practice
- `rel="nofollow"` - only when intentionally distancing (paid, UGC, untrusted)

---

## OUTBOUND LINK STRATEGY BY CONTENT TYPE

### Informational article
- 3–5 external: 2 data sources, 1 tool/resource, 1 expert reference
- 5–8 internal: cornerstone, 2 related articles, money page, case study

### Commercial/product page
- 1–2 external: 1 industry report, 1 tool comparison (if relevant)
- 3–5 internal: case studies, testimonials page, pricing, FAQ, blog posts

### Review/comparison
- 2–4 external: subject of review, alternative options, industry standard
- 3–6 internal: related reviews, buying guide, product page, blog

### How-to/tutorial
- 2–4 external: official docs, tools mentioned, reference material
- 4–8 internal: related tutorials, prerequisite guides, advanced guides, product

---

## TOPIC CLUSTER STRATEGY

### Pillar page → Cluster pages
- Pillar page links OUT to all cluster pages
- Each cluster page links BACK to the pillar page
- Cluster pages interlink with related cluster pages

### Implementation pattern
```
Pillar: "Complete SEO Guide" (10,000 words)
  ├── Cluster: "SEO Checklist" → links to Pillar + "Keyword Research" cluster
  ├── Cluster: "Keyword Research Guide" → links to Pillar + "SEO Checklist"
  ├── Cluster: "On-Page SEO" → links to Pillar
  └── Cluster: "Technical SEO" → links to Pillar + "On-Page SEO"
```

---

## LINK AUDIT QUICK CHECK

Before delivering any content, verify:
1. ☐ At least 3 internal links (in-body, contextual)
2. ☐ At least 2 external links (authoritative sources)
3. ☐ At least 1 DoFollow external link
4. ☐ No more than 2 exact-match anchor texts
5. ☐ First link within 300 words
6. ☐ Links distributed throughout (not clustered)
7. ☐ No broken links (verify if possible)
8. ☐ External links open in new tab with `rel="noopener"`
9. ☐ Internal links are topically relevant
10. ☐ Page has at least 1 incoming link from another page (orphan check)
