"""RankWise Validator — CLI entry point.

Usage:
    python -m validator.cli --text "content" --keyword "seo" --title "My Title" [--meta "desc"] [--lang en]
    python -m validator.cli --file article.txt --keyword "seo" --title "Title"
    python -m validator.cli --text "..." --json
"""

import argparse
import json
import sys
import os
from pathlib import Path

from .metrics import analyze, score_checklist


def main():
    # Ensure stdout uses UTF-8 on Windows
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description="RankWise Text Metrics Validator")
    parser.add_argument("--text", type=str, default=None, help="Content text (body)")
    parser.add_argument("--file", type=str, default=None, help="Read content from file")
    parser.add_argument("--keyword", type=str, default="", help="Focus keyword")
    parser.add_argument("--title", type=str, default="", help="SEO title or H1")
    parser.add_argument("--meta", type=str, default="", help="Meta description")
    parser.add_argument("--lang", type=str, default="en", help="Language code")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    parser.add_argument("--checklist", action="store_true", help="Output checklist scores only")

    args = parser.parse_args()

    if args.file:
        if not Path(args.file).exists():
            print(f"[ERROR] File not found: {args.file}", file=sys.stderr)
            sys.exit(1)
        text = Path(args.file).read_text(encoding="utf-8")
    elif args.text:
        text = args.text
    else:
        print("[ERROR] Provide --text or --file", file=sys.stderr)
        sys.exit(1)

    m = analyze(
        text=text,
        keyword=args.keyword,
        title=args.title,
        meta_description=args.meta,
        lang=args.lang,
    )

    if args.checklist:
        scores = score_checklist(m)
        if args.json:
            print(json.dumps(scores, ensure_ascii=False, indent=2))
        else:
            for fid, info in sorted(scores.items()):
                icon = {"pass": "PASS", "fail": "FAIL", "warning": "WARN", "na": "N/A"}.get(info["status"], "???")
                print(f"[{icon}] {fid}: {info['detail']}")
        return

    from .metrics import report

    if args.json:
        dumped = {k: v for k, v in m.__dict__.items() if k not in ("sentences", "paragraphs")}
        dumped["sentences_count"] = len(m.sentences)
        dumped["paragraphs_count"] = len(m.paragraphs)
        print(json.dumps(dumped, ensure_ascii=False, indent=2, default=str))
    else:
        print(report(m))


if __name__ == "__main__":
    main()
