# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = build
PYTHON        ?= python3

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
.PHONY: help Makefile

# Run the unified docs generator: emits generated/*.rst, coverage.rst,
# problem_index.rst, and the per-difficulty index pages from the structured
# source under problems/.
generate:
	@echo "[generate] Generating RST from problems/ source"
	@$(PYTHON) scripts/generate_docs.py

.PHONY: generate

html: generate
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

doctest: generate
	@$(SPHINXBUILD) -M doctest "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: clean
clean:
	@echo "[clean] Removing build/ and all generated rst files"
	@rm -rf "$(BUILDDIR)"
	@find generated -type f -name '*.rst' -maxdepth 1 -delete 2>/dev/null || true
	@rm -f patterns.rst pattern_index.rst coverage.rst problem_index.rst \
	       easy_index.rst medium_index.rst hard_index.rst
	@echo "[clean] Done."

.PHONY: lint
lint:
	@echo "[flake8] Linting Python sources"
	@$(PYTHON) -m flake8 problems scripts

.PHONY: format fmt
format fmt:
	@echo "[black] Formatting Python sources"
	@$(PYTHON) -m black problems scripts conf.py

.PHONY: all
all: clean format lint html

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
