# 🗺️ Roadmap

## Features

- [x] **Solution pattern index** — Group existing solutions by technique (two pointers, sliding window, BFS/DFS, backtracking, dynamic programming) so problems can be studied by concept rather than by name.
- [x] **Coverage tracker** — Pages showing which problems from these canonical prep lists are covered and which are still missing, providing a clear study roadmap.
  - [x] [Blind 75](https://leetcode.com/problem-list/oizxjoit/)
  - [x] [Grind 75](https://www.techinterviewhandbook.org/grind75/)
  - [x] [Grind 169](https://www.techinterviewhandbook.org/grind75/?weeks=28&hours=6)
  - [x] [NeetCode 150](https://neetcode.io/practice/practice/neetcode150)
  - [x] [Amazon Top 50](https://leetcode.com/problem-list/7p5x763/)
  - [x] [Google Top 50](https://leetcode.com/problem-list/7p55wqm/)
- [x] **Big O annotations** — Add time and space complexity to each solution's docstring and surface it in the documentation.
- [ ] **CONTRIBUTING.md** — Document the expected file structure, doctest format, and solution explanation style to guide external contributors.
- [x] **Interactive code snippets** — Embed runnable code snippets in the documentation allowing users to experiment with solutions directly on the site.
- [x] **Unified search** — Unify the Problem Index and Pattern Index searches.
- [x] **Problem list links** — Add links to each canonical problem list from the coverage tracker.

## Architectural Improvements

- [x] **Generate solutions from structured source** — Rearchitect the build to read a structured source (clean `.py` + `meta.yaml` per problem under `problems/`, plus `problems/catalog.yaml` replacing `problems.csv`) and produce every Sphinx page from it without mutating the source. `scripts/generate_docs.py` emits `generated/*.rst`, `coverage.rst`, `problem_index.rst`, and the per-difficulty indexes; `scripts/migrate_solution.py` converts legacy-format files (still used for finishing existing `solutions/<diff>/_*.py` drafts).
- [ ] **Multiple solutions per problem** — Support more than one solution for a given problem so alternative approaches (e.g., brute-force vs. optimal, iterative vs. recursive) can be compared side by side in the documentation.

## Fixes

- [x] **Stop showing all solutions in the sidebar** — Restructure the Sphinx sidebar to only show problem categories or patterns, not every individual solution, to reduce clutter.
- [x] **Put entries per page on same line as dropdown for Patterns Index page** — The current layout has "entries per page" on a separate line from the dropdown.
- [x] **Fix spacing after Code block** — The spacing after code blocks is inconsistent with the rest of the sections.
