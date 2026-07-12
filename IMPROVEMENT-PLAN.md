# RankWise Improvement Plan — Single-File AI Executability

> **Version:** 1.3.0-proposal
> **Status:** Draft for review
> **Principle:** Zero regressions. All existing files preserved. Backward-compatible.

---

## 1. PROBLEM STATEMENT

### Current state (v1.2.2)

SKILL.md (696 lines) + 7 shared/ files (~1700 lines) + 10 scenarios/ files (~2300 lines) + examples/ (~280 lines). **Total: ~5000 lines across 30 files.**

This architecture works ONLY for AI tools that can ingest an entire directory tree at once (OpenCode, Claude Code with full workspace access). It **fails** for:

| AI Tool / Platform | Failure Mode |
|---------------------|--------------|
| Tools with file-count limits (5-file cap) | Can't load 30 files |
| Tools with context-window limits (<32K tokens) | Can't fit 5000 lines |
| API-based integrations (single system prompt) | Only one slot for the skill |
| GitHub Copilot Chat | Works with single file references |
| Claude.ai / ChatGPT with file upload | 1–5 file upload limits |
| Any tool where user pastes the skill manually | Impossible to paste 30 files |

### Root cause

The skill's reference data (power words, burned words, readability params, schema templates, etc.) and scenario procedures are spread across separate files that the LLM MUST read to function correctly. There is no single-file entry point that contains the core logic plus pointers to fetchable data.

---

## 2. SOLUTION ARCHITECTURE

### Core principle: "Orchestrator + Fetchable References"

```
┌─────────────────────────────────────────────┐
│  SKILL.md  (~900 lines — the ONE file)       │
│                                              │
│  ┌─ ROLE (inline)                            │
│  ┌─ OPERATING MODES + scenario summaries     │
│  ┌─ 49-FACTOR SCORECARD (compact inline)     │
│  ┌─ CORE SEO RULES (keyword, content, links) │
│  ┌─ LANGUAGE ADAPTATION (quick table)        │
│  ┌─ MODULE ACTIVATION LOGIC                  │
│  ┌─ OUTPUT FORMATS                           │
│  ┌─ FETCH STRATEGY (decision tree)           │
│  ┌─ SCENARIO SUMMARIES (5-10 lines each)     │
│  ┌─ RAW URL INDEX (complete file map)        │
│  └─ QUICK START                              │
└─────────────────────────────────────────────┘
         │
         │  AI fetches on demand via raw GitHub URLs
         ▼
┌──────────────────────────────────────────────┐
│  https://raw.githubusercontent.com/           │
│  MADEVAL/RankWise/main/                       │
│                                              │
│  ├── shared/checklist.md          (fetched always)  │
│  ├── shared/keyword-rules.md      (generate/rewrite)│
│  ├── shared/power-words.md        (non-EN languages)│
│  ├── shared/burned-words.md       (rewrite mode)    │
│  ├── shared/readability-params.md (non-EN languages)│
│  ├── shared/link-strategy.md      (generate/rewrite)│
│  ├── shared/schema-templates.md   (schema requests) │
│  └── scenarios/*.md               (per-mode detail) │
└──────────────────────────────────────────────┘
```

### How it works in practice

1. **AI loads SKILL.md** — the only mandatory file. Contains complete orchestrator logic.
2. **AI reads the FETCH STRATEGY** section — a decision tree that tells it exactly which URLs to fetch based on the task.
3. **AI fetches only what's needed** — English generation? Fetch 2 files. German rewrite? Fetch 5 files. Audit only? Fetch 1 file.
4. **AI executes the task** using inline rules + fetched reference data.
5. **Scenario summaries inline** are sufficient for simple tasks. Full scenario files fetched only for complex operations.

### Why raw GitHub URLs work

- No authentication required (public repo)
- Versioned by branch/tag (`main` = always latest, can pin to tag for stability)
- Cached by CDN — fast fetches
- Standard `webfetch` tool support in all major AI platforms
- Fallback: if web fetch unavailable, SKILL.md's inline content is sufficient for basic operations

---

## 3. IMPLEMENTATION PLAN

### PHASE 1: Enhance SKILL.md (THE CRITICAL PHASE)

**File:** `SKILL.md` — rewrite as single-file orchestrator with fetchable references.

#### 3.1.1 Add FETCH STRATEGY section (insert after metadata header, before ROLE)

New section `## ── HOW TO USE THIS SKILL ──` containing:

```
### Single-File Operation

You are reading the COMPLETE RankWise orchestrator. This single file contains
all core SEO logic needed to generate, rewrite, audit, and optimize content.

For language-specific word lists and detailed scenario procedures, fetch the
corresponding file from the URL INDEX at the bottom of this file.

### Fetch Decision Tree

After reading this file, determine what to fetch based on the task:

1. ALWAYS fetch `shared/checklist.md` for the full 49-factor scoring matrix

2. IF task language ≠ English:
   → fetch `shared/power-words.md` (title/heading vocabulary)
   → fetch `shared/readability-params.md` (per-language targets)
   
3. IF mode is GENERATE or REWRITE:
   → fetch `shared/keyword-rules.md` (density, placement, LSI)
   → fetch `shared/link-strategy.md` (internal/external rules)
   
4. IF mode is REWRITE:
   → fetch `shared/burned-words.md` (AI marker removal)
   
5. IF task requires schema markup:
   → fetch `shared/schema-templates.md` (JSON-LD templates)
   
6. IF task is URL optimization:
   → fetch `scenarios/url-optimize.md` (per-language stop words)
   
7. IF task requires detailed step-by-step procedure beyond the inline summary:
   → fetch `scenarios/[name].md` from the URL INDEX
   
8. IF web fetch is UNAVAILABLE:
   → Proceed with inline data only. English is fully covered.
     For non-English, rely on the compact LANGUAGE ADAPTATION table.
     For burned words, apply the universal list.
     Mark output with ⚠️ "No web access — used inline reference data only."
```

**Why here:** Placed at the top so the AI reads it FIRST, before processing any user request. This is the "meta-instruction" that governs all subsequent behavior.

**Consequences:**
- AI tools that parse SKILL.md line-by-line will see the fetch strategy immediately
- No regression: multi-file tools can ignore this and load files directly
- Adds ~40 lines to SKILL.md

#### 3.1.2 Restructure OPERATING MODES section with inline scenario summaries

**Current:** Each mode says "Load `scenarios/xxx.md` — follow pipeline"

**New:** Each mode gets a 5-10 line summary of the pipeline PLUS the fetch URL.

Example for MODE 1 (GENERATE):

```
### Mode 1: GENERATE
**Trigger:** Topic + focus keyword. No source content.
**Pipeline:** intent → title → outline → write → meta → links → QA
**Core procedure (inline):**
  1. INTENT: Determine search intent (informational/commercial/transactional/navigational).
     With web access: search SERP. Without: infer from keyword type.
  2. TITLE: Formula = [Number] + [Power Word] + [Keyword] + [Promise].
     50-60 chars, keyword in first 3-5 words, ≥1 odd number, ≥2 power words.
  3. OUTLINE: 5-9 H2 sections covering: Problem → Definition → Method →
     Evidence → Steps → Mistakes → Tools → Advanced → Conclusion.
     Word count: low competition 600-1000, medium 1000-1800, high 1800-3000+.
  4. CONTENT: Hook → Pain → Promise → Keyword in first 100-150 words.
     Body: opening sentence + core content + visual relief + transition per H2.
     1 data point/500 words, 1 example/H2, 1 contrarian insight/article.
     Conclusion: 1-2 sentence summary + key takeaway + specific CTA. No regurgitation.
  5. META: Title 50-60 chars. Description 145-158 chars, keyword in first 20 words.
     URL: keyword, hyphens, ≤75 chars, no stop words.
  6. LINKS: 3-10 internal (varied anchors), 2-5 external (authoritative).
  7. QA: 8-factor quick scan before delivery (K1, K2, K4, K7, K10, C1, C13, L1).
**Full pipeline + writing templates:** fetch `scenarios/article-generate.md`
```

**What's different:**
- LLM can execute directly from inline summary without fetching the scenario file
- The summary contains ALL critical rules — title formula, outline blueprint, content rules, QA checklist
- Fetch URL is provided for richer detail (edge cases, examples, format templates)
- Net addition: ~15 lines per mode

**Apply same pattern to all 6 modes and the 3 content-type routes (home, product, video).**

#### 3.1.3 Merge critical shared/ rules inline

Currently SKILL.md says "Full rules: `shared/keyword-rules.md`" in multiple places. Instead, inline a condensed version and keep the URL for the full version.

**Keyword Strategy section** — currently ~15 lines. Expand to ~40 lines with:
- Primary/secondary/LSI hierarchy
- Density calculation method (exact/partial/stem/combined, 0.8%-1.5% target)
- 7 placement rules (compact list)
- Cannibalization check procedure
- LSI source methods (6 categories in one sentence)
- Fetch URL for full rules + language-specific notes

**Linking Strategy section** — currently ~15 lines. Expand to ~30 lines with:
- Internal: 3-10 links, anchor text ratios (partial 30-40%, branded 20-25%, generic 20-25%, naked 5-10%, exact ≤2)
- External: 2-5 links, authority criteria, DoFollow rules
- Placement: first link within 300 words, distributed throughout
- Topic cluster strategy (pillar ↔ cluster bidirectional)
- Fetch URL for full rules + audit checklist

**Technical SEO section** — already fairly complete, just add fetch URLs for schema templates.

**Power Words section** — currently lists 6 categories with examples. Keep the categories inline. Add fetch URL for full per-language word lists. Add a compact table:

```
| Category | EN (sample) | Full list |
|----------|-------------|-----------|
| Fear/Loss | "Stop losing", "Hidden", "Mistake", "Warning" | fetch shared/power-words.md |
| Curiosity | "Secret", "Little-known", "Unconventional" | fetch shared/power-words.md |
| ... | ... | ... |
```

**Language Adaptation section** — currently ~40 lines with per-language notes. Keep inline. Add compact per-language readability target table:

```
| Lang | Title chars | Desc chars | Readability Target | Formula |
|------|------------|------------|--------------------|--------|
| EN   | 50-60       | 145-158    | Grade 7-9           | FK Grade |
| RU   | 55-70       | 140-160    | FRE 50-70           | FRE      |
| ... | ... | ... | ... | ... |
```
Fetch URL for full per-language parameters (sentence length limits, passive targets, transition targets).

#### 3.1.4 Add compact 49-factor scorecard inline

Currently SKILL.md has the full 5-table scorecard (~75 lines). Keep it — it's the heart of the skill. This MUST be inline.

But enhance each category header with the fetch URL:
```
### KEYWORD PLACEMENT (12 factors) — Full fix instructions: fetch `shared/checklist.md`
```

#### 3.1.5 Add URL INDEX section (at the bottom, before QUICK START)

Complete, copy-pasteable file map with raw GitHub URLs:

```
## ── RAW URL INDEX ──

Base URL: `https://raw.githubusercontent.com/MADEVAL/RankWise/main/`

### Always-needed references
- 49-factor checklist + fix instructions: [shared/checklist.md](https://raw.githubusercontent.com/MADEVAL/RankWise/main/shared/checklist.md)
- Keyword rules (density, placement, LSI, cannibalization): [shared/keyword-rules.md](https://raw.githubusercontent.com/MADEVAL/RankWise/main/shared/keyword-rules.md)

### Language-specific references
- Power words × 9 languages: [shared/power-words.md](https://raw.githubusercontent.com/MADEVAL/RankWise/main/shared/power-words.md)
- Burned words (AI markers) × 9 languages: [shared/burned-words.md](https://raw.githubusercontent.com/MADEVAL/RankWise/main/shared/burned-words.md)
- Readability params per language: [shared/readability-params.md](https://raw.githubusercontent.com/MADEVAL/RankWise/main/shared/readability-params.md)
- URL stop words × 9 languages: embedded in [scenarios/url-optimize.md](https://raw.githubusercontent.com/MADEVAL/RankWise/main/scenarios/url-optimize.md)

### Strategy references
- Internal/external linking rules: [shared/link-strategy.md](https://raw.githubusercontent.com/MADEVAL/RankWise/main/shared/link-strategy.md)
- JSON-LD schema templates (13 types): [shared/schema-templates.md](https://raw.githubusercontent.com/MADEVAL/RankWise/main/shared/schema-templates.md)

### Scenario procedures (full step-by-step)
- Article generation: [scenarios/article-generate.md](https://raw.githubusercontent.com/MADEVAL/RankWise/main/scenarios/article-generate.md)
- Article rewrite: [scenarios/article-rewrite.md](https://raw.githubusercontent.com/MADEVAL/RankWise/main/scenarios/article-rewrite.md)
- Audit report format: [scenarios/audit-report.md](https://raw.githubusercontent.com/MADEVAL/RankWise/main/scenarios/audit-report.md)
- Content brief/plan: [scenarios/content-brief.md](https://raw.githubusercontent.com/MADEVAL/RankWise/main/scenarios/content-brief.md)
- Meta tag optimization: [scenarios/meta-optimize.md](https://raw.githubusercontent.com/MADEVAL/RankWise/main/scenarios/meta-optimize.md)
- Alt texts: [scenarios/alt-texts.md](https://raw.githubusercontent.com/MADEVAL/RankWise/main/scenarios/alt-texts.md)
- URL slug optimization: [scenarios/url-optimize.md](https://raw.githubusercontent.com/MADEVAL/RankWise/main/scenarios/url-optimize.md)
- Quick-fix (all 49 factors): [scenarios/quick-fix.md](https://raw.githubusercontent.com/MADEVAL/RankWise/main/scenarios/quick-fix.md)
- Home page / brand SEO: [scenarios/home-page.md](https://raw.githubusercontent.com/MADEVAL/RankWise/main/scenarios/home-page.md)
- Product / e-commerce SEO: [scenarios/product-page.md](https://raw.githubusercontent.com/MADEVAL/RankWise/main/scenarios/product-page.md)
- Video / podcast SEO: [scenarios/video-podcast.md](https://raw.githubusercontent.com/MADEVAL/RankWise/main/scenarios/video-podcast.md)

### Annotated examples
- Full rewrite before/after: [examples/before-after-article.md](https://raw.githubusercontent.com/MADEVAL/RankWise/main/examples/before-after-article.md)
- Meta tag examples: [examples/meta-examples.md](https://raw.githubusercontent.com/MADEVAL/RankWise/main/examples/meta-examples.md)
- Audit report example: [examples/audit-example.md](https://raw.githubusercontent.com/MADEVAL/RankWise/main/examples/audit-example.md)

### Validator (for CI/CD or programmatic use)
- CLI entry: `validator/cli.py` (run `pip install rankwise-validator && rankwise-validator --help`)

> All URLs point to the **main** branch. To pin a specific version, replace `main`
> with a tag: `v1.2.2` → `https://raw.githubusercontent.com/MADEVAL/RankWise/v1.2.2/...`
```

#### 3.1.6 Add offline fallback instructions

In the FETCH STRATEGY section, add:

```
### Offline Mode (No Web Fetch Available)

If you cannot fetch any URLs, proceed with the inline rules only:
- English is fully covered (power words, transition words, stop words are inline in the LANGUAGE RESOURCES tables below)
- For non-English: use the compact LANGUAGE ADAPTATION table for targets,
  apply universal burned words, and flag output with
  ⚠️ "No web access — used inline reference data only."
- All 49 factors are scoreable without fetching — use the inline scorecard
- Scenario summaries are sufficient for basic operation in all 6 modes
```

#### 3.1.7 Add inline LANGUAGE RESOURCES table

Add compact tables for English word lists (currently all languages are only in shared/ files). English is the default and most-used language — its word lists should be inline for offline operation.

```
## ── LANGUAGE RESOURCES (ENGLISH — inline) ──

### English Power Words (for titles/headings)
proven, secret, simple, exclusive, hidden, surprising, shocking, amazing,
incredible, ultimate, essential, critical, guaranteed, instant, effortless,
breakthrough, insider, revealed, mistake, warning, never, avoid, dangerous,
risk, urgent, little-known, unknown, unconventional, tested, research-backed,
data-driven, expert, step-by-step, definitive, powerful, effective

### English Transition Words (for body — target ≥30% of sentences)
however, therefore, because, although, specifically, for example, for instance,
in contrast, similarly, consequently, notably, meanwhile, furthermore, moreover,
additionally, nevertheless, nonetheless, otherwise, instead, accordingly, hence,
thus, in addition, on the other hand, as a result, in particular, in conclusion,
to summarize, first, second, third, finally, next, then, also, besides, indeed,
in fact, of course, certainly, surely, undoubtedly, regardless, despite,
even though, while, whereas

### English Stop Words (for URL slugs — remove these)
the, a, an, and, or, but, in, on, at, to, for, of, with, by, from, up, about,
into, through, during, before, after, above, below, between, is, are, was, were,
be, been, being, have, has, do, does, did, will, would, can, could, may, might,
must, shall, should, not, no

### English Passive Voice Patterns (for detection)
- "am/is/are/was/were/be/been/being + [adverb] + [past participle]"
- "has/have/had/will have + been + [past participle]"

> For non-English word lists, fetch `shared/power-words.md`, `shared/burned-words.md`,
> `shared/readability-params.md` from the URL INDEX.
```

**Net change to SKILL.md size:** from 696 lines → approximately 950–1050 lines. This is still well within any reasonable context window (even 8K tokens can handle ~1000 lines of markdown).

---

### PHASE 2: Create missing referenced files (Bug fix)

Two files are referenced in documentation but don't exist:

1. **`examples/integration-pipeline.md`** — Referenced in:
   - README.md line 103
   - README.ru.md line 119
   - CHANGELOG.md v1.1 entry

2. **`INTEGRATION-GUIDE.md`** — Referenced in:
   - CHANGELOG.md v1.2.1 line 41

**Action:**
- Create minimal stub files with link to the relevant section in SKILL.md or README.md
- This fixes broken references without requiring content to be written from scratch
- The integration section in SKILL.md (lines 520-561) already contains the relevant content

**No regression:** Files are added, nothing is removed.

---

### PHASE 3: Version pinning strategy (Optional, recommended)

Add version pinning instructions in the URL INDEX:

```
> **Stable reference:** Replace `main` with a tagged version for guaranteed stability:
> `https://raw.githubusercontent.com/MADEVAL/RankWise/v1.2.2/shared/checklist.md`
> Current stable tag: `v1.2.2`
```

And in the metadata header, add:

```
pinned_urls: "v1.2.2"  # change to "main" for latest, or a tag for stability
```

This allows users to choose between always-latest (`main`) and stable (`v1.2.2`).

---

### PHASE 4: Testing the single-file workflow

#### 4.1 Manual smoke test

Test that SKILL.md alone (without loading any shared/ or scenarios/ files) is sufficient for:

| Test Case | Expected Outcome |
|-----------|-----------------|
| "Write an SEO article about email marketing. Keyword: email strategy. EN." | Full article generated using inline rules only |
| "Audit this text: [paste]. Keyword: SEO." | Full 49-factor audit using inline scorecard |
| "Rewrite this article for better SEO: [URL]. Keyword: growth hacking. EN." | Rewrite with AI marker removal from inline burned words |
| "Generate meta tags for landing page. Keyword: project management tool. RU." | AI fetches shared/power-words.md for RU power words, generates RU meta |
| "Quick-fix: my keyword density is 4.2%. Keyword: SaaS. EN." | Fix produced from inline K10 rules |
| "Create SEO content brief for pillar page. Keyword: growth marketing. DE." | AI fetches scenarios/content-brief.md + shared/power-words.md for DE |

#### 4.2 Automated validation

The existing validator and test suite remain unchanged. They validate the Python validator, not the skill prompt. No new tests needed for the prompt itself (prompt testing requires an LLM in the loop).

#### 4.3 Regression check

| Component | Verifies unchanged |
|-----------|-------------------|
| `python -m pytest tests/ -v` | Validator integrity |
| `python -m validator.cli --file benchmarks/01-well-optimized.txt --keyword "content marketing strategy" --checklist` | Deterministic scoring |
| `.\run_tests.ps1` | Full benchmark regression |
| Multi-file tools (OpenCode, Claude Code) | Can still load shared/ + scenarios/ directly |
| HumanAI / MindFluence integration | Integration section in SKILL.md unchanged |

---

## 4. WHAT STAYS UNCHANGED (NO REGRESSIONS)

| Component | Status |
|-----------|--------|
| `validator/` (all files) | **Untouched** — zero changes |
| `tests/` (all files) | **Untouched** |
| `benchmarks/` (all files) | **Untouched** |
| `shared/` (all files) | **Untouched** — still loadable directly |
| `scenarios/` (all files) | **Untouched** — still loadable directly |
| `examples/` (existing: before-after, meta, audit) | **Untouched** |
| `pyproject.toml` | **Untouched** |
| `requirements.txt` | **Untouched** |
| `run_tests.ps1` | **Untouched** |
| `README.md`, `README.ru.md` | **Untouched** |
| `CHANGELOG.md` | **Untouched** |
| `LICENSE`, `.gitignore`, `.gitattributes` | **Untouched** |

**Only changed files:**
- `SKILL.md` — enhanced inline, scenario summaries added, fetch strategy added, URL index added
- `examples/integration-pipeline.md` — NEW (stub, fixes broken reference)
- `INTEGRATION-GUIDE.md` — NEW (stub, fixes broken reference)

---

## 5. RISK ANALYSIS

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| SKILL.md grows too large for very small context windows (<4K tokens) | Low | Medium | Inline English word lists replace need to fetch for EN tasks. Non-EN tasks fetch as needed. |
| GitHub raw URLs become unavailable (repo goes private, renamed, deleted) | Low | High | URLs point to public repo. If unavailable, inline content is sufficient for basic operation. |
| Raw URL version mismatch (fetching `main` after breaking changes) | Medium | Medium | Document version pinning strategy. Users can pin to a tag. |
| AI tools that lack webfetch capability | Medium | Medium | Offline mode covered in FETCH STRATEGY. English = fully inline. Non-EN = flagged with warning. |
| Increased SKILL.md length = higher token cost for every invocation | Low | Low | From 696 to ~1000 lines ~ +45% tokens. Acceptable tradeoff for single-file capability. |
| Scenario summaries become stale vs full scenario files | Medium | Low | Summaries are intentionally "essential rules only." Full files remain authoritative. Fetch URL provided. |

---

## 6. SUCCESS CRITERIA

After implementation, the following must be true:

1. **Single-file execution:** An AI that reads ONLY `SKILL.md` can generate a complete, correctly optimized English SEO article without fetching any additional files.
2. **Fetch-enhanced execution:** An AI that reads `SKILL.md` + fetches the recommended URLs can generate/rewrite/audit content in ANY of the 9 supported languages with full reference data.
3. **Offline graceful degradation:** An AI that reads `SKILL.md` but CANNOT fetch URLs can still operate, producing English output at full quality and non-English output with a warning flag.
4. **No regressions:** All 45 existing tests pass. The validator produces identical scores. Multi-file loading tools still work.
5. **Broken references fixed:** `examples/integration-pipeline.md` and `INTEGRATION-GUIDE.md` exist and are reachable.
6. **Backward-compatible:** Existing integrations (HumanAI, MindFluence) continue to work because they load files directly and don't depend on the fetch strategy.

---

## 7. ESTIMATED EFFORT

| Phase | Task | Lines changed | Risk |
|-------|------|---------------|------|
| 1 | Rewrite SKILL.md as single-file orchestrator | ~400 lines added, ~50 lines restructured | Medium |
| 2 | Create missing stub files (integration-pipeline, INTEGRATION-GUIDE) | ~30 lines each | None |
| 3 | Add version pinning docs | ~5 lines | None |
| 4 | Manual smoke tests (6 test cases) | 0 lines, ~1 hour | None |

**Total:** ~2-3 hours of work. Zero risk of regression (only SKILL.md changes; everything else is additive).

---

## 8. QUICK VALIDATION COMMAND

After implementing, run to confirm no regressions:

```powershell
# 1. Validator tests
python -m pytest tests/ -v --tb=short

# 2. Benchmark regression
python -m validator.cli --file benchmarks/01-well-optimized.txt --keyword "content marketing strategy" --title "7 Proven Content Marketing Strategies That Actually Work in 2026" --meta "Content marketing strategy guide: 7 proven tactics to grow organic traffic. Based on analysis of 200+ SaaS companies. Free template included." --checklist

# 3. Verify file count
@(Get-ChildItem -Recurse -File | Where-Object { $_.Extension -ne '.pyc' }).Count
# Expected: 31 (existing) + 2 (new stubs) = 33 files

# 4. Check no shared/ or scenarios/ files were modified
git diff --name-only -- shared/ scenarios/ benchmarks/ tests/ validator/
# Expected: empty (no output)
```
