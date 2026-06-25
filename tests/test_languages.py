"""Multi-language readability and metric tests for all 9 RankWise languages."""

import pytest
from validator.metrics import (
    analyze,
    score_checklist,
    READABILITY_LANGS,
    TEXTSTAT_LANG_MAP,
)


class TestReadabilityLanguageSupport:
    """Verify textstat readability support across RankWise languages."""

    def test_supported_langs_have_scores(self, multilingual):
        supported = READABILITY_LANGS
        for lang in supported:
            text = multilingual[lang]
            m = analyze(text, lang=lang)
            assert m.readability_supported, f"Expected readability_supported=True for {lang}"
            assert m.flesch_reading_ease >= 0, f"Expected valid FRE for {lang}, got {m.flesch_reading_ease}"
            assert m.lang_specific_score >= 0, f"Expected valid lang_score for {lang}"

    def test_unsupported_langs_na(self, multilingual):
        unsupported = set(multilingual.keys()) - READABILITY_LANGS
        for lang in unsupported:
            text = multilingual[lang]
            m = analyze(text, lang=lang)
            assert not m.readability_supported, f"Expected readability_supported=False for {lang}"
            assert m.flesch_reading_ease < 0, f"Expected negative FRE for {lang}"
            scores = score_checklist(m)
            assert scores["C8"]["status"] == "na", f"Expected C8=na for {lang}"

    def test_lang_specific_formulas_called(self, multilingual):
        for lang in ("es", "de", "it"):
            text = multilingual[lang]
            m = analyze(text, lang=lang)
            assert m.lang_specific_score > 0
            if lang == "es":
                assert "Fernández" in m.lang_specific_name
            elif lang == "de":
                assert "Wiener" in m.lang_specific_name
            elif lang == "it":
                assert "Gulpease" in m.lang_specific_name


class TestAllLanguagesBasicMetrics:
    """Basic word/sentence counts work for all 9 languages."""

    @pytest.mark.parametrize("lang", ["en", "ru", "uk", "de", "fr", "es", "pt", "it", "pl"])
    def test_word_count_positive(self, multilingual, lang):
        text = multilingual[lang]
        m = analyze(text, lang=lang)
        assert m.word_count > 0, f"Word count = 0 for {lang}"
        assert m.sentence_count > 0, f"Sentence count = 0 for {lang}"

    @pytest.mark.parametrize("lang", ["en", "ru", "uk", "de", "fr", "es", "pt", "it", "pl"])
    def test_passive_pattern_loaded(self, multilingual, lang):
        text = multilingual[lang]
        m = analyze(text, lang=lang)
        assert m.passive_ratio_pct >= 0, f"No passive ratio for {lang}"

    @pytest.mark.parametrize("lang", ["en", "ru", "uk", "de", "fr", "es", "pt", "it", "pl"])
    def test_transition_pattern_loaded(self, multilingual, lang):
        text = multilingual[lang]
        m = analyze(text, lang=lang)
        assert m.transition_ratio_pct >= 0, f"No transition ratio for {lang}"

    @pytest.mark.parametrize("lang", ["en", "ru", "uk", "de", "fr", "es", "pt", "it", "pl"])
    def test_power_words_loaded(self, multilingual, lang):
        titles = {
            "en": "7 Proven Secrets",
            "ru": "7 Доказано Секретов",
            "uk": "7 Доведено Секретів",
            "de": "7 Bewährte Geheimnisse",
            "fr": "7 Secrets Prouvés",
            "es": "7 Secretos Probados",
            "pt": "7 Segredos Comprovados",
            "it": "Il Segreto Provato",
            "pl": "7 Sprawdzonych Sekretów",
        }
        title = titles.get(lang, "Title")
        m = analyze(multilingual[lang], lang=lang, title=title)
        assert m.title_power_word_count >= 1, f"No power words detected in {lang} title: '{title}'"


class TestReadabilityScoringPerLanguage:
    """C8 scoring with language-specific targets."""

    def test_en_readability_grade(self):
        text = "SEO strategy is important for websites. Good content ranks better. Simple words help readers understand. Short sentences are clear."
        m = analyze(text, lang="en")
        scores = score_checklist(m)
        assert scores["C8"]["status"] in ("pass", "warning")
        assert "FK Grade" in scores["C8"]["detail"]

    def test_es_readability_formula(self):
        text = "La estrategia de SEO es importante para los sitios web. El buen contenido se posiciona mejor. Las palabras simples ayudan a los lectores."
        m = analyze(text, lang="es")
        scores = score_checklist(m)
        assert scores["C8"]["status"] != "na"
        assert "FH" in scores["C8"]["value"] or "FRE" in scores["C8"]["value"]

    def test_de_readability_formula(self):
        text = "SEO-Strategie ist wichtig für Webseiten. Guter Inhalt wird besser platziert. Einfache Worte helfen den Lesern."
        m = analyze(text, lang="de")
        scores = score_checklist(m)
        assert scores["C8"]["status"] != "na"
        assert "WSTF" in scores["C8"]["value"] or "FRE" in scores["C8"]["value"]

    def test_it_readability_formula(self):
        text = "La strategia SEO è importante per i siti web. I buoni contenuti si posizionano meglio. Le parole semplici aiutano i lettori."
        m = analyze(text, lang="it")
        scores = score_checklist(m)
        assert scores["C8"]["status"] != "na"
        assert "Gulpease" in scores["C8"]["value"] or "FRE" in scores["C8"]["value"]

    def test_uk_pt_no_readability(self):
        for lang in ("uk", "pt"):
            m = analyze("Test content", lang=lang)
            scores = score_checklist(m)
            assert scores["C8"]["status"] == "na", f"C8 should be N/A for {lang}"
