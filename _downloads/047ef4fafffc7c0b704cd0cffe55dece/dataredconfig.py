"""
Module to hold a few general settings that will be used by several steps of the reduction procedure
"""

from pathlib import Path

# Path to the raw data files (we follow good practice and won't modify these files):
data_dir = Path("/export/data1/fprak1/Data/2024-04-21")
data_dir = Path("/Users/mtewes/Desktop/no_backup/2024-03-08")


# Path to a directory where intermediate files and results can be written:
# (Note: this will need some space, typically 100 GB or more)
work_dir = Path("/export/data1/fprak1/Desktop/my_group_name")
work_dir = Path("/Users/mtewes/Desktop/no_backup/workdir_2024-03-08/")
work_dir.mkdir(exist_ok=True) # We create this directory in case it does not yet exist.

# Our FITS files have long headers.
# Just to make some summary tables easier to read, we give a list of the few important header keywords we care about:
ifc_header_keywords = ["imagetyp", "filter", "exptime", "object", "xbinning", "ybinning", "naxis1", "naxis2"]

