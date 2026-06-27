# Schema Templates - JSON-LD Structured Data
> **Version:** 1.2.2

> Copy-paste-ready templates for every content type.
> Add to `<head>` or inject via RankWise when generating.

---

## Article

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "{{SEO_TITLE}}",
  "description": "{{META_DESCRIPTION}}",
  "image": "{{FEATURED_IMAGE_URL}}",
  "author": {
    "@type": "Person",
    "name": "{{AUTHOR_NAME}}",
    "url": "{{AUTHOR_URL}}"
  },
  "publisher": {
    "@type": "Organization",
    "name": "{{SITE_NAME}}",
    "logo": {
      "@type": "ImageObject",
      "url": "{{LOGO_URL}}"
    }
  },
  "datePublished": "{{PUBLISH_DATE}}",
  "dateModified": "{{MODIFIED_DATE}}",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "{{PAGE_URL}}"
  }
}
```

---

## BlogPosting (extends Article)

```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "{{SEO_TITLE}}",
  "description": "{{META_DESCRIPTION}}",
  "image": "{{FEATURED_IMAGE_URL}}",
  "author": {
    "@type": "Person",
    "name": "{{AUTHOR_NAME}}",
    "url": "{{AUTHOR_URL}}"
  },
  "publisher": {
    "@type": "Organization",
    "name": "{{SITE_NAME}}",
    "logo": {
      "@type": "ImageObject",
      "url": "{{LOGO_URL}}"
    }
  },
  "datePublished": "{{PUBLISH_DATE}}",
  "dateModified": "{{MODIFIED_DATE}}",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "{{PAGE_URL}}"
  }
}
```

---

## Product

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "{{PRODUCT_NAME}}",
  "description": "{{PRODUCT_DESCRIPTION}}",
  "image": "{{PRODUCT_IMAGE_URL}}",
  "sku": "{{SKU}}",
  "brand": {
    "@type": "Brand",
    "name": "{{BRAND_NAME}}"
  },
  "offers": {
    "@type": "Offer",
    "url": "{{PRODUCT_URL}}",
    "priceCurrency": "{{CURRENCY}}",
    "price": "{{PRICE}}",
    "priceValidUntil": "{{PRICE_VALID_DATE}}",
    "availability": "https://schema.org/{{InStock|OutOfStock|PreOrder}}",
    "itemCondition": "https://schema.org/NewCondition"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "{{RATING}}",
    "reviewCount": "{{REVIEW_COUNT}}"
  }
}
```

---

## FAQPage (for search engine FAQ rich results)

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "{{QUESTION_1}}",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "{{ANSWER_1}}"
      }
    },
    {
      "@type": "Question",
      "name": "{{QUESTION_2}}",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "{{ANSWER_2}}"
      }
    }
  ]
}
```

**Rules for FAQ schema:**
- Only use if the page has a genuine FAQ section
- Questions must be actual user questions (not fabricated)
- Answers must be on the page as visible text - not hidden
- Min 1 question, max unlimited (but 3–8 is ideal)
- Search engines show max 2 FAQ items in rich results (can expand)

---

## HowTo (for step-by-step content)

```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "{{HOW_TO_TITLE}}",
  "description": "{{HOW_TO_DESC}}",
  "image": "{{FEATURED_IMAGE}}",
  "totalTime": "{{TIME}}",
  "supply": [
    {
      "@type": "HowToSupply",
      "name": "{{TOOL_1}}"
    }
  ],
  "tool": [
    {
      "@type": "HowToTool",
      "name": "{{TOOL_2}}"
    }
  ],
  "step": [
    {
      "@type": "HowToStep",
      "position": "1",
      "name": "{{STEP_1_TITLE}}",
      "text": "{{STEP_1_DESC}}",
      "image": "{{STEP_1_IMAGE}}",
      "url": "{{STEP_1_URL}}"
    },
    {
      "@type": "HowToStep",
      "position": "2",
      "name": "{{STEP_2_TITLE}}",
      "text": "{{STEP_2_DESC}}"
    }
  ]
}
```

**Rules for HowTo schema:**
- Each step must have visible text on the page
- Images per step: optional but recommended
- Search engines show HowTo rich results for step-by-step content
- Steps must be ordered (position property)

---

## Review

```json
{
  "@context": "https://schema.org",
  "@type": "Review",
  "itemReviewed": {
    "@type": "{{TYPE}}",
    "name": "{{ITEM_NAME}}"
  },
  "author": {
    "@type": "Person",
    "name": "{{REVIEWER_NAME}}"
  },
  "reviewRating": {
    "@type": "Rating",
    "ratingValue": "{{RATING}}",
    "bestRating": "5"
  },
  "datePublished": "{{PUBLISH_DATE}}",
  "reviewBody": "{{REVIEW_SUMMARY}}"
}
```

---

## BreadcrumbList

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "{{HOME_URL}}"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "{{CATEGORY_NAME}}",
      "item": "{{CATEGORY_URL}}"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "{{PAGE_TITLE}}",
      "item": "{{PAGE_URL}}"
    }
  ]
}
```

---

## LocalBusiness

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "{{BUSINESS_NAME}}",
  "image": "{{IMAGE_URL}}",
  "@id": "{{PAGE_URL}}",
  "url": "{{WEBSITE_URL}}",
  "telephone": "{{PHONE}}",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "{{STREET}}",
    "addressLocality": "{{CITY}}",
    "addressRegion": "{{STATE}}",
    "postalCode": "{{ZIP}}",
    "addressCountry": "{{COUNTRY}}"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "{{LAT}}",
    "longitude": "{{LNG}}"
  },
  "openingHoursSpecification": {
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "opens": "09:00",
    "closes": "18:00"
  },
  "priceRange": "{{PRICE_RANGE}}"
}
```

---

## Person (Author bio)

```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "{{PERSON_NAME}}",
  "url": "{{PROFILE_URL}}",
  "image": "{{PHOTO_URL}}",
  "jobTitle": "{{JOB_TITLE}}",
  "worksFor": {
    "@type": "Organization",
    "name": "{{COMPANY_NAME}}"
  },
  "sameAs": [
    "{{LINKEDIN_URL}}",
    "{{TWITTER_URL}}"
  ]
}
```

---

## SCHEMA SELECTION LOGIC

| Content Type | Schema |
|-------------|--------|
| News article, blog post | Article / BlogPosting |
| "How to" guide, tutorial | HowTo |
| Page with FAQ section | FAQPage |
| Product page (e-commerce) | Product + Offer |
| Review of product/service | Review |
| Recipe | Recipe |
| Local business page | LocalBusiness |
| About page with author info | Person |
| All pages | BreadcrumbList |
| Contact page | ContactPage |
| Event page | Event |
| Video content | VideoObject |
| Course / educational | Course |

---

## VALIDATION

Always validate schema before delivery:
1. Check required fields are present
2. Check date formats: `YYYY-MM-DD` or ISO 8601
3. Check URL formats: absolute URLs (https://)
4. Check price: number only, no currency symbol in price field
5. Validate schema using search engine rich results testing tools
