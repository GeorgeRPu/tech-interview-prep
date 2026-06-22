"""Render :class:`~discovery.Problem` objects into Sphinx RST pages.

Produces:
* the per-problem ``generated/<slug>.rst`` body (:func:`render_problem_rst`),
* the global ``coverage.rst`` (:func:`render_coverage_rst`),
* the global ``problem_index.rst`` (:func:`render_problem_index_rst`),
* the per-difficulty index bullets (:func:`render_difficulty_rst`).
"""

from __future__ import annotations

from discovery import LEETCODE_BASE, ROOT, Problem, Variant

# ---------------------------------------------------------------------------
# Rendering-only constants
# ---------------------------------------------------------------------------

DIFFICULTY_EMOJI: dict[str, str] = {
    "Easy": "🟢",
    "Medium": "🟡",
    "Hard": "🔴",
}

LIST_URLS: dict[str, str] = {
    "Blind 75": "https://neetcode.io/practice?tab=blind75",
    "Grind 75": "https://www.techinterviewhandbook.org/grind75",
    "Grind 169": "https://www.techinterviewhandbook.org/grind75?hours=40&grouping=topics",
    "NeetCode 150": "https://neetcode.io/practice?tab=neetcode150",
    "Amazon Top 50": "https://leetcode.com/problem-list/top-amazon-questions/",
    "Google Top 50": "https://leetcode.com/problem-list/top-google-questions/",
}

LIST_DISPLAY = {
    "blind75": "Blind 75",
    "grind75": "Grind 75",
    "grind169": "Grind 169",
    "nc150": "NeetCode 150",
    "amazon50": "Amazon Top 50",
    "google50": "Google Top 50",
}

# Display order for the "Lists" column in problem_index.rst.
LIST_DISPLAY_ORDER = ("blind75", "grind75", "grind169", "nc150", "amazon50", "google50")


# ---------------------------------------------------------------------------
# Small label / progress helpers
# ---------------------------------------------------------------------------


def progress_bar(covered: int, total: int, width: int = 20) -> str:
    filled = round(width * covered / total) if total else 0
    pct = f"{100 * covered // total}%" if total else "0%"
    return "■" * filled + "□" * (width - filled) + f" {pct}"


def lists_label(list_keys: list[str]) -> str:
    """Render the comma-joined list-membership label in canonical order."""
    keyset = set(list_keys)
    return ", ".join(LIST_DISPLAY[k] for k in LIST_DISPLAY_ORDER if k in keyset)


def list_link(display_name: str) -> str:
    url = LIST_URLS.get(display_name)
    return f"`{display_name} <{url}>`__" if url else display_name


# ---------------------------------------------------------------------------
# Per-problem RST
# ---------------------------------------------------------------------------


def _section(header: str, body: str) -> str:
    return f"{header}\n{'-' * len(header)}\n{body}"


def _indent(text: str, prefix: str) -> str:
    """Indent every non-empty line of ``text`` by ``prefix``."""
    return "\n".join(prefix + line if line else line for line in text.splitlines())


def _autodoc_lines(v: Variant) -> list[str]:
    """Module-qualified autodoc directives for a variant's public symbols."""
    lines: list[str] = []
    for kind, name in v.public_symbols:
        qualified = f"{v.module}.{name}"
        if kind == "function":
            lines.append(f".. autofunction:: {qualified}")
        else:
            lines.append(f".. autoclass:: {qualified}")
            lines.append("   :members:")
            lines.append("   :show-inheritance:")
            lines.append("   :undoc-members:")
        lines.append("")
    return lines


def _literalinclude_lines(v: Variant) -> list[str]:
    rel_source = v.source_path.relative_to(ROOT).as_posix()
    return [
        "",
        f".. literalinclude:: ../{rel_source}",
        "    :language: python",
        f"    :lines: {v.first_code_line}-",
    ]


def _render_variant_tab_body(v: Variant) -> str:
    """Inner content of a single ``.. tab-item::`` block (before indentation)."""
    lines: list[str] = []
    if v.explanation:
        lines.append("**Explanation**")
        lines.append("")
        lines.append(v.explanation)
        lines.append("")
    lines.append("**Code**")
    lines.extend(_literalinclude_lines(v))
    lines.append("")
    if v.test_block:
        lines.append("**Test**")
        lines.append("")
        lines.append(v.test_block)
        lines.append("")
    if v.complexity:
        lines.append("**Complexity**")
        lines.append("")
        lines.append(v.complexity)
        lines.append("")
    lines.extend(_autodoc_lines(v))
    return "\n".join(lines).rstrip()


def _render_multi_variant_body(variants: list[Variant]) -> list[str]:
    chunks: list[str] = [_section("Approaches", "")]
    chunks.append(".. tab-set::")
    chunks.append("")
    for v in variants:
        chunks.append(f"    .. tab-item:: {v.name}")
        chunks.append("")
        body = _render_variant_tab_body(v)
        chunks.append(_indent(body, "        "))
        chunks.append("")
    return chunks


def render_problem_rst(p: Problem) -> str:
    title = p.name
    chunks: list[str] = [
        ":orphan:",
        "",
        title,
        "=" * len(title),
        "",
        # Disable syntax highlighting for the Problem section: the ``::``
        # literal blocks there hold sample Input/Output data, not code.
        # ``.. literalinclude::`` below carries its own :language: option so
        # the Code section stays Python-highlighted regardless.
        ".. highlight:: none",
        "",
    ]
    chunks.append(_section("Problem", f"{p.problem_url}\n\n{p.description_rst}"))
    chunks.append("")
    chunks.append(".. highlight:: python")
    chunks.append("")
    chunks.append(_section("Pattern", ", ".join(p.patterns)))
    chunks.append("")
    chunks += _render_multi_variant_body(p.variants)
    return "\n".join(chunks).rstrip() + "\n"


# ---------------------------------------------------------------------------
# coverage.rst + problem_index.rst
# ---------------------------------------------------------------------------


def render_coverage_rst(catalog: list[dict], covered_slugs: set[str]) -> str:
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
    for key in LIST_DISPLAY_ORDER:
        rows = [r for r in catalog if key in (r.get("lists") or [])]
        total = len(rows)
        covered = sum(1 for r in rows if not r.get("premium") and r["slug"] in covered_slugs)
        lines.append(f"   * - {list_link(LIST_DISPLAY[key])}")
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
        lists_cell = lists_label(row.get("lists") or [])
        if slug in problems:
            p = problems[slug]
            problem_cell = f":doc:`{name} <generated/{p.slug}>`"
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


def render_difficulty_rst(
    difficulty_label: str,
    problems: dict[str, Problem],
    catalog_by_slug: dict[str, dict],
) -> str:
    title = difficulty_label
    lines = [
        title,
        "=" * len(title),
        "",
        ".. list-table::",
        "   :header-rows: 1",
        "   :class: sphinx-datatable",
        "   :widths: auto",
        "",
        "   * - Problem",
        "     - Pattern",
        "     - Lists",
        "     - Description",
    ]
    matches = sorted(
        (p for p in problems.values() if p.difficulty == difficulty_label),
        key=lambda p: p.name,
    )
    for p in matches:
        pattern_cell = ", ".join(p.patterns) if p.patterns else ""
        cat_entry = catalog_by_slug.get(p.slug, {})
        lists_cell = lists_label(cat_entry.get("lists") or [])
        desc_cell = p.short_description or ""
        lines.append(f"   * - :doc:`{p.name} <generated/{p.slug}>`")
        lines.append(f"     - {pattern_cell}")
        lines.append(f"     - {lists_cell}")
        lines.append(f"     - {desc_cell}")
    lines.append("")
    return "\n".join(lines) + "\n"
