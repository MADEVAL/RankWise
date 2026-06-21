# Scenario: Product Page

**Use when:** User asks to generate, rewrite, or audit a product page, service page, or e-commerce listing.

**Pipeline:** product analysis → feature-benefit mapping → structure → SEO signals → deliver

---

## STEP 1: PRODUCT KEYWORD STRATEGY

### Primary keyword
- Product name or "[category] [product type]" — e.g., "ErgoFlex Office Chair" or "ergonomic office chair"
- If product has a unique name: brand + product name is primary
- If generic product: "[main feature] + [product category]" is primary

### Secondary keywords
- Use case keywords: "office chair for back pain", "adjustable lumbar support chair"
- Feature keywords: "mesh office chair", "headrest office chair"
- Intent keywords: "buy ergonomic chair", "best office chair 2026"

### Keyword placement
- Primary in: title, meta, H1, first 100 words, product specs section
- Secondary in: feature H3s, use-case sections
- Do NOT over-stuff the product name — density 0.8–1.2% (product names are naturally repeated)

---

## STEP 2: STRUCTURE BLUEPRINT

### H1
`[Product Name] — [Primary Benefit in One Line]`
- 50–70 characters
- Product name first, benefit second
- Example: "ErgoFlex Pro — The Office Chair That Actually Fixes Back Pain"

### Body sections (5–8 H2s)

1. **Overview / Introduction** (~100 words)
   - What the product is, who it's for, primary benefit
   - Primary keyword in first 100 words

2. **Key Features** (3–5 H3s)
   - Each H3 = one feature → benefit → proof
   - "Adjustable Lumbar Support" → "Your lower back stays supported through 8-hour days" → "Rated #1 by 200+ physiotherapists"
   - Secondary keywords in H3s

3. **Technical Specifications** (table or list)
   - Dimensions, weight, materials, compatibility
   - Keyword in section heading: "[Product Name] Specifications"

4. **Use Cases / Who It's For** (2–3 paragraphs)
   - "For remote workers", "For programmers", "For executives"
   - Secondary intent keywords

5. **Comparison** (vs alternatives or vs previous model)
   - Table format: feature | ErgoFlex | Generic Chair
   - Anchoring: show why premium price = premium value

6. **Reviews / Social Proof** (3–5 testimonials)
   - Name, role, specific result: "My back pain disappeared in 2 weeks. — Mark D., Software Engineer"
   - Aggregate rating: "4.8/5 from 1,200+ reviews"

7. **Pricing & Guarantee**
   - Anchor with premium tier first
   - Risk reversal: "30-day trial. If your back still hurts, return it. Full refund."

8. **FAQ** (3–5 questions)
   - Real customer questions
   - FAQPage schema opportunity

---

## STEP 3: META LAYER

### SEO Title (50–60 chars)
```
[Product Name] — [Primary Benefit] | [Brand]
```
- "ErgoFlex Pro — Ergonomic Office Chair for Back Pain | ErgoFlex"

### Meta Description (145–158 chars)
- Product + primary benefit + key feature + social proof + CTA
- "ErgoFlex Pro: ergonomic office chair designed by physiotherapists. Adjustable lumbar support, mesh back, 12-year warranty. Rated 4.8/5. Free shipping."

### URL Slug
- `/product-name` (clean, no category path unless hierarchy is intentional)
- "/ergoflex-pro-office-chair" not "/products/chairs/ergoflex-pro-office-chair-2026"

---

## STEP 4: E-COMMERCE SIGNALS

- **Schema:** Product + Offer + AggregateRating + Review
- **Images:** ≥5 (main + angles + lifestyle + specs). Alt texts: product name + angle/feature.
- **Price:** Visible, with currency. Sale price + original price for anchoring.
- **Availability:** "In Stock" + quantity urgency (if genuine): "Only 7 left"
- **Breadcrumb:** Home > Category > Product
- **Internal links:** Related products, category page, comparison page
- **External links:** Review sites, award pages, press mentions

---

## STEP 5: FACTOR ADAPTATION

| Factor | Adaptation for Product Pages |
|--------|------------------------------|
| C1 | 600–1200 words (features + specs + reviews add up) |
| C3 | 5+ images expected (product photography) |
| C4 | ⊘ N/A — TOC not applicable |
| C5 | Price = number in content (satisfies the factor naturally) |
| C6 | Power words in H1 and feature headings |
| K10 | 0.8–1.2% for product name (higher is acceptable for e-commerce) |
| L1 | Link to category, related products, comparison pages |
| T6 | Product schema mandatory |
| A1 | Price + availability in featured snippet format |

---

## STEP 6: DELIVERY

Output follows standard module format (TEXT → META → ALTS). Include schema recommendation as a separate block:

```
[MODULES: text + meta + alts]

[Product page content as structured above]

---
[SCHEMA]
Type: Product + Offer + AggregateRating
(see shared/schema-templates.md)
```
