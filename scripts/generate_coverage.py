"""Generate coverage.rst and problem_index.rst.

coverage.rst — "Problem Coverage": summary stats and a per-category breakdown
              table (Category | Blind 75 | Grind 75 | NeetCode 150).

problem_index.rst — "Problem Index": full filterable DataTable
                    (Problem | Pattern | Lists | Status).

Scans every solution file's docstring for a LeetCode URL, extracts the problem
slug, and checks each list problem against that map.

Both files are rebuilt on every ``make html`` run and removed by ``make clean``.
Running this script more than once is safe — unchanged files are left untouched.
"""

from __future__ import annotations

import ast
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOLUTIONS = ROOT / "solutions"
COVERAGE_FILE = ROOT / "coverage.rst"
INDEX_FILE = ROOT / "problem_index.rst"

DIFFICULTY_DIRS = [("Easy", "easy"), ("Medium", "medium"), ("Hard", "hard")]

# ---------------------------------------------------------------------------
# Problem data — loaded from problems.csv
# ---------------------------------------------------------------------------

_PROBLEMS_CSV = Path(__file__).parent / "problems.csv"


def _load_problems() -> list[tuple[str, str, bool, bool, bool, bool, bool]]:
    def _bool(v: str) -> bool:
        return v.strip().lower() == "true"

    with _PROBLEMS_CSV.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [
            (
                row["name"],
                row["slug"],
                _bool(row["blind75"]),
                _bool(row["nc150"]),
                _bool(row["grind75"]),
                _bool(row["grind169"]),
                _bool(row["premium"]),
            )
            for row in reader
        ]


PROBLEMS = _load_problems()

# ---------------------------------------------------------------------------
# Slug extraction
# ---------------------------------------------------------------------------

_SLUG_RE = re.compile(r"leetcode\.com/problems/([\w-]+)/")


def collect_covered_slugs() -> dict[str, tuple[str, str]]:
    """Return {slug: (module_name, difficulty)} for every solution that has a LeetCode URL."""
    slug_map: dict[str, tuple[str, str]] = {}
    for difficulty, dirname in DIFFICULTY_DIRS:
        dirpath = SOLUTIONS / dirname
        if not dirpath.is_dir():
            continue
        for pyfile in sorted(dirpath.glob("*.py")):
            if pyfile.name.startswith("_"):
                continue
            source = pyfile.read_text(encoding="utf-8")
            try:
                tree = ast.parse(source)
            except SyntaxError as exc:
                print(
                    f"[generate-coverage] WARNING: could not parse {pyfile.name}: {exc}",
                    file=sys.stderr,
                )
                continue
            docstring = ast.get_docstring(tree)
            if docstring:
                m = _SLUG_RE.search(docstring)
                if m:
                    slug_map[m.group(1)] = (pyfile.stem, difficulty)
    return slug_map


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

LEETCODE_BASE = "https://leetcode.com/problems"


def _lists_label(blind75: bool, nc150: bool, grind75: bool, grind169: bool) -> str:
    parts = []
    if blind75:
        parts.append("Blind 75")
    if grind75:
        parts.append("Grind 75")
    if grind169:
        parts.append("Grind 169")
    if nc150:
        parts.append("NeetCode 150")
    return ", ".join(parts)


def _pct(covered: int, total: int) -> str:
    return f"{100 * covered // total}%" if total else "0%"


def _bar(covered: int, total: int, width: int = 20) -> str:
    filled = round(width * covered / total) if total else 0
    return "■" * filled + "□" * (width - filled) + f" {_pct(covered, total)}"


def _count_covered(
    problems: list[tuple],
    slug_map: dict[str, tuple[str, str]],
) -> tuple[int, int]:
    total = len(problems)
    covered = sum(1 for _, slug, *_, premium in problems if not premium and slug in slug_map)
    return covered, total


# ---------------------------------------------------------------------------
# Page 1: Problem Coverage (summary stats + per-category breakdown)
# ---------------------------------------------------------------------------

def build_coverage_rst(slug_map: dict[str, tuple[str, str]]) -> str:
    b75  = [(n, s, b, nc, g, g169, p) for n, s, b, nc, g, g169, p in PROBLEMS if b]
    nc   = [(n, s, b, nc, g, g169, p) for n, s, b, nc, g, g169, p in PROBLEMS if nc]
    g75  = [(n, s, b, nc, g, g169, p) for n, s, b, nc, g, g169, p in PROBLEMS if g]
    g169 = [(n, s, b, nc, g, g169, p) for n, s, b, nc, g, g169, p in PROBLEMS if g169]

    b75_cov,  b75_tot  = _count_covered(b75,  slug_map)
    g75_cov,  g75_tot  = _count_covered(g75,  slug_map)
    g169_cov, g169_tot = _count_covered(g169, slug_map)
    nc_cov,   nc_tot   = _count_covered(nc,   slug_map)

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
        f"   * - Blind 75",
        f"     - {b75_cov}",
        f"     - {b75_tot}",
        f"     - {_bar(b75_cov, b75_tot)}",
        f"   * - Grind 75",
        f"     - {g75_cov}",
        f"     - {g75_tot}",
        f"     - {_bar(g75_cov, g75_tot)}",
        f"   * - Grind 169",
        f"     - {g169_cov}",
        f"     - {g169_tot}",
        f"     - {_bar(g169_cov, g169_tot)}",
        f"   * - NeetCode 150",
        f"     - {nc_cov}",
        f"     - {nc_tot}",
        f"     - {_bar(nc_cov, nc_tot)}",
        "",
        "See :doc:`problem_index` for the full problem list.",
        "",
    ]
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Page 2: Problem Index (full filterable table)
# ---------------------------------------------------------------------------

def build_problem_index_rst(slug_map: dict[str, tuple[str, str]]) -> str:
    title = "Problem Index"
    lines: list[str] = [
        title,
        "=" * len(title),
        "",
        "All problems from the Blind 75, Grind 75, Grind 169, and NeetCode 150 lists.",
        "Problems marked 🔒 require a LeetCode Premium subscription.",
        "",
        "Use the dropdowns to filter by pattern, list, or status.",
        "",
        ".. list-table::",
        "   :header-rows: 1",
        "   :class: sphinx-datatable coverage-datatable",
        "   :widths: auto",
        "",
        "   * - Problem",
        "     - Lists",
        "     - Status",
    ]

    for name, slug, blind75, nc150, grind75, grind169, premium in PROBLEMS:
        lists_label = _lists_label(blind75, nc150, grind75, grind169)
        lc_url = f"{LEETCODE_BASE}/{slug}/"

        if slug in slug_map:
            module, _difficulty = slug_map[slug]
            problem_cell = f":doc:`{name} <generated/{module}>`"
            status = "✅ Covered"
        elif premium:
            problem_cell = f"`{name} <{lc_url}>`__"
            status = "🔒 Premium"
        else:
            problem_cell = f"`{name} <{lc_url}>`__"
            status = "⬜ Missing"

        lines.append(f"   * - {problem_cell}")
        lines.append(f"     - {lists_label}")
        lines.append(f"     - {status}")

    lines.append("")
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def _write_if_changed(path: Path, content: str) -> None:
    if path.exists() and path.read_text(encoding="utf-8") == content:
        print(f"[generate-coverage] {path.name} is already up to date — skipping write.")
        return
    path.write_text(content, encoding="utf-8")
    print(f"[generate-coverage] Written {path.relative_to(ROOT)}")


def main() -> int:
    slug_map = collect_covered_slugs()
    _write_if_changed(COVERAGE_FILE, build_coverage_rst(slug_map))
    _write_if_changed(INDEX_FILE, build_problem_index_rst(slug_map))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
