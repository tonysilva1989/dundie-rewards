# Makefile
.PHONY: install virtualenv ipython clean


install:
	@echo "Installing for dev environment"
	@.venv/bin/python -m pip install -e '.[dev]'


virtualenv:
	@.venv/bin/python -m pip -m venv .venv

# TODO: fix ptw arguments
watch:
	@.venv/bin/ptw -- -vv -s tests/

# TODO: Check --profile=NNNNN --logfile=/tmp/... argument
ipython:
	@.venv/bin/ipython

fmt:
	@.venv/bin/black
	# black --check --diff folder1 folder2 ...

test:
	@.venv/bin/pytest -vv -s tests/

integrationtest:
	@.venv/bin/pytest -s -m "integration"

testci:
	@pytest -vv tests/ --junitxml=ouput.xml

clean:            ## Clean unused files.
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '__pycache__' -exec rm -rf {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	@rm -rf .cache
	@rm -rf .pytest_cache
	@rm -rf .mypy_cache
	@rm -rf build
	@rm -rf dist
	@rm -rf *.egg-info
	@rm -rf htmlcov
	@rm -rf .tox/
	@rm -rf docs/_build