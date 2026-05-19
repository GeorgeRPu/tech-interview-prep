#!/usr/bin/env python3
"""Unified docs generator: reads the structured ``problems/`` source and emits
every Sphinx page that the old per-script pipeline produced.

Outputs:
* ``generated/<Pascal>.rst`` per problem
* ``coverage.rst``, ``problem_index.rst``
* ``easy_index.rst``, ``medium_index.rst``, ``hard_index.rst``

The source tree under ``problems/`` is never modified — line numbers,
literalinclude paths, and rendered RST all live in the generator's output.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass, field
from pathlib import Path

import yaml

from _solutions import (
    DIFFICULTY_DIRS,
    DIFFICULTY_EMOJI,
    GENERATED_DIR,
    LEETCODE_BASE,
    LIST_DISPLAY,
    LIST_DISPLAY_ORDER,
    PROBLEMS_DIR,
    ROOT,
    find_module_docstring_bounds,
    first_nonblank_noncomment_after,
    list_link,
    lists_label,
    pascal_to_words,
    progress_bar,
    public_top_level_symbols,
    read_module_docstring,
    truncate_description,
)

CATALOG_PATH = PROBLEMS_DIR / "catalog.yaml"
COVERAGE_FILE = ROOT / "coverage.rst"
PROBLEM_INDEX_FILE = ROOT / "problem_index.rst"


@dataclass
class Problem:
    """In-memory model used by every page renderer."""

    slug: str
    name: str
    pascal: str
    difficulty: str  # "Easy" | "Medium" | "Hard"
    patterns: list[str]
    description_rst: str  # raw RST block, no surrounding blank lines
    short_description: str  # for difficulty index bullet
    source_path: Path  # absolute path to the source .py
    explanation: str
    complexity: str
    test_block: str
    first_code_line: int
    public_symbols: list[tuple[str, str]]
    problem_url: str  # full URL to the problem (LeetCode or other)
    in_catalog: bool  # True iff this slug appears in catalog.yaml


# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------


def load_catalog() -> list[dict]:
    if not CATALOG_PATH.exists():
        print(f"[generate-docs] ERROR: missing {CATALOG_PATH}", file=sys.stderr)
        return []
    with CATALOG_PATH.open(encoding="utf-8") as f:
        return yaml.safe_load(f) or []


def _new_source_problems(catalog_by_slug: dict[str, dict]) -> dict[str, Problem]:
    """Scan ``problems/<diff>/<slug>/`` for the new structured source."""
    out: dict[str, Problem] = {}
    if not PROBLEMS_DIR.is_dir():
        return out
    for difficulty_label, dirname in DIFFICULTY_DIRS:
        diff_dir = PROBLEMS_DIR / dirname
        if not diff_dir.is_dir():
            continue
        for slug_dir in sorted(p for p in diff_dir.iterdir() if p.is_dir()):
            slug = slug_dir.name
            meta_path = slug_dir / "meta.yaml"
            if not meta_path.exists():
                continue
            py_files = [p for p in slug_dir.glob("*.py") if not p.name.startswith("_")]
            if len(py_files) != 1:
                print(
                    f"[generate-docs] WARNING: {slug_dir} must contain exactly one .py "
                    f"(found {len(py_files)})",
                    file=sys.stderr,
                )
                continue
            py_path = py_files[0]
            pascal = py_path.stem
            with meta_path.open(encoding="utf-8") as f:
                meta = yaml.safe_load(f) or {}

            source = py_path.read_text(encoding="utf-8")
            bounds = find_module_docstring_bounds(source)
            if bounds is None:
                print(
                    f"[generate-docs] WARNING: no docstring in {py_path}",
                    file=sys.stderr,
                )
                continue
            _start, end = bounds
            first_code_line = first_nonblank_noncomment_after(source.splitlines(), end) or 1
            test_block = (read_module_docstring(py_path) or "").strip("\n")

            description_rst = (meta.get("description_rst") or "").rstrip("\n")
            short = truncate_description(description_rst)
            catalog_entry = catalog_by_slug.get(slug, {})
            name = catalog_entry.get("name", pascal_to_words(pascal))
            problem_url = meta.get("problem_url") or f"{LEETCODE_BASE}/{slug}/"

            out[slug] = Problem(
                slug=slug,
                name=name,
                pascal=pascal,
                difficulty=difficulty_label,
                patterns=list(meta.get("patterns") or []),
                description_rst=description_rst,
                short_description=short,
                source_path=py_path,
                explanation=(meta.get("explanation") or "").rstrip("\n"),
                complexity=(meta.get("complexity") or "").rstrip("\n"),
                test_block=test_block,
                first_code_line=first_code_line,
                public_symbols=public_top_level_symbols(py_path),
                problem_url=problem_url,
                in_catalog=slug in catalog_by_slug,
            )
    return out


def discover(catalog: list[dict]) -> dict[str, Problem]:
    catalog_by_slug = {entry["slug"]: entry for entry in catalog}
    return _new_source_problems(catalog_by_slug)


# ---------------------------------------------------------------------------
# Per-problem RST
# ---------------------------------------------------------------------------


def _section(header: str, body: str) -> list[str]:
    return [header, "-" * len(header), body]


def render_problem_rst(p: Problem) -> str:
    rel_source = p.source_path.relative_to(ROOT).as_posix()
    literalinclude_path = f"../{rel_source}"
    chunks: list[str] = [
        ":orphan:",
        "",
        p.pascal,
        "=" * len(p.pascal),
        "",
        f".. currentmodule:: {p.pascal}",
        "",
        # Disable syntax highlighting for the Problem section: the ``::``
        # literal blocks there hold sample Input/Output data, not code.
        # ``.. literalinclude::`` below carries its own :language: option so
        # the Code section stays Python-highlighted regardless.
        ".. highlight:: none",
        "",
    ]
    chunks += _section("Problem", f"{p.problem_url}\n\n{p.description_rst}")
    chunks.append("")
    chunks.append(".. highlight:: python")
    chunks.append("")
    chunks += _section("Solution", p.explanation)
    chunks.append("")
    chunks += _section("Pattern", ", ".join(p.patterns))
    chunks.append("")
    code_block = (
        f"\n.. literalinclude:: {literalinclude_path}\n"
        f"    :language: python\n"
        f"    :lines: {p.first_code_line}-"
    )
    chunks += _section("Code", code_block)
    chunks.append("")
    chunks += _section("Test", p.test_block)
    chunks.append("")
    chunks += _section("Complexity", p.complexity)
    chunks.append("")
    for kind, name in p.public_symbols:
        if kind == "function":
            chunks.append(f".. autofunction:: {name}")
        else:
            chunks.append(f".. autoclass:: {name}")
            chunks.append("   :members:")
            chunks.append("   :show-inheritance:")
            chunks.append("   :undoc-members:")
        chunks.append("")
    return "\n".join(chunks).rstrip() + "\n"


# ---------------------------------------------------------------------------
# coverage.rst + problem_index.rst
# ---------------------------------------------------------------------------


def _count_covered(catalog: list[dict], covered_slugs: set[str], list_key: str) -> tuple[int, int]:
    rows = [r for r in catalog if list_key in (r.get("lists") or [])]
    total = len(rows)
    covered = sum(1 for r in rows if not r.get("premium") and r["slug"] in covered_slugs)
    return covered, total


def render_coverage_rst(catalog: list[dict], covered_slugs: set[str]) -> str:
    rows_out: list[tuple[str, int, int]] = []
    for key in LIST_DISPLAY_ORDER:
        covered, total = _count_covered(catalog, covered_slugs, key)
        rows_out.append((LIST_DISPLAY[key], covered, total))

    title = "Problem Coverage"
    lines: list[str] = [
        title,
        "=" * len(title),
        "",
        "Coverage of canonical interview prep problem lists.",
        "",
        ".. list-table::",
        "   :header-rows: 1",
        "   :widths: auto",
        "",
        "   * - List",
        "     - Covered",
        "     - Total",
        "     - Progress",
    ]
    for label, covered, total in rows_out:
        lines.append(f"   * - {list_link(label)}")
        lines.append(f"     - {covered}")
        lines.append(f"     - {total}")
        lines.append(f"     - {progress_bar(covered, total)}")
    lines += [
        "",
        "See :doc:`problem_index` for the full problem list.",
        "",
    ]
    return "\n".join(lines) + "\n"


def render_problem_index_rst(catalog: list[dict], problems: dict[str, Problem]) -> str:
    title = "Problem Index"
    lines: list[str] = [
        title,
        "=" * len(title),
        "",
        "All problems from the Blind 75, Grind 75, Grind 169, NeetCode 150, Amazon Top 50, and Google Top 50 lists.",
        "Problems marked 🔒 require a LeetCode Premium subscription.",
        "",
        "Use the dropdowns to filter by difficulty, pattern, list, or status.",
        "",
        ".. list-table::",
        "   :header-rows: 1",
        "   :class: sphinx-datatable coverage-datatable",
        "   :widths: auto",
        "",
        "   * - Problem",
        "     - Difficulty",
        "     - Pattern",
        "     - Lists",
        "     - Status",
    ]
    for row in catalog:
        slug = row["slug"]
        name = row["name"]
        lc_url = f"{LEETCODE_BASE}/{slug}/"
        lists = row.get("lists") or []
        lists_cell = lists_label(lists)
        if slug in problems:
            p = problems[slug]
            problem_cell = f":doc:`{name} <generated/{p.pascal}>`"
            emoji = DIFFICULTY_EMOJI.get(p.difficulty, "")
            difficulty_cell = f"{emoji} {p.difficulty}"
            pattern_cell = ", ".join(p.patterns)
            status = "✅ Covered"
        elif row.get("premium"):
            problem_cell = f"`{name} <{lc_url}>`__"
            difficulty_cell = ""
            pattern_cell = ""
            status = "🔒 Premium"
        else:
            problem_cell = f"`{name} <{lc_url}>`__"
            difficulty_cell = ""
            pattern_cell = ""
            status = "⬜ Missing"
        lines += [
            f"   * - {problem_cell}",
            f"     - {difficulty_cell}",
            f"     - {pattern_cell}",
            f"     - {lists_cell}",
            f"     - {status}",
        ]
    lines.append("")
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Difficulty indexes
# ---------------------------------------------------------------------------


def render_difficulty_rst(difficulty_label: str, problems: dict[str, Problem]) -> str:
    title = difficulty_label
    lines = [title, "=" * len(title), ""]
    matches = sorted(
        (p for p in problems.values() if p.difficulty == difficulty_label),
        key=lambda p: p.pascal,
    )
    for p in matches:
        display = pascal_to_words(p.pascal)
        if p.short_description:
            lines.append(
                f"- :doc:`{display} <generated/{p.pascal}>` -- {p.short_description}"
            )
        else:
            lines.append(f"- :doc:`{display} <generated/{p.pascal}>`")
    lines.append("")
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def _write_if_changed(path: Path, content: str) -> bool:
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def main() -> int:
    catalog = load_catalog()
    problems = discover(catalog)

    GENERATED_DIR.mkdir(exist_ok=True)
    rst_written = 0
    for p in problems.values():
        out = GENERATED_DIR / f"{p.pascal}.rst"
        if _write_if_changed(out, render_problem_rst(p)):
            rst_written += 1

    cov_changed = _write_if_changed(
        COVERAGE_FILE, render_coverage_rst(catalog, set(problems))
    )
    idx_changed = _write_if_changed(
        PROBLEM_INDEX_FILE, render_problem_index_rst(catalog, problems)
    )

    diff_changed = 0
    for label, dirname in DIFFICULTY_DIRS:
        out = ROOT / f"{dirname}_index.rst"
        if _write_if_changed(out, render_difficulty_rst(label, problems)):
            diff_changed += 1

    print(
        f"[generate-docs] {len(problems)} problems; "
        f"{rst_written} per-problem rst files (re)written, "
        f"coverage{'*' if cov_changed else ''}, "
        f"problem_index{'*' if idx_changed else ''}, "
        f"{diff_changed} difficulty index file(s) updated."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
