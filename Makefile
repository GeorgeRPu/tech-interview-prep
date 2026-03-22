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
update-lines:
	@echo "[update-lines] Adjusting literalinclude directives in solution docstrings"
	@$(PYTHON) scripts/update_literalinclude.py

fetch-descriptions:
	@echo "[fetch-descriptions] Fetching LeetCode problem descriptions"
	@$(PYTHON) scripts/fetch_leetcode_description.py $(FILES)

.PHONY: fetch-descriptions

api-doc:
	sphinx-apidoc -T -o generated solutions/easy
	sphinx-apidoc -T -o generated solutions/medium
	sphinx-apidoc -T -o generated solutions/hard
	@$(PYTHON) scripts/prune_module_suffix.py

generate-patterns:
	@echo "[generate-patterns] Generating patterns.rst"
	@$(PYTHON) scripts/generate_patterns_index.py

.PHONY: generate-patterns

generate-coverage:
	@echo "[generate-coverage] Generating coverage.rst"
	@$(PYTHON) scripts/generate_coverage.py

.PHONY: generate-coverage

generate-difficulty:
	@echo "[generate-difficulty] Generating difficulty index pages"
	@$(PYTHON) scripts/generate_difficulty_index.py

.PHONY: generate-difficulty

# Override the html target so we can ensure literalinclude line ranges are up to date before building.
html: update-lines api-doc generate-patterns generate-coverage generate-difficulty
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Custom clean: also wipe generated/ RST files
.PHONY: clean
clean:
	@echo "[clean] Removing build/, generated/*.rst, patterns.rst, and coverage.rst"
	@rm -rf "$(BUILDDIR)"
	@find generated -type f -name '*.rst' -maxdepth 1 -delete 2>/dev/null || true
	@rm -f patterns.rst coverage.rst easy_index.rst medium_index.rst hard_index.rst
	@echo "[clean] Done."

.PHONY: format fmt
format fmt:
	@echo "[black] Formatting Python sources"
	@$(PYTHON) -m black solutions scripts conf.py

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
