# 🗺️ Roadmap

## Features

- [x] **Solution pattern index** — Group existing solutions by technique (two pointers, sliding window, BFS/DFS, backtracking, dynamic programming) so problems can be studied by concept rather than by name.
- [x] **Coverage tracker** — Pages showing which problems from these canonical prep lists are covered and which are still missing, providing a clear study roadmap.
  - [x] [Blind 75](https://leetcode.com/problem-list/oizxjoit/)
  - [x] [Grind 75](https://www.techinterviewhandbook.org/grind75/)
  - [x] [Grind 169](https://www.techinterviewhandbook.org/grind75/?weeks=28&hours=6)
  - [x] [NeetCode 150](https://neetcode.io/practice/practice/neetcode150)
  - [ ] [Amazon Top 50](https://leetcode.com/problem-list/7p5x763/)
  - [ ] [Google Top 50](https://leetcode.com/problem-list/7p55wqm/)
  - [ ] Meta Top 50
- [ ] **Big O annotations** — Add time and space complexity to each solution's docstring and surface it in the documentation.
- [ ] **CONTRIBUTING.md** — Document the expected file structure, doctest format, and solution explanation style to guide external contributors.
- [ ] **Interactive code snippets** — Embed runnable code snippets in the documentation allowing users to experiment with solutions directly on the site.
- [ ] **Pattern overview pages** — Create dedicated pages for each solution pattern that explain the concept, common pitfalls, and link to all relevant problems in the repo that use that pattern.

## Fixes/Architectural Improvments

- [ ] **Generate solutions from JSON** — Rearchitect the build process to automatically generate solution files from a structured JSON file.
- [ ] **Stop showing all solutions in the sidebar** — Restructure the Sphinx sidebar to only show problem categories or patterns, not every individual solution, to reduce clutter.
- [ ] **Refine patterns list** — Refine patterns instead of just using the Topics tags from LeetCode.
- [ ] **Put entries per page on same line as dropdown* for Patterns Index page* — The current layout has "entries per page" on a separate line from the dropdown.
