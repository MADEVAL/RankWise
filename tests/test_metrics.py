"""Unit tests for RankWise Validator — metrics.py."""

import re
import pytest
from validator.metrics import (
    analyze,
    score_checklist,
    report,
    TextMetrics,
    _split_sentences,
    _tokenize_words,
    READABILITY_LANGS,
)


class TestSentenceSplitting:
    """Sentence boundary detection with abbreviation handling."""

    def test_simple_sentences(self):
        text = "Hello world. This is a test. Goodbye!"
        sents = _split_sentences(text)
        assert len(sents) == 3

    def test_abbreviation_not_split(self):
        text = "Dr. Smith wrote the report. He sent it to Mr. Jones."
        sents = _split_sentences(text)
        assert len(sents) == 2
        assert sents[0].startswith("Dr. Smith")

    def test_multiple_abbreviations(self):
        text = "Mr. and Mrs. Johnson met Prof. Davis at approx. 3 PM. They discussed the results."
        sents = _split_sentences(text)
        assert len(sents) == 2
        assert "Mr." in sents[0]

    def test_etc_not_split(self):
        text = "We need apples, oranges, etc. They are all in the basket."
        sents = _split_sentences(text)
        # "etc." followed by uppercase = sentence boundary → 2 sentences
        assert len(sents) == 2
        assert "etc." in sents[0]

    def test_i_e_not_split(self):
        text = "The strategy, i.e. content marketing, works well. Many companies use it."
        sents = _split_sentences(text)
        assert len(sents) == 2

    def test_empty_text(self):
        assert _split_sentences("") == []

    def test_no_sentence_end(self):
        text = "This is a fragment without proper ending"
        sents = _split_sentences(text)
        assert len(sents) == 1
        assert text in sents[0]


class TestWordTokenization:
    """Word tokenization across languages."""

    def test_english(self):
        words = _tokenize_words("Hello world! This is a test.", "en")
        assert "hello" in words
        assert "world" in words

    def test_russian(self):
        words = _tokenize_words("Привет мир. Это тест.", "ru")
        assert "привет" in words
        assert "мир" in words

    def test_german_umlauts(self):
        words = _tokenize_words("Grüße aus München. Äpfel sind lecker.", "de")
        assert "grüße" in words
        assert "münchen" in words

    def test_spanish_accents(self):
        words = _tokenize_words("Háblame más sobre el café.", "es")
        assert "háblame" in words
        assert "café" in words

    def test_defaults_to_english(self):
        words = _tokenize_words("Hello world", "zz")
        assert "hello" in words
        assert "world" in words


class TestBasicAnalyze:
    """Core analyze() function — basic metrics."""

    def test_word_count(self, en_text):
        m = analyze(en_text)
        assert m.word_count > 0
        assert isinstance(m.word_count, int)

    def test_sentence_count(self, en_text):
        m = analyze(en_text)
        assert m.sentence_count > 0

    def test_char_count(self, en_text):
        m = analyze(en_text)
        assert m.char_count > m.char_count_no_spaces
        assert m.char_count > 0

    def test_keyword_detection(self):
        text = "SEO strategy is important. Every SEO strategy needs planning. Your SEO strategy defines success."
        m = analyze(text, keyword="SEO strategy", title="The Ultimate SEO strategy Guide")
        assert m.keyword_occurrences == 3
        assert m.keyword_in_title
        assert m.keyword_density_pct > 0

    def test_no_keyword(self):
        m = analyze("Some text without a keyword.")
        assert m.keyword_occurrences == 0
        assert m.keyword_density_pct == 0.0
        assert not m.keyword_in_title

    def test_keyword_in_first_150(self):
        prefix = "x " * 50
        text = prefix + "SEO strategy is the focus here." + " more text. " * 20
        m = analyze(text, keyword="SEO strategy")
        assert m.keyword_in_first_150

    def test_keyword_not_in_first_150(self):
        prefix = "x " * 160
        text = prefix + "SEO strategy comes too late."
        m = analyze(text, keyword="SEO strategy")
        assert not m.keyword_in_first_150

    def test_title_metrics(self):
        title = "7 Proven Ways to Improve Your SEO Strategy"
        m = analyze("content", title=title)
        assert m.title_has_number
        assert m.title_power_word_count >= 1  # "Proven" is a power word
        assert m.title_char_count == len(title)


class TestPassiveVoice:
    """C9: Passive voice detection."""

    def test_passive_detection_en(self):
        text = "The report was written by the team. The results were analyzed by experts. We fixed all bugs."
        m = analyze(text, lang="en")
        # 2 passive sentences out of 3
        assert m.passive_sentence_count >= 2
        assert m.passive_ratio_pct > 30

    def test_no_passive_en(self):
        text = "We wrote the report. The team analyzed the results. We fixed all bugs."
        m = analyze(text, lang="en")
        assert m.passive_sentence_count == 0
        assert m.passive_ratio_pct == 0.0

    def test_passive_de(self):
        text = "Der Bericht wurde vom Team geschrieben. Die Ergebnisse wurden analysiert."
        m = analyze(text, lang="de")
        assert m.passive_sentence_count >= 1


class TestTransitionWords:
    """C10: Transition word detection."""

    def test_transitions_en(self):
        text = "First, we must plan. However, plans can fail. Therefore, we need backups. The end."
        m = analyze(text, lang="en")
        assert m.transition_sentence_count >= 2

    def test_no_transitions(self):
        text = "We plan. Plans fail. We need backups. The end."
        m = analyze(text, lang="en")
        assert m.transition_ratio_pct < 50


class TestSentenceVariety:
    """C11/C12: Sentence variety detection."""

    def test_monotony_detected(self):
        text = "This is short. This is short. This is short. Now this one is quite a bit longer and different."
        m = analyze(text, lang="en")
        assert m.monotony_violations > 0

    def test_no_monotony(self):
        text = "Short. This one is medium length. And this final sentence is quite a bit longer than the previous ones."
        m = analyze(text, lang="en")
        assert m.monotony_violations == 0

    def test_starter_violations(self):
        text = "The cat sat. The cat looked. The cat jumped. Then something different happened."
        m = analyze(text, lang="en")
        assert m.starter_violations > 0


class TestChecklistScoring:
    """score_checklist() validation."""

    def test_all_scored_factors_present(self):
        text = "SEO content. " * 50
        title = "7 Proven SEO Tips for Better Rankings"
        m = analyze(text, keyword="SEO", title=title, meta_description="Learn the best SEO tips for ranking higher in search engines today.")
        scores = score_checklist(m)
        expected_factors = {"K1", "K2", "K6", "K7", "K10", "C1", "C2", "C5", "C6", "C8", "C9", "C10", "C11", "C12", "T3", "T4"}
        assert set(scores.keys()) == expected_factors

    def test_pass_statuses(self):
        text = "SEO strategy. " * 100
        title = "7 Proven SEO Strategy Tips"
        m = analyze(text, keyword="SEO strategy", title=title, meta_description="The best SEO strategy tips for 2026. Learn proven techniques.")
        scores = score_checklist(m)
        assert scores["K1"]["status"] == "pass"
        assert scores["K2"]["status"] == "pass"
        assert scores["K7"]["status"] == "pass"

    def test_fail_statuses(self):
        m = analyze("just text", lang="en")
        scores = score_checklist(m)
        assert scores["K1"]["status"] == "fail"
        assert scores["K7"]["status"] == "fail"

    def test_density_warning(self):
        text = "SEO " * 200
        m = analyze(text, keyword="SEO", title="A Title")
        scores = score_checklist(m)
        assert scores["K10"]["status"] in ("warning", "fail")

    def test_c1_fail_too_short(self):
        m = analyze("tiny", lang="en")
        scores = score_checklist(m)
        assert scores["C1"]["status"] == "fail"


class TestReportGenerator:
    """Report string generation."""

    def test_report_contains_expected_sections(self):
        text = "SEO strategy. " * 50
        title = "7 SEO Strategy Tips"
        m = analyze(text, keyword="SEO strategy", title=title)
        r = report(m)
        assert "RankWise Validator" in r
        assert "LINGUISTIC" in r
        assert "PARAGRAPHS" in r
        assert "KEYWORD" in r
        assert "TITLE / META" in r
        assert "CHECKLIST SCORING" in r

    def test_report_without_meta(self):
        m = analyze("content", keyword="test", title="Title")
        r = report(m)
        assert "Meta description:" in r
