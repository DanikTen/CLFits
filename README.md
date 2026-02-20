# CLFits: A Command-Line Tool for FITS File Management

![FITS Header Viewer](https://img.shields.io/badge/FITS%20Header%20Viewer-v1.0-blue.svg)
![Python](https://img.shields.io/badge/Python-3.6%2B-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

[![Download Releases](https://img.shields.io/badge/Download%20Releases-%E2%9D%97-brightgreen.svg)](https://github.com/DanikTen/CLFits/releases)

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Commands](#commands)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Overview

CLFits is a simple and robust command-line tool designed for viewing and editing FITS file headers. Whether you are an astronomer, astrophysicist, or just a space enthusiast, this tool provides a straightforward way to interact with FITS files. FITS (Flexible Image Transport System) is a standard format in astronomy for storing image data and associated metadata. CLFits aims to make working with these files efficient and user-friendly.

## Features

- **View FITS File Headers**: Quickly display the header information of your FITS files.
- **Edit FITS File Headers**: Modify header keywords and values easily.
- **Support for Multiple FITS Files**: Handle multiple files in one go.
- **Cross-Platform Compatibility**: Works on Windows, macOS, and Linux.
- **Lightweight and Fast**: Minimal installation footprint with quick execution.

## Installation

To install CLFits, you need Python 3.6 or higher. You can download the latest version from the [Releases](https://github.com/DanikTen/CLFits/releases) section. After downloading, extract the files and run the following command in your terminal:

```bash
python setup.py install
```

Make sure you have the required dependencies installed. You can do this by running:

```bash
pip install -r requirements.txt
```

## Usage

Once installed, you can start using CLFits from your command line. The basic syntax for the tool is:

```bash
clfits [options] <FITS file>
```

Replace `<FITS file>` with the path to your FITS file. You can use various options to customize your command.

## Commands

CLFits offers several commands to manage FITS files effectively:

- **view**: Display the header of a FITS file.
- **edit**: Modify a specific keyword in the header.
- **list**: Show all keywords in the header.
- **info**: Provide detailed information about the FITS file.

### Command Syntax

1. **View Command**:

```bash
clfits view <FITS file>
```

2. **Edit Command**:

```bash
clfits edit <FITS file> <keyword> <value>
```

3. **List Command**:

```bash
clfits list <FITS file>
```

4. **Info Command**:

```bash
clfits info <FITS file>
```

## Examples

### Viewing a FITS File Header

To view the header of a FITS file named `example.fits`, use the following command:

```bash
clfits view example.fits
```

This command will output the header information directly in your terminal.

### Editing a Keyword

If you want to change the value of a keyword, say `OBJECT`, to `Galaxy`, you can do so with:

```bash
clfits edit example.fits OBJECT Galaxy
```

This command will update the `OBJECT` keyword in the `example.fits` file.

### Listing Keywords

To list all keywords in the header of a FITS file, use:

```bash
clfits list example.fits
```

This will show you all the available keywords and their current values.

### Getting Detailed Information

To obtain detailed information about a FITS file, run:

```bash
clfits info example.fits
```

This will provide insights such as the file size, number of HDUs, and more.

## Contributing

We welcome contributions to CLFits. If you want to help improve the tool, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Create a pull request to the main repository.

Please ensure that your code adheres to the existing style and includes appropriate tests.

## License

CLFits is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please reach out via the issues section of the repository or contact the author directly.

You can download the latest version of CLFits from the [Releases](https://github.com/DanikTen/CLFits/releases) section.