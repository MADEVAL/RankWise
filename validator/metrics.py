"""
RankWise Validator — computable SEO metrics for text content.
Uses textstat for readability, regex for linguistic patterns.
Supports EN; per-language extension points for RU, UK, DE, FR, ES, PT, IT, PL.
"""

import re
import statistics
from dataclasses import dataclass, field
from typing import Optional

import textstat


# ── Language-specific resources ────────────────────────────────────────────

STOP_WORDS_EN = {
    "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for",
    "of", "with", "by", "from", "up", "about", "into", "through", "during",
    "before", "after", "above", "below", "between", "out", "off", "over",
    "under", "again", "further", "then", "once", "here", "there", "when",
    "where", "why", "how", "all", "both", "each", "few", "more", "most",
    "other", "some", "such", "no", "nor", "not", "only", "own", "same",
    "so", "than", "too", "very", "just", "because", "as", "until", "while",
    "is", "are", "was", "were", "be", "been", "being", "have", "has", "had",
    "do", "does", "did", "will", "would", "shall", "should", "may", "might",
    "must", "can", "could",
}

TRANSITION_WORDS_EN = {
    "however", "therefore", "because", "although", "specifically",
    "for example", "for instance", "in contrast", "similarly", "consequently",
    "notably", "meanwhile", "furthermore", "moreover", "additionally",
    "nevertheless", "nonetheless", "otherwise", "instead", "accordingly",
    "hence", "thus", "in addition", "on the other hand", "as a result",
    "in particular", "in conclusion", "to summarize", "first", "second",
    "third", "finally", "next", "then", "also", "besides", "indeed",
    "in fact", "of course", "certainly", "surely", "undoubtedly",
    "regardless", "despite", "even though", "while", "whereas",
}

PASSIVE_PATTERNS_EN = [
    re.compile(r"\b(?:am|is|are|was|were|be|been|being)\s+(?:\w+ly\s+)?(?:\w+ed|built|done|made|found|known|seen|taken|given|said|set|shown|told|written)\b", re.IGNORECASE),
    re.compile(r"\b(?:has|have|had|will have)\s+been\s+\w+(?:ed|d|t|en)\b", re.IGNORECASE),
    re.compile(r"\b(?:is|are|was|were|be)\s+(?:being|getting)\s+\w+(?:ed|d|t|en)\b", re.IGNORECASE),
]

POWER_WORDS_EN = {
    "proven", "secret", "stop", "simple", "exclusive", "limited", "hidden",
    "surprising", "shocking", "unexpected", "amazing", "incredible", "ultimate",
    "essential", "critical", "guaranteed", "instant", "immediate", "automatic",
    "effortless", "breakthrough", "insider", "behind the scenes", "revealed",
    "mistake", "warning", "never", "avoid", "dangerous", "risk", "urgent",
    "little-known", "unknown", "unconventional", "tested", "research-backed",
    "data-driven", "expert", "science-based", "actual", "real", "exact",
    "specific", "step-by-step", "definitive", "powerful", "effective",
}

# ── Data structures ────────────────────────────────────────────────────────

@dataclass
class SentenceInfo:
    text: str
    word_count: int
    first_word: str
    has_transition: bool
    is_passive: bool


@dataclass
class ParagraphInfo:
    sentence_count: int
    word_count: int
    text: str


@dataclass
class TextMetrics:
    lang: str
    word_count: int
    sentence_count: int
    char_count: int
    char_count_no_spaces: int
    avg_sentence_length: float
    avg_syllables_per_word: float
    avg_words_per_sentence: float

    # Readability
    flesch_reading_ease: float
    flesch_kincaid_grade: float
    gunning_fog: float
    smog_index: float
    automated_readability_index: float
    coleman_liau_index: float
    aggregate_grade: str

    # Passive voice
    passive_sentence_count: int
    passive_ratio_pct: float

    # Transition words
    transition_sentence_count: int
    transition_ratio_pct: float

    # Sentence variety
    sentences: list[SentenceInfo] = field(default_factory=list)
    monotony_violations: int = 0
    starter_violations: int = 0

    # Paragraphs
    paragraphs: list[ParagraphInfo] = field(default_factory=list)
    paragraphs_too_long: int = 0
    avg_words_per_paragraph: float = 0.0

    # Keyword
    keyword: str = ""
    keyword_occurrences: int = 0
    keyword_density_pct: float = 0.0
    keyword_in_first_150: bool = False
    keyword_in_title: bool = False

    # Title / Meta
    title_text: str = ""
    title_char_count: int = 0
    title_has_number: bool = False
    title_power_word_count: int = 0
    meta_description: str = ""
    meta_description_char_count: int = 0


# ── Tokenization ───────────────────────────────────────────────────────────

def _split_sentences(text: str) -> list[str]:
    """Simple sentence splitter — handles ., !, ? terminators. Falls back to textstat."""
    result = []
    current: list[str] = []
    for ch in text:
        current.append(ch)
        if ch in ".!?":
            result.append("".join(current).strip())
            current = []
    if current:
        remaining = "".join(current).strip()
        if remaining:
            result.append(remaining)
    return result or [text]


def _tokenize_words(text: str) -> list[str]:
    return re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿ0-9]+", text.lower())


def _first_word(sentence: str) -> str:
    words = _tokenize_words(sentence)
    return words[0] if words else ""


# ── Core analysis ──────────────────────────────────────────────────────────

def analyze(
    text: str,
    keyword: str = "",
    title: str = "",
    meta_description: str = "",
    lang: str = "en",
) -> TextMetrics:
    """
    Compute all measurable SEO metrics for a text.

    Args:
        text: Body content (headings + paragraphs).
        keyword: Focus keyword (case-insensitive matching).
        title: SEO title (H1 or <title>).
        meta_description: Meta description text.
        lang: Language code (currently 'en' only for advanced features).

    Returns:
        TextMetrics dataclass with all computed values.
    """
    # ── Basic counts ───────────────────────────────────────────────────
    word_count = textstat.lexicon_count(text, removepunct=True)
    sentence_count = textstat.sentence_count(text)
    char_count = textstat.char_count(text, ignore_spaces=False)
    char_count_no_spaces = textstat.char_count(text, ignore_spaces=True)
    avg_sentence_length = textstat.avg_sentence_length(text)
    avg_syllables_per_word = textstat.avg_syllables_per_word(text)

    # ── Readability (all EN formulas via textstat) ─────────────────────
    fre = textstat.flesch_reading_ease(text)         # 0–100, higher = easier
    fkg = textstat.flesch_kincaid_grade(text)        # US grade level
    gf = textstat.gunning_fog(text)
    smog = textstat.smog_index(text)
    ari = textstat.automated_readability_index(text)
    cli = textstat.coleman_liau_index(text)
    agg = textstat.text_standard(text, float_output=False)  # e.g. "9th and 10th grade"

    # ── Sentence-level analysis ────────────────────────────────────────
    raw_sentences = _split_sentences(text)
    sentences: list[SentenceInfo] = []
    passive_count = 0
    transition_count = 0

    for s in raw_sentences:
        words = _tokenize_words(s)
        if not words:
            continue
        wc = len(words)
        fw = words[0] if words else ""

        has_transition = False
        for tw in TRANSITION_WORDS_EN:
            if tw in s.lower():
                has_transition = True
                break

        is_passive = False
        for pat in PASSIVE_PATTERNS_EN:
            if pat.search(s):
                is_passive = True
                break

        if is_passive:
            passive_count += 1
        if has_transition:
            transition_count += 1

        sentences.append(SentenceInfo(
            text=s.strip(),
            word_count=wc,
            first_word=fw,
            has_transition=has_transition,
            is_passive=is_passive,
        ))

    total_sent = len(sentences)
    passive_ratio = (passive_count / total_sent * 100) if total_sent else 0.0
    transition_ratio = (transition_count / total_sent * 100) if total_sent else 0.0

    # Sentence monotony: 3+ consecutive sentences within ±2 words
    monotony_violations = 0
    for i in range(len(sentences) - 2):
        a, b, c = sentences[i].word_count, sentences[i + 1].word_count, sentences[i + 2].word_count
        if abs(a - b) <= 2 and abs(b - c) <= 2:
            monotony_violations += 1

    # Starter monotony: 3+ consecutive same first word
    starter_violations = 0
    for i in range(len(sentences) - 2):
        a, b, c = sentences[i].first_word, sentences[i + 1].first_word, sentences[i + 2].first_word
        if a and a == b == c:
            starter_violations += 1

    # ── Paragraph analysis ─────────────────────────────────────────────
    paragraphs_raw = re.split(r"\n\s*\n", text)
    too_long_count = 0
    para_list: list[ParagraphInfo] = []
    total_para_words = 0
    total_para_sentences = 0

    for p in paragraphs_raw:
        p = p.strip()
        if not p:
            continue
        p_words = textstat.lexicon_count(p, removepunct=True)
        p_sents = textstat.sentence_count(p)
        para_list.append(ParagraphInfo(sentence_count=p_sents, word_count=p_words, text=p))
        total_para_words += p_words
        total_para_sentences += p_sents
        if p_words > 150 or p_sents > 3:
            too_long_count += 1

    avg_para_words = total_para_words / len(para_list) if para_list else 0.0

    # ── Keyword analysis ───────────────────────────────────────────────
    kw = keyword.lower().strip()
    kw_occurrences = 0
    kw_in_first_150 = False
    kw_in_title = False

    if kw:
        text_lower = text.lower()
        kw_occurrences = len(re.findall(re.escape(kw), text_lower))
        if kw_occurrences > 0 and word_count > 0:
            kw_density = (kw_occurrences * 100) / word_count
        else:
            kw_density = 0.0

        first_150 = " ".join(text_lower.split()[:150])
        kw_in_first_150 = kw in first_150
        kw_in_title = kw in title.lower() if title else False
    else:
        kw_density = 0.0

    # ── Title / Meta ───────────────────────────────────────────────────
    title_chars = len(title) if title else 0
    title_has_num = bool(re.search(r"\d", title)) if title else False
    title_pw_count = 0
    if title:
        title_lower = title.lower()
        for pw in POWER_WORDS_EN:
            if pw in title_lower:
                title_pw_count += 1

    meta_chars = len(meta_description) if meta_description else 0

    return TextMetrics(
        lang=lang,
        word_count=word_count,
        sentence_count=sentence_count,
        char_count=char_count,
        char_count_no_spaces=char_count_no_spaces,
        avg_sentence_length=avg_sentence_length,
        avg_syllables_per_word=avg_syllables_per_word,
        avg_words_per_sentence=avg_sentence_length,

        flesch_reading_ease=fre,
        flesch_kincaid_grade=fkg,
        gunning_fog=gf,
        smog_index=smog,
        automated_readability_index=ari,
        coleman_liau_index=cli,
        aggregate_grade=agg,

        passive_sentence_count=passive_count,
        passive_ratio_pct=round(passive_ratio, 1),
        transition_sentence_count=transition_count,
        transition_ratio_pct=round(transition_ratio, 1),

        sentences=sentences,
        monotony_violations=monotony_violations,
        starter_violations=starter_violations,

        paragraphs=para_list,
        paragraphs_too_long=too_long_count,
        avg_words_per_paragraph=round(avg_para_words, 1),

        keyword=keyword,
        keyword_occurrences=kw_occurrences,
        keyword_density_pct=round(kw_density, 2),
        keyword_in_first_150=kw_in_first_150,
        keyword_in_title=kw_in_title,

        title_text=title,
        title_char_count=title_chars,
        title_has_number=title_has_num,
        title_power_word_count=title_pw_count,
        meta_description=meta_description,
        meta_description_char_count=meta_chars,
    )


# ── Checklist mapping ──────────────────────────────────────────────────────
# Maps metrics to the 49-factor scorecard, returning factor ID → {status, detail}

def score_checklist(m: TextMetrics) -> dict:
    """
    Map computed metrics to RankWise 49-factor checklist.
    Only scores factors that are reliably computable without web access.
    Returns dict of factor_id → {status: pass/fail/warning/na, detail: str, value: str}.
    """
    result = {}

    # ── K: Keyword Placement ────────────────────────────────────────────
    if m.keyword:
        result["K1"] = {"status": "pass", "detail": f"Keyword set: '{m.keyword}'", "value": m.keyword}
    else:
        result["K1"] = {"status": "fail", "detail": "No focus keyword provided", "value": ""}

    result["K2"] = {"status": "pass" if m.keyword_in_title else "fail",
                    "detail": "Keyword in title" if m.keyword_in_title else "Keyword missing from title",
                    "value": "yes" if m.keyword_in_title else "no"}

    result["K6"] = {"status": "pass" if m.keyword_in_first_150 else "fail",
                    "detail": "Keyword in first 150 words" if m.keyword_in_first_150 else "Keyword not in first 150",
                    "value": "yes" if m.keyword_in_first_150 else "no"}

    if m.keyword_occurrences > 0:
        result["K7"] = {"status": "pass", "detail": f"Keyword in body ({m.keyword_occurrences} occurrences)",
                        "value": str(m.keyword_occurrences)}
    else:
        result["K7"] = {"status": "fail", "detail": "Keyword not found in body", "value": "0"}

    density = m.keyword_density_pct
    if density == 0:
        result["K10"] = {"status": "fail", "detail": "Keyword density: 0%", "value": "0%"}
    elif density < 0.8:
        result["K10"] = {"status": "warning", "detail": f"Keyword density too low: {density:.2f}% (target 0.8–1.5%)",
                         "value": f"{density:.2f}%"}
    elif 0.8 <= density <= 1.5:
        result["K10"] = {"status": "pass", "detail": f"Keyword density: {density:.2f}% (target 0.8–1.5%)",
                         "value": f"{density:.2f}%"}
    elif density <= 3.0:
        result["K10"] = {"status": "warning", "detail": f"Keyword density elevated: {density:.2f}% (target 0.8–1.5%, >3% = stuffing)",
                         "value": f"{density:.2f}%"}
    else:
        result["K10"] = {"status": "fail", "detail": f"Keyword stuffing: {density:.2f}% (target 0.8–1.5%)",
                         "value": f"{density:.2f}%"}

    # ── C: Content Quality ─────────────────────────────────────────────
    if m.word_count >= 1500:
        result["C1"] = {"status": "pass", "detail": f"Word count: {m.word_count} (competitive)", "value": str(m.word_count)}
    elif m.word_count >= 600:
        result["C1"] = {"status": "pass", "detail": f"Word count: {m.word_count} (meets minimum)", "value": str(m.word_count)}
    else:
        result["C1"] = {"status": "fail", "detail": f"Word count too low: {m.word_count} (min 600)", "value": str(m.word_count)}

    result["C2"] = {"status": "fail" if m.paragraphs_too_long > 0 else "pass",
                    "detail": f"Paragraphs too long: {m.paragraphs_too_long} of {len(m.paragraphs)}" if m.paragraphs_too_long > 0 else "All paragraphs within limits",
                    "value": f"{m.paragraphs_too_long}/{len(m.paragraphs)}"}

    result["C5"] = {"status": "pass" if m.title_has_number else "fail",
                    "detail": "Number in title" if m.title_has_number else "No number in title",
                    "value": "yes" if m.title_has_number else "no"}

    result["C6"] = {"status": "pass" if m.title_power_word_count >= 2 else "warning",
                    "detail": f"Power words in title: {m.title_power_word_count} (target ≥2)" if m.title_power_word_count < 2 else f"Power words in title: {m.title_power_word_count}",
                    "value": str(m.title_power_word_count)}

    # Readability (C8)
    fkg_rounded = round(m.flesch_kincaid_grade, 1)
    if m.flesch_kincaid_grade <= 0:
        result["C8"] = {"status": "warning", "detail": f"Readability: Grade {fkg_rounded} (unusually low)", "value": f"FK Grade {fkg_rounded}"}
    elif m.flesch_kincaid_grade <= 9:
        result["C8"] = {"status": "pass", "detail": f"Readability: Grade {fkg_rounded} (target 7–9)", "value": f"FK Grade {fkg_rounded}"}
    elif m.flesch_kincaid_grade <= 12:
        result["C8"] = {"status": "warning", "detail": f"Readability: Grade {fkg_rounded} (high)", "value": f"FK Grade {fkg_rounded}"}
    else:
        result["C8"] = {"status": "fail", "detail": f"Readability too high: Grade {fkg_rounded} (target 7–9)", "value": f"FK Grade {fkg_rounded}"}

    # Passive voice (C9)
    if m.passive_ratio_pct <= 10:
        result["C9"] = {"status": "pass", "detail": f"Passive voice: {m.passive_ratio_pct}% (target ≤10%)", "value": f"{m.passive_ratio_pct}%"}
    else:
        result["C9"] = {"status": "fail", "detail": f"Passive voice too high: {m.passive_ratio_pct}% (target ≤10%)", "value": f"{m.passive_ratio_pct}%"}

    # Transition words (C10)
    target_tw = 30 if m.lang in ("en",) else 25
    if m.transition_ratio_pct >= target_tw:
        result["C10"] = {"status": "pass", "detail": f"Transition words: {m.transition_ratio_pct}% (target ≥{target_tw}%)", "value": f"{m.transition_ratio_pct}%"}
    else:
        result["C10"] = {"status": "fail", "detail": f"Transition words too low: {m.transition_ratio_pct}% (target ≥{target_tw}%)", "value": f"{m.transition_ratio_pct}%"}

    # Sentence variety (C11)
    if m.monotony_violations == 0:
        result["C11"] = {"status": "pass", "detail": "Sentence length variety: OK", "value": "no violations"}
    else:
        result["C11"] = {"status": "fail", "detail": f"Sentence length monotony: {m.monotony_violations} violation(s)", "value": f"{m.monotony_violations}"}

    # Consecutive sentence starts (C12)
    if m.starter_violations == 0:
        result["C12"] = {"status": "pass", "detail": "Sentence starts varied: OK", "value": "no violations"}
    else:
        result["C12"] = {"status": "fail", "detail": f"Repeated sentence starts: {m.starter_violations} violation(s)", "value": f"{m.starter_violations}"}

    # ── T: Title / Meta length ─────────────────────────────────────────
    if m.title_char_count == 0:
        result["T3"] = {"status": "fail", "detail": "No title provided", "value": "0 chars"}
    elif 50 <= m.title_char_count <= 60:
        result["T3"] = {"status": "pass", "detail": f"Title length: {m.title_char_count} chars (target 50–60)", "value": f"{m.title_char_count} chars"}
    else:
        result["T3"] = {"status": "warning", "detail": f"Title length off: {m.title_char_count} chars (target 50–60)", "value": f"{m.title_char_count} chars"}

    if m.meta_description_char_count == 0:
        result["T4"] = {"status": "fail", "detail": "No meta description provided", "value": "0 chars"}
    elif 145 <= m.meta_description_char_count <= 158:
        result["T4"] = {"status": "pass", "detail": f"Meta description length: {m.meta_description_char_count} chars", "value": f"{m.meta_description_char_count} chars"}
    else:
        result["T4"] = {"status": "warning", "detail": f"Meta description length off: {m.meta_description_char_count} chars (target 145–158)", "value": f"{m.meta_description_char_count} chars"}

    return result


# ── Report generator ───────────────────────────────────────────────────────

def report(m: TextMetrics) -> str:
    """Generate a human-readable report from metrics."""
    lines = [
        "=" * 60,
        "  RankWise Validator — Text Metrics Report",
        "=" * 60,
        "",
        f"  Language:            {m.lang}",
        f"  Keyword:             {m.keyword or '(not set)'}",
        "",
        "── COUNTS ──",
        f"  Words:               {m.word_count}",
        f"  Sentences:           {m.sentence_count}",
        f"  Characters:          {m.char_count} ({m.char_count_no_spaces} no spaces)",
        f"  Avg sentence length: {m.avg_sentence_length:.1f} words",
        f"  Avg syllables/word:  {m.avg_syllables_per_word:.2f}",
        "",
        "── READABILITY ──",
        f"  Flesch Reading Ease: {m.flesch_reading_ease:.1f} (60–70 = standard)",
        f"  Flesch-Kincaid Grade:{m.flesch_kincaid_grade:.1f} (target 7–9)",
        f"  Gunning Fog:         {m.gunning_fog:.1f}",
        f"  SMOG Index:          {m.smog_index:.1f}",
        f"  ARI:                 {m.automated_readability_index:.1f}",
        f"  Coleman-Liau:        {m.coleman_liau_index:.1f}",
        f"  Aggregate:           {m.aggregate_grade}",
        "",
        "── LINGUISTIC ──",
        f"  Passive voice:       {m.passive_ratio_pct}% ({m.passive_sentence_count}/{m.sentence_count} sentences, target ≤10%)",
        f"  Transition words:    {m.transition_ratio_pct}% ({m.transition_sentence_count}/{m.sentence_count} sentences, target ≥30%)",
        f"  Length monotony:     {m.monotony_violations} violation(s)",
        f"  Starter monotony:    {m.starter_violations} violation(s)",
        "",
        "── PARAGRAPHS ──",
        f"  Total paragraphs:    {len(m.paragraphs)}",
        f"  Too long (>150w/>3s):{m.paragraphs_too_long}",
        f"  Avg words/paragraph: {m.avg_words_per_paragraph:.1f}",
        "",
        "── KEYWORD ──",
        f"  Occurrences:         {m.keyword_occurrences}",
        f"  Density:             {m.keyword_density_pct}% (target 0.8–1.5%)",
        f"  In first 150 words:  {'yes' if m.keyword_in_first_150 else 'NO'}",
        f"  In title:            {'yes' if m.keyword_in_title else 'NO'}",
        "",
        "── TITLE / META ──",
        f"  Title:               \"{m.title_text}\"",
        f"  Title length:        {m.title_char_count} chars (target 50–60)",
        f"  Title has number:    {'yes' if m.title_has_number else 'NO'}",
        f"  Title power words:   {m.title_power_word_count} (target ≥2)",
        f"  Meta description:    {m.meta_description_char_count} chars (target 145–158)",
        "",
        "── CHECKLIST SCORING ──",
    ]

    scores = score_checklist(m)
    for fid, info in sorted(scores.items()):
        icon = {"pass": "[PASS]", "fail": "[FAIL]", "warning": "[WARN]", "na": "[N/A]"}.get(info["status"], "[???]")
        lines.append(f"  {icon} {fid}: {info['detail']}")

    return "\n".join(lines)
