# I made a simple command line interface (CLI) tool for editing FITS headers

tags: `astropy`, `fits`, `table`, `release`

Kia ora everyone,

I frequently find myself needing to make quick, small changes to FITS headers (like fixing an `OBJECT` keyword) without wanting to open a full GUI, especially when I'm remote over SSH.

So I built `CLFits`, a simple, non-interactive command-line tool for that specific task.

```txt
Manage FITS headers from the command line.

╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --version  -v        Show the version and exit.                              │
│ --help     -h        Show this message and exit.                             │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────╮
│ view      View the header of a FITS file.                                    │
│ get       Get the value of a specific header keyword.                        │
│ set       Set a keyword's value, with an optional comment.                   │
│ del       Delete a keyword from the header.                                  │
│ export    Export the FITS header to a specified format (JSON, YAML, or CSV). │
│ search    Search for keywords in a FITS header by pattern.                   │
╰──────────────────────────────────────────────────────────────────────────────╯
```

It's built on `Astropy`, is installable via `pip`, and the code is open source. Maybe it can save some of you a few steps, too.

-   **Source Code:** [`https://github.com/AmberLee2427/CLFits`](https://github.com/AmberLee2427/CLFits)
    
-   **Docs:** [`https://clfits.readthedocs.io/en/latest/`](https://clfits.readthedocs.io/en/latest/)
    
-   **Install:** `pip install clfits`
    

Let me know if you find it useful.