
import subprocess
import pathlib


def check_corr_file(corr_file_path):
    pass



def run(fitspath, outdirpath, wcspath=None, verify=False):
    """Runs solve-field on a FITS file

    if verify, the option verify is used to run on an existing WCS
    """

    cmd_one = ["solve-field",
           "--overwrite",
           "--scale-units", "arcsecperpix",
           "--scale-low", "0.60",
           "--scale-high", "0.62",
           "--downsample", "4",
           "--crpix-center",
           "--tweak-order", "3",
           "--resort",
           "--dir", outdir_path,
           "--no-plots",
           "--new-fits", "%s.fits",
           fits_path
      ]

    cmd_two = ["solve-field",
           "--overwrite",
           "--scale-units", "arcsecperpix",
           "--scale-low", "0.60",
           "--scale-high", "0.62",
           "--downsample", "4",
           "--crpix-center",
           "--tweak-order", "3",
           "--resort",
           "--dir", outdir_path,
           "--verify", wcs_path,
           "--no-plots",
           "--new-fits", "%s.fits",
           fits_path
      ]

    if verify:
        cmd = cmd_two
    else:
        cmd = cmd_one
        
    res = subprocess.run(cmd, text=True, capture_output=True)
        
    if(res.returncode != 0): # only need to see this if problems
        print(res.stderr)





orig_dirpath = pathlib.Path("/export/data1/fprak1/tests_mtewes/transit_runtwice/run_one")
orig_filepaths = sorted(list(orig_dirpath.glob('*.fits')))
print(f"Found {len(orig_filepaths)} input images.")

out_dir_path = pathlib.Path("/export/data1/fprak1/tests_mtewes/transit_runtwice/run_two")

for filepath in orig_filepaths:
    print(filepath.parent, filepath.stem)
    wcs_filepath = filepath.with_suffix('.wcs')

    run_two(filepath, wcs_filepath, out_dir_path)

    #print(wcs_filepath)

