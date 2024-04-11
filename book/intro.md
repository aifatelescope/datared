# AIfA telescope data reduction tutorial

## Foreword


The aim of this tutorial is to show you a way to "reduce" data acquired with the AIfA telescope, that is to turn the raw data into a scientific result.
This task can typically be split into two separate parts:

1) **Pre-reduction of the images**
 * Remove the instrumental signatures
 * Mask (or flag) defects and missing data
 * Characterize the noise, create a weight map
 * Calibrate the images astrometrically and photometrically (and for spectra: perform wavelength calibration)
 * Produce a stack (coaddition)


2) **Extracting the information of interest**
 * For example: object detection and photometry, creating a light curve, extraction of a spectrum, production of a color image...

:::{note}
The name "reduction" is somewhat misleading. It won't give you back disk space, on the contrary!
:::

Many approaches and software solutions for data reduction exist. The focus of this particular tutorial is on:
* keeping it short and simple, suited for a lab course,
* preferring well documented and easily installable tools, so that the tutorial can be used on any platform,
* getting you to code a little bit, to interact with every step (versus a black-box automated pipeline),
* providing background information on the key concepts. Computational efficiency is less important.


## Overview of what we will use


The whole data reduction and analysis is done in Python, using a series of professional packages under active development:


* `ccdproc` (framework for the image pre-reduction)
* `photutils` (for source detection and photometry)
* `astropy` (basis of the above, but also for manipulating catalogs)
* `matplotlib` (for visualization)

We no longer use SourceExtractor / SCAMP / SWarp or Theli, to make the installation as easy as possible (among other reasons). See [](more.md).


% ```{tableofcontents}
% ```
