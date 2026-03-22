"""Generate easy_index.rst, medium_index.rst, hard_index.rst.

Each file lists solutions as bullet points with a truncated problem description
extracted from the module docstring. Rebuilt on every ``make html`` run.
"""

from __future__ import annotations

import ast
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOLUTIONS = ROOT / "solutions"

DIFFICULTY_DIRS = [("Easy", "easy"), ("Medium", "medium"), ("Hard", "hard")]

MAX_DESC_LEN = 120

_PASCAL_WORD_RE = re.compile(r"[A-Z]+(?=[A-Z][a-z]|$)|[A-Z][a-z0-9]*")


def pascal_to_words(name: str) -> str:
    words = _PASCAL_WORD_RE.findall(name)
    return " ".join(words) if words else name


def extract_description(docstring: str) -> str:
    """Extract the problem description text between the URL and the first Example."""
    lines = docstring.splitlines()
    # Find start: first line after the URL (http...) line in the Problem section
    start = None
    for i, line in enumerate(lines):
        if line.strip().startswith("http"):
            start = i + 1
            break
    if start is None:
        return ""

    # Collect lines until we hit **Example or an empty-ish section
    parts: list[str] = []
    for i in range(start, len(lines)):
        stripped = lines[i].strip()
        if stripped.startswith("**Example"):
            break
        # Stop at next RST section heading
        if (
            i + 1 < len(lines)
            and stripped
            and lines[i + 1].strip()
            and set(lines[i + 1].strip()).issubset(set("-=^~"))
        ):
            break
        if stripped:
            # Remove RST inline markup for cleaner plain text
            clean = stripped
            clean = re.sub(r"\*\*(.+?)\*\*", r"\1", clean)  # bold
            clean = re.sub(r"\*(.+?)\*", r"\1", clean)  # italic
            clean = re.sub(r"``(.+?)``", r"\1", clean)  # inline code
            parts.append(clean)

    desc = " ".join(parts).strip()
    if len(desc) > MAX_DESC_LEN:
        # Cut at word boundary
        desc = desc[:MAX_DESC_LEN].rsplit(" ", 1)[0] + "..."
    return desc


def build_rst(difficulty_label: str, dirname: str) -> str:
    title = difficulty_label
    lines = [title, "=" * len(title), ""]

    dirpath = SOLUTIONS / dirname
    if not dirpath.is_dir():
        return "\n".join(lines) + "\n"

    for pyfile in sorted(dirpath.glob("*.py")):
        if pyfile.name.startswith("_"):
            continue
        module = pyfile.stem
        display = pascal_to_words(module)

        desc = ""
        source = pyfile.read_text(encoding="utf-8")
        try:
            tree = ast.parse(source)
            docstring = ast.get_docstring(tree)
            if docstring:
                desc = extract_description(docstring)
        except SyntaxError:
            pass

        if desc:
            lines.append(f"- :doc:`{display} <generated/{module}>` -- {desc}")
        else:
            lines.append(f"- :doc:`{display} <generated/{module}>`")

    lines.append("")
    return "\n".join(lines) + "\n"


def main() -> int:
    for difficulty, dirname in DIFFICULTY_DIRS:
        out_file = ROOT / f"{dirname}_index.rst"
        content = build_rst(difficulty, dirname)
        if out_file.exists() and out_file.read_text(encoding="utf-8") == content:
            print(f"[generate-difficulty] {out_file.name} is already up to date.")
            continue
        out_file.write_text(content, encoding="utf-8")
        print(f"[generate-difficulty] Written {out_file.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
