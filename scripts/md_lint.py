#!/usr/bin/env python3
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent


def check_file(path: pathlib.Path):
    issues = []
    with path.open(encoding='utf-8') as f:
        for idx, line in enumerate(f, 1):
            if re.search(r"\bteh\b", line, re.IGNORECASE):
                issues.append(f"{path}:{idx}: misspelling 'teh'")
    return issues


def main() -> int:
    issues = []
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        issues.extend(check_file(path))
    if issues:
        print("\n".join(issues))
        return 1
    print("No issues found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
