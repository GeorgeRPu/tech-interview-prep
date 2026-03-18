#!/usr/bin/env python3
"""Fetch problem descriptions from LeetCode and insert them into solution docstrings.

For each solution file that contains a LeetCode URL in its Problem section, this script
queries LeetCode's GraphQL API, converts the HTML response to RST via pandoc, and inserts
(or replaces) the description between the URL line and the next RST section. Files that
already have an up-to-date description are left untouched.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import pypandoc
import requests

ROOT = Path(__file__).resolve().parents[1]
SOLUTIONS = ROOT / "solutions"

LEETCODE_GRAPHQL = "https://leetcode.com/graphql"
SLUG_RE = re.compile(r"https://leetcode\.com/problems/([\w-]+)/?")
TRIPLE_QUOTE_RE = re.compile(r"^(?P<prefix>[rubfRUBF]*)(?P<quote>\"\"\"|\'\'\')")


def _html_to_rst(html: str) -> str:
    return pypandoc.convert_text(html, "rst", format="html").strip()


def fetch_description(slug: str) -> str | None:
    resp = requests.post(
        LEETCODE_GRAPHQL,
        json={
            "query": (
                "query questionContent($titleSlug: String!) {"
                "  question(titleSlug: $titleSlug) { content }"
                "}"
            ),
            "variables": {"titleSlug": slug},
        },
        headers={"Referer": f"https://leetcode.com/problems/{slug}/"},
        timeout=15,
    )
    resp.raise_for_status()
    content = (resp.json().get("data") or {}).get("question", {}).get("content")
    if not content:
        return None
    return _html_to_rst(content)


def _find_module_docstring_bounds(text: str) -> tuple[int, int] | None:
    lines = text.splitlines()
    idx = 0
    while idx < len(lines) and (
        not lines[idx].strip() or lines[idx].startswith("#")
    ):
        idx += 1
    if idx >= len(lines):
        return None
    m = TRIPLE_QUOTE_RE.match(lines[idx])
    if not m:
        return None
    quote = m.group("quote")
    if lines[idx].count(quote) >= 2:
        return (idx, idx)
    j = idx + 1
    while j < len(lines):
        if quote in lines[j]:
            return (idx, j)
        j += 1
    return None


def update_file(path: Path, dry_run: bool = False) -> tuple[bool, str]:
    text = path.read_text(encoding="utf-8")
    bounds = _find_module_docstring_bounds(text)
    if not bounds:
        return False, "no docstring"
    start, end = bounds
    lines = text.splitlines()
    doc = lines[start : end + 1]

    # Find LeetCode URL line within the docstring
    url_idx: int | None = None
    slug: str | None = None
    for i, line in enumerate(doc):
        m = SLUG_RE.search(line)
        if m:
            url_idx = i
            slug = m.group(1)
            break
    if url_idx is None or slug is None:
        return False, "no LeetCode URL"

    # Find the next RST section after the URL (heading + underline of dashes)
    next_section_idx: int | None = None
    for i in range(url_idx + 1, len(doc)):
        if re.match(r"^-{3,}\s*$", doc[i]):
            next_section_idx = i - 1  # heading line
            break
    if next_section_idx is None:
        return False, "no RST section after Problem"

    try:
        description = fetch_description(slug)
    except requests.RequestException as e:
        return False, f"request failed: {e}"
    if description is None:
        return False, f"no content returned for {slug!r}"

    # Replace lines from url_idx+1 up to (not including) next_section_idx
    # with a blank line + description + blank line
    new_middle = [doc[url_idx], ""] + description.splitlines() + [""]
    new_doc = doc[:url_idx] + new_middle + doc[next_section_idx:]

    if new_doc == doc:
        return False, "no change"

    new_lines = lines[:start] + new_doc + lines[end + 1 :]
    final = "\n".join(new_lines) + ("\n" if text.endswith("\n") else "")
    if not dry_run:
        path.write_text(final, encoding="utf-8")
    return True, slug


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Fetch LeetCode problem descriptions into solution docstrings"
    )
    parser.add_argument(
        "files",
        nargs="*",
        type=Path,
        help="Solution files to update (default: all under solutions/)",
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Preview changes without writing"
    )
    args = parser.parse_args(argv)

    targets: list[Path] = args.files or sorted(SOLUTIONS.rglob("*.py"))
    dry_run: bool = args.dry_run
    changed: list[Path] = []
    failed: list[Path] = []
    skipped = 0

    for path in targets:
        if path.name == "__init__.py":
            continue
        label = path.relative_to(ROOT)
        print(f"  {label} ... ", end="", flush=True)
        ok, detail = update_file(path, dry_run=dry_run)
        if ok:
            print(f"updated ({detail})")
            changed.append(path)
        elif detail == "no change":
            print("up to date")
            skipped += 1
        elif detail.startswith(("no ", "could not", "no content")):
            print(f"skipped ({detail})")
            skipped += 1
        else:
            print(f"FAILED ({detail})", file=sys.stderr)
            failed.append(path)

    prefix = "[DRY-RUN] " if dry_run else ""
    print(f"\n{prefix}Updated {len(changed)}, skipped {skipped}, failed {len(failed)}.")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
