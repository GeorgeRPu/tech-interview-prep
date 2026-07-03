"""Read the structured ``problems/`` source into in-memory ``Problem`` objects.

Owns the shared path/difficulty constants, the source-file introspection
helpers, and the slug→module-name derivation. Consumed by :mod:`rendering`
(for RST output) and by ``generate_docs.py`` (for the top-level wiring).
"""

from __future__ import annotations

import ast
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

import yaml

# ---------------------------------------------------------------------------
# Shared constants
# ---------------------------------------------------------------------------

ROOT = Path(__file__).resolve().parents[1]
PROBLEMS_DIR = ROOT / "problems"
GENERATED_DIR = ROOT / "generated"

LEETCODE_BASE = "https://leetcode.com/problems"

DIFFICULTY_DIRS = [("Easy", "easy"), ("Medium", "medium"), ("Hard", "hard")]

UNDERLINE_CHARS = set("-=^~")
MAX_DESC_LEN = 120


def _warn(msg: str) -> None:
    print(f"[generate-docs] WARNING: {msg}", file=sys.stderr)


# ---------------------------------------------------------------------------
# Source-file introspection
# ---------------------------------------------------------------------------


@dataclass
class ModuleInfo:
    """Everything the renderer needs from one solution ``.py`` file."""

    docstring: str  # raw module docstring (holds the doctests)
    first_code_line: int  # 1-based start line for the literalinclude block
    public_symbols: list[tuple[str, str]]  # (kind, name) for autodoc directives


def inspect_module(py_path: Path) -> ModuleInfo | None:
    """Parse a solution module once and pull out all build-time metadata.

    Returns ``None`` when the file cannot be parsed or has no module
    docstring (the docstring carries the doctests, so it is required).
    """
    try:
        tree = ast.parse(py_path.read_text(encoding="utf-8"))
    except SyntaxError:
        return None
    docstring = ast.get_docstring(tree, clean=False)
    if docstring is None:
        return None

    # The docstring is ``tree.body[0]``; the first statement after it gives
    # the literalinclude start line (counting a leading decorator if present).
    first_code_line = 1
    if len(tree.body) > 1:
        node = tree.body[1]
        decorators = getattr(node, "decorator_list", None)
        first_code_line = decorators[0].lineno if decorators else node.lineno

    symbols: list[tuple[str, str]] = []
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if not node.name.startswith("_"):
                symbols.append(("function", node.name))
        elif isinstance(node, ast.ClassDef):
            if not node.name.startswith("_"):
                symbols.append(("class", node.name))

    if symbols:
        kind, name = symbols[0]
        first_def = next(
            n
            for n in tree.body
            if isinstance(
                n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)
            )
            and n.name == name
        )
        if ast.get_docstring(first_def) is None:
            _warn(f"{py_path}: {kind} '{name}' is missing a docstring")

    return ModuleInfo(docstring, first_code_line, symbols)


# ---------------------------------------------------------------------------
# Module-name derivation
# ---------------------------------------------------------------------------


def slug_to_module_prefix(slug: str) -> str:
    """Convert ``two-sum`` to ``two_sum`` for use as a Python module prefix.

    Slugs that start with a digit (e.g. ``3sum``) are prefixed with ``p_`` so
    the result is a valid Python identifier.
    """
    prefix = slug.replace("-", "_")
    if prefix and prefix[0].isdigit():
        prefix = "p_" + prefix
    return prefix


def solution_module_name(slug: str, solution_name: str) -> str:
    """Derive the Python module name for a solution variant.

    ``two-sum`` + ``Brute Force`` -> ``two_sum__brute_force``.
    The double-underscore separator keeps the slug and solution components
    visually distinct and guarantees uniqueness on ``sys.path`` even when
    multiple problems share a solution name.
    """
    normalized = solution_name.lower().replace(" ", "_").replace("-", "_")
    solution_part = re.sub(r"[^a-z0-9_]", "", normalized)
    return f"{slug_to_module_prefix(slug)}__{solution_part}"


# ---------------------------------------------------------------------------
# Description truncation (used to populate Problem.short_description)
# ---------------------------------------------------------------------------


def truncate_description(
    description_rst: str, max_len: int = MAX_DESC_LEN
) -> str:
    """Plain-text truncation for the difficulty bullet lists."""
    parts: list[str] = []
    for raw in description_rst.splitlines():
        stripped = raw.strip()
        if stripped.startswith("**Example"):
            break
        if (
            parts
            and stripped
            and set(stripped).issubset(UNDERLINE_CHARS)
            and len(stripped) >= 3
        ):
            # next-section underline — shouldn't appear in stored description_rst
            # but keep this guard for safety against legacy raw blocks
            break
        if stripped:
            clean = stripped
            clean = re.sub(r"\*\*(.+?)\*\*", r"\1", clean)
            clean = re.sub(r"\*(.+?)\*", r"\1", clean)
            clean = re.sub(r"``(.+?)``", r"\1", clean)
            parts.append(clean)
    desc = " ".join(parts).strip()
    if len(desc) > max_len:
        desc = desc[:max_len].rsplit(" ", 1)[0] + "..."
    desc = _strip_rst_markup(desc)
    return desc


def _strip_rst_markup(text: str) -> str:
    """Remove residual RST inline markup from a plain-text summary."""
    text = text.replace("\\", "")
    text = re.sub(r"\*+", "", text)
    text = re.sub(r"`+", "", text)
    text = re.sub(r" {2,}", " ", text)
    return text.strip().strip(".")


# ---------------------------------------------------------------------------
# In-memory model
# ---------------------------------------------------------------------------


@dataclass
class Variant:
    """One approach to a problem (one tab on the rendered page)."""

    name: str  # display label, e.g. "Brute Force"
    module: str  # python module name on sys.path, e.g. "two_sum__brute_force"
    source_path: Path  # absolute path to the variant's .py file
    explanation: str
    complexity: str
    test_block: str  # raw docstring text containing the doctests
    first_code_line: int  # 1-based; first executable line after the docstring
    public_symbols: list[tuple[str, str]]  # (kind, name) for autodoc directives


@dataclass
class Problem:
    """In-memory model used by every page renderer."""

    slug: str  # canonical identifier ("two-sum"); used as page filename
    name: str  # display title from catalog.yaml ("Two Sum")
    difficulty: str  # "Easy" | "Medium" | "Hard"
    patterns: list[str]
    description_rst: str  # raw RST block, no surrounding blank lines
    short_description: str  # for difficulty index bullet
    problem_url: str  # full URL to the problem (LeetCode or other)
    in_catalog: bool  # True iff this slug appears in catalog.yaml
    variants: list[Variant] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------


def _build_variant(slug: str, slug_dir: Path, entry: dict) -> Variant | None:
    """Parse one ``solutions:`` entry into a Variant, or return None on error."""
    name = (entry.get("name") or "").strip()
    if not name:
        _warn(f"{slug_dir}/meta.yaml: solution entry missing required 'name'")
        return None
    module = solution_module_name(slug, name)
    py_path = slug_dir / f"{module}.py"
    if not py_path.exists():
        _warn(
            f"{slug_dir}/meta.yaml: solution '{name}' expects file "
            f"{py_path.name} which does not exist"
        )
        return None
    info = inspect_module(py_path)
    if info is None:
        _warn(f"no parseable module docstring in {py_path}")
        return None
    explanation = (entry.get("explanation") or "").rstrip("\n")
    complexity = (entry.get("complexity") or "").rstrip("\n")
    missing = [
        f
        for f, v in [("explanation", explanation), ("complexity", complexity)]
        if not v
    ]
    if missing:
        _warn(
            f"{slug_dir}/meta.yaml: solution '{name}' is missing "
            + ", ".join(missing)
        )

    return Variant(
        name=name,
        module=module,
        source_path=py_path,
        explanation=explanation,
        complexity=complexity,
        test_block=info.docstring.strip("\n"),
        first_code_line=info.first_code_line,
        public_symbols=info.public_symbols,
    )


def discover_problems(catalog_by_slug: dict[str, dict]) -> dict[str, Problem]:
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
            with meta_path.open(encoding="utf-8") as f:
                meta = yaml.safe_load(f) or {}

            solutions_meta = meta.get("solutions")
            if not solutions_meta:
                _warn(f"{meta_path} must define a non-empty 'solutions:' list")
                continue

            variants: list[Variant] = []
            for entry in solutions_meta:
                variant = _build_variant(slug, slug_dir, entry or {})
                if variant is not None:
                    variants.append(variant)
            if not variants:
                continue

            description_rst = (meta.get("description_rst") or "").rstrip("\n")
            short = truncate_description(description_rst)
            catalog_entry = catalog_by_slug.get(slug, {})
            name = catalog_entry.get("name") or slug.replace("-", " ").title()
            problem_url = meta.get("problem_url") or f"{LEETCODE_BASE}/{slug}/"

            out[slug] = Problem(
                slug=slug,
                name=name,
                difficulty=difficulty_label,
                patterns=list(meta.get("patterns") or []),
                description_rst=description_rst,
                short_description=short,
                problem_url=problem_url,
                in_catalog=slug in catalog_by_slug,
                variants=variants,
            )
    return out
