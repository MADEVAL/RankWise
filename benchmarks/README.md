# RankWise Benchmark Dataset
> **Version:** 1.3.0

Five reference texts with manually verified SEO properties. Used to validate scoring consistency across versions.

## Usage

```bash
python -m validator.cli --file benchmarks/01-well-optimized.txt --keyword "content marketing strategy" --title "7 Proven Content Marketing Strategies That Actually Work in 2026" --meta "Content marketing strategy guide: 7 proven tactics to grow organic traffic. Based on analysis of 200+ SaaS companies. Free template included." --checklist
```

Omit `--title` / `--meta` when not applicable — do NOT pass empty strings.

## Cases

| # | File | Type | Validator Factors (16 of 49) | Expected Result |
|---|------|------|------------------------------|-----------------|
| 1 | `01-well-optimized.txt` | Blog article (moderate optimization) | 8 pass, 4 fail, 4 warn | Mixed — keyword in body, density elevated, missing from title (plural vs singular) |
| 2 | `02-keyword-stuffed.txt` | Blog article (23% keyword density) | 7 pass, 6 fail, 3 warn | D–F: critical density fail + word count |
| 3 | `03-too-short.txt` | Blog post (69 words, no structure) | 8 pass, 6 fail, 2 warn | D: word count, title length, meta missing |
| 4 | `04-no-meta.txt` | Article body only (no title/meta) | 5 pass, 8 fail, 3 warn | D: no title, word count, C2/C10/C11/C12 fails |
| 5 | `05-product-page.txt` | E-commerce product page | 8 pass, 5 fail, 3 warn | C+: best density, keyword placement OK |

## Validator Coverage

The Python validator computes **16 of 49** factors:
**K1, K2, K6, K7, K10, C1, C2, C5, C6, C8, C9, C10, C11, C12, T3, T4**

Not computed (require LLM, web access, or manual judgment):
K3–K5, K8, K9, K11, K12, C3, C4, C7, C13, C14, L1–L9, T1, T2, T5–T8, A1–A6

## Limitations

- **Exact keyword matching only** — does not handle stemming or plural forms (e.g., "strategies" ≠ "strategy")
- **Readability via ReadSightPy** — all 9 languages covered; UK and PL have no Flesch model so C8 uses LIX (UK) and FOG-PL (PL)
- **Regex-based passive voice** — catches ~80% of cases, not 100%
- **Simple sentence splitter** — may mis-split on abbreviations (Dr., U.S., etc.)
- **No heading hierarchy analysis** — assumes flat body text input
