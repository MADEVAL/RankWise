# RankWise — Professional SEO Content Engine

[![Version](https://img.shields.io/badge/version-1.3.0-blue)]()
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Compatibility](https://img.shields.io/badge/compatibility-any%20LLM-purple)]()

\[ **English** | [Русский](#) \]

> **Rank higher by writing for humans first, search engines second.**

An AI skill system that generates, rewrites, and audits content against 49 SEO ranking factors - covering everything from keyword placement to schema markup, E-E-A-T signals, and featured snippet optimization.

---

## Scope

RankWise is a **content-level SEO engine** — it optimizes text, meta tags, alt texts, URLs, and content structure. It does **not** measure page speed, Core Web Vitals, server configuration, SSL, or cookie compliance. For those, use Lighthouse, PageSpeed Insights, or Screaming Frog.

---

## What is this?

**RankWise** is a system prompt (skill) for any LLM - GPT, Claude, Gemini, DeepSeek, or any capable model. It transforms the AI into a world-class SEO strategist and content engineer who:

- Writes content that scores 46+/49 on the ranking factors checklist
- Rewrites existing content to fix SEO gaps (from URL or pasted text)
- Audits content against 49 measurable ranking signals
- Generates optimized meta tags, image alt texts, and URL slugs
- Creates complete SEO content briefs and editorial plans

It covers every critical SEO signal: readability scoring, schema markup, E-E-A-T signals, featured snippet targeting, topic clustering, and LSI keyword strategy.

---

## How it works

1. **Load `SKILL.md`** as a system prompt into any LLM.
2. **Give a task:** "SEO article. Keyword: email marketing." / "Write about email strategy + meta. Keyword: email." / "Audit this content." / "Full package for my landing page."
3. **Get output** - only what you asked for. No extra modules. No fluff.

**Six modes with modular output:**

- **Generate** - Create SEO-optimized content from scratch (keyword → article, topic + keyword → article + meta)
- **Rewrite** - Transform existing content (URL or text) with full SEO optimization + AI-marker removal
- **Audit** - Score any content against 49 factors with weighted scoring, grade, prioritized fixes
- **Meta-Only** - Generate/optimize meta titles, descriptions, OG tags, alt texts, URL slugs
- **Brief** - Create a complete content brief - keywords, structure, linking plan, media plan
- **Quick-Fix** - Fix individual factors: «fix my title length», «add keyword to H2», «reduce passive voice»

**Context-aware defaults:**
- Keyword only → article body (no meta, no alts)
- Topic + keyword → article + meta
- Topic + keyword + images → full package (article + meta + alts)
- Any combination can be explicitly requested: «just the article», «meta only», «full package»

---

## The 49-Factor SEO Scorecard

Every piece of content is scored against 49 factors across 5 categories with weighted multipliers (CRITICAL=×3, HIGH=×2, MEDIUM=×1, LOW=×0.5). Below are the highlights - full checklist in `shared/checklist.md`.

| Category | Factors | Highlights |
|----------|---------|------------|
| **Keyword Placement** (K1–K12) | 12 | Focus keyword, title, meta, URL, headings, density, cannibalization |
| **Content Quality** (C1–C14) | 14 | Word count, readability, heading hierarchy, passive voice, paragraph structure |
| **Linking** (L1–L9) | 9 | Internal links, external links, DoFollow, anchor variety, orphan prevention |
| **URL & Technical** (T1–T8) | 8 | URL length/structure, title/description length, schema, canonical, OG tags |
| **Advanced Signals** (A1–A6) | 6 | Featured snippet, E-E-A-T, LSI keywords, freshness, mobile readability, breadcrumbs |

**Weighted scoring:** CRITICAL factors carry ×3 weight (any CRITICAL failure caps maximum grade at B). N/A factors excluded from denominator. Full methodology in `shared/checklist.md`.

---

## Architecture

```
rankwise/
├── SKILL.md                        ← Main orchestrator (6 modes, 49 factors)
├── README.md                       ← This documentation
├── CHANGELOG.md                    ← Version history
├── LICENSE                         ← MIT | Copyright Yevhen Leonidov
├── shared/
│   ├── checklist.md                ← 49 SEO factors with thresholds, severity, fixes
│   ├── keyword-rules.md            ← Density, placement, LSI, cannibalization rules
│   ├── power-words.md              ← Power words × languages for sentiment & CTR
│   ├── schema-templates.md         ← JSON-LD structured data templates
│   ├── readability-params.md       ← Readability targets per language
│   ├── burned-words.md             ← AI detection patterns × 9 languages
│   └── link-strategy.md            ← Internal/external linking rules
  ├── scenarios/
│   ├── article-generate.md         ← Full article generation from topic + keywords
│   ├── article-rewrite.md          ← Rewrite pipeline (URL or pasted text)
│   ├── meta-optimize.md            ← Meta titles, descriptions, OG tags
│   ├── alt-texts.md                ← Image alt text optimization (array/inline)
│   ├── audit-report.md             ← Full SEO audit with scoring
│   ├── content-brief.md            ← Content brief / plan generation
│   ├── url-optimize.md             ← URL slug optimization
│   ├── quick-fix.md                ← Single-factor quick fixes (all 49)
│   ├── home-page.md                ← Home page / brand page optimization
│   ├── product-page.md             ← Product / e-commerce page optimization
│   └── video-podcast.md            ← YouTube / podcast description & metadata SEO
├── examples/
│   ├── before-after-article.md     ← Full article rewrite example
│   ├── meta-examples.md            ← Meta tag before/after examples
│   ├── audit-example.md            ← Complete audit report example
│   └── integration-pipeline.md     ← End-to-end triple integration example
├── validator/
│   ├── metrics.py                  ← Python: readability, density, passive voice, etc.
│   └── cli.py                      ← CLI entry point
└── benchmarks/
    ├── README.md                    ← Benchmark dataset documentation
    ├── 01-well-optimized.txt        ← Reference: Grade A article
    ├── 02-keyword-stuffed.txt       ← Reference: keyword stuffing
    ├── 03-too-short.txt             ← Reference: too short, no structure
    ├── 04-no-meta.txt               ← Reference: article body only
    └── 05-product-page.txt          ← Reference: e-commerce product page
```

---

## Validator (Python)

The `validator/` directory contains a Python tool that computes measurable SEO metrics from text — complementing the LLM-based scoring with deterministic calculations:

```bash
pip install readsight

# Full report
python -m validator.cli --text "Your content..." --keyword "seo" --title "My Title" --meta "Description"

# Read from file
python -m validator.cli --file article.txt --keyword "seo strategy" --title "SEO Guide"

# Checklist scores only (machine-readable JSON)
python -m validator.cli --file article.txt --keyword "seo" --title "Title" --checklist --json
```

**What it computes:** word count (C1), paragraph metrics (C2), readability — Flesch-Kincaid, Gunning Fog, SMOG, ARI, Coleman-Liau for EN only (C8), passive voice ratio per language (C9), transition word ratio per language (C10), sentence length variety (C11), consecutive sentence starts (C12), keyword density (K10), keyword placement (K2, K6, K7), title/meta length with per-language ranges (T3, T4), power words in all 9 languages (C6).

**Multi-language support:** `--lang en|ru|uk|de|fr|es|pt|it|pl`. Passive voice, transition words, and power words use language-specific patterns for all 9 languages. Readability (C8) is computed deterministically via [ReadSightPy](https://github.com/MADEVAL/ReadSightPy) (TeX/Liang syllable counting) for all 9 languages — EN uses Flesch-Kincaid Grade, DE Wiener Sachtextformel, ES Fernández-Huerta, IT Gulpease, FR/RU/PT Flesch Reading Ease, UK LIX, PL FOG-PL. Title/meta length targets adjust per language.

---

## Benchmarks

`benchmarks/` contains 5 reference texts with known SEO properties for regression testing across versions:

| # | File | Expected Result |
|---|------|----------------|
| 1 | `01-well-optimized.txt` | Mixed — keyword in body, title mismatch (plural) |
| 2 | `02-keyword-stuffed.txt` | D–F: 23% density, word count fail |
| 3 | `03-too-short.txt` | D: 69 words, missing meta |
| 4 | `04-no-meta.txt` | D: no title/meta, short content |
| 5 | `05-product-page.txt` | C+: best density & keyword placement |

```bash
# Run a single benchmark (omit --title/--meta if not applicable)
python -m validator.cli --file benchmarks/01-well-optimized.txt --keyword "content marketing strategy" --title "7 Proven Content Marketing Strategies That Actually Work in 2026" --meta "Content marketing strategy guide: 7 proven tactics." --checklist
```

> **Coverage:** The validator computes 16 of 49 factors (K1-K2, K6-K7, K10, C1-C2, C5-C6, C8-C12, T3-T4). Remaining 33 factors require LLM judgment or web access. See `benchmarks/README.md` for details.

---

## Quick Start

**Keyword only → article body:**
> "SEO article. Keyword: email marketing strategy."

**Topic + keyword → article + meta:**
> "Write about email marketing strategy for SaaS founders. Keyword: email strategy. Language: en."

**Full package (article + meta + alts):**
> "Full package about content marketing. Keyword: content strategy. Images: dashboard, chart, team photo."

**Meta tags only:**
> "Generate meta title and description for my SaaS landing page. Keyword: project management software."

**Image alt texts only:**
> "Generate SEO alt texts for these 5 images: [array]. Focus keyword: email marketing."

**Full SEO audit:**
> "Audit this content for SEO: [paste text]. Focus keyword: project management software."

**Content brief:**
> "Create an SEO content brief for a pillar page. Target keyword: content marketing strategy."

**Rewrite from URL:**
> "Rewrite this article for SEO: [URL]. Focus keyword: SEO checklist."

**Joint with HumanAI:**
> "SEO-rewrite this article using RankWise, then humanize it with [HumanAI](https://github.com/MADEVAL/HumanAI). EN. Keyword: seo audit."

**Joint with MindFluence:**
> "RankWise SEO brief for SaaS landing page, then [MindFluence](https://github.com/MADEVAL/MindFluence) from that brief. Expert-calm tone."

---

## Integration with HumanAI and MindFluence

RankWise is designed to work with, not against, these skills:

- **[HumanAI](https://github.com/MADEVAL/HumanAI)** - Text Humanization Engine. RankWise handles SEO structure → HumanAI humanizes the voice. Monitor keyword density and heading keywords after humanization.
- **[MindFluence](https://github.com/MADEVAL/MindFluence)** - Cognitive Bias Marketing Engine. RankWise provides SEO structure → MindFluence applies cognitive bias persuasion. Monitor for keyword over-stuffing in `bold-sell` tone.
- **Triple pipeline:** RankWise (structure) → MindFluence (persuasion) → HumanAI (voice) → RankWise Audit (final check).

See `SKILL.md` → INTEGRATION WITH OTHER SKILLS for full compatibility guide.

---

## Requirements

- Any capable LLM with a system prompt / custom instructions field
- For full skill functionality: a skill system that loads files from a folder (OpenCode, Claude Code)
- **SKILL.md is self-sufficient** - contains all core rules for standalone use. `shared/` and `scenarios/` files add professional depth (scoring formulas, AI-marker lists, per-language readability, schema templates, content-type blueprints)
- No API keys, no tools, no dependencies — pure prompt engineering
- Works in any language; per-language parameters for 9 languages (EN, RU, UK, DE, FR, ES, PT, IT, PL)
- **Optional:** Python 3.10+ + `readsight` for deterministic metric validation via `validator/`

---

## Installation

### OpenCode
```
rankwise/ → .opencode/skills/          (project)
          → ~/.config/opencode/skills/  (global)
```

### Claude Code
```
rankwise/ → ~/.claude/skills/
```

### Any LLM (standalone)
Copy contents of `SKILL.md` as system prompt. Add `shared/` and `scenarios/` files for richer detail.

---

## License

MIT | Copyright Yevhen Leonidov
