#!/usr/bin/env python3
"""Structural validator for RankWise.

Stdlib only. Run from the repository root or from any directory:

    python tests/validate_skill.py

Exits 1 if any hard check fails.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "skills" / "rankwise"
SKILL = SKILL_DIR / "SKILL.md"
CHANGELOG = ROOT / "CHANGELOG.md"
README = ROOT / "README.md"
README_RU = ROOT / "README.ru.md"

REQUIRED_SECTIONS = [
    "How to Use This Skill",
    "Role",
    "When Not to Use",
    "Operating Modes",
    "Output Contract",
    "The 49-Factor SEO Scorecard",
    "Keyword Strategy",
    "Content Architecture",
    "Linking Strategy",
    "Technical SEO",
    "Power Words & Sentiment",
    "Language Adaptation",
    "Language Resources",
    "Integration with Other Skills",
    "Output Formats",
    "Module Activation Logic",
    "Scenario Summaries",
    "Reference Files",
    "Post-Generation Validation",
    "Quick Start",
    "Project Layout",
]

errors: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


def read(path: Path) -> str:
    if not path.exists():
        fail(f"missing file: {path.relative_to(ROOT)}")
        return ""
    return path.read_text(encoding="utf-8")


def between(text: str, start: str, end: str) -> str:
    i = text.find(start)
    if i < 0:
        return ""
    j = text.find(end, i + len(start))
    return text[i:j] if j >= 0 else text[i:]


def main() -> int:
    text = read(SKILL)
    changelog = read(CHANGELOG)
    readme = read(README)
    readme_ru = read(README_RU)

    match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
    if not match:
        fail("SKILL.md: missing or malformed frontmatter")
        return report()
    raw = match.group(1)
    top = dict(re.findall(r"^([a-z_]+):\s*(.+)$", raw, re.M))
    meta = dict(re.findall(r"^  ([a-z_]+):\s*(.+)$", raw, re.M))

    def clean(value: str) -> str:
        return value.strip().strip('"').strip("'")

    if clean(top.get("name", "")) != "rankwise":
        fail(f"frontmatter name must be 'rankwise', got {top.get('name')!r}")
    description = clean(top.get("description", ""))
    if not 80 <= len(description) <= 1024:
        fail(f"description length must be 80..1024, got {len(description)}")
    if "do not use" not in description.lower():
        fail("description must include negative triggers ('Do NOT use')")
    if clean(top.get("license", "")) != "MIT":
        fail("frontmatter license must be MIT")
    if not top.get("compatibility"):
        fail("frontmatter compatibility is required")

    version = clean(meta.get("version", ""))
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        fail(f"metadata.version must be semver, got {version!r}")
    elif f"[{version}]" not in changelog:
        fail(f"CHANGELOG.md has no entry for {version}")
    if version and version not in readme:
        fail(f"README.md does not mention version {version}")
    if version and version not in readme_ru:
        fail(f"README.ru.md does not mention version {version}")
    if not meta.get("repository"):
        fail("metadata.repository is required")

    for section in REQUIRED_SECTIONS:
        if f"## {section}" not in text:
            fail(f"missing section: ## {section}")

    modes = [int(n) for n in re.findall(r"^### Mode (\d+):", text, re.M)]
    if modes != list(range(1, 7)):
        fail(f"operating modes must be numbered 1..6, got {modes}")

    factors = {
        "K": 12,
        "C": 14,
        "L": 9,
        "T": 8,
        "A": 6,
    }
    for prefix, count in factors.items():
        found = [int(n) for n in re.findall(rf"^\| {prefix}(\d+) \|", text, re.M)]
        if found != list(range(1, count + 1)):
            fail(f"{prefix} factors must be numbered 1..{count}, got {found}")
    if sum(factors.values()) != 49:
        fail("factor groups do not add up to 49")

    scenarios = re.findall(r"^\| \*\*[a-z-]+\*\* \|", between(text, "## Scenario Summaries", "## Reference Files"), re.M)
    if len(scenarios) != 11:
        fail(f"scenario summaries must contain 11 rows, got {len(scenarios)}")

    for folder in ("shared", "scenarios", "examples", "validator"):
        if not (SKILL_DIR / folder).is_dir():
            fail(f"missing folder: {folder}/")

    for linked in re.findall(r"\]\(([^)]+)\)", text):
        if linked.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = linked.split("#", 1)[0]
        if not target or "[" in target or target in {"src"} or target.endswith((".jpg", ".png")):
            continue
        if not (SKILL_DIR / target).exists():
            fail(f"SKILL.md link missing: {linked}")

    for rel in re.findall(r"`((?:shared|scenarios|examples|validator)/[^`]+)`", text):
        if "[" in rel:
            continue
        if not (SKILL_DIR / rel).exists():
            fail(f"SKILL.md path missing: {rel}")

    for needle in ("TODO", "FIXME"):
        if needle in text:
            fail(f"SKILL.md contains forbidden string: {needle!r}")

    plugin = ROOT / ".claude-plugin" / "plugin.json"
    if plugin.exists():
        data = json.loads(plugin.read_text(encoding="utf-8"))
        if clean(str(data.get("version"))) != version:
            fail("plugin.json version does not match SKILL.md")

    marketplace = ROOT / ".claude-plugin" / "marketplace.json"
    if marketplace.exists():
        data = json.loads(marketplace.read_text(encoding="utf-8"))
        entry = (data.get("plugins") or [{}])[0]
        if clean(str(entry.get("version"))) != version:
            fail("marketplace.json version does not match SKILL.md")

    return report()


def report() -> int:
    if errors:
        print("RankWise validator")
        print("\nErrors:")
        for message in errors:
            print(f"  - {message}")
        print(f"\nFAILED: {len(errors)} error(s)")
        return 1
    print("RankWise validator")
    print("OK: all structural checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
