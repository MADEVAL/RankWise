"""Keyword matching regression tests: word boundaries, plurals, hyphens."""

from validator.metrics import analyze, score_checklist


class TestKeywordMatching:
    def test_substring_is_not_a_match(self):
        m = analyze("We visited SEOUL last year. The city is loud.", keyword="SEO", title="SEO guide")
        assert m.keyword_occurrences == 0

    def test_plural_matches(self):
        m = analyze(
            "Content marketing strategies work when the plan is clear.",
            keyword="content marketing strategy",
            title="Content Marketing Strategies",
        )
        assert m.keyword_occurrences == 1
        assert m.keyword_in_title
        assert score_checklist(m)["K2"]["status"] == "pass"

    def test_hyphen_is_normalized(self):
        m = analyze(
            "Content-marketing works when the plan is clear.",
            keyword="content marketing",
            title="Content marketing",
        )
        assert m.keyword_occurrences == 1

    def test_word_boundary(self):
        m = analyze("The art of starting is hard. Start small.", keyword="art", title="Art guide")
        assert m.keyword_occurrences == 1

    def test_existing_exact_phrase_count_is_stable(self):
        text = (
            "SEO strategy is important. Every SEO strategy needs planning. "
            "Your SEO strategy defines success."
        )
        m = analyze(text, keyword="SEO strategy", title="The Ultimate SEO strategy Guide")
        assert m.keyword_occurrences == 3
        assert m.keyword_in_title

    def test_phrase_in_first_150_still_works(self):
        prefix = "x " * 50
        text = prefix + "SEO strategy is the focus here." + " more text. " * 20
        assert analyze(text, keyword="SEO strategy").keyword_in_first_150

    def test_phrase_after_first_150_still_fails(self):
        prefix = "x " * 160
        text = prefix + "SEO strategy comes too late."
        assert not analyze(text, keyword="SEO strategy").keyword_in_first_150
