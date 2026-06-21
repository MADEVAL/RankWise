# Scenario: Home Page

**Use when:** User asks to generate, rewrite, or audit a home page. Content type: navigational/brand.

**Pipeline:** intent → brand messaging → structure → SEO signals → deliver

---

## STEP 0: HOME PAGE SPECIFICS

Unlike articles, home pages have:
- Brand name as primary keyword (not a long-tail phrase)
- Multiple service/product keywords competing for space
- Heavy design dependency (hero, CTAs, trust signals)
- Minimal body text — every word counts double

### Multi-keyword strategy
A home page typically targets 3–5 keywords:
- Primary: brand name
- Secondary: main service/category (1–2)
- Tertiary: location or sub-service (1–2)

**Example:** Brand "TaskFlow" → Primary: TaskFlow | Secondary: "project management software", "team collaboration tool" | Tertiary: "for remote teams"

---

## STEP 1: STRUCTURE BLUEPRINT

### H1
- Brand name + main value prop (not keyword-stuffed)
- "TaskFlow — Project Management Software for Remote Teams" (not "TaskFlow Project Management Software Team Collaboration Tool")

### Above-fold content
- Hero: H1 + tagline + CTA (3 elements, ≤50 words total)
- Trust signals: numbers (customers, countries, uptime) in hero area
- CTA: specific action verb, not "Learn More"

### Body sections (3–5 H2s)
1. **What we do** — 2-3 sentence value prop. Primary service keyword naturally.
2. **How it works / Features** — 3 key features. Bullet points, not paragraphs. Secondary keywords.
3. **Social proof** — Numbers, logos, testimonials. Not "trusted by thousands" — "Used by 3,400 teams in 42 countries."
4. **Pricing / Plans** — Anchor with highest tier first.
5. **CTA** — Final conversion push.

### Keywords per section
- H1: brand name + primary service keyword
- H2 "What we do": primary service keyword
- H2 "Features": 1-2 secondary keywords in H3s
- Never stuff the brand name — it appears in H1, footer, and logo (already present visually)

---

## STEP 2: META LAYER

### SEO Title
```
[Brand Name] — [Primary Service Keyword] | [Unique Selling Point]
```
- 50–60 characters
- Brand first (navigational intent)
- Service keyword second

### Meta Description
- Brand + what they do + who it's for + social proof number
- "TaskFlow: project management software built for remote teams. Task tracking, time estimates, team chat. Used by 3,400+ teams."

### URL
- Root domain (/) — no slug needed
- If sub-page: /about, /features, /pricing

---

## STEP 3: TECHNICAL SIGNALS

- Schema: Organization + WebSite + SearchAction
- OG tags: brand name, tagline, logo image
- Internal links: to key service/product pages (3–5 links)
- External links: minimal (home pages rarely link out)
- No TOC (not applicable)
- Images: logo + hero image (max 2-3). Alt texts: descriptive + brand name.

---

## STEP 4: FACTOR ADAPTATION

Factors that work differently for home pages:

| Factor | Adaptation |
|--------|-----------|
| K1 | Brand name IS the primary keyword |
| K10 | Density 0.3–0.5% (brand appears sparsely — logo + footer suffice) |
| C1 | 300–500 words acceptable (home pages are lean by design) |
| C3 | ⊘ N/A — images are design elements, not content |
| C4 | ⊘ N/A — no TOC on home pages |
| C5 | Number in H1/tagline (trust signal) |
| L1 | Link to service pages, not blog posts |
| L2 | 0–2 external links acceptable |
| T1 | URL is root (/) — perfect by default |

---

## STEP 5: DELIVERY

### Generate Mode
```
[MODULES: text + meta + alts]

H1: [brand + value prop]
Tagline: [one-liner]
Hero CTA: [button text]

[Body — 3-5 H2 sections as above]

SEO Title: [brand — keyword | USP]
Meta Description: [brand + what + who + proof]
OG: [brand + tagline]
URL: /
Alt Texts:
1. [logo description with brand name]
2. [hero image description]
```

### Audit Mode — additional checks
- Is brand name present in H1, title, description, OG?
- Is there exactly 1 H1?
- Are service keywords naturally distributed (not stuffed into every sentence)?
- Is schema type Organization (not Article)?
- Are trust signals specific (numbers, not adjectives)?
