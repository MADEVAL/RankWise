"""
RankWise Orchestrator — automated pipeline bridging LLM generation and
deterministic validation.  Generates targeted fix prompts for the LLM
based on validator results, supports iterative re-validation.
"""

import copy
import json
import math
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from .metrics import (
    TextMetrics,
    ParagraphInfo,
    SentenceInfo,
    analyze,
    score_checklist,
    report,
    WORD_PATTERNS,
    PASSIVE_PATTERNS,
    TRANSITION_WORDS,
    POWER_WORDS,
    READABILITY_TARGETS,
)


def _tokenize_words(text: str, lang: str = "en") -> list[str]:
    pat = WORD_PATTERNS.get(lang, WORD_PATTERNS["en"])
    return pat.findall(text.lower())


# ── Language-specific label tables ───────────────────────────────────────
_TITLE_RANGES = {
    "en": (50, 60), "de": (50, 65), "fr": (50, 63), "es": (50, 63),
    "pt": (50, 63), "it": (50, 63), "pl": (50, 65), "ru": (55, 70), "uk": (55, 70),
}
_META_RANGES = {
    "en": (145, 158), "de": (145, 158), "fr": (145, 158), "es": (145, 158),
    "pt": (145, 158), "it": (145, 158), "pl": (145, 158), "ru": (140, 160), "uk": (140, 160),
}
_TW_TARGETS = {"en": 30, "ru": 25, "uk": 25, "de": 25, "fr": 25, "es": 25, "pt": 25, "it": 25, "pl": 25}


@dataclass
class FixInstruction:
    factor_id: str
    factor_name: str
    severity: str  # CRITICAL / HIGH / MEDIUM / LOW
    status: str    # fail / warning
    detail: str    # what's wrong
    target: str    # what it should be
    llm_prompt: str = ""       # ready-to-inject prompt for the LLM
    text_locations: list[str] = field(default_factory=list)  # quoted snippets
    deterministic_fix: str = ""  # auto-applicable suggestion (e.g. title truncation)


@dataclass
class FixPlan:
    lang: str
    keyword: str
    total_factors: int
    passed: int
    failed: int
    warnings: int
    na_count: int
    weighted_score_pct: float
    grade: str
    critical_count: int
    instructions: list[FixInstruction] = field(default_factory=list)


@dataclass
class IterationResult:
    round: int
    metrics_before: dict
    metrics_after: dict
    fixes_applied: list[str]
    regressions: list[str]
    needs_another_round: bool


class Orchestrator:
    """Bridge between deterministic validation and LLM content generation.

    Usage::

        orch = Orchestrator(text, keyword="seo strategy", title="My Title")
        plan = orch.build_fix_plan()
        for instr in plan.instructions:
            print(instr.llm_prompt)

        # After LLM applies fixes:
        new_plan = orch.revalidate(new_text)
    """

    def __init__(
        self,
        text: str,
        keyword: str = "",
        title: str = "",
        meta_description: str = "",
        lang: str = "en",
    ):
        self._original_text = text
        self._original_keyword = keyword
        self._original_title = title
        self._original_meta = meta_description
        self._lang = lang
        self._metrics = analyze(text, keyword=keyword, title=title,
                                meta_description=meta_description, lang=lang)
        self._scores = score_checklist(self._metrics)
        self._history: list[IterationResult] = []

    # ── public API ──────────────────────────────────────────────────────
    @property
    def metrics(self) -> TextMetrics:
        return self._metrics

    @property
    def checklist_scores(self) -> dict:
        return self._scores

    def build_fix_plan(self) -> FixPlan:
        """Generate a structured fix plan with LLM-ready prompts."""
        instructions = []
        failure_order = {"fail": 0, "warning": 1, "pass": 2, "na": 3}
        severity_order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}

        sorted_factors = sorted(
            self._scores.items(),
            key=lambda item: (
                failure_order.get(item[1]["status"], 99),
                severity_order.get(_factor_severity(item[0]), 99),
                item[0],
            )
        )

        for fid, info in sorted_factors:
            if info["status"] in ("pass", "na"):
                continue
            instr = self._build_instruction(fid, info)
            instructions.append(instr)

        passed = sum(1 for v in self._scores.values() if v["status"] == "pass")
        failed = sum(1 for v in self._scores.values() if v["status"] == "fail")
        warnings = sum(1 for v in self._scores.values() if v["status"] == "warning")
        na = sum(1 for v in self._scores.values() if v["status"] == "na")
        critical_fails = sum(
            1 for fid, v in self._scores.items()
            if v["status"] == "fail" and _factor_severity(fid) == "CRITICAL"
        )
        critical_warns = sum(
            1 for fid, v in self._scores.items()
            if v["status"] == "warning" and _factor_severity(fid) == "CRITICAL"
        )

        ws, grade = _compute_weighted_score(self._scores)

        return FixPlan(
            lang=self._lang,
            keyword=self._original_keyword,
            total_factors=len(self._scores),
            passed=passed,
            failed=failed,
            warnings=warnings,
            na_count=na,
            weighted_score_pct=ws,
            grade=grade,
            critical_count=critical_fails,
            instructions=instructions,
        )

    def revalidate(self, new_text: str, new_title: str = "",
                   new_meta: str = "") -> FixPlan:
        """Re-run validation on updated content.  Returns a new FixPlan."""
        self._metrics = analyze(
            new_text,
            keyword=self._original_keyword,
            title=new_title or self._original_title,
            meta_description=new_meta or self._original_meta,
            lang=self._lang,
        )
        self._scores = score_checklist(self._metrics)
        return self.build_fix_plan()

    def diff_report(self, before: FixPlan, after: FixPlan) -> str:
        """Human-readable before→after comparison."""
        lines = [
            "=" * 60,
            "  RankWise Orchestrator — Iteration Diff",
            "=" * 60,
            "",
            f"  Before: {before.weighted_score_pct:.1f}% ({before.grade})  |  "
            f"P:{before.passed} F:{before.failed} W:{before.warnings} N/A:{before.na_count}",
            f"  After:  {after.weighted_score_pct:.1f}% ({after.grade})  |  "
            f"P:{after.passed} F:{after.failed} W:{after.warnings} N/A:{after.na_count}",
            "",
            "  Changes:",
        ]
        before_map = {i.factor_id: i.status for i in before.instructions}
        after_scores = self._scores
        changed = []
        for fid in set(list(before_map.keys()) + list(after_scores.keys())):
            bs = before_map.get(fid, "pass")
            ad = after_scores.get(fid, {}).get("status", "pass")
            if bs != ad:
                icon = "+" if ad == "pass" else "→" if ad == "warning" else "↓"
                changed.append(f"    {icon} {fid}: {bs} → {ad}")

        if changed:
            lines.extend(changed)
        else:
            lines.append("    (no status changes)")
        return "\n".join(lines)

    def fix_prompt_batch(self) -> str:
        """Return a single consolidated prompt with all fixes, ready for the LLM."""
        plan = self.build_fix_plan()
        if not plan.instructions:
            return "[ALL CLEAR] All 16 computable factors pass. No fixes needed."

        parts = [
            f"[SEO FIX BATCH — {plan.lang.upper()} | keyword: '{plan.keyword}']",
            f"Score: {plan.weighted_score_pct:.1f}% ({plan.grade}) | "
            f"Pass:{plan.passed} Fail:{plan.failed} Warn:{plan.warnings} N/A:{plan.na_count}",
            "",
            "Apply these fixes in order. After each fix, re-check related factors.",
            "",
        ]
        for instr in plan.instructions:
            parts.append(f"### {instr.factor_id} — {instr.factor_name} "
                         f"[{instr.severity}] [{instr.status.upper()}]")
            parts.append(f"Issue: {instr.detail}")
            parts.append(f"Target: {instr.target}")
            if instr.llm_prompt:
                parts.append(f"Action:\n{instr.llm_prompt}")
            parts.append("")
        return "\n".join(parts)

    def to_dict(self) -> dict:
        """Full serialisable state for JSON export."""
        plan = self.build_fix_plan()
        return {
            "lang": plan.lang,
            "keyword": plan.keyword,
            "score_pct": plan.weighted_score_pct,
            "grade": plan.grade,
            "passed": plan.passed,
            "failed": plan.failed,
            "warnings": plan.warnings,
            "na": plan.na_count,
            "critical_failures": plan.critical_count,
            "factors": {
                fid: info for fid, info in self._scores.items()
            },
            "fix_instructions": [
                {
                    "factor_id": i.factor_id,
                    "factor_name": i.factor_name,
                    "severity": i.severity,
                    "status": i.status,
                    "detail": i.detail,
                    "target": i.target,
                    "llm_prompt": i.llm_prompt,
                    "text_locations": i.text_locations,
                    "deterministic_fix": i.deterministic_fix,
                }
                for i in plan.instructions
            ],
        }

    # ── instruction builders ────────────────────────────────────────────
    def _build_instruction(self, fid: str, info: dict) -> FixInstruction:
        builder = getattr(self, f"_fix_{fid}", None)
        if builder:
            return builder(fid, info)
        return FixInstruction(
            factor_id=fid,
            factor_name=_FACTOR_NAMES.get(fid, fid),
            severity=_factor_severity(fid),
            status=info["status"],
            detail=info.get("detail", ""),
            target=_FACTOR_TARGETS.get(fid, ""),
        )

    # ── K1: Focus keyword set ──────────────────────────────────────────
    def _fix_K1(self, fid, info):
        return FixInstruction(
            factor_id=fid, factor_name="Focus Keyword Set", severity="CRITICAL",
            status=info["status"], detail=info["detail"],
            target="Define one primary keyword for this page",
            llm_prompt=(
                "No focus keyword is set. Assign ONE primary keyword "
                "that best describes the page topic. Use a 2-5 word phrase "
                "(e.g. 'email marketing strategy', not just 'email')."
            ),
        )

    # ── K2: Keyword in SEO title ───────────────────────────────────────
    def _fix_K2(self, fid, info):
        kw = self._original_keyword
        t = self._original_title
        return FixInstruction(
            factor_id=fid, factor_name="Keyword in SEO Title", severity="CRITICAL",
            status=info["status"], detail=info["detail"],
            target=f"SEO title must contain '{kw}'",
            llm_prompt=(
                f"The focus keyword **'{kw}'** is missing from the SEO title.\n"
                f"Current title: \"{t}\"\n"
                f"Rewrite the title to include '{kw}' naturally, keeping it within "
                f"the first 3-5 words. Preserve any existing number and power words."
            ),
        )

    # ── K6: Keyword in first 150 words ─────────────────────────────────
    def _fix_K6(self, fid, info):
        kw = self._original_keyword
        return FixInstruction(
            factor_id=fid, factor_name="Keyword at Content Start", severity="HIGH",
            status=info["status"], detail=info["detail"],
            target=f"'{kw}' must appear within the first 100-150 words",
            llm_prompt=(
                f"The keyword **'{kw}'** does not appear in the first 150 words "
                f"of the body text. Rewrite the opening paragraph to naturally "
                f"include '{kw}' once. Do NOT use a forced construction like "
                f"'In this article about {kw}...' — weave it into a real sentence."
            ),
        )

    # ── K7: Keyword in content body ────────────────────────────────────
    def _fix_K7(self, fid, info):
        kw = self._original_keyword
        return FixInstruction(
            factor_id=fid, factor_name="Keyword in Content Body", severity="CRITICAL",
            status=info["status"], detail=info["detail"],
            target=f"'{kw}' must appear at least once in the body",
            llm_prompt=(
                f"The keyword **'{kw}'** was not found anywhere in the body text. "
                f"Add 1-2 natural instances of '{kw}' where it fits the topic. "
                f"Spread them across different sections — do not cluster."
            ),
        )

    # ── K10: Keyword density ───────────────────────────────────────────
    def _fix_K10(self, fid, info):
        kw = self._original_keyword
        m = self._metrics
        density = m.keyword_density_pct
        occurrences = m.keyword_occurrences
        wc = m.word_count

        if density == 0:
            prompt = (
                f"Keyword '{kw}' density is 0% — the keyword does not appear "
                f"in the body. Add 2-4 instances distributed naturally."
            )
        elif density < 0.8:
            needed = max(1, math.ceil((0.8 * wc / 100) - occurrences))
            prompt = (
                f"Keyword density is too low: {density:.2f}% ({occurrences} occurrences "
                f"in {wc} words). Target: 0.8-1.5%.\n"
                f"Add {needed} more natural instance(s) of '{kw}'. "
                f"Place in sections that discuss the topic but don't yet use the exact phrase."
            )
        elif density <= 3.0:
            excess = occurrences - math.floor(1.5 * wc / 100)
            prompt = (
                f"Keyword density is elevated: {density:.2f}% ({occurrences} occurrences "
                f"in {wc} words). Target: 0.8-1.5%.\n"
                f"Replace ~{excess} instance(s) of '{kw}' with synonyms, pronouns ('it', 'this approach'), "
                f"or rephrase sentences to avoid the exact phrase."
            )
        else:
            excess = occurrences - math.floor(1.5 * wc / 100)
            prompt = (
                f"KEYWORD STUFFING detected: {density:.2f}% ({occurrences} occurrences "
                f"in {wc} words). Target: 0.8-1.5%.\n"
                f"Remove or replace ~{excess} instances of '{kw}'. Use synonyms, pronouns, "
                f"stemmed forms, or restructure sentences entirely."
            )

        return FixInstruction(
            factor_id=fid, factor_name="Keyword Density", severity="HIGH",
            status=info["status"], detail=info["detail"],
            target="0.8%–1.5% keyword density",
            llm_prompt=prompt,
        )

    # ── C1: Word count ─────────────────────────────────────────────────
    def _fix_C1(self, fid, info):
        wc = self._metrics.word_count
        short = 600 - wc
        return FixInstruction(
            factor_id=fid, factor_name="Word Count", severity="HIGH",
            status=info["status"], detail=info["detail"],
            target="600+ words minimum (1500+ competitive)",
            llm_prompt=(
                f"Word count is {wc} — {short} words below the 600-word minimum.\n"
                f"Expand the thinnest sections. For each, add:\n"
                f"  - 1 concrete example or case study\n"
                f"  - 1 data point / statistic\n"
                f"  - 1 actionable step the reader can take\n"
                f"Target: at least +{short} words total."
            ),
        )

    # ── C2: Short paragraphs ───────────────────────────────────────────
    def _fix_C2(self, fid, info):
        m = self._metrics
        max_w = 150 if self._lang == "en" else 120
        long_paras = [p for p in m.paragraphs if p.word_count > max_w or p.sentence_count > 3]
        locations = [f"\"{p.text[:80]}...\" ({p.word_count}w, {p.sentence_count}s)" for p in long_paras[:5]]

        return FixInstruction(
            factor_id=fid, factor_name="Short Paragraphs", severity="MEDIUM",
            status=info["status"], detail=info["detail"],
            target=f"≤3 sentences, ≤{max_w} words per paragraph",
            llm_prompt=(
                f"{len(long_paras)} paragraph(s) exceed limits:\n" +
                "\n".join(f"  • {loc}" for loc in locations) +
                f"\n\nBreak each at a logical transition point. Each new paragraph "
                f"should carry exactly one core idea."
            ),
            text_locations=locations,
        )

    # ── C5: Number in title ────────────────────────────────────────────
    def _fix_C5(self, fid, info):
        t = self._original_title
        return FixInstruction(
            factor_id=fid, factor_name="Number in Title", severity="MEDIUM",
            status=info["status"], detail=info["detail"],
            target="At least 1 number in the title (odd numbers preferred)",
            llm_prompt=(
                f"The title has no number. Odd numbers increase CTR.\n"
                f"Current: \"{t}\"\n"
                f"Add a specific number. Options:\n"
                f"  - 'X Ways to...' (use 5, 7, 9, or 11)\n"
                f"  - '...Increased Y by X%'\n"
                f"  - 'X Steps...' / 'Top X...'"
            ),
        )

    # ── C6: Power words in title ───────────────────────────────────────
    def _fix_C6(self, fid, info):
        t = self._original_title
        pw_set = POWER_WORDS.get(self._lang, POWER_WORDS["en"])
        current = self._metrics.title_power_word_count
        missing = 2 - current
        return FixInstruction(
            factor_id=fid, factor_name="Power Words in Title", severity="MEDIUM",
            status=info["status"], detail=info["detail"],
            target="≥2 power words in title",
            llm_prompt=(
                f"Title has only {current} power word(s). Need ≥2.\n"
                f"Current: \"{t}\"\n"
                f"Add {missing} emotionally charged word(s) from the {self._lang} "
                f"power word set. Examples from the approved list: "
                + ", ".join(sorted(pw_set)[:12]) + "..."
            ),
        )

    # ── C8: Readability ────────────────────────────────────────────────
    def _fix_C8(self, fid, info):
        m = self._metrics
        target = READABILITY_TARGETS.get(self._lang, READABILITY_TARGETS["en"])
        lo, hi = target["range"]
        mode = target["mode"]

        long_sents = [s for s in m.sentences if s.word_count > 25]
        locations = [f"\"{s.text[:80]}...\" ({s.word_count}w)" for s in long_sents[:5]]

        return FixInstruction(
            factor_id=fid, factor_name="Readability Score", severity="HIGH",
            status=info["status"], detail=info["detail"],
            target=f"Readability within target range ({mode}: {lo}-{hi})",
            llm_prompt=(
                f"Readability is outside the target range for {self._lang} "
                f"({mode}: target {lo}-{hi}).\n"
                + (f"Found {len(long_sents)} sentences exceeding 25 words:\n" +
                   "\n".join(f"  • {loc}" for loc in locations) +
                   "\n\n" if locations else "") +
                f"Actions:\n"
                f"  1. Split sentences longer than 25 words into two\n"
                f"  2. Replace complex/jargon words with simpler alternatives\n"
                f"  3. Break dense paragraphs into smaller chunks"
            ),
            text_locations=locations,
        )

    # ── C9: Passive voice ──────────────────────────────────────────────
    def _fix_C9(self, fid, info):
        m = self._metrics
        passive_sents = [s for s in m.sentences if s.is_passive]
        locations = [f"\"{s.text[:80]}...\"" for s in passive_sents[:8]]

        return FixInstruction(
            factor_id=fid, factor_name="Passive Voice Ratio", severity="MEDIUM",
            status=info["status"], detail=info["detail"],
            target="≤10% of sentences in passive voice",
            llm_prompt=(
                f"Passive voice: {m.passive_ratio_pct}% ({m.passive_sentence_count}/{m.sentence_count} sentences). "
                f"Target: ≤10%.\n"
                f"Convert these passive sentences to active voice:\n" +
                "\n".join(f"  • {loc}" for loc in locations) +
                "\n\nRule: identify the actor and make it the subject. "
                f"'was written by X' → 'X wrote'. 'can be done' → 'you can do'."
            ),
            text_locations=locations,
        )

    # ── C10: Transition words ──────────────────────────────────────────
    def _fix_C10(self, fid, info):
        m = self._metrics
        target_tw = _TW_TARGETS.get(self._lang, 30)
        tw_set = TRANSITION_WORDS.get(self._lang, TRANSITION_WORDS["en"])
        no_tw_sents = [s for s in m.sentences if not s.has_transition]

        return FixInstruction(
            factor_id=fid, factor_name="Transition Words", severity="LOW",
            status=info["status"], detail=info["detail"],
            target=f"≥{target_tw}% of sentences use transition words",
            llm_prompt=(
                f"Transition words: {m.transition_ratio_pct}% ({m.transition_sentence_count}/{m.sentence_count} sentences). "
                f"Target: ≥{target_tw}%.\n"
                f"Add transition words at logical turning points between ideas.\n"
                f"Approved transitions for {self._lang}: "
                + ", ".join(sorted(tw_set)[:15]) + "...\n"
                f"Add transitions to ~{max(1, int(target_tw * m.sentence_count / 100) - m.transition_sentence_count)} "
                f"more sentences, especially at paragraph boundaries and between contrasting ideas."
            ),
        )

    # ── C11: Sentence length variety ───────────────────────────────────
    def _fix_C11(self, fid, info):
        m = self._metrics
        violations = []
        for i in range(len(m.sentences) - 2):
            a, b, c = m.sentences[i].word_count, m.sentences[i + 1].word_count, m.sentences[i + 2].word_count
            if abs(a - b) <= 2 and abs(b - c) <= 2:
                violations.append(
                    f"\"{m.sentences[i].text[:60]}...\" "
                    f"({a}w) → \"{m.sentences[i+1].text[:60]}...\" "
                    f"({b}w) → \"{m.sentences[i+2].text[:60]}...\" ({c}w)"
                )

        return FixInstruction(
            factor_id=fid, factor_name="Sentence Length Variety", severity="MEDIUM",
            status=info["status"], detail=info["detail"],
            target="No 3 consecutive sentences of similar length (±2 words)",
            llm_prompt=(
                f"Found {m.monotony_violations} monotony violation(s) — "
                f"3+ consecutive sentences with nearly identical length:\n" +
                "\n".join(f"  • {v}" for v in violations[:5]) +
                "\n\nRewrite to vary sentence length. Mix short (2-5w), "
                "medium (10-15w), and long (18-25w) sentences."
            ),
            text_locations=violations,
        )

    # ── C12: Consecutive sentence starts ───────────────────────────────
    def _fix_C12(self, fid, info):
        m = self._metrics
        violations = []
        for i in range(len(m.sentences) - 2):
            a = m.sentences[i].first_word
            b = m.sentences[i + 1].first_word
            c = m.sentences[i + 2].first_word
            if a and a == b == c:
                violations.append(
                    f"All start with '{a}': \"{m.sentences[i].text[:50]}...\" / "
                    f"\"{m.sentences[i+1].text[:50]}...\" / "
                    f"\"{m.sentences[i+2].text[:50]}...\""
                )

        return FixInstruction(
            factor_id=fid, factor_name="Consecutive Sentence Starts", severity="MEDIUM",
            status=info["status"], detail=info["detail"],
            target="No 3 consecutive sentences with the same first word",
            llm_prompt=(
                f"Found {m.starter_violations} repeated-start violation(s):\n" +
                "\n".join(f"  • {v}" for v in violations[:5]) +
                "\n\nVary sentence openers. Alternatives: start with a preposition "
                "('In...', 'By...'), a conjunction ('But...', 'Because...'), "
                "a question word, or flip subject-object order."
            ),
            text_locations=violations,
        )

    # ── T3: Title length ───────────────────────────────────────────────
    def _fix_T3(self, fid, info):
        t = self._original_title
        t_lo, t_hi = _TITLE_RANGES.get(self._lang, (50, 60))
        chars = self._metrics.title_char_count

        if chars == 0:
            prompt = "No title provided. Write an SEO title with the keyword near the beginning."
        elif chars < t_lo:
            prompt = (
                f"Title is too short: {chars} chars (target {t_lo}-{t_hi}).\n"
                f"Current: \"{t}\"\n"
                f"Expand by adding: a power word, a number, specificity, or a benefit hook."
            )
        else:
            prompt = (
                f"Title is too long: {chars} chars (target {t_lo}-{t_hi}).\n"
                f"Current: \"{t}\"\n"
                f"Trim by: removing filler words ('the', 'very', 'just'), "
                f"condensing phrases, or splitting brand to end with ' | Brand'."
            )

        return FixInstruction(
            factor_id=fid, factor_name="SEO Title Length", severity="HIGH",
            status=info["status"], detail=info["detail"],
            target=f"{t_lo}-{t_hi} characters (per {self._lang} limits)",
            llm_prompt=prompt,
        )

    # ── T4: Meta description length ────────────────────────────────────
    def _fix_T4(self, fid, info):
        md = self._original_meta
        m_lo, m_hi = _META_RANGES.get(self._lang, (145, 158))
        chars = self._metrics.meta_description_char_count

        if chars == 0:
            prompt = "No meta description provided. Write one with the keyword in the first 20 words."
        elif chars < m_lo:
            prompt = (
                f"Meta description is too short: {chars} chars (target {m_lo}-{m_hi}).\n"
                f"Current: \"{md}\"\n"
                f"Expand with: a supporting detail, credibility element, or CTA."
            )
        else:
            prompt = (
                f"Meta description is too long: {chars} chars (target {m_lo}-{m_hi}).\n"
                f"Current: \"{md}\"\n"
                f"Trim by removing redundant phrases, cutting to one value proposition."
            )

        return FixInstruction(
            factor_id=fid, factor_name="Meta Description Length", severity="HIGH",
            status=info["status"], detail=info["detail"],
            target=f"{m_lo}-{m_hi} characters (per {self._lang} limits)",
            llm_prompt=prompt,
        )


# ═══════════════════════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════════════════════

_FACTOR_NAMES = {
    "K1": "Focus Keyword Set", "K2": "Keyword in SEO Title",
    "K6": "Keyword at Content Start", "K7": "Keyword in Content Body",
    "K10": "Keyword Density", "C1": "Word Count", "C2": "Short Paragraphs",
    "C5": "Number in Title", "C6": "Power Words in Title",
    "C8": "Readability Score", "C9": "Passive Voice Ratio",
    "C10": "Transition Words", "C11": "Sentence Length Variety",
    "C12": "Consecutive Sentence Starts", "T3": "SEO Title Length",
    "T4": "Meta Description Length",
}

_FACTOR_TARGETS = {
    "K1": "Define one primary keyword", "K2": "Keyword must appear in title",
    "K6": "Keyword within first 100-150 words", "K7": "Keyword in body text",
    "K10": "Density 0.8%–1.5%", "C1": "600+ words (1500+ competitive)",
    "C2": "≤3 sentences, ≤150 words per paragraph",
    "C5": "At least 1 number in title", "C6": "≥2 power words in title",
    "C8": "Readability within target range per language",
    "C9": "≤10% passive voice", "C10": "≥25-30% transition words",
    "C11": "Vary sentence length rhythm",
    "C12": "Vary sentence openers", "T3": "Title within per-language range",
    "T4": "Meta description within per-language range",
}

_FACTOR_SEVERITY_MAP = {
    "K1": "CRITICAL", "K2": "CRITICAL", "K6": "HIGH", "K7": "CRITICAL",
    "K10": "HIGH", "C1": "HIGH", "C2": "MEDIUM", "C5": "MEDIUM",
    "C6": "MEDIUM", "C8": "HIGH", "C9": "MEDIUM", "C10": "LOW",
    "C11": "MEDIUM", "C12": "MEDIUM", "T3": "HIGH", "T4": "HIGH",
}


def _factor_severity(fid: str) -> str:
    return _FACTOR_SEVERITY_MAP.get(fid, "MEDIUM")


def _compute_weighted_score(scores: dict) -> tuple[float, str]:
    multiplier = {"CRITICAL": 3, "HIGH": 2, "MEDIUM": 1, "LOW": 0.5}
    total_weight = 0.0
    earned_weight = 0.0
    critical_fails = 0.0

    for fid, info in scores.items():
        if info["status"] == "na":
            continue
        sev = _factor_severity(fid)
        w = multiplier.get(sev, 1)
        total_weight += w

        if info["status"] == "pass":
            earned_weight += w
        elif info["status"] == "warning":
            earned_weight += w * 0.5
            if sev == "CRITICAL":
                critical_fails += 0.5
        elif info["status"] == "fail":
            if sev == "CRITICAL":
                critical_fails += 1

    if total_weight == 0:
        return 0.0, "N/A"

    raw = (earned_weight / total_weight) * 100

    if raw >= 90 and critical_fails == 0:
        grade = "A"
    elif raw >= 75 and critical_fails <= 1:
        grade = "B"
    elif raw >= 60 and critical_fails <= 3:
        grade = "C"
    elif raw >= 40:
        grade = "D"
    else:
        grade = "F"

    return round(raw, 1), grade
