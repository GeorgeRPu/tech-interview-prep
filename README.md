# Tech Interview Prep

A growing collection of LeetCode solutions with explanations, built into a searchable documentation site with Sphinx and deployed to GitHub Pages.

🌐 **Live site:** https://georgerpu.github.io/tech-interview-prep/

Covers **Easy**, **Medium**, and **Hard** problems — from Two Sum to LRU Cache to Merge K Sorted Lists.

## 📦 Installation

Install [`uv`](https://docs.astral.sh/uv/getting-started/installation/) if you don't have it, then install project dependencies:

```bash
uv sync
```

## 📖 Building the Documentation

```bash
uv run make clean
uv run make format
uv run make html
```

Open `build/html/index.html` in your browser to preview locally.

The build also runs doctests (`make doctest`) so every solution is verified against its embedded examples. ✅

## 🧪 Testing GitHub Actions with `act`

[`act`](https://github.com/nektos/act) lets you run the deploy workflow locally without pushing to GitHub.

`act` requires [Docker](https://docs.docker.com/get-started/get-docker/) to be installed and running.

Install [`act`](https://nektosact.com/installation/index.html) if you don't have it, then run the deploy workflow:

```bash
act push
```

The workflow uses `if: ${{ !env.ACT }}` guards on the Pages-specific steps (configure-pages, upload-artifact, deploy-pages), so those are automatically skipped when running under `act`. The build and doctest steps still run in full, making `act` useful for catching CI failures before pushing.

**Run with a specific Docker image** (faster, smaller):

```bash
act push -P ubuntu-latest=catthehacker/ubuntu:act-latest
```

## 🗂️ Package Structure

```
tech-interview-prep/
├── solutions/              # Python solution files
│   ├── easy/               # Easy difficulty solutions
│   ├── medium/             # Medium difficulty solutions
│   └── hard/               # Hard difficulty solutions
├── generated/              # Auto-generated RST files (from sphinx-apidoc)
├── scripts/                # Build-time utility scripts
│   ├── fetch_leetcode_description.py
│   ├── generate_patterns_index.py
│   ├── update_literalinclude.py
│   └── prune_module_suffix.py
├── _static/                # Static assets (CSS, JS)
├── _templates/             # Sphinx HTML templates
├── build/                  # Build output (gitignored)
├── conf.py                 # Sphinx configuration
├── index.rst               # Documentation homepage
├── patterns.rst            # Auto-generated technique index
├── Makefile                # Build automation
└── pyproject.toml          # Project metadata and dependencies
```

Each solution in `solutions/` is a standalone `.py` file containing the problem description, implementation, and embedded doctests in its docstring. The `generated/` directory is populated automatically during the build by `sphinx-apidoc` and should not be edited by hand.

## 🗺️ Roadmap

- [x] **Solution pattern index** — Group existing solutions by technique (two pointers, sliding window, BFS/DFS, backtracking, dynamic programming) so problems can be studied by concept rather than by name.
- [ ] **Blind 75 / NeetCode 150 coverage tracker** — A page showing which problems from these canonical prep lists are covered and which are still missing, providing a clear study roadmap.
- [ ] **Big O annotations** — Add time and space complexity to each solution's docstring and surface it in the documentation.
- [ ] **CONTRIBUTING.md** — Document the expected file structure, doctest format, and solution explanation style to guide external contributors.
- [ ] **Generate solutions from JSON** — Rearchitect the build process to automatically generate solution files from a structured JSON file.
