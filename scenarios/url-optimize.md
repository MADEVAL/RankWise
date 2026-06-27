# Scenario: URL Optimize
> **Version:** 1.2.2

**Use when:** User asks to optimize a URL slug. Mode: META-ONLY (URL focus).

**Pipeline:** parse URL → extract keyword → strip stop words → shorten → deliver

---

## URL SLUG RULES

### Structure requirements
- ≤75 characters total
- Contains primary keyword
- Keyword near the beginning of slug
- Hyphens between words (never underscores, never spaces)
- Lowercase
- No special characters: ! @ # $ % ^ & * ( ) + = { } [ ] | \ : ; " ' < > ? / (except path separators)
- No stop words: the, a, an, and, or, but, in, on, at, to, for, of, with, by, from, up, about, into, through, during, before, after, above, below, between
- No dates in slug (unless intentionally part of URL strategy for annual content)
- No trailing slash in suggestion
- No file extensions (.html, .php, .asp)

### Language-specific stop words

**English:** the, a, an, and, or, but, in, on, at, to, for, of, with, by, from, up, about, into, through, during, before, after, above, below, between, out, off, over, under, again, further, then, once, here, there, when, where, why, how, all, both, each, few, more, most, other, some, such, no, nor, not, only, own, same, so, than, too, very, just, because, as, until, while

**Russian:** и, в, на, с, по, к, от, из, о, об, за, до, для, без, над, под, при, про, у, через, или, но, а, не, ни, бы, ли, же, то, что, как, так, это, весь, тут, там, где, когда, ещё, уже, только

**Ukrainian:** і, й, та, в, у, на, з, до, для, без, над, під, при, про, через, або, але, не, ні, би, ж, що, як, це, тут, там, де, коли, ще, вже, тільки, від, по, за, перед, між, біля, поза, навколо

**German:** der, die, das, den, dem, des, ein, eine, einer, eines, in, auf, mit, von, zu, für, an, bei, aus, nach, über, vor, durch, um, gegen, zwischen, oder, und, aber, nicht, auch, noch, nur, schon, so, wie, als, am, im, ins, zum, zur

**French:** le, la, les, l', un, une, des, de, du, à, au, aux, en, sur, dans, par, pour, avec, sans, sous, entre, et, ou, mais, ne, pas, plus, moins, très, tout, tous, toute, comme, que, qui, quoi, dont, où, dont

**Spanish:** el, la, los, las, un, una, unos, unas, de, del, a, al, en, por, para, con, sin, sobre, entre, y, e, o, u, pero, no, ni, que, cual, cuales, como, más, muy, tan, todo, todos, esta, este, esto

**Portuguese:** o, a, os, as, um, uma, uns, umas, de, do, da, dos, das, em, no, na, nos, nas, por, para, com, sem, sobre, entre, e, ou, mas, não, nem, que, qual, quais, como, mais, muito, tão, todo, todos

**Italian:** il, lo, la, i, gli, le, un, uno, una, di, a, da, in, con, su, per, tra, fra, e, o, ma, non, né, che, chi, cui, come, più, molto, tanto, tutto

**Polish:** w, na, z, do, po, za, przez, dla, przy, nad, pod, przed, między, i, oraz, lub, albo, ale, nie, tak, jak, to, ten, ta, te, się, już, jeszcze, tylko, bardzo

---

## OPTIMIZATION PROCEDURE

### Step 1: Parse current URL
- Extract slug path (everything after domain and before any query params)
- Example: `https://example.com/blog/the-best-seo-checklist-for-wordpress-beginners-in-2026/`
- Slug: `the-best-seo-checklist-for-wordpress-beginners-in-2026`

### Step 2: Identify keyword
- From user input, or infer from slug
- This slug suggests keyword: "SEO checklist"

### Step 3: Strip stop words
- Remove stop words per language
- `the-best-seo-checklist-for-wordpress-beginners-in-2026`
- After stripping: `best-seo-checklist-wordpress-beginners-2026`

### Step 4: Remove unnecessary elements
- Remove dates unless intentional: `2026` → remove
- Result: `best-seo-checklist-wordpress-beginners`

### Step 5: Shorten to ≤75 characters
- `best-seo-checklist-wordpress-beginners` = 43 chars ✓
- If >75: condense further - remove least essential words
- Priority hierarchy: keyword > key modifier > context word > descriptor

### Step 6: Validate
- Contains primary keyword?
- No stop words?
- Hyphens not underscores?
- ≤75 characters?
- No special characters?
- No trailing slash?

---

## COMMON TRANSFORMATIONS

| Current URL | Issues | Optimized |
|------------|--------|-----------|
| `/2026/03/15/seo-checklist` | Date path, adds length | `/seo-checklist` |
| `/the_best_SEO_tools_for_Beginners` | Underscores, stop words, mixed case | `/best-seo-tools-beginners` |
| `/how-to-create-an-seo-checklist-for-your-wordpress-website` | Stop words, too long | `/create-seo-checklist-wordpress` |
| `/category/blog/seo-checklist-tips` | Unnecessary path | `/seo-checklist-tips` |
| `/SEO-Checklist` | Uppercase | `/seo-checklist` |
| `/seo-checklist.html` | File extension | `/seo-checklist` |
| `/seo-checklist/` | Trailing slash (in suggestion) | `/seo-checklist` |

---

## DELIVERY FORMAT

```
[MODE: meta-only - URL]
[LANG: xx]
[KEYWORD: xxx]

Current URL (if provided):
[current-url] - [length] chars

Issues found:
- [issue 1]
- [issue 2]

Optimized URL:
/suggested-slug - [length] chars

Changes made:
- Removed stop words: [list]
- Removed dates: [list]
- Condensed: [before] → [after]

Note: Changing live URLs requires 301 redirect from old URL to new URL.
```

### If generating from scratch (no current URL):

```
[MODE: meta-only - URL]
[LANG: xx]
[KEYWORD: xxx]

Generated URL:
/suggested-slug - [length] chars

Complies with:
✅ Keyword present
✅ ≤75 characters
✅ Hyphens used
✅ No stop words
✅ Lowercase
```
