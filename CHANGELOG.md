# Changelog

## [1.3.0] - 2026-07-12

### Added
- `scenarios/video-podcast.md` — YouTube / podcast description & metadata SEO (11th scenario)
- `SKILL.md` architecture now includes `INTEGRATION-GUIDE.md` reference

### Changed
- Scenarios count: 10 → 11

## [1.2.3] - 2026-07-12

### Added
- **LANGUAGE RESOURCES** section — complete English word lists inline: power words (46), transition words (45), stop words (52), passive voice detection patterns, burned words × 8 categories. English operation requires zero external files.
- **Scoring formula + grade thresholds** — `Score % = (Σ PASS) / (Σ ALL) × 100`, A/B/C/D/F table with CRITICAL constraints
- **8-Factor Quick Scan** — pre-delivery checklist: K1, K2, K4, K7, K10, C1, C13, L1
- **Offline mode scoring** — explicit 7-factor exclusion (K11, L5-L8, T6-T7), max denominator 42

### Changed
- **L5 (Outbound link quality):** "DA 40+ or recognized authority" → "Recognized authority (.edu, .gov, known brands)"
- **A2 (E-E-A-T signals):** "Experience, Expertise, Authoritativeness, Trustworthiness" → "≥3 of 5 signals: author bio, publication date, citation, about page, contact/privacy"
- **C14 (Content-to-ad ratio):** "Main content dominates above-fold" → "≤20% ad/nav in first 300 words"
- **C10 (Transition words):** "≥30% of sentences contain transitions" → "≥30% of sentences (EN); ≥25% other languages"
- **Keyword density:** added formula `(exact_matches / total_words) × 100`
- **Anchor text:** added ratio targets (partial 30-40%, branded 20-25%, generic 20-25%, naked 5-10%, exact ≤2)
- **Paragraph rules:** added "120 for non-English"

## [1.2.2] - 2026-06-27

### Changed
- **Validator readability engine: `textstat` → [ReadSightPy](https://github.com/MADEVAL/ReadSightPy)** (`readsight>=1.0.0`). Syllable counting now uses the Frank M. Liang (TeX) hyphenation algorithm; 17 formulas with published per-language coefficients.
- **C8 readability is now computed deterministically for all 9 languages** (was EN-only via textstat). UK and PT are no longer `[N/A]` / delegated to the LLM — both are scored from real metrics.
- Per-language C8 metric: EN → Flesch-Kincaid Grade · DE → Wiener Sachtextformel · ES → Fernández-Huerta · IT → Gulpease · FR/RU/PT → Flesch Reading Ease · UK → LIX · PL → FOG-PL.
- PL readability moved off the old pyphen-based Flesch workaround onto the proper Polish **FOG-PL** formula.
- Basic counts (words, sentences, characters) are now library-independent — derived from the validator's own per-language tokenizer and sentence splitter, consistent with keyword/passive/transition analysis.
- `TEXTSTAT_LANG_MAP` renamed to `READSIGHT_LANG_MAP`; `READABILITY_LANGS` now covers all 9 languages.

### Added
- **LIX readability index** in validator output (`TextMetrics.lix`) — closes a previously missing readability signal.
- ReadSightPy engine caching per language code for repeated analyses.

### Fixed
- Validator no longer depends on `textstat` (removed from `requirements.txt` and `pyproject.toml`). Readability for UK/PT/PL is no longer silently handed to the LLM.

## [1.2.1] - 2026-06-21

### Fixed
- **B1:** Duplicate rule numbering in MODULE ACTIVATION LOGIC - rules now correctly numbered 1–9 (was: two rules #6, two rules #2)
- **B3:** T8 factor sync between `shared/checklist.md` and `scenarios/audit-report.md` - both now consistently require OG title+description OR twitter:card (audit-report no longer incorrectly requires OG image)
- **B5:** Removed duplicate Specificity/Numbers and Emotional/Human categories from `shared/power-words.md` (were listed twice - once with translations, once without)
- **B6:** Quick Readability Checklist in `shared/readability-params.md` now reflects per-language max sentence lengths (was: generic "30 (25 for EN)", now: language-specific)
- **B4:** Added explicit exception note in `scenarios/alt-texts.md` - "Bar chart of...", "Infographic of...", "Diagram of..." are acceptable as content-type labels
- **B7:** Added "audit this meta + rewrite it" routing rule to MODULE ACTIVATION LOGIC (Scoped audit now covers meta-audit-then-rewrite scenario)

### Improved
- **C14 (Content-to-ad ratio):** Hardened from vague "main content visible" to measurable heuristic: >20% ad/nav in first 300 words = ❌ Fail
- **L5 (Outbound link quality):** Replaced arbitrary "DA 40+" threshold with domain reputation check (.edu, .gov, known brands). Unknown domains score ⚠️ Warning, not ❌ Fail.
- **A2 (E-E-A-T signals):** Tightened from "any 2 of 4" to "≥3 of 5 specific signals" with explicit pass/warning/fail thresholds
- **Editor role:** Added explicit "ruthless editor" persona to ROLE section - default stance is DELETE, keep only what earns its place
- **Incomplete input handling:** Added structured fallback table - what to ask when keyword/language/content/mode/modules are missing
- **Image generation disclaimer:** Explicitly stated RankWise does NOT generate images - scope is text, meta, alt texts, URLs only
- **README EN:** Replaced incomplete 13-factor table with compact category summary covering all 49 factors
- **OUTPUT FORMATS section:** Condensed from 55 lines to 15 lines - merged legacy formats into a quick-reference table, removed redundant code blocks

### Added
- `INTEGRATION-GUIDE.md` - integration specification for HumanAI and MindFluence maintainers: what rules to add, joint prompt recognition, density caps per tone, bias-SEO compatibility matrix, triple pipeline protocol
- `scenarios/home-page.md` - dedicated home page / brand page optimization with multi-keyword strategy
- `scenarios/product-page.md` - product / e-commerce page optimization with feature-benefit mapping and e-commerce signals
- Quick-fix coverage expanded to all 49 factors - each factor now has explicit fix instructions
- Universal power-word translations for Specificity/Numbers and Emotional/Human in all 9 languages
- Content-type routing table in SKILL.md - auto-routes blog/product/home/landing pages to correct scenario
- Multi-keyword page handling for home pages and pillar pages
- JS/SPA content notes - flag for client-rendered content
- Auto-translated content detection notes
- Code-heavy technical content readability adaptations
- Granular module sub-selection - "just the H2s", "only the intro", "just internal links"
- Audit + Brief composition rule
- Delivery validation rule - verifies all 49 factors are accounted for before output

### Changed
- MODULE ACTIVATION LOGIC: expanded from 7 to 9 rules (added Sub-selection, Audit+Brief)
- Output Composition: expanded from 10 to 12 rules
- Scenarios count: 8 → 10

## [1.1] - 2026-06-21

### Added
- **Ukrainian (uk) language support** - burned words, power words, stop words, keyword rules
- Output Composition system - 4 modular delivery units (TEXT, META, ALTS, AUDIT) with flexible combinations
- 4 new scored factors: K11 (cannibalization check), K12 (keyword length), L9 (link title attributes), T8 (OG/Twitter Card tags) - total now 49 factors
- `shared/burned-words.md` - AI detection patterns for all 8 supported languages
- `README.ru.md` - Russian documentation
- `examples/integration-pipeline.md` - end-to-end triple integration example (RankWise → MindFluence → HumanAI → Audit)
- Power words for Portuguese, Italian, Polish in `shared/power-words.md`
- Meta Length Parameters table in `shared/readability-params.md` with per-language title/description limits
- Triple integration section in `SKILL.md` with conflict matrix
- Quick-Fix mode detection rule in central mode detection logic
- N/A handling rules and weighted scoring methodology across checklist + audit-report

### Fixed
- Mode detection: "audit this title" now correctly routes to Meta-Only mode instead of full Audit
- Mode detection: Quick-Fix requests now auto-detected
- Transition word threshold: C10 now shows ≥30% EN / ≥25% other languages in checklist
- C14, L5, L6, L7, L8: replaced "Subjective" labels with proxy heuristics in audit-report
- Web-access fallback instructions added to article-generate, article-rewrite, and content-brief
- No-image handling: K9 and C3 now correctly marked N/A when no images present
- Language metadata: changed from "any" to explicit list "en, ru, de, fr, es, pt, it, pl"
- Meta-Only scoring expanded from 8 to 13 factors

### Changed
- Scoring system: from flat 1-point-per-factor to weighted scoring (CRITICAL=×3, HIGH=×2, MEDIUM=×1, LOW=×0.5)
- Grade constraints: A requires 0 CRITICAL failures, B requires ≤1, C requires ≤3
- Total factors: 45 → 49

## [1.0] - 2026-06-21

### Initial Release
- 5 operating modes: Generate, Rewrite, Audit, Meta-Only, Brief
- 45 ranking factors across keyword, content, linking, technical, and advanced categories
- 6 shared data files: checklist, keyword rules, power words, schema templates, readability params, link strategy
- 8 scenario playbooks: article-generate, article-rewrite, meta-optimize, alt-texts, audit-report, content-brief, url-optimize, quick-fix
- Multilingual support: all rules adapt to content language (EN, RU, DE, FR, ES, PT, IT, PL)
- Integration guides for HumanAI and MindFluence skills
- 3 annotated examples: article rewrite, meta optimization, audit report
- Industry-standard SEO flags fully covered + extended with advanced professional factors
