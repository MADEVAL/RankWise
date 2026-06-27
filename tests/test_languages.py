"""Multi-language readability and metric tests for all 9 RankWise languages."""

import pytest
from validator.metrics import (
    analyze,
    score_checklist,
    READABILITY_LANGS,
    READSIGHT_LANG_MAP,
)

# Languages that carry a Flesch model in ReadSightPy (UK and PL do not)
LANGS_WITH_FLESCH = {"en", "ru", "de", "fr", "es", "pt", "it"}


class TestReadabilityLanguageSupport:
    """Verify ReadSightPy readability support across RankWise languages."""

    def test_supported_langs_have_scores(self, multilingual):
        for lang in READABILITY_LANGS:
            text = multilingual[lang]
            m = analyze(text, lang=lang)
            assert m.readability_supported, f"Expected readability_supported=True for {lang}"
            assert m.lang_specific_score >= 0, f"Expected valid lang_score for {lang}"

    def test_flesch_langs_have_fre(self, multilingual):
        for lang in LANGS_WITH_FLESCH:
            text = multilingual[lang]
            m = analyze(text, lang=lang)
            assert m.flesch_reading_ease >= 0, f"Expected valid FRE for {lang}, got {m.flesch_reading_ease}"

    def test_all_languages_supported(self, multilingual):
        # ReadSightPy covers every RankWise language — no LLM fallback needed.
        unsupported = set(multilingual.keys()) - READABILITY_LANGS
        assert unsupported == set(), f"Unexpected unsupported langs: {unsupported}"
        for lang in multilingual:
            m = analyze(multilingual[lang], lang=lang)
            assert m.readability_supported
            assert score_checklist(m)["C8"]["status"] != "na"

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

    def test_uk_readability_lix(self):
        # UK has no Flesch model in ReadSightPy → C8 scored via LIX (now computable, not N/A).
        text = "Ігри завжди вважалися важливими для розвитку дітей. Однак дорослі також отримують користь від ігор. Це доведений факт."
        m = analyze(text, lang="uk")
        scores = score_checklist(m)
        assert scores["C8"]["status"] != "na"
        assert "LIX" in scores["C8"]["value"]

    def test_pt_readability_fre(self):
        # PT now has a deterministic Flesch model (Martins) → C8 is no longer N/A.
        text = "Jogar sempre foi considerado importante para o desenvolvimento das crianças. No entanto, os adultos também se beneficiam muito. É um fato comprovado."
        m = analyze(text, lang="pt")
        scores = score_checklist(m)
        assert scores["C8"]["status"] != "na"
        assert "FRE" in scores["C8"]["value"]

    def test_pl_readability_fogpl(self):
        # PL uses FOG-PL (no Flesch model) → C8 computable, not N/A.
        text = "Granie zawsze było uważane za ważne dla rozwoju dzieci. Jednak dorośli również czerpią korzyści. To sprawdzony fakt."
        m = analyze(text, lang="pl")
        scores = score_checklist(m)
        assert scores["C8"]["status"] != "na"
        assert "FOG-PL" in scores["C8"]["value"]
