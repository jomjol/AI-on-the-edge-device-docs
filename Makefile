DOCSDIR = docs
VENVDIR = venv
VENV = $(VENVDIR)/bin/activate
MKDOCS_CONFIG ?= mkdocs.yml
BUILDDIR ?= site
TARGET = docs
VALE_CONFIG = .vale.ini

.PHONY: build install serve spelling vale-install 


# If requirements are updated, venv should be rebuilt and timestamped.
$(VENVDIR):
	@echo "... setting up virtualenv"
	python3 -m venv $(VENVDIR) || { echo "You must install python3-venv before you can build the documentation."; exit 1; }
	. $(VENV); pip install $(PIPOPTS) --require-virtualenv \
	    --upgrade -r requirements.txt \
            --log $(VENVDIR)/pip_install.log
	@test ! -f $(VENVDIR)/pip_list.txt || \
            mv $(VENVDIR)/pip_list.txt $(VENVDIR)/pip_list.txt.bak
	@. $(VENV); pip list --local --format=freeze > $(VENVDIR)/pip_list.txt
	@touch $(VENVDIR)

install: $(VENVDIR)

build: install
	. $(VENV); mkdocs build -f $(MKDOCS_CONFIG)

lint-md: pymarkdownlnt-install
	@. $(VENV); pymarkdownlnt --config .pymarkdown.json scan docs --recurse --exclude=./$(SPHINXDIR)/** $(SOURCEDIR)

lint-md-fix: pymarkdownlnt-install
	@. $(VENV); pymarkdownlnt fix --recurse $(DOCSDIR)

pymarkdownlnt-install:
	@. $(VENV); test -d $(VENVDIR)/lib/python*/site-packages/pymarkdown || pip install pymarkdownlnt

serve: install
	. $(VENV); mkdocs serve -f $(MKDOCS_CONFIG) --livereload

vale-install: install
	@. $(VENV);
	@. $(VENV); find $(VENVDIR)/lib/python*/site-packages/vale/vale_bin -size 195c -exec vale --version \;

spelling: vale-install
	@echo "Running Vale against $(TARGET). To change target set TARGET= with make command"
	@. $(VENV); vale --config="$(VALE_CONFIG)" --glob='*.{md,rst}' $(TARGET)
