# Structure and Python tools

## Structure of this tutorial

Here is an overview of what we will do on the following pages, that can be seen as separate consecutive steps:

 * [](./data.md): download the data, and write a small configuration module
 * [](./pre-red.ipynb): analyse the calibration frames, create masterbias, masterdark, and masterflats, and apply the corresponding calibration to the science frames
 * [](./astrometry.ipynb): builds an accurate WCS for your science images (could be skipped in case your images already have a good WCS, including a distortion model)
 * [](./photometry.ipynb): perform forced aperture photometry on the individual science frames (i.e., estimate the flux with apertures at the same sky coordinates in each science frame).

At this stage, you'll have one photometric catalog per science frame. Depending on your lab course, you can then proceed with one of the following: 

 * [](./CMD.ipynb): construct and calibrate a CMD from the photometric catalogs
 * [](./lightcurve.ipynb): build a light curve (i.e., brightness as function of time) of an exoplanet transit based on the photometric catalogs


You might also be interested in:
  * [](./stack.ipynb): (optional!) reproject science frames on a common pixel grid, coadd them, and create a colour composite or a nice graylevel image. This can be run at any time after the [](./astrometry.ipynb).


```{note}
This whole tutorial is still under construction. If you encounter any issues or have suggestions, feel invited to post them on our github repository, here: https://github.com/aifatelescope/datared/issues
````


## Python tools


Before starting to work with the data, let's get a quick overview of the most important specialized Python tools and objects that we will use in this tutorial. This is meant as a minimal reference, providing links to further documentation. Clearly you won't need to dive into this further documentation right now! The pages of the tutorial are largely self-explanatory and provide plenty of examples.


### `ccdproc`

In principle, images are just 2D arrays, and we could therefore use plain `numpy` arrays to manipulate them.
Instead, we will use the `ccdproc` package (https://ccdproc.readthedocs.io), which provides the framework for our pre-reduction. As you will see, `ccdproc` makes it particularly easy to **work with metadata** of the images (exposure times, dates, filters, coordinates... everything that is stored in the header of FITS files), and futhermore it offers efficient functions to **combine** images. Indeed, it is not completely trivial to median-combine (for example) a large number of frames which would not fit altogether into the computer's memory. Furthermore, `ccdproc` can also take care of propagating uncertainties and masks.

The two most important classes that we'll use are:

 * `ccdproc.ImageFileCollection` to summarize, filter, and iterate over a collection of FITS images (see the [official tutorial](https://ccdproc.readthedocs.io/en/latest/image_management.html)), and

 * `ccdproc.CCDData` to represent an image (see the [official tutorial](https://ccdproc.readthedocs.io/en/latest/ccddata.html)), regardless if the image was acquired by a CCD or a CMOS. At the core of `CCDData`, an image is a 2D numpy array, but this class offers many additional and convenient features, for example to propagate metadata and uncertainties.


### `photutils`

For background estimation, source detection, and photometry, we will use the `photutils` package (https://photutils.readthedocs.io). 


### `astropy`

The `astropy` package (https://docs.astropy.org) is the backbone library used by `ccdproc` and `photutils` as well as for many other astronomical computations.
The classes from `astropy` that we'll encounter most are the following:

 * `astropy.table.Table` provides a container for catalogues, such as tables of properties for many sources detected in an image (see [documentation](https://docs.astropy.org/en/stable/table/index.html)). Notably, these tables can hold multi-dimensional columns. We will make use of this feature.


 * `astropy.coordinates.SkyCoord` to represent celestial coordinates (see [user guide](https://docs.astropy.org/en/stable/coordinates/)). This class is encountered for example when we transform between pixel and sky coordinates, and to compute angular separations between sources.

