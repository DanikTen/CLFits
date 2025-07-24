"""Main CLI for clfits."""

import sys
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console

from clfits import __version__
from clfits.io import read_header, write_header

app = typer.Typer(
    add_completion=False,
    rich_markup_mode="markdown",
    context_settings={"help_option_names": ["-h", "--help"]},
)

console = Console(stderr=True)


def version_callback(value: bool):
    """Print the version of the package and exit."""
    if value:
        print(f"clfits version: {__version__}")
        raise typer.Exit()


@app.command()
def view(
    fits_file: Path = typer.Argument(..., exists=True, dir_okay=False, readable=True),
) -> None:
    """View the header of a FITS file."""
    try:
        header = read_header(fits_file)
        console.print(repr(header))
    except (FileNotFoundError, OSError) as e:
        console.print(f"[bold red]{e}[/bold red]")
        raise typer.Exit(code=1)


@app.command()
def get(
    fits_file: Path = typer.Argument(..., exists=True, dir_okay=False, readable=True),
    keyword: str = typer.Argument(..., help="The header keyword to retrieve."),
) -> None:
    """Get the value of a specific header keyword."""
    try:
        header = read_header(fits_file)
        value = header.get(keyword)
        if value is None:
            console.print(f"[bold red]Error: Keyword '{keyword}' not found in '{fits_file}'.[/bold red]")
            raise typer.Exit(code=1)
        console.print(value)
    except (FileNotFoundError, OSError) as e:
        console.print(f"[bold red]{e}[/bold red]")
        raise typer.Exit(code=1)


@app.command()
def set(
    fits_file: Path = typer.Argument(..., exists=True, dir_okay=False, writable=True),
    keyword: str = typer.Argument(..., help="The header keyword to set."),
    value: str = typer.Argument(..., help="The value to set for the keyword."),
    comment: Optional[str] = typer.Option(None, "--comment", "-c", help="An optional comment for the keyword."),
) -> None:
    """Set a keyword's value, with an optional comment."""
    try:
        header = read_header(fits_file)
        header[keyword] = (value, comment) if comment else value
        write_header(fits_file, header)
        console.print(
            f"[bold green]Success: Set '{keyword}' to '{value}' in '{fits_file}'.[/bold green]"
        )
    except (FileNotFoundError, OSError) as e:
        console.print(f"[bold red]{e}[/bold red]")
        raise typer.Exit(code=1)


@app.command()
def delete(
    fits_file: Path = typer.Argument(..., exists=True, dir_okay=False, writable=True),
    keyword: str = typer.Argument(..., help="The header keyword to delete."),
) -> None:
    """Delete a keyword from the header."""
    try:
        header = read_header(fits_file)
        if keyword not in header:
            console.print(f"[bold yellow]Warning: Keyword '{keyword}' not found in '{fits_file}'.[/bold yellow]")
            raise typer.Exit(code=0)
        del header[keyword]
        write_header(fits_file, header)
        console.print(f"[bold green]Success: Deleted '{keyword}' from '{fits_file}'.[/bold green]")
    except (FileNotFoundError, OSError) as e:
        console.print(f"[bold red]{e}[/bold red]")
        raise typer.Exit(code=1)


@app.callback()
def main(
    version: bool = typer.Option(
        None,
        "--version",
        "-v",
        callback=version_callback,
        is_eager=True,
        help="Show the version and exit.",
    ),
):
    """A command-line FITS header editor."""
    pass


if __name__ == "__main__":
    sys.exit(app()) 