#!/usr/bin/env python3
"""Prune trailing " module" from top-level titles in generated RST files.

Usage:
  python scripts/prune_module_suffix.py        # modifies files in-place

Environment:
  DRY_RUN=1  -> show planned changes without writing.

Behavior:
  * Scans the ``generated`` directory for ``*.rst`` files.
  * For each file, looks at the first heading (a line followed by ===== / ---- etc.).
  * If the heading text ends with " module" (case insensitive), the suffix is removed
    and the underline length is adjusted to match the new title length.
  * Idempotent: running again makes no further changes.
  * Skips ``modules.rst`` (often a master toctree) by default, unless ``--all`` is passed.
"""
from __future__ import annotations

import argparse
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
GENERATED = ROOT / "generated"
SUFFIX = " module"

HEADING_UNDERLINE_CHARS = set("=-~`^.:_*+#")  # common RST adornments


def find_heading(lines: list[str]):
    """Return (title_index, underline_index, title_text) of first simple heading.

    Simple heading = line of text (no leading whitespace) followed by a line of the
    same length consisting of a repeated adornment character.
    """
    for i in range(len(lines) - 1):
        title = lines[i].rstrip("\n")
        underline = lines[i + 1].rstrip("\n")
        if not title.strip():
            continue
        if title.startswith(" "):
            continue  # skip indented blocks
        if len(underline) == len(title) and underline and all(c == underline[0] for c in underline):
            if underline[0] in HEADING_UNDERLINE_CHARS:
                return i, i + 1, title
    return None


def prune_title(title: str) -> str | None:
    lower = title.lower()
    if lower.endswith(SUFFIX):
        return title[: -len(SUFFIX)]
    return None


def process_file(path: Path, dry_run: bool) -> bool:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    heading = find_heading(lines)
    if not heading:
        return False
    ti, ui, title = heading
    new_title = prune_title(title)
    if not new_title:
        return False
    # Preserve trailing newline on title line if present
    lines[ti] = f"{new_title}\n"
    lines[ui] = lines[ui][0] * len(new_title) + "\n"
    new_text = "".join(lines)
    if not dry_run:
        path.write_text(new_text, encoding="utf-8")
    return True


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Prune trailing ' module' from RST titles")
    parser.add_argument("--all", action="store_true", help="Also process modules.rst")
    args = parser.parse_args(argv)

    if not GENERATED.is_dir():
        print(f"[prune-module] Directory not found: {GENERATED}", file=sys.stderr)
        return 2

    dry_run = os.environ.get("DRY_RUN") == "1"
    changed = []
    skipped = 0
    for rst in sorted(GENERATED.glob("*.rst")):
        if not args.all and rst.name == "modules.rst":
            skipped += 1
            continue
        try:
            if process_file(rst, dry_run):
                changed.append(rst)
            else:
                skipped += 1
        except Exception as e:  # pragma: no cover
            print(f"[ERROR] {rst}: {e}", file=sys.stderr)
    prefix = "[DRY-RUN] " if dry_run else ""
    print(f"{prefix}Updated {len(changed)} files; skipped {skipped}.")
    for c in changed:
        print(f" - {c.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
