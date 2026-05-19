#!/usr/bin/env python3
"""Convert a legacy-format ``solutions/<diff>/<Pascal>.py`` (the old
docstring-laden style) into the new ``problems/<diff>/<slug>/`` source layout.

Usage:

    python scripts/migrate_solution.py <path-or-difficulty> ...

* ``<path>`` — migrate a single solution file (e.g. ``solutions/medium/Foo.py``).
* ``all`` — migrate every non-underscore-prefixed ``.py`` under ``solutions/``.

Non-LeetCode problems (e.g. HackerRank) are recognized by their URL and stored
with ``problem_url`` in ``meta.yaml`` and a slug derived from the filename.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

from _solutions import (
    DIFFICULTY_DIRS,
    PROBLEMS_DIR,
    ROOT,
    SOLUTIONS_DIR,
    description_url_split,
    extract_patterns_from_section,
    extract_slug,
    find_module_docstring_bounds,
    split_rst_sections,
)

_LEETCODE_URL_TOKEN = "leetcode.com/problems/"

_LEGACY_DIR_TO_DIFFICULTY = {dirname: label for label, dirname in DIFFICULTY_DIRS}


class _LiteralStr(str):
    """Tag a string so yaml dumps it as a literal block scalar."""


def _literal_representer(dumper: yaml.Dumper, data: _LiteralStr) -> yaml.ScalarNode:
    return dumper.represent_scalar("tag:yaml.org,2002:str", str(data), style="|")


yaml.add_representer(_LiteralStr, _literal_representer)


def _split_legacy(py_path: Path) -> tuple[dict[str, str], str]:
    """Return ``(sections, code_body)`` for a legacy solution file.

    ``sections`` keys: Problem/Solution/Pattern/Code/Test/Complexity (each may
    be missing). ``code_body`` is everything after the module docstring, with
    a single leading blank line stripped to preserve the convention.
    """
    text = py_path.read_text(encoding="utf-8")
    bounds = find_module_docstring_bounds(text)
    if bounds is None:
        raise ValueError(f"no module docstring in {py_path}")
    start, end = bounds
    lines = text.splitlines()

    quote = '"""' if '"""' in lines[start] else "'''"
    if start == end:
        inner = lines[start].split(quote, 2)
        body_text = inner[1] if len(inner) >= 3 else ""
    else:
        first_inner = lines[start][lines[start].find(quote) + len(quote):]
        last_inner = lines[end][:lines[end].find(quote)]
        body_lines = [first_inner] + lines[start + 1:end] + [last_inner]
        while body_lines and not body_lines[0].strip():
            body_lines.pop(0)
        while body_lines and not body_lines[-1].strip():
            body_lines.pop()
        body_text = "\n".join(body_lines)

    sections = split_rst_sections(body_text)
    code_lines = lines[end + 1:]
    if code_lines and not code_lines[0].strip():
        code_lines = code_lines[1:]
    return sections, "\n".join(code_lines)


def _slug_for(py_path: Path, url: str | None) -> tuple[str, str | None]:
    """Return ``(slug, problem_url_override)``.

    For LeetCode URLs the slug comes from the URL and there's no override.
    Otherwise the slug is the lowercased PascalCase filename and the original
    URL is stored verbatim as the ``problem_url`` override.
    """
    if url and _LEETCODE_URL_TOKEN in url:
        slug = extract_slug(url) or py_path.stem.lower()
        return slug, None
    return py_path.stem.lower(), url


def migrate_path(py_path: Path) -> int:
    difficulty = _LEGACY_DIR_TO_DIFFICULTY.get(py_path.parent.name)
    if difficulty is None:
        print(
            f"[migrate] ERROR: {py_path} is not under solutions/easy|medium|hard",
            file=sys.stderr,
        )
        return 1

    sections, code_body = _split_legacy(py_path)

    problem_block = sections.get("Problem", "")
    url, description_rst = description_url_split(problem_block)
    if url is None:
        print(
            f"[migrate] ERROR: no URL in Problem section of {py_path}",
            file=sys.stderr,
        )
        return 1

    slug, problem_url_override = _slug_for(py_path, url)
    pascal = py_path.stem
    out_dir = PROBLEMS_DIR / difficulty.lower() / slug
    out_dir.mkdir(parents=True, exist_ok=True)

    patterns = extract_patterns_from_section(sections.get("Pattern", ""))
    explanation = sections.get("Solution", "")
    complexity = sections.get("Complexity", "")
    test_block = sections.get("Test", "")

    meta: dict = {"slug": slug}
    if problem_url_override:
        meta["problem_url"] = problem_url_override
    meta["patterns"] = patterns
    meta["description_rst"] = (
        _LiteralStr(description_rst + "\n") if description_rst else ""
    )
    meta["explanation"] = _LiteralStr(explanation + "\n") if explanation else ""
    meta["complexity"] = _LiteralStr(complexity + "\n") if complexity else ""
    (out_dir / "meta.yaml").write_text(
        yaml.dump(meta, sort_keys=False, allow_unicode=True, width=1000),
        encoding="utf-8",
    )

    new_py = f'r"""\n{test_block}\n"""\n\n{code_body}\n'
    if not new_py.endswith("\n"):
        new_py += "\n"
    (out_dir / f"{pascal}.py").write_text(new_py, encoding="utf-8")

    py_path.unlink()
    print(
        f"[migrate] {slug}: {py_path.relative_to(ROOT)} -> "
        f"{out_dir.relative_to(ROOT)}/{{{pascal}.py, meta.yaml}}"
    )
    return 0


def migrate_all() -> int:
    rc = 0
    for _label, dirname in DIFFICULTY_DIRS:
        diff_dir = SOLUTIONS_DIR / dirname
        if not diff_dir.is_dir():
            continue
        for py in sorted(diff_dir.glob("*.py")):
            if py.name.startswith("_"):
                continue
            rc |= migrate_path(py)
    return rc


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "targets",
        nargs="+",
        help="paths to legacy .py files, or the literal 'all'",
    )
    args = parser.parse_args()

    if args.targets == ["all"]:
        return migrate_all()
    rc = 0
    for t in args.targets:
        rc |= migrate_path(Path(t).resolve())
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
