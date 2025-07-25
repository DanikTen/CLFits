"""Utility for creating a dummy FITS file for testing."""

from pathlib import Path

import numpy as np
from astropy.io import fits
from astropy.io.fits.header import Header


def create_test_fits(tmp_path: Path, with_table: bool = False) -> Path:
    """Create a simple FITS file for testing.

    The primary HDU contains a 1x1 image. The header contains standard
    keywords plus a custom one ('OBJECT').

    Parameters
    ----------
    tmp_path : Path
        The directory where the FITS file will be created (provided by pytest).
    with_table : bool, optional
        If True, add a binary table extension to the FITS file, by default False.

    Returns
    -------
    Path
        The path to the created FITS file.

    """
    # Create a primary HDU with a minimal header and a 1x1 image
    primary_header = Header()
    primary_header["SIMPLE"] = True
    primary_header["BITPIX"] = 8
    primary_header["NAXIS"] = 2
    primary_header["NAXIS1"] = 1
    primary_header["NAXIS2"] = 1
    primary_header["OBJECT"] = "NGC 101"
    primary_header["COMMENT"] = "This is a test comment."

    image_data = np.zeros((1, 1), dtype=np.uint8)
    primary_hdu = fits.PrimaryHDU(data=image_data, header=primary_header)

    hdul = fits.HDUList([primary_hdu])

    if with_table:
        # Create a simple binary table extension
        col1 = fits.Column(name="TARGET", format="10A", array=["NGC 101", "NGC 102"])
        col2 = fits.Column(name="RA", format="E", array=[120.1, 120.2])
        col3 = fits.Column(name="DEC", format="D", array=[-30.1, -30.2])
        cols = fits.ColDefs([col1, col2, col3])
        table_hdu = fits.BinTableHDU.from_columns(cols)
        table_hdu.name = "OBSERVATIONS"
        hdul.append(table_hdu)

    fits_file = tmp_path / "test.fits"
    hdul.writeto(fits_file, overwrite=True)
    hdul.close()
    return fits_file
