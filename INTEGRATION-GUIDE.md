# INTEGRATION GUIDE — RankWise for External Skill Maintainers
> **Version:** 1.3.0

> This guide is for maintainers of HumanAI, MindFluence, and other downstream skills that integrate with RankWise.

---

## 1. Rules to Add in Your Skill

When your skill receives a RankWise output as input, enforce these guardrails:

### 1.1 Keyword Placement Preservation
Your skill may rewrite sentences but MUST preserve keyword positions in:
- Title/H1 (keyword in first 3-5 words)
- First 150 words of body
- At least one H2/H3 heading
- Meta description (within first 20 words)
- At least one image alt text

**Implementation:** If your skill uses text cleanup/paraphrasing, add a blacklist of sentences that contain the focus keyword — do not modify or remove them.

### 1.2 Heading Hierarchy Lock
H1 → H2 → H3 nesting must survive any rewrite. If your skill restructures content:
- Never change heading levels (H2 stays H2)
- Never add/remove numbered headings
- Only rewrite content UNDER headings, never the heading text itself (unless your skill is specifically an SEO heading optimizer)

### 1.3 Density Caps
After any text expansion or contraction by your skill:
- Check keyword density stays within 0.8%–1.5%
- If your skill expands text by >20%, recommend a follow-up RankWise audit
- If your skill shortens text, cap minimum word count at 600 for blog content

### 1.4 Link Integrity
Preserve all hyperlinks (internal and external) from the RankWise output. If your skill removes formatting, re-add links at their original positions.

### 1.5 Meta Tags Separation
Do NOT generate your own SEO title or meta description. RankWise handles the SEO meta layer. If your skill needs to output a title, use a non-SEO field (e.g., display title, social title).

### 1.6 Language Consistency
If your skill translates or localizes content, apply the target language's:
- Readability targets (see `shared/readability-params.md`)
- Power words (see `shared/power-words.md`)
- Burned words / AI markers (see `shared/burned-words.md`)

---

## 2. Tone × SEO Compatibility Matrix

| Tone/Domain | SEO Risk | Mitigation |
|-------------|----------|------------|
| Persuasive/sales copy | May over-stuff power words → dilutes emotional impact | Cap power words at 2 per 300 words |
| Technical/academic | Passive voice may exceed 10% → justified if contextually necessary | Flag as ⚠️ not ❌ if >10% but domain-appropriate |
| Conversational/casual | May drop transition words below 30% → fragments become choppy | Add transitions at paragraph boundaries only |
| Humorous/satirical | Keyword placement may feel forced → unnatural density | Allow keyword density down to 0.5% if contextually justified |
| Minimalist/poetic | May drop below 600 words → not enough substance for ranking | Set minimum 300 words for artistic content, flag C1 as ⚠️ |

---

## 3. Triple Pipeline Protocol

```
Phase 1: RankWise Brief or Generate
         → SEO structure: keywords, headings, word count, meta drafts

Phase 2: MindFluence (persuasion layer)
         → Apply cognitive biases, persuasion frameworks, emotional arcs
         → Constraint: preserve keyword positions and heading hierarchy

Phase 3: HumanAI (humanization layer)
         → Strip remaining AI markers, add personality, vary cadence
         → Constraint: re-check density after pass, fix if drifted

Phase 4: RankWise Audit
         → Score final output against 49 factors
         → Flag any factors broken during Phase 2 or 3
```

---

## 4. Quick Reference

- **Full skill specification:** `SKILL.md`
- **49-factor scorecard:** `shared/checklist.md`
- **Power words × 9 languages:** `shared/power-words.md`
- **Burned words × 9 languages:** `shared/burned-words.md`
- **Readability targets × 9 languages:** `shared/readability-params.md`
- **Schema templates:** `shared/schema-templates.md`
