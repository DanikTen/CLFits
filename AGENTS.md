***

## 📜 Master Prompt for `CLFits` 

**Objective:** Create `CLFits`, a professional-grade command-line FITS header editor. The project must be robust, maintainable, and easily distributable. The agent will adhere to the following specifications precisely.

### 1. Project Setup & Configuration

* **Structure:** Standard `src/` layout. Source in `src/clfits/`, tests in `tests/`, docs in `docs/`, CI in `.github/workflows/`.
* **Configuration File:** A single `pyproject.toml` will manage the entire project: metadata, dependencies, and tool settings (`ruff`, `mypy`, `pytest`, `bump-my-version`).
* **License:** Generate an **MIT License** file.
* **Changelog:** Create a `CHANGELOG.md` in the [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) format.

### 2. Dependencies & Installation

* **Core:** `astropy` (logic), `typer` (CLI), `rich` (for colored output).
* **Development Dependencies:** Do **not** create `requirements-dev.txt`. Instead, create a `[project.optional-dependencies]` group named `dev` in `pyproject.toml`. This group must include:
    * `pytest` & `pytest-doctest`
    * `ruff`
    * `mypy`
    * `bump-my-version`
    * `sphinx`
    * `furo` (for the docs theme)
    * `pre-commit`

### 3. Automation & CI/CD

* **Version Bumping:**
    * Use **`bump-my-version`**. The single source of truth for the version number will be in `pyproject.toml` (`[project] version`).
    * Configure `bump-my-version` to automatically update the version in `src/clfits/__init__.py` and `docs/conf.py`.
* **Pre-commit Hooks:**
    * Set up a `.pre-commit-config.yaml`.
    * Include hooks for `ruff format`, `ruff check --fix`, and `mypy`. 
    * Adjust the line length limit to 120 characters.
    * Document that `make install-dev` will set up pre-commit hooks (do not auto-install).
* **GitHub Actions:**
    * **`ci.yml`:** On push/PR to `main`, run linting, formatting checks, type checks, the full `pytest` suite, and enforce **90% test coverage**. Run on Linux, macOS, and Windows.
    * **`release.yml`:** On a new version tag (e.g., `v0.1.0`), build the package and publish to PyPI. Auto-generate GitHub release notes from the `CHANGELOG.md` for the current version.

### 4. CLI & Features (v1)

* **Scope:** Header editing ONLY. No FITS data manipulation or GUI.
* **Commands:**
    * `clfits view <filename>`: Prints the full header.
    * `clfits get <filename> <KEYWORD>`: Gets the value of a single keyword.
    * `clfits set <filename> <KEYWORD> <VALUE> [--comment="..."]`: Sets a keyword's value and an optional comment.
    * `clfits del <filename> <KEYWORD>`: Deletes a keyword.
    * (Command names may be adjusted for clarity and ergonomics.)
* **Error Handling:** Use colored output (green=success, yellow=warning, red=error) via `rich` or Typer's support. Use standard non-zero exit codes on failure.

### 5. Testing

* **Test Coverage:** Enforce **90% coverage** in CI.
* **Sample Data:** Provide a script in `tests/` to generate a minimal FITS file (e.g., 1x1 pixel image with a simple header) for tests. Do not check in large static files.

### 6. Distribution

* **PyPI Metadata:**
    * **Author:** "Amber Malpas (AmberLee2427)"
    * **Project URL:** https://github.com/AmberLee2427/CLFits.git
    * **Classifiers:** Python 3.9+, MIT License, Science/Research
* **Platform Support:** Must run on Linux, macOS, and Windows. CI must test all three.

### 7. Documentation

* **README:** The `README.md` must contain: a project summary, PyPI/CI status badges, installation instructions, and a "Quick Start" usage example.
* **Docstrings:** All code must use `numpydoc` style.
* **Read the Docs:**
    * Use **Sphinx** with the **`furo`** theme.
    * Create a `.readthedocs.yaml` file to configure the build.
    * Documentation must contain an **API reference** (public API only, no internals) and a comprehensive **Tutorial** page focused on fixing a common header keyword (e.g., correcting the `OBJECT` keyword).
    * Include a page on shell completion for Bash, Zsh, etc., using Typer's support.

### 8. Developer Experience

* **Makefile:** Create a simple `Makefile` with targets for common tasks:
    * `make install-dev`: Installs the package with dev dependencies and sets up pre-commit.
    * `make test`: Runs pytest.
    * `make lint`: Runs ruff and mypy.
    * `make docs`: Builds the documentation locally.
    * `make release-patch`: Bumps the patch version using `bump-my-version`.
* **Code Style:** Use only `ruff format` (no `black`, no `isort`).
* **Contributing Guide:** Add a `CONTRIBUTING.md` with basic instructions: Fork, branch, test, pass linting, submit PR.

### 9. Out of Scope (v1)

* Any form of GUI.
* Any FITS data manipulation (header only).
* Complex interactive modes (non-interactive, command-and-done only).
* Any features not explicitly listed above.

***
// Executive decisions and clarifications have been incorporated per user direction.