#!/usr/bin/env python3
"""Post-process generated RST files.

1. Strip the trailing " module" suffix from titles (Sphinx autodoc adds it).
2. Add ``:orphan:`` metadata so the files don't need to appear in any toctree
   (they are linked from difficulty index pages and the pattern index instead).

Running it more than once is safe — files that are already clean are left untouched.
"""
from __future__ import annotations

import argparse
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


def ensure_orphan(lines: list[str]) -> bool:
    """Prepend ``:orphan:`` metadata if not already present. Returns True if changed."""
    for line in lines:
        stripped = line.strip()
        if stripped == ":orphan:":
            return False
        if stripped:
            break  # first non-blank line is not :orphan:
    lines.insert(0, ":orphan:\n")
    lines.insert(1, "\n")
    return True


def process_file(path: Path, dry_run: bool) -> bool:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    changed = False

    # Add :orphan: metadata
    changed |= ensure_orphan(lines)

    # Prune " module" suffix from title
    heading = find_heading(lines)
    if heading:
        ti, ui, title = heading
        new_title = prune_title(title)
        if new_title:
            lines[ti] = f"{new_title}\n"
            lines[ui] = lines[ui][0] * len(new_title) + "\n"
            changed = True

    if changed and not dry_run:
        path.write_text("".join(lines), encoding="utf-8")
    return changed


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Prune trailing ' module' from RST titles")
    parser.add_argument("--all", action="store_true", help="Also process modules.rst")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without writing")
    args = parser.parse_args(argv)

    if not GENERATED.is_dir():
        print(f"[prune-module] Directory not found: {GENERATED}", file=sys.stderr)
        return 2

    dry_run = args.dry_run
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
