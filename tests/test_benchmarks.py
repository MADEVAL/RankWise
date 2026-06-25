"""Benchmark regression tests — validate scoring consistency against reference texts."""

import pytest
from validator.metrics import analyze, score_checklist
from tests.conftest import load_benchmark


class TestBenchmark01WellOptimized:
    """01-well-optimized.txt: Keyword in body, title mismatch."""

    def test_basic_metrics(self):
        text = load_benchmark("01-well-optimized.txt")
        m = analyze(
            text,
            keyword="content marketing strategy",
            title="7 Proven Content Marketing Strategies That Actually Work in 2026",
            meta_description="Content marketing strategy guide: 7 proven tactics.",
        )
        assert m.word_count > 0
        assert m.sentence_count > 0
        assert m.keyword_occurrences > 0

    def test_checklist_scores(self):
        text = load_benchmark("01-well-optimized.txt")
        m = analyze(
            text,
            keyword="content marketing strategy",
            title="7 Proven Content Marketing Strategies That Actually Work in 2026",
            meta_description="Content marketing strategy guide: 7 proven tactics.",
        )
        scores = score_checklist(m)
        assert scores["K1"]["status"] == "pass"
        assert scores["K7"]["status"] == "pass"  # Keyword in body
        assert scores["C1"]["status"] == "pass"  # >600 words
        assert scores["C5"]["status"] == "pass"  # Number in title


class TestBenchmark02KeywordStuffed:
    """02-keyword-stuffed.txt: 23% keyword density."""

    def test_keyword_stuffing_detected(self):
        text = load_benchmark("02-keyword-stuffed.txt")
        m = analyze(text, keyword="SEO", title="SEO Tips Guide")
        scores = score_checklist(m)
        assert scores["K10"]["status"] == "fail"  # Should detect >3% density
        assert float(scores["K10"]["value"].rstrip("%")) > 3.0

    def test_word_count(self):
        text = load_benchmark("02-keyword-stuffed.txt")
        m = analyze(text, keyword="SEO checklist", title="SEO Checklist Guide")
        assert m.word_count > 0


class TestBenchmark03TooShort:
    """03-too-short.txt: 69 words, no structure."""

    def test_word_count_below_minimum(self):
        text = load_benchmark("03-too-short.txt")
        m = analyze(text, lang="en")
        assert m.word_count < 600

    def test_c1_fails(self):
        text = load_benchmark("03-too-short.txt")
        m = analyze(text, lang="en")
        scores = score_checklist(m)
        assert scores["C1"]["status"] == "fail"


class TestBenchmark04NoMeta:
    """04-no-meta.txt: No title, no meta."""

    def test_no_title_fails(self):
        text = load_benchmark("04-no-meta.txt")
        m = analyze(text, lang="en")
        scores = score_checklist(m)
        assert scores["T3"]["status"] == "fail"  # No title
        assert scores["T4"]["status"] == "fail"  # No meta

    def test_basic_metrics_exist(self):
        text = load_benchmark("04-no-meta.txt")
        m = analyze(text, lang="en")
        assert m.word_count > 0
        assert m.sentence_count > 0


class TestBenchmark05ProductPage:
    """05-product-page.txt: E-commerce product page."""

    def test_keyword_density_in_range(self):
        text = load_benchmark("05-product-page.txt")
        m = analyze(text, keyword="ErgoFlex Pro", title="ErgoFlex Pro Office Chair")
        scores = score_checklist(m)
        assert scores["K10"]["status"] in ("pass", "warning")  # Should not be stuffing

    def test_word_count_decent(self):
        text = load_benchmark("05-product-page.txt")
        m = analyze(text, keyword="ergonomic office chair", title="ErgoFlex Ergonomic Office Chair")
        assert m.word_count >= 300


class TestBenchmarkConsistency:
    """All benchmarks load and analyze without errors."""

    @pytest.mark.parametrize("filename,keyword,title", [
        ("01-well-optimized.txt", "content marketing strategy", "7 Proven Content Marketing Strategies"),
        ("02-keyword-stuffed.txt", "SEO checklist", "SEO Checklist Guide"),
        ("03-too-short.txt", "SEO", "SEO Basics"),
        ("04-no-meta.txt", "SEO", ""),
        ("05-product-page.txt", "ergonomic office chair", "Ergonomic Office Chair"),
    ])
    def test_analyze_no_crash(self, filename, keyword, title):
        text = load_benchmark(filename)
        m = analyze(text, keyword=keyword, title=title)
        scores = score_checklist(m)
        assert len(scores) == 16  # 16 factors always returned


class TestEdgeCases:
    """Edge case handling."""

    def test_empty_text(self):
        m = analyze("", lang="en")
        assert m.word_count == 0
        assert m.sentence_count == 0

    def test_single_word(self):
        m = analyze("Hello", lang="en")
        assert m.word_count == 1

    def test_numbers_only(self):
        m = analyze("123 456 789", lang="en")
        assert m.word_count >= 0

    def test_very_long_text(self):
        long_text = "SEO strategy. " * 1000
        m = analyze(long_text, keyword="SEO strategy", title="7 SEO Strategy Tips")
        assert m.word_count > 0
        assert m.keyword_occurrences > 0

    def test_special_characters(self):
        text = "SEO – strategy: it's important! What about ellipsis… Yes."
        m = analyze(text, keyword="SEO strategy", lang="en")
        assert m.sentence_count > 0

    def test_keyword_with_regex_chars(self):
        text = "SEO+ strategy (special) [brackets] are fine. SEO+ strategy works."
        m = analyze(text, keyword="SEO+ strategy")
        assert m.keyword_occurrences == 2

    def test_lang_fallback(self):
        m = analyze("Hello world", lang="zz")
        assert m.lang == "en"  # Falls back to en
        assert m.word_count > 0


class TestMetricRanges:
    """Sanity checks on metric ranges."""

    def test_density_percentage(self, en_text):
        m = analyze(en_text, keyword="SEO")
        if m.keyword_density_pct > 0:
            assert 0 <= m.keyword_density_pct <= 100

    def test_passive_ratio_range(self, en_text):
        m = analyze(en_text)
        assert 0 <= m.passive_ratio_pct <= 100

    def test_transition_ratio_range(self, en_text):
        m = analyze(en_text)
        assert 0 <= m.transition_ratio_pct <= 100
