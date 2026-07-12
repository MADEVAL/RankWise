# Integration Pipeline Example
> **Version:** 1.3.0

> Multi-skill integration example: RankWise → downstream skill → Audit.

This file is a placeholder. The integration pipeline examples and protocols are maintained in:

- **SKILL.md → INTEGRATION WITH OTHER SKILLS** — general integration protocol, conflict awareness matrix, and joint prompt pattern
- **INTEGRATION-GUIDE.md** — integration specification for external skill maintainers

### Quick Reference Pattern

```
"1) RankWise SEO brief for [topic]. Keyword: [kw].
 2) [Skill Name] [action] from that output.
 3) RankWise audit the final result. [LANG: xx]."
```

### Triple Pipeline (RankWise → MindFluence → HumanAI → Audit)

1. **RankWise Generate/Brief** → establish SEO structure (keywords, headings, meta drafts)
2. **MindFluence** → apply persuasion/bias optimization within the SEO framework
3. **HumanAI** → humanize tone, remove remaining AI markers, add personality
4. **RankWise Audit** → verify all 49 factors survived the downstream transformations

### Guardrails for downstream skills
- Preserve keyword positions (title, first 150 words, ≥1 H2)
- Keep H1→H2→H3 hierarchy intact
- Re-check keyword density (0.8-1.5%) after any text transformation
- Preserve all inline hyperlinks
- Leave SEO meta layer to RankWise
- Apply target-language readability targets after translation

> **Full integration specification:** `INTEGRATION-GUIDE.md`
> **Burned words per language:** `shared/burned-words.md`
> **Readability targets per language:** `shared/readability-params.md`
