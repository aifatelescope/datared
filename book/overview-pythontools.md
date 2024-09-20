# Structure and Python tools

## Structure of this tutorial

Here is an overview of what we will do on the following pages, that can be seen as separate consecutive steps:

 * [](./data.md): download the data, and write a small configuration module
 * [](./pre-red.ipynb): analyse the calibration frames, create masterbias, masterdark, and masterflats, and apply the corresponding calibration to the science frames
 * [](./photometry.ipynb): perform forced aperture photometry on the individual science frames (i.e., estimate the flux with apertures at the same sky coordinates in each science frame).

At this stage, you'll have one photometric catalog per science frame. Depending on your lab course, you can then proceed with one of the following: 

 * [](./CMD.ipynb): construct and calibrate a CMD from the photometric catalogs
 * [](./lightcurve.ipynb): build a light curve (i.e., brightness as function of time) of an exoplanet transit based on the photometric catalogs


You might also be interested in:
 * [](./astrometry.ipynb): builds an accurate WCS for your science images. In case your images don't come with a (good) WCS, use this before performing photometry or stacking. A good moment to run this is right after [](./pre-red.ipynb).
 * [](./stack.ipynb): (optional!) reproject science frames on a common pixel grid, coadd them, and create a colour composite or a nice graylevel image.


```{note}
This whole tutorial is still under construction. If you encounter any issues or have suggestions, feel invited to post them on our github repository, here: https://github.com/aifatelescope/datared/issues
````


## Python tools

```{note}
This section remains to be written, just skip it for now. We provide plenty of examples, so that the following pages are self-explanatory even without this section.  
````

Before starting to work with the data, let's get a quick overview of the most important specialized Python tools and objects that we will use in this tutorial. This is meant as a minimal reference, providing links to further documentation. Clearly you won't need to dive into this further documentation right now. The following pages are largely self-explanatory and provide plenty of examples.


### `ccdproc`

In principle, images are just 2D arrays, and we could therefore use plain `numpy` arrays to manipulate them.
Instead, we will use the `ccdproc` package (https://ccdproc.readthedocs.io), which provides the framework for our pre-reduction. As you will see, `ccdproc` makes it particularly easy to **work with metadata** of the images (exposure times, dates, filters, coordinates... everything that is stored in the header of FITS files), and futhermore it offers efficient functions to **combine** images. Indeed, it is not completely trivial to median-combine (for example) a large number of frames which would not fit altogether into the computer's memory. Furthermore, `ccdproc` can also take care of propagating uncertainties and masks.



`ccdproc.ImageFileCollection` [Official tutorial](https://ccdproc.readthedocs.io/en/latest/image_management.html)

`ccdproc.CCDData`


```python

ccdproc.ImageFileCollection

photutils.aperture

SkyCoord

```

`astropy.table.Table``


### 



