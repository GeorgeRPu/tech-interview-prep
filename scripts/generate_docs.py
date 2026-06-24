#!/usr/bin/env python3
"""Top-level entry point: discover problems, render every Sphinx page,
write whatever changed.

The work itself lives in two sibling modules:

* :mod:`discovery` — constants, source-file introspection, the ``Problem`` /
  ``Variant`` model, and the ``problems/`` scanner.
* :mod:`rendering` — every ``render_*`` function that turns those objects
  into RST strings.

This file just wires them together.
"""

from __future__ import annotations

import sys
from pathlib import Path

import yaml

from discovery import (
    DIFFICULTY_DIRS,
    GENERATED_DIR,
    PROBLEMS_DIR,
    ROOT,
    discover_problems,
)
from rendering import (
    render_coverage_rst,
    render_difficulty_rst,
    render_problem_index_rst,
    render_problem_rst,
)

CATALOG_PATH = PROBLEMS_DIR / "catalog.yaml"
COVERAGE_FILE = ROOT / "coverage.rst"
PROBLEM_INDEX_FILE = ROOT / "problem_index.rst"


def _write_if_changed(path: Path, content: str) -> bool:
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def main() -> int:
    if not CATALOG_PATH.exists():
        print(f"[generate-docs] ERROR: missing {CATALOG_PATH}", file=sys.stderr)
        return 1
    with CATALOG_PATH.open(encoding="utf-8") as f:
        catalog: list[dict] = yaml.safe_load(f) or []

    catalog_by_slug = {entry["slug"]: entry for entry in catalog}
    problems = discover_problems(catalog_by_slug)

    GENERATED_DIR.mkdir(exist_ok=True)
    rst_written = 0
    for p in problems.values():
        out = GENERATED_DIR / f"{p.slug}.rst"
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
        content = render_difficulty_rst(
            label,
            problems,
            catalog_by_slug,
        )
        if _write_if_changed(out, content):
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
