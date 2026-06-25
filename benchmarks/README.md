# RankWise Benchmark Dataset
> **Version:** 1.2.1

Five reference texts with manually verified SEO properties. Used to validate scoring consistency across versions.

## Usage

```bash
python -m validator.cli --file benchmarks/01-well-optimized.txt --keyword "content marketing strategy" --title "7 Proven Content Marketing Strategies That Actually Work in 2026" --meta "Content marketing strategy guide: 7 proven tactics to grow organic traffic. Based on analysis of 200+ SaaS companies. Free template included." --checklist
```

## Cases

| # | File | Type | Expected Grade |
|---|------|------|---------------|
| 1 | `01-well-optimized.txt` | Blog article (well-optimized) | A (90%+) |
| 2 | `02-keyword-stuffed.txt` | Blog article (keyword-stuffed) | D-F (density fail) |
| 3 | `03-too-short.txt` | Blog post (too short, no structure) | D (word count + hierarchy fail) |
| 4 | `04-no-meta.txt` | Article body only (missing meta layer) | C (meta factors fail) |
| 5 | `05-product-page.txt` | E-commerce product page | B (some N/A, good structure) |

## Expected Validator Factors

Each benchmark has expected pass/fail status for factors computable by `validator/metrics.py`:
K1, K2, K6, K7, K10, C1, C2, C5, C6, C8, C9, C10, C11, C12, T3, T4.

Web-access-only factors (K11, L5, L6, L7, L8, T6, T7) are excluded from validator scoring.
