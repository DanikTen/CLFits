"""Utility for creating a dummy FITS file for testing."""

from pathlib import Path

import numpy as np
from astropy.io import fits


def create_test_fits(tmp_path: Path) -> Path:
    """
    Create a simple FITS file for testing.

    The FITS file will have a 1x1 pixel image and a minimal header.

    Parameters
    ----------
    tmp_path : Path
        The temporary directory path provided by pytest.

    Returns
    -------
    Path
        The path to the created FITS file.
    """
    fits_file = tmp_path / "test.fits"
    image_data = np.ones((1, 1), dtype=np.int16)
    hdu = fits.PrimaryHDU(data=image_data)

    # Add some initial keywords to the header
    hdu.header["OBJECT"] = "NGC 101"
    hdu.header["OBSERVER"] = "Hubble"
    hdu.header["EXPTIME"] = (300.0, "Total exposure time (s)")

    hdu.writeto(fits_file, overwrite=True)
    return fits_file 