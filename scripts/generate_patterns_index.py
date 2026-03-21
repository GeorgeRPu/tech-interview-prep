"""Generate patterns.rst — a Patterns Index with a single filterable table.

Each solution file's module docstring contains a ``Pattern`` section listing the
techniques used (comma-separated).  This script collects those tags from every file
under ``solutions/``, builds one flat table (Solution | Difficulty | Pattern), and
writes ``patterns.rst`` at the project root.  The table supports client-side
filtering by Difficulty and Pattern via inline JavaScript.

The generated file is rebuilt on every ``make html`` run and removed by ``make clean``.
Running this script more than once is safe — if the output is identical to what is
already on disk the file is left untouched.
"""

from __future__ import annotations

import ast
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOLUTIONS = ROOT / "solutions"
OUT_FILE = ROOT / "patterns.rst"

DIFFICULTY_DIRS = [("Easy", "easy"), ("Medium", "medium"), ("Hard", "hard")]

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

_PASCAL_WORD_RE = re.compile(r"[A-Z]+(?=[A-Z][a-z]|$)|[A-Z][a-z0-9]*")


def pascal_to_words(name: str) -> str:
    """Convert a PascalCase identifier to a space-separated human-readable string.

    Examples::

        >>> pascal_to_words("TwoSum")
        'Two Sum'
        >>> pascal_to_words("LRUCache")
        'LRU Cache'
        >>> pascal_to_words("TwoSumII")
        'Two Sum II'
        >>> pascal_to_words("ConvertSortedArrayToBST")
        'Convert Sorted Array To BST'
        >>> pascal_to_words("InsertDeleteGetRandomO1")
        'Insert Delete Get Random O1'
        >>> pascal_to_words("Sqrtx")
        'Sqrtx'
    """
    words = _PASCAL_WORD_RE.findall(name)
    return " ".join(words) if words else name


def extract_patterns(docstring: str) -> list[str]:
    """Return pattern tags from the ``Pattern`` section of an RST docstring.

    The section looks like::

        Pattern
        -------
        Two Pointers, Hash Map

    Content starts immediately after the underline (no blank line).
    Returns an empty list when no ``Pattern`` section is found.
    """
    lines = docstring.splitlines()
    for i, line in enumerate(lines):
        if line.strip() == "Pattern" and i + 1 < len(lines) and set(lines[i + 1].strip()) <= {"-"}:
            content: list[str] = []
            j = i + 2
            while j < len(lines):
                # Stop when the next line is a section underline
                if (
                    j + 1 < len(lines)
                    and lines[j + 1].strip()
                    and set(lines[j + 1].strip()).issubset(set("-=^~"))
                ):
                    break
                if lines[j].strip():
                    content.append(lines[j].strip())
                j += 1
            return [p.strip() for raw in content for p in raw.split(",") if p.strip()]
    return []


# Row: (display_name, module, difficulty, patterns)
Row = tuple[str, str, str, list[str]]


def collect() -> list[Row]:
    """Walk solution directories and return one row per solution, sorted by display name."""
    solution_map: dict[str, tuple[str, list[str]]] = {}  # module -> (difficulty, patterns)
    missing: list[str] = []

    for difficulty, dirname in DIFFICULTY_DIRS:
        dirpath = SOLUTIONS / dirname
        if not dirpath.is_dir():
            continue
        for pyfile in sorted(dirpath.glob("*.py")):
            if pyfile.name.startswith("_"):
                continue
            module = pyfile.stem
            source = pyfile.read_text(encoding="utf-8")
            try:
                tree = ast.parse(source)
            except SyntaxError as exc:
                print(f"[generate-patterns] WARNING: could not parse {pyfile.name}: {exc}", file=sys.stderr)
                continue
            docstring = ast.get_docstring(tree)
            if not docstring:
                missing.append(f"{dirname}/{pyfile.name}")
                continue
            patterns = extract_patterns(docstring)
            if not patterns:
                missing.append(f"{dirname}/{pyfile.name}")
                continue
            solution_map[module] = (difficulty, patterns)

    if missing:
        for path in missing:
            print(f"[generate-patterns] WARNING: no Pattern section found in {path}", file=sys.stderr)

    rows: list[Row] = []
    for module, (difficulty, patterns) in solution_map.items():
        display = pascal_to_words(module)
        rows.append((display, module, difficulty, patterns))

    return sorted(rows)  # sort by display_name


DIFFICULTY_EMOJI: dict[str, str] = {
    "Easy": "🟢",
    "Medium": "🟡",
    "Hard": "🔴",
}


def build_rst(rows: list[Row]) -> str:
    """Render the full RST content for patterns.rst as a single DataTables-powered table."""
    title = "Patterns Index"
    lines: list[str] = [
        title,
        "=" * len(title),
        "",
        "Browse all solutions. Use the dropdowns to filter by difficulty or pattern.",
        "",
        ".. list-table::",
        "   :header-rows: 1",
        "   :class: sphinx-datatable",
        "   :widths: auto",
        "",
        "   * - Solution",
        "     - Difficulty",
        "     - Pattern",
    ]

    for display, module, difficulty, patterns in rows:
        emoji = DIFFICULTY_EMOJI.get(difficulty, "")
        patterns_str = ", ".join(patterns)
        lines.append(f"   * - :doc:`{display} <generated/{module}>`")
        lines.append(f"     - {emoji} {difficulty}")
        lines.append(f"     - {patterns_str}")

    lines.append("")

    return "\n".join(lines) + "\n"


def main() -> int:
    rows = collect()
    if not rows:
        print("[generate-patterns] ERROR: no patterns found — is any solution file tagged?", file=sys.stderr)
        return 1
    content = build_rst(rows)
    if OUT_FILE.exists() and OUT_FILE.read_text(encoding="utf-8") == content:
        print("[generate-patterns] patterns.rst is already up to date — skipping write.")
        return 0
    OUT_FILE.write_text(content, encoding="utf-8")
    print(f"[generate-patterns] Written {OUT_FILE.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
