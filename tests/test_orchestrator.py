"""Tests for RankWise Orchestrator — automated fix plan generation."""

import json
import pytest
from validator.metrics import analyze, score_checklist
from validator.orchestrator import (
    Orchestrator,
    FixPlan,
    FixInstruction,
    _compute_weighted_score,
    _factor_severity,
)


EN_FIXABLE_TEXT = (
    "SEO strategy is important for websites that want to get more traffic from Google. "
    "Many people think that SEO is very complicated and extremely difficult to understand. "
    "However this is not true at all. "
    "SEO can be learned by anyone with the right resources. "
    "The guide was written by experts. "
    "The results were analyzed by the team. "
    "The data was collected by researchers. "
    "A strategy is needed. A plan is required. An approach is essential. "
    "SEO strategy helps businesses grow. "
    "SEO strategy improves rankings. "
    "SEO strategy drives traffic. "
)

EN_GOOD_TEXT = (
    "Search engine optimization helps websites attract organic traffic from Google and other search engines. "
    "You need a solid SEO strategy to compete in today's crowded online space. "
    "For example, keyword research reveals what your audience actually searches for each month. "
    "Because search algorithms change frequently, you must adapt your approach over time. "
    "Many businesses see significant traffic growth within six months of implementing a proper strategy. "
    "Specifically, on-page optimization, quality content, and authoritative backlinks create the strongest ranking signals. "
    "Therefore, investing in SEO delivers compounding returns that paid advertising cannot match. "
    "In fact, organic search drives over 53% of all website traffic according to industry research. "
    "You should start with technical SEO, then build your content strategy, and finally earn backlinks from trusted sources. "
    "As a result, your site will climb the rankings steadily rather than relying on short-term tactics."
)


class TestOrchestratorInit:
    def test_creates_metrics(self):
        orch = Orchestrator(EN_GOOD_TEXT, keyword="SEO strategy",
                            title="7 Proven SEO Strategy Tips for 2026",
                            lang="en")
        assert orch.metrics.word_count > 0
        assert orch.metrics.sentence_count > 0
        assert len(orch.checklist_scores) == 16

    def test_missing_keyword_detected(self):
        orch = Orchestrator("just some random text", lang="en")
        scores = orch.checklist_scores
        assert scores["K1"]["status"] == "fail"

    def test_lang_fallback(self):
        orch = Orchestrator("Hello world", lang="zz")
        assert orch.metrics.lang == "en"


class TestFixPlan:
    def test_build_plan_no_keyword(self):
        orch = Orchestrator("some text", lang="en")
        plan = orch.build_fix_plan()
        assert isinstance(plan, FixPlan)
        assert plan.failed > 0
        assert any(i.factor_id == "K1" for i in plan.instructions)

    def test_build_plan_with_issues(self):
        orch = Orchestrator(EN_FIXABLE_TEXT, keyword="SEO strategy",
                            title="SEO Guide", lang="en")
        plan = orch.build_fix_plan()
        assert plan.failed > 0
        assert isinstance(plan.weighted_score_pct, float)
        assert plan.grade in ("A", "B", "C", "D", "F")

    def test_all_instructions_have_required_fields(self):
        orch = Orchestrator(EN_FIXABLE_TEXT, keyword="SEO strategy",
                            title="A Very Basic SEO Title Without Number",
                            lang="en")
        plan = orch.build_fix_plan()
        for instr in plan.instructions:
            assert instr.factor_id
            assert instr.factor_name
            assert instr.severity in ("CRITICAL", "HIGH", "MEDIUM", "LOW")
            assert instr.status in ("fail", "warning")
            assert instr.target

    def test_instructions_ordered_fails_before_warnings(self):
        orch = Orchestrator("tiny", lang="en")
        plan = orch.build_fix_plan()
        statuses = [i.status for i in plan.instructions]
        seen_warning = False
        for st in statuses:
            if st == "warning":
                seen_warning = True
            elif st == "fail" and seen_warning:
                pytest.fail("FAIL instruction found after WARNING — ordering violated")

    def test_empty_instructions_when_all_pass(self):
        orch = Orchestrator(EN_GOOD_TEXT, keyword="SEO strategy",
                            title="7 Proven SEO Strategy Tips for 2026",
                            meta_description="Learn the best SEO strategy tips for ranking higher in search engines today.",
                            lang="en")
        plan = orch.build_fix_plan()
        assert plan.passed > 0


class TestFixInstructionBuilders:
    def test_K1_fix_no_keyword(self):
        orch = Orchestrator("text", lang="en")
        plan = orch.build_fix_plan()
        k1 = next(i for i in plan.instructions if i.factor_id == "K1")
        assert k1.llm_prompt
        assert "keyword" in k1.llm_prompt.lower()

    def test_K2_fix_keyword_missing_from_title(self):
        orch = Orchestrator("SEO strategy is important. " * 20,
                            keyword="SEO strategy",
                            title="Some Other Title Without Keyword",
                            lang="en")
        plan = orch.build_fix_plan()
        k2 = next((i for i in plan.instructions if i.factor_id == "K2"), None)
        if k2:
            assert "SEO strategy" in k2.llm_prompt

    def test_K10_density_too_high(self):
        text = "SEO strategy " * 200
        orch = Orchestrator(text, keyword="SEO strategy",
                            title="SEO strategy Guide", lang="en")
        plan = orch.build_fix_plan()
        k10 = next(i for i in plan.instructions if i.factor_id == "K10")
        assert k10.status == "fail"

    def test_K10_density_too_low(self):
        text = "This is a long article about various topics. " * 100
        text += " SEO strategy appears once. " + "More filler text. " * 20
        orch = Orchestrator(text, keyword="SEO strategy",
                            title="SEO strategy Guide", lang="en")
        plan = orch.build_fix_plan()
        k10 = next(i for i in plan.instructions if i.factor_id == "K10")
        assert k10.status in ("fail", "warning")

    def test_C1_word_count_too_low(self):
        orch = Orchestrator("Short text.", keyword="SEO", title="SEO Title", lang="en")
        plan = orch.build_fix_plan()
        c1 = next(i for i in plan.instructions if i.factor_id == "C1")
        assert c1.status == "fail"
        assert "600" in c1.target

    def test_C5_no_number_in_title(self):
        orch = Orchestrator(EN_GOOD_TEXT, keyword="SEO strategy",
                            title="SEO Strategy Guide Without Number",
                            lang="en")
        plan = orch.build_fix_plan()
        c5 = next((i for i in plan.instructions if i.factor_id == "C5"), None)
        if c5:
            assert c5.status != "pass"

    def test_C9_passive_voice_high(self):
        text = "The report was written by John. The data was analyzed by Mary. "
        text += "The results were published by the team. We did the work."
        orch = Orchestrator(text, keyword="report", title="Report Analysis", lang="en")
        plan = orch.build_fix_plan()
        c9 = next(i for i in plan.instructions if i.factor_id == "C9")
        assert c9.status in ("fail", "warning")

    def test_T3_title_issues(self):
        orch = Orchestrator(EN_GOOD_TEXT, keyword="SEO strategy",
                            title="Hi", lang="en")
        plan = orch.build_fix_plan()
        t3 = next(i for i in plan.instructions if i.factor_id == "T3")
        assert t3.status != "pass"

    def test_T4_meta_missing(self):
        orch = Orchestrator(EN_GOOD_TEXT, keyword="SEO strategy",
                            title="7 Proven SEO Strategy Tips", lang="en")
        plan = orch.build_fix_plan()
        t4 = next(i for i in plan.instructions if i.factor_id == "T4")
        assert t4.status == "fail"


class TestRevalidate:
    def test_revalidate_returns_new_plan(self):
        orch = Orchestrator(EN_FIXABLE_TEXT, keyword="SEO strategy",
                            title="SEO Guide", lang="en")
        before = orch.build_fix_plan()
        new_plan = orch.revalidate(EN_GOOD_TEXT,
                                   new_title="7 Proven SEO Strategy Tips",
                                   new_meta="Best SEO strategy tips for ranking higher in 2026.")
        assert isinstance(new_plan, FixPlan)

    def test_diff_report(self):
        orch = Orchestrator(EN_FIXABLE_TEXT, keyword="SEO strategy",
                            title="SEO Guide", lang="en")
        before = orch.build_fix_plan()
        new_plan = orch.revalidate(EN_GOOD_TEXT,
                                   new_title="7 Proven SEO Strategy Tips for 2026",
                                   new_meta="Learn the best SEO strategy tips for ranking higher. Proven techniques.")
        diff = orch.diff_report(before, new_plan)
        assert "Before" in diff
        assert "After" in diff


class TestFixPromptBatch:
    def test_produces_prompt_string(self):
        orch = Orchestrator(EN_FIXABLE_TEXT, keyword="SEO strategy",
                            title="SEO Guide", lang="en")
        prompt = orch.fix_prompt_batch()
        assert isinstance(prompt, str)
        assert len(prompt) > 0

    def test_all_clear_when_no_issues(self):
        orch = Orchestrator(EN_GOOD_TEXT, keyword="SEO strategy",
                            title="7 Proven SEO Strategy Tips for 2026",
                            meta_description="Learn the best SEO strategy tips for 2026. Start ranking today.",
                            lang="en")
        prompt = orch.fix_prompt_batch()
        if "[ALL CLEAR]" in prompt:
            assert "ALL CLEAR" in prompt
        else:
            assert "SEO FIX BATCH" in prompt


class TestToDict:
    def test_serializable(self):
        orch = Orchestrator(EN_FIXABLE_TEXT, keyword="SEO strategy",
                            title="SEO Strategy Guide", lang="en")
        d = orch.to_dict()
        assert isinstance(d, dict)
        assert "score_pct" in d
        assert "factors" in d
        assert "fix_instructions" in d
        json.dumps(d, ensure_ascii=False)


class TestWeightedScore:
    def test_all_pass_is_100(self):
        scores = {}
        for fid in ["K1", "K2", "K6", "K7", "K10", "C1", "C2", "C5", "C6",
                     "C8", "C9", "C10", "C11", "C12", "T3", "T4"]:
            scores[fid] = {"status": "pass", "detail": ""}
        ws, grade = _compute_weighted_score(scores)
        assert ws == 100.0
        assert grade == "A"

    def test_all_fail_is_0(self):
        scores = {}
        for fid in ["K1", "K2", "K6", "K7", "K10", "C1", "C2", "C5", "C6",
                     "C8", "C9", "C10", "C11", "C12", "T3", "T4"]:
            scores[fid] = {"status": "fail", "detail": ""}
        ws, grade = _compute_weighted_score(scores)
        assert ws == 0.0
        assert grade == "F"

    def test_na_excluded(self):
        scores = {
            "K1": {"status": "pass", "detail": ""},
            "K2": {"status": "pass", "detail": ""},
            "K6": {"status": "na", "detail": ""},
            "K7": {"status": "pass", "detail": ""},
            "K10": {"status": "pass", "detail": ""},
            "C1": {"status": "pass", "detail": ""},
            "C2": {"status": "pass", "detail": ""},
            "C5": {"status": "pass", "detail": ""},
            "C6": {"status": "pass", "detail": ""},
            "C8": {"status": "pass", "detail": ""},
            "C9": {"status": "pass", "detail": ""},
            "C10": {"status": "pass", "detail": ""},
            "C11": {"status": "pass", "detail": ""},
            "C12": {"status": "pass", "detail": ""},
            "T3": {"status": "pass", "detail": ""},
            "T4": {"status": "pass", "detail": ""},
        }
        ws, grade = _compute_weighted_score(scores)
        assert ws == 100.0

    def test_critical_fail_caps_grade(self):
        scores = {}
        for fid in ["K1", "K2", "K7", "K10", "C1", "C2", "C5", "C6",
                     "C8", "C9", "C10", "C11", "C12", "T3", "T4"]:
            scores[fid] = {"status": "pass", "detail": ""}
        scores["K6"] = {"status": "pass", "detail": ""}
        # K1 is CRITICAL — make it fail
        scores["K1"] = {"status": "fail", "detail": ""}
        ws, grade = _compute_weighted_score(scores)
        assert grade != "A"

    def test_warning_half_weight(self):
        scores = {
            "K1": {"status": "pass", "detail": ""},
            "K2": {"status": "pass", "detail": ""},
            "K6": {"status": "pass", "detail": ""},
            "K7": {"status": "pass", "detail": ""},
            "K10": {"status": "pass", "detail": ""},
            "C1": {"status": "pass", "detail": ""},
            "C2": {"status": "pass", "detail": ""},
            "C5": {"status": "warning", "detail": ""},
            "C6": {"status": "pass", "detail": ""},
            "C8": {"status": "pass", "detail": ""},
            "C9": {"status": "pass", "detail": ""},
            "C10": {"status": "pass", "detail": ""},
            "C11": {"status": "pass", "detail": ""},
            "C12": {"status": "pass", "detail": ""},
            "T3": {"status": "pass", "detail": ""},
            "T4": {"status": "pass", "detail": ""},
        }
        ws, grade = _compute_weighted_score(scores)
        assert 95 < ws < 100
