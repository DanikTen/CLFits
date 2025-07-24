.PHONY: help install-dev test lint docs release-patch

help:
	@echo "Commands:"
	@echo "  install-dev    : Installs the package with dev dependencies and pre-commit hooks."
	@echo "  test           : Runs the pytest suite."
	@echo "  lint           : Runs ruff and mypy checks."
	@echo "  docs           : Builds the documentation locally."
	@echo "  release-patch  : Bumps the patch version using bump-my-version."

install-dev:
	pip install -e .[dev]
	pre-commit install

test:
	pytest --cov=clfits --cov-report=term-missing --cov-fail-under=90

lint:
	ruff format .
	ruff check . --fix
	mypy src/

docs:
	sphinx-build -b html docs/source docs/build/html

release-patch:
	bump-my-version bump patch 