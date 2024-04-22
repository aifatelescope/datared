# Structure and Python tools

Here is an overview of what we will do on the following pages, that can be seen as separate consecutive steps:

 * [](./data.md): download the data, and write a small configuration module
 * [](./pre-red.ipynb): analyse the calibration frames, create masterbias, masterdark, and masterflats, and apply the corresponding callibration to the science frames
 * [](./stack.ipynb): (optional!) reproject science frames on a common pixel grid, coadd them, and create a colour image
 * [](./photometry.ipynb): perform forced aperture photometry on the individual science frames (i.e., estimate the flux of each star)
 * [](./CMD.ipynb): construct and calibrate a CMD from the photometric catalogs
 * [](./lightcurve.ipynb): build a lightcurve (i.e., brightness as function of time) of an exoplanet transit based on the photometric catalogs



## Python tools

This section gives a very quick overview of specialized Python tools and objects that we will use in the following tutorial.


TO BE WRITTEN, add link to doc.

### `ccdproc`

In principle, an image is just a 2D array, and we could use plain `numpy` to manipulate it.

We will however use the `ccdproc` package (https://ccdproc.readthedocs.io), which provides the framework for our pre-reduction. 
It has some convenient objects to handle images, and can propagate uncertainties and masks.



`ccdproc.ImageFileCollection`

`ccdproc.CCDData`


```python

ccdproc.ImageFileCollection

photutils.aperture

SkyCoord

```

`astropy.table.Table``


### 


