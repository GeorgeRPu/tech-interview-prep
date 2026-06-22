#!/usr/bin/env python3
"""Scaffold a new problem directory from a LeetCode slug.

Usage::

    uv run python scripts/scaffold_problem.py two-sum
    uv run python scripts/scaffold_problem.py climbing-stairs -d easy
"""

from __future__ import annotations

import argparse
import re
import sys
import textwrap
from pathlib import Path

import pypandoc
import requests
import yaml

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "problems" / "catalog.yaml"

GRAPHQL_URL = "https://leetcode.com/graphql"
QUERY = """\
query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    title
    titleSlug
    content
    difficulty
    topicTags { name }
    codeSnippets { langSlug code }
  }
}"""

# ---------------------------------------------------------------------------
# Standard helper classes (match project convention)
# ---------------------------------------------------------------------------

TREE_NODE = '''\
class TreeNode:
    """Node in a binary tree."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, vals: List[int | None]) -> TreeNode | None:
        if not vals:
            return None
        root = TreeNode(vals[0])
        queue = [root]
        i = 1
        while i < len(vals):
            node = queue.pop(0)
            if i < len(vals) and vals[i] is not None:
                node.left = TreeNode(vals[i])
                queue.append(node.left)
            i += 1
            if i < len(vals) and vals[i] is not None:
                node.right = TreeNode(vals[i])
                queue.append(node.right)
            i += 1
        return root'''

LIST_NODE = '''\
class ListNode:
    """Node in a linked list."""

    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next

    def to_list(self) -> List[int]:
        result = []
        node = self
        while node is not None:
            result.append(node.val)
            node = node.next
        return result

    @classmethod
    def from_list(cls, vals: List[int]) -> ListNode | None:
        head: ListNode | None = None
        tail: ListNode | None = None
        for v in vals:
            node = ListNode(v)
            if head is None:
                head = tail = node
            else:
                tail.next = node
                tail = node
        return head'''


# ---------------------------------------------------------------------------
# YAML helpers — force literal-block style for multiline strings
# ---------------------------------------------------------------------------

class _Literal(str):
    pass


def _literal_representer(dumper, data):
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")


yaml.add_representer(_Literal, _literal_representer)


# ---------------------------------------------------------------------------
# LeetCode API
# ---------------------------------------------------------------------------

def fetch_problem(slug: str) -> dict:
    resp = requests.post(
        GRAPHQL_URL,
        json={"query": QUERY, "variables": {"titleSlug": slug}},
        headers={"Content-Type": "application/json"},
        timeout=15,
    )
    resp.raise_for_status()
    question = resp.json().get("data", {}).get("question")
    if question is None:
        sys.exit(f"Error: problem '{slug}' not found on LeetCode.")
    return question


# ---------------------------------------------------------------------------
# Converters
# ---------------------------------------------------------------------------

def html_to_rst(html: str) -> str:
    rst = pypandoc.convert_text(html, "rst", format="html")
    lines = [line.rstrip() for line in rst.splitlines()]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip()


def slug_to_snake(slug: str) -> str:
    return slug.replace("-", "_")


def _parse_commented_class(comment_lines: list[str]) -> str | None:
    """Uncomment a class definition from LeetCode's header comments."""
    uncommented = []
    for line in comment_lines:
        if line.startswith("# "):
            uncommented.append(line[2:])
        elif line == "#":
            uncommented.append("")
        else:
            uncommented.append(line)
    text = "\n".join(uncommented)
    match = re.search(r"(class \w+.*)", text, re.DOTALL)
    return match.group(1).rstrip() if match else None


def extract_code(snippet: str) -> tuple[str, str, list[str], set[str]]:
    """Parse LeetCode's Python3 snippet.

    Returns ``(code_body, main_name, helpers, typing_imports)``.
    """
    lines = snippet.splitlines()

    # Separate leading comment header from code
    comment_lines: list[str] = []
    code_start = 0
    for i, line in enumerate(lines):
        if line.startswith("#"):
            comment_lines.append(line)
        else:
            code_start = i
            break

    code_str = "\n".join(lines[code_start:]).strip()

    # Detect typing imports needed
    typing_imports: set[str] = set()
    for tok in ("List", "Optional", "Dict", "Tuple", "Set"):
        if f"{tok}[" in code_str:
            typing_imports.add(tok)

    # Determine which helpers to include
    helpers: list[str] = []
    needs_tree = "TreeNode" in code_str
    needs_list = "ListNode" in code_str
    needs_node = "Node" in code_str and not needs_tree and not needs_list

    if needs_tree:
        helpers.append(TREE_NODE)
        typing_imports.add("List")
    if needs_list:
        helpers.append(LIST_NODE)
        typing_imports.add("List")
    if needs_node and comment_lines:
        parsed = _parse_commented_class(comment_lines)
        if parsed:
            helpers.append(parsed)

    # Process main code
    if code_str.startswith("class Solution"):
        # Function-based problem: unwrap Solution class
        _, _, after = code_str.partition("\n")
        body = textwrap.dedent(after)
        body = re.sub(r"\(self, ", "(", body)
        body = re.sub(r"\(self\)", "()", body)
        match = re.search(r"def (\w+)\(", body)
        main_name = match.group(1) if match else "solve"
        return body.strip(), main_name, helpers, typing_imports

    # Data-structure problem: keep class, strip trailing usage comments
    stripped_lines = code_str.splitlines()
    while stripped_lines and stripped_lines[-1].lstrip().startswith("#"):
        stripped_lines.pop()
    while stripped_lines and stripped_lines[-1].strip() == "":
        stripped_lines.pop()
    code_str = "\n".join(stripped_lines)

    match = re.search(r"class (\w+)", code_str)
    main_name = match.group(1) if match else "Solution"
    return code_str, main_name, helpers, typing_imports


def _solution_module_name(slug: str, approach: str) -> str:
    prefix = slug.replace("-", "_")
    if prefix and prefix[0].isdigit():
        prefix = "p_" + prefix
    solution_part = re.sub(r"[^a-z0-9_]", "", approach.lower().replace(" ", "_").replace("-", "_"))
    return f"{prefix}__{solution_part}"


def build_py_file(
    slug: str,
    code_body: str,
    main_name: str,
    helpers: list[str],
    typing_imports: set[str],
    approach: str = "TODO",
) -> str:
    module = _solution_module_name(slug, approach)
    parts: list[str] = []

    # Docstring with placeholder doctest
    parts.append(
        f'r"""\n>>> from {module} import {main_name}\n>>> # TODO: add doctests\n"""'
    )

    # from __future__ import annotations (needed for forward refs in helpers)
    if helpers:
        parts.append("\nfrom __future__ import annotations")

    # Typing imports
    if typing_imports:
        parts.append(f"\nfrom typing import {', '.join(sorted(typing_imports))}")

    # Helper classes
    for h in helpers:
        parts.append(f"\n\n{h}")

    # Main code
    parts.append(f"\n\n{code_body}\n")

    return "\n".join(parts)


def build_meta(
    slug: str, patterns: list[str], description_rst: str, approach: str,
) -> dict:
    return {
        "slug": slug,
        "patterns": patterns,
        "description_rst": _Literal(description_rst + "\n"),
        "solutions": [
            {
                "name": approach,
                "explanation": _Literal("TODO\n"),
                "complexity": _Literal("TODO\n"),
            }
        ],
    }


# ---------------------------------------------------------------------------
# Catalog
# ---------------------------------------------------------------------------

def update_catalog(slug: str, title: str, difficulty: str) -> bool:
    """Add to catalog.yaml if absent. Returns True when a new entry is added."""
    with open(CATALOG) as f:
        catalog = yaml.safe_load(f) or []

    for entry in catalog:
        if entry.get("slug") == slug:
            if "difficulty" not in entry:
                entry["difficulty"] = difficulty
                with open(CATALOG, "w") as f:
                    yaml.dump(
                        catalog, f,
                        default_flow_style=False,
                        sort_keys=False,
                        allow_unicode=True,
                    )
            return False

    catalog.append(
        {
            "name": title,
            "slug": slug,
            "premium": False,
            "lists": [],
            "difficulty": difficulty,
        }
    )
    with open(CATALOG, "w") as f:
        yaml.dump(
            catalog, f,
            default_flow_style=False,
            sort_keys=False,
            allow_unicode=True,
        )
    return True


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Scaffold a new problem from a LeetCode slug.",
    )
    parser.add_argument("slug", help="LeetCode problem slug (e.g. two-sum)")
    parser.add_argument(
        "-d",
        "--difficulty",
        choices=["easy", "medium", "hard"],
        help="Override difficulty (auto-detected from LeetCode if omitted)",
    )
    parser.add_argument(
        "-a",
        "--approach",
        default="TODO",
        help="Solution approach name (e.g. 'Two Pointers', 'BFS')",
    )
    args = parser.parse_args()
    slug: str = args.slug

    print(f"Fetching '{slug}' from LeetCode...")
    q = fetch_problem(slug)

    title: str = q["title"]
    difficulty = (args.difficulty or q["difficulty"].lower()).capitalize()
    patterns = [t["name"] for t in q.get("topicTags", [])]

    snippets = q.get("codeSnippets") or []
    py_code = next(
        (s["code"] for s in snippets if s["langSlug"] == "python3"), None
    )
    if py_code is None:
        sys.exit("Error: no Python3 code snippet available.")

    print(f"  {title} ({difficulty})")
    print(f"  Patterns: {', '.join(patterns) or 'none'}")

    # Convert description (premium problems may have no content)
    html = q.get("content") or ""
    desc_rst = html_to_rst(html) if html else "TODO: add problem description"

    # Parse code snippet
    code_body, main_name, helpers, typing_imports = extract_code(py_code)

    # Create directory
    problem_dir = ROOT / "problems" / difficulty.lower() / slug
    if problem_dir.exists():
        sys.exit(f"Error: {problem_dir.relative_to(ROOT)} already exists.")
    problem_dir.mkdir(parents=True)

    # Write meta.yaml
    meta = build_meta(slug, patterns, desc_rst, args.approach)
    meta_path = problem_dir / "meta.yaml"
    meta_path.write_text(
        yaml.dump(
            meta,
            default_flow_style=False,
            sort_keys=False,
            allow_unicode=True,
            width=999,
        )
    )
    print(f"  Created {meta_path.relative_to(ROOT)}")

    # Write stub .py
    module = _solution_module_name(slug, args.approach)
    py_path = problem_dir / f"{module}.py"
    py_path.write_text(
        build_py_file(slug, code_body, main_name, helpers, typing_imports, args.approach)
    )
    print(f"  Created {py_path.relative_to(ROOT)}")

    # Update catalog
    added = update_catalog(slug, title, difficulty)
    print(f"  {'Added to' if added else 'Already in'} catalog.yaml")

    rel_py = py_path.relative_to(ROOT)
    rel_meta = meta_path.relative_to(ROOT)
    print("\nNext steps:")
    print(f"  1. Implement the solution in {rel_py}")
    print("  2. Add doctests to the module docstring")
    print(f"  3. Fill in explanation/complexity in {rel_meta}")
    print("  4. Run: uv run make doctest")


if __name__ == "__main__":
    main()
