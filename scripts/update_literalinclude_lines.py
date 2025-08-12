#!/usr/bin/env python3
"""Update ``:lines:`` ranges in solution files' top-level docstrings.

Algorithm (per file):
 1. Locate the module docstring at the very top of the file (after any shebang/encoding/comments).
 2. Find the first non-blank, non-comment line after the docstring: that's the first code line number (1-based).
 3. Inside the docstring text, locate any ``.. literalinclude:: ../solutions/.../<name>.py`` blocks and rewrite an existing
     ``:lines: X-`` (or ``:lines: X-Y``) option so that X becomes the computed first code line number, and force an open-ended
     range ``<start>-``.
 4. Leave everything else untouched.

Edge cases handled:
 * Raw / prefixed docstrings (r, u, f, b, combinations and case insensitivity) are supported.
 * Multiple literalinclude blocks referencing the file are all updated.
 * If no docstring or no matching literalinclude is present, the file is skipped.
 * If code begins immediately after the docstring (no blank line), that immediate next line number is used.

Set environment variable ``DRY_RUN=1`` to preview without writing changes.
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOLUTIONS = ROOT / 'solutions'

LITERALINCLUDE_RE = re.compile(r"(^\s*\.\.\s+literalinclude::\s+\.{2}/solutions/.+?\.py\s*$)(?:\n(^\s+:[a-zA-Z0-9_-]+:.*$))*", re.MULTILINE)
LINES_OPTION_RE = re.compile(r"^(?P<indent>\s*):lines:\s*([0-9]+)(?:-([0-9]*))?\s*$", re.MULTILINE)
TRIPLE_QUOTE_RE = re.compile(r'^(?P<indent>\s*)(?P<prefix>[rubfRUBF]*)(?P<quote>"""|\'\'\')')


def find_module_docstring_bounds(text: str):
    # Skip shebang or encoding lines and leading comments/blank lines
    lines = text.splitlines()
    idx = 0
    while idx < len(lines) and (not lines[idx].strip() or lines[idx].startswith('#') or lines[idx].startswith(('#!/', '#!')) or lines[idx].startswith('# -*-')):
        idx += 1
    if idx >= len(lines):
        return None
    m = TRIPLE_QUOTE_RE.match(lines[idx])
    if not m:
        return None
    quote = m.group('quote')
    # Search for closing quote
    # If opening and closing on same line
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
    rel_from_root = path.relative_to(ROOT)
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

    # Determine path reference used in literalinclude (normalize for matching)
    # Accept patterns like .. literalinclude:: ../solutions/easy/Foo.py
    updated = False

    # We only update :lines: options inside the docstring region
    docstring_text = '\n'.join(lines[start:end+1])

    def replace_lines_option(match):
        block = match.group(0)
        # Only modify :lines: lines inside this block
        def repl_line_option(mo):
            indent = mo.group('indent')
            return f"{indent}:lines: {first_code_line_number}-"
        new_block = LINES_OPTION_RE.sub(repl_line_option, block)
        return new_block

    new_docstring_text, count = re.subn(LITERALINCLUDE_RE, replace_lines_option, docstring_text)
    if count:
        if new_docstring_text != docstring_text:
            updated = True
            # Reassemble file
            new_lines = lines.copy()
            new_doc_lines = new_docstring_text.splitlines()
            new_lines[start:start+len(new_doc_lines)] = new_doc_lines
            # If lengths differ adjust (simpler to rebuild entire text region)
            # Compose final text
            final_text = '\n'.join(new_lines) + ('\n' if text.endswith('\n') else '')
            if not dry_run:
                path.write_text(final_text, encoding='utf-8')
    return updated


def main():
    dry_run = os.environ.get('DRY_RUN') == '1'
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
