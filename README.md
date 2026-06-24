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
uv run make all
```

This runs `clean`, `format`, `lint`, `doctest`, and `html` in sequence. You can also run each step individually:

```bash
uv run make clean
uv run make format
uv run make lint
uv run make html
```

Open `build/html/index.html` in your browser to preview locally.

## Testing

### ✅ Running Doctests

Every solution file includes embedded doctests in its docstring. Run them with:

```bash
uv run make doctest
```

The CI pipeline also runs doctests before building the site, so every solution is verified against its embedded examples.

### 🔍 Linting

Run flake8 to check for style and correctness issues:

```bash
uv run make lint
```

The CI pipeline runs linting before the build. Configuration is in [`.flake8`](.flake8).

### 🧪 Testing GitHub Actions with `act`

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
├── problems/               # Structured problem source
│   ├── catalog.yaml        # Problem titles and ordering
│   ├── easy/               # Easy difficulty problems
│   ├── medium/             # Medium difficulty problems
│   └── hard/               # Hard difficulty problems
├── generated/              # Auto-generated per-problem RST (from generate_docs.py)
├── scripts/                # Build-time utility scripts
│   ├── generate_docs.py    # Entry point: discover problems, render RST
│   ├── discovery.py        # Scan problems/ into in-memory models
│   ├── rendering.py        # Turn models into RST pages
│   └── scaffold_problem.py # Scaffold a new problem directory
├── _static/                # Static assets (CSS, JS)
├── _templates/             # Sphinx HTML templates
├── build/                  # Build output (gitignored)
├── conf.py                 # Sphinx configuration
├── index.rst               # Documentation homepage
├── Makefile                # Build automation
└── pyproject.toml          # Project metadata and dependencies
```

Each problem lives under `problems/<difficulty>/<slug>/` with a `meta.yaml` and one `.py` file per approach. Running `make generate` (invoked automatically by `make html` and `make doctest`) scans that source and writes the per-problem pages into `generated/`, plus `coverage.rst`, `problem_index.rst`, and the per-difficulty index pages. None of those generated files should be edited by hand.

## 🧩 Multiple solutions per problem

Problems migrated to the new structured source under `problems/<difficulty>/<slug>/` can document several approaches side by side, rendered as tabs on the problem page.

The shape of a multi-solution problem on disk:

```
problems/easy/two-sum/
├── meta.yaml
├── two_sum__two_pointer.py
└── two_sum__hash_map.py
```

`meta.yaml` lists the approaches in display order:

```yaml
slug: two-sum
patterns: [Array, Hash Table]
description_rst: |
  ...
solutions:
  - name: Two Pointer
    explanation: |
      ...
    complexity: |
      ...
  - name: Hash Map
    explanation: |
      ...
    complexity: |
      ...
```

Each approach's `.py` filename is derived from `<slug-snake>__<name-snake>.py`, so `Two Pointer` under slug `two-sum` lives at `two_sum__two_pointer.py`. Each file owns its own doctests and imports itself by its module name (`>>> from two_sum__two_pointer import twoSum`). Single-approach problems use the same `solutions:` list with one entry — there is no separate single-solution schema.
