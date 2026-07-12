"""RankWise Validator — CLI entry point.

Usage:
    # Validation
    python -m validator.cli --text "content" --keyword "seo" --title "My Title" [--meta "desc"] [--lang en]
    python -m validator.cli --file article.txt --keyword "seo" --title "Title"
    python -m validator.cli --text "..." --json

    # Orchestration (automated fix plans)
    python -m validator.cli --file article.txt --keyword "seo" --title "Title" --orchestrate
    python -m validator.cli --file article.txt --keyword "seo" --title "Title" --fix-prompt
    python -m validator.cli --file article.txt --keyword "seo" --title "Title" --orchestrate --json
    python -m validator.cli --file v1.txt --keyword "seo" --title "T" --orchestrate --revalidate-file v2.txt
"""

import argparse
import json
import sys
import os
from pathlib import Path

from .metrics import analyze, score_checklist
from .orchestrator import Orchestrator


def _icon(status: str) -> str:
    return {"pass": "PASS", "fail": "FAIL", "warning": "WARN", "na": "N/A"}.get(status, "???")


def _load_text(args) -> str:
    if args.file:
        if not Path(args.file).exists():
            print(f"[ERROR] File not found: {args.file}", file=sys.stderr)
            sys.exit(1)
        return Path(args.file).read_text(encoding="utf-8")
    if args.text:
        return args.text
    print("[ERROR] Provide --text or --file", file=sys.stderr)
    sys.exit(1)


def _cmd_checklist(args):
    text = _load_text(args)
    m = analyze(text, keyword=args.keyword, title=args.title,
                meta_description=args.meta, lang=args.lang)
    scores = score_checklist(m)
    if args.json:
        print(json.dumps(scores, ensure_ascii=False, indent=2))
    else:
        for fid, info in sorted(scores.items()):
            print(f"[{_icon(info['status'])}] {fid}: {info['detail']}")


def _cmd_report(args):
    text = _load_text(args)
    m = analyze(text, keyword=args.keyword, title=args.title,
                meta_description=args.meta, lang=args.lang)
    from .metrics import report
    if args.json:
        dumped = {k: v for k, v in m.__dict__.items() if k not in ("sentences", "paragraphs")}
        dumped["sentences_count"] = len(m.sentences)
        dumped["paragraphs_count"] = len(m.paragraphs)
        print(json.dumps(dumped, ensure_ascii=False, indent=2, default=str))
    else:
        print(report(m))


def _cmd_orchestrate(args):
    """Orchestrator mode — build fix plan and optionally re-validate."""
    text = _load_text(args)

    # Re-validation mode: compare before/after
    if args.revalidate_file:
        rv_path = Path(args.revalidate_file)
        if not rv_path.exists():
            print(f"[ERROR] Revalidate file not found: {args.revalidate_file}", file=sys.stderr)
            sys.exit(1)
        new_text = rv_path.read_text(encoding="utf-8")

        orch_before = Orchestrator(text, keyword=args.keyword, title=args.title,
                                   meta_description=args.meta, lang=args.lang)
        plan_before = orch_before.build_fix_plan()

        orch_after = Orchestrator(new_text, keyword=args.keyword, title=args.title,
                                  meta_description=args.meta, lang=args.lang)
        plan_after = orch_after.build_fix_plan()

        diff = orch_before.diff_report(plan_before, plan_after)
        print(diff)

        if args.json:
            result = {
                "before": {
                    "score_pct": plan_before.weighted_score_pct,
                    "grade": plan_before.grade,
                    "passed": plan_before.passed,
                    "failed": plan_before.failed,
                    "warnings": plan_before.warnings,
                    "na": plan_before.na_count,
                },
                "after": {
                    "score_pct": plan_after.weighted_score_pct,
                    "grade": plan_after.grade,
                    "passed": plan_after.passed,
                    "failed": plan_after.failed,
                    "warnings": plan_after.warnings,
                    "na": plan_after.na_count,
                },
                "remaining_issues": len(plan_after.instructions),
                "needs_another_round": len(plan_after.instructions) > 0,
            }
            print("\n--- JSON ---")
            print(json.dumps(result, ensure_ascii=False, indent=2))
        return

    # Standard orchestration
    orch = Orchestrator(text, keyword=args.keyword, title=args.title,
                        meta_description=args.meta, lang=args.lang)
    plan = orch.build_fix_plan()

    if args.fix_prompt:
        print(orch.fix_prompt_batch())
        return

    if args.json:
        print(json.dumps(orch.to_dict(), ensure_ascii=False, indent=2))
        return

    # Human-readable fix plan
    print(f"[RANKWISE ORCHESTRATOR] lang={plan.lang} keyword='{plan.keyword}'")
    print(f"Score: {plan.weighted_score_pct:.1f}% ({plan.grade})  |  "
          f"P:{plan.passed} F:{plan.failed} W:{plan.warnings} N/A:{plan.na_count}")
    if plan.critical_count:
        print(f"CRITICAL failures: {plan.critical_count} — grade cap applies")
    print()

    if not plan.instructions:
        print("[ALL CLEAR] All 16 computable factors pass.")
        return

    sev_order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}
    grouped = {}
    for instr in plan.instructions:
        grouped.setdefault(instr.severity, []).append(instr)

    for sev in sorted(grouped, key=lambda s: sev_order.get(s, 99)):
        print(f"{'='*60}")
        print(f"  {sev} PRIORITY ({len(grouped[sev])} issue(s))")
        print(f"{'='*60}")
        for instr in grouped[sev]:
            tag = "FAIL" if instr.status == "fail" else "WARN"
            print(f"\n  [{tag}] {instr.factor_id} — {instr.factor_name}")
            print(f"  Issue: {instr.detail}")
            print(f"  Target: {instr.target}")
            if instr.llm_prompt:
                print(f"\n  ── LLM Fix Prompt ──")
                for line in instr.llm_prompt.strip().splitlines():
                    print(f"  {line}")
            if instr.deterministic_fix:
                print(f"\n  ── Suggested Fix ──")
                print(f"  {instr.deterministic_fix}")
            print()

    # Summary
    print(f"{'='*60}")
    print(f"  SUMMARY: {len(plan.instructions)} issue(s) to fix")
    print(f"  Run with --fix-prompt for a consolidated LLM-ready prompt")
    print(f"  After fixes: re-run with --revalidate-file to check progress")
    print(f"{'='*60}")


def main():
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(
        description="RankWise Validator — deterministic SEO metrics + automated fix orchestration"
    )
    parser.add_argument("--text", type=str, default=None, help="Content text (body)")
    parser.add_argument("--file", type=str, default=None, help="Read content from file")
    parser.add_argument("--keyword", type=str, default="", help="Focus keyword")
    parser.add_argument("--title", type=str, default="", help="SEO title or H1")
    parser.add_argument("--meta", type=str, default="", help="Meta description")
    parser.add_argument("--lang", type=str, default="en", help="Language code")

    # Output modes
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--checklist", action="store_true",
                        help="Output checklist scores only")

    # Orchestration
    parser.add_argument("--orchestrate", action="store_true",
                        help="Run orchestration: validate → build fix plan")
    parser.add_argument("--fix-prompt", action="store_true",
                        help="Output a single consolidated LLM-ready fix prompt")
    parser.add_argument("--revalidate-file", type=str, default=None,
                        help="Path to revised content for before/after diff")

    args = parser.parse_args()

    if args.orchestrate or args.fix_prompt or args.revalidate_file:
        _cmd_orchestrate(args)
    elif args.checklist:
        _cmd_checklist(args)
    else:
        _cmd_report(args)


if __name__ == "__main__":
    main()
