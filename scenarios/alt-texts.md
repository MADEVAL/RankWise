# Scenario: Alt Texts
> **Version:** 1.3.0

**Use when:** User asks for image alt texts. Provides images as array, inline markdown, HTML, or JSON. Mode: META-ONLY (media layer).

**Pipeline:** extract images → identify context → generate alt texts → apply SEO rules → deliver in same format

---

## INPUT FORMATS ACCEPTED

### Format 1: Plain array
```
["Image of a desk with laptop", "Screenshot of analytics dashboard", "Photo of team meeting"]
```

### Format 2: Inline markdown
```
![old alt text](image1.jpg)
![another alt](image2.png)
```

### Format 3: HTML
```
<img src="image1.jpg" alt="old alt text">
<img src="image2.png" alt="">
```

### Format 4: JSON with metadata
```
[
  {"src": "image1.jpg", "alt": "old alt", "context": "hero image for SEO article"},
  {"src": "image2.png", "alt": "", "context": "screenshot of tool"}
]
```

### Format 5: With focus keyword
```
Focus keyword: "SEO checklist"
Images: ["chart showing ranking factors", "screenshot of audit tool", "person writing content"]
```

---

## ALT TEXT RULES

### SEO requirements
- At least 1 image: focus keyword in alt text (natural, not stuffed)
- Length: ≤125 characters
- Descriptive: what is IN the image, not just what it represents
- No keyword stuffing: "SEO checklist SEO audit SEO ranking factors checklist" ❌
- No "image of...", "picture of...", "photo of..." (redundant - screen readers already announce it's an image). Exception: descriptive type labels like "Bar chart of...", "Infographic of...", "Diagram of..." ARE acceptable - they describe content type, not the medium.
- Empty alt (`alt=""`) only for purely decorative images

### Accessibility requirements
- Convey the same information a sighted user would get
- For screenshots with text: include the key text from the screenshot
- For charts/graphs: summarize the data trend (not just "chart")
- For logos: "[Company Name] logo"
- For icons: describe the action/meaning, not the shape ("search" not "magnifying glass")
- For portraits: person's name if known, or descriptive role

### Per-image-type patterns

| Image Type | Pattern | Example |
|-----------|---------|---------|
| **Screenshot** | [Tool name] [screen name] showing [key data/element] | "Search performance report showing 40% traffic increase over 6 months" |
| **Chart/Graph** | [Chart type] of [data subject] showing [trend] from [period] | "Bar chart of SEO ranking factors by importance score from 2026 study" |
| **Product photo** | [Product name] in [context/setting] with [key feature visible] | "Blue ergonomic office chair with adjustable lumbar support in home office" |
| **Person/Portrait** | [Name or role] [action if applicable] at [location/event] | "Sarah Chen, SEO Director, presenting keyword research at industry conference" |
| **Infographic** | Infographic explaining [topic] with [key points] | "Infographic of 45 SEO ranking factors grouped by category: keyword, content, links, technical" |
| **Illustration/Icon** | [Concept] represented by [visual element] | "SEO checklist icon with green checkmarks indicating completion status" |
| **Logo** | [Company] logo | "RankWise logo" |
| **Decorative** | Empty alt (alt="") | alt="" |

---

## KEYWORD INJECTION RULES

When adding focus keyword to alt text:

1. **Choose the most relevant image** - not random
2. **Weave keyword naturally** - it must describe what's actually in the image
3. **One keyword instance per alt text max** - don't stuff
4. **Mix approaches:**
   - Direct: "SEO checklist template with all 45 factors filled in"
   - Contextual: "Completed ranking factors audit using SEO checklist methodology"
   - Component: "Section 3 of the SEO checklist covering internal linking strategy"

### Before/After examples

| Before (bad) | After (good) |
|-------------|--------------|
| "SEO checklist" | "Complete 45-factor SEO checklist with pass/fail indicators for each ranking signal" |
| "image1.jpg" | "SEO audit results dashboard showing 38 of 45 factors passing" |
| "Picture of checklist" | "Printable SEO checklist organized by keyword, content, link, and technical categories" |
| "SEO, checklist, SEO checklist, audit" | "Step-by-step SEO checklist workflow for auditing blog posts before publishing" |

---

## GENERATION PROCEDURE

1. **Parse input format** - determine array, markdown, HTML, or JSON
2. **For each image, note:**
   - Current alt text (if any)
   - Image description/context (from user or inferred from filename/context)
   - Is this image a candidate for keyword placement?
3. **Select keyword image** - choose the image most topically relevant to the focus keyword
4. **Generate all alt texts** - following rules above
5. **Verify:**
   - At least 1 image has keyword (unless none are keyword-relevant)
   - All alt texts ≤125 characters
   - No alt text starts with "Image of..." or "Picture of..."
   - Read each aloud - would it help a blind user?

---

## OUTPUT FORMAT

### Return in same format as input

**If input was array:**
```
1. [alt text 1]
2. [alt text 2]
3. [alt text 3]
```

**If input was markdown:**
```
![new alt text 1](image1.jpg)
![new alt text 2](image2.png)
```

**If input was HTML:**
```
<img src="image1.jpg" alt="new alt text 1">
<img src="image2.png" alt="new alt text 2">
```

**If input was JSON:**
```
[
  {"src": "image1.jpg", "alt": "new alt text 1"},
  {"src": "image2.png", "alt": "new alt text 2"}
]
```

### Add keyword annotation
```
[MODE: meta-only - alt texts]
[LANG: xx]
[KEYWORD: xxx]

[Generated alt texts in input format]

[NOTES]
- Image #N carries the focus keyword: "[alt text]"
- Keyword density in alts: 1 of X images
```
