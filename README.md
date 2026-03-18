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

Install [`act`](https://nektosact.com/installation/index.html) if you don't have it, then run the deploy workflow:

```bash
act push
```

The workflow uses `if: ${{ !env.ACT }}` guards on the Pages-specific steps (configure-pages, upload-artifact, deploy-pages), so those are automatically skipped when running under `act`. The build and doctest steps still run in full, making `act` useful for catching CI failures before pushing.

**Run with a specific Docker image** (faster, smaller):

```bash
act push -P ubuntu-latest=catthehacker/ubuntu:act-latest
```

## Roadmap

- [ ] **Common patterns index** — Group existing solutions by technique (two pointers, sliding window, BFS/DFS, backtracking, dynamic programming) so problems can be studied by concept rather than by name.
- [ ] **Blind 75 / NeetCode 150 coverage tracker** — A page showing which problems from these canonical prep lists are covered and which are still missing, providing a clear study roadmap.
- [ ] **Big O annotations** — Add time and space complexity to each solution's docstring and surface it in the documentation.
- [ ] **CONTRIBUTING.md** — Document the expected file structure, doctest format, and solution explanation style to guide external contributors.
