# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.4.0] - YYYY-MM-DD

### Added

- Multi-HDU support: All commands now accept an `--hdu` option to target specific FITS extensions by index or name.
- Comprehensive user documentation, including a new tutorial and shell completion guides.

### Changed

- Test coverage increased to 95% with new edge case tests.

## [0.3.0] - 2024-07-30

### Added

- `search` command to filter header keywords by pattern.

## [0.2.0] - 2024-07-29

### Added

- `export` command to save the FITS header to JSON, YAML, or CSV.

## [0.1.4] - 2024-07-29

### Fixed

- Resolved persistent test failures by refactoring CLI output to use `typer.echo`.
- Corrected `bump-my-version` configuration to enable automated releases.
- Fixed Read the Docs build failures by specifying documentation dependencies.

## [0.1.0] - 2024-07-29

### Added

- Initial release of `clfits`.
- `view` command to display the FITS header.
- `get` command to retrieve a header keyword value.
- `set` command to add or modify a header keyword.
- `del` command to remove a header keyword.
- Project setup with `pyproject.toml`, `ruff`, `mypy`, and `pytest`.
- MIT License, `README.md`, and `CHANGELOG.md`.
- Pre-commit hooks for formatting and linting.
- GitHub Actions for CI and release.
- Sphinx documentation with Furo theme.
- Makefile for common development tasks. 