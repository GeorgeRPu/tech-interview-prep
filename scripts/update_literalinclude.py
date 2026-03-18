#!/usr/bin/env python3
"""Keep ``.. literalinclude::`` directives in solution docstrings accurate.

For each solution file, this script locates the module docstring and finds the first line of
code after it. Any ``.. literalinclude::`` blocks inside the docstring are then updated so that
the file path reflects the file's actual location under ``solutions/`` and the ``:lines:``
option starts at that first code line.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOLUTIONS = ROOT / 'solutions'

# Matches any .. literalinclude:: block (directive line + any option lines)
LITERALINCLUDE_RE = re.compile(
    r"^\s*\.\.\s+literalinclude::\s+\S+\s*$(?:\n^\s+:[a-zA-Z0-9_-]+:.*$)*",
    re.MULTILINE,
)
# Matches the path portion of a literalinclude directive line
LITERALINCLUDE_PATH_RE = re.compile(
    r"^(\s*\.\.\s+literalinclude::\s+)\S+",
    re.MULTILINE,
)
LINES_OPTION_RE = re.compile(r"^(?P<indent>\s*):lines:\s*([0-9]+)(?:-([0-9]*))?\s*$", re.MULTILINE)
TRIPLE_QUOTE_RE = re.compile(r'^(?P<indent>\s*)(?P<prefix>[rubfRUBF]*)(?P<quote>"""|\'\'\')')


def find_module_docstring_bounds(text: str):
    lines = text.splitlines()
    idx = 0
    while idx < len(lines) and (
        not lines[idx].strip()
        or lines[idx].startswith('#')
        or lines[idx].startswith(('#!/', '#!'))
        or lines[idx].startswith('# -*-')
    ):
        idx += 1
    if idx >= len(lines):
        return None
    m = TRIPLE_QUOTE_RE.match(lines[idx])
    if not m:
        return None
    quote = m.group('quote')
    if lines[idx].count(quote) >= 2:
        return (idx, idx)
    j = idx + 1
    while j < len(lines):
        if quote in lines[j]:
            if lines[j].count(quote) >= 1:
                return (idx, j)
        j += 1
    return None


def first_nonblank_noncomment_after(lines, end_idx):
    j = end_idx + 1
    while j < len(lines):
        stripped = lines[j].strip()
        if stripped and not stripped.startswith('#'):
            return j
        j += 1
    return None


def update_file(path: Path, dry_run: bool = False) -> bool:
    correct_path = '../' + path.relative_to(ROOT).as_posix()

    text = path.read_text(encoding='utf-8')
    doc_bounds = find_module_docstring_bounds(text)
    if not doc_bounds:
        return False
    start, end = doc_bounds
    lines = text.splitlines()
    first_code_line_idx = first_nonblank_noncomment_after(lines, end)
    if first_code_line_idx is None:
        return False
    first_code_line_number = first_code_line_idx + 1  # 1-based

    docstring_text = '\n'.join(lines[start:end + 1])

    def replace_block(match):
        block = match.group(0)
        block = LITERALINCLUDE_PATH_RE.sub(lambda m: m.group(1) + correct_path, block, count=1)
        block = LINES_OPTION_RE.sub(
            lambda mo: f"{mo.group('indent')}:lines: {first_code_line_number}-", block
        )
        return block

    new_docstring_text, count = re.subn(LITERALINCLUDE_RE, replace_block, docstring_text)
    if count and new_docstring_text != docstring_text:
        new_lines = lines.copy()
        new_doc_lines = new_docstring_text.splitlines()
        new_lines[start:start + len(new_doc_lines)] = new_doc_lines
        final_text = '\n'.join(new_lines) + ('\n' if text.endswith('\n') else '')
        if not dry_run:
            path.write_text(final_text, encoding='utf-8')
        return True
    return False


def main():
    parser = argparse.ArgumentParser(description="Update literalinclude directives in solution docstrings")
    parser.add_argument('--dry-run', action='store_true', help="Preview changes without writing")
    args = parser.parse_args()
    dry_run = args.dry_run
    changed = []
    skipped = 0
    for py in SOLUTIONS.rglob('*.py'):
        if py.name == '__init__.py':
            continue
        try:
            if update_file(py, dry_run=dry_run):
                changed.append(py)
            else:
                skipped += 1
        except Exception as e:
            print(f"Error processing {py}: {e}", file=sys.stderr)
    if dry_run:
        print(f"[DRY-RUN] Would update {len(changed)} files:")
    else:
        print(f"Updated {len(changed)} files.")
    for c in changed:
        print(f" - {c.relative_to(ROOT)}")
    print(f"Skipped {skipped} files (no change).")


if __name__ == '__main__':
    main()
