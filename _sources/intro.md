# AIfA telescope data reduction tutorial

## Foreword


The aim of this tutorial is to show you a way to "reduce" and analyse imaging data acquired with the 35-cm AIfA telescope in the scope of a lab course. We'll go from the raw data towards a scientific result, using professional and easy-to-install Python packages. The tutorial focuses on aperture photometry and its calibration, but also touches on reprojection and stacking. No prerequisite knowledge of these topics is needed, as we'll start with a general introduction to optical observations.


```{figure} ./figures/results_teaser.png
---
width: 100%
name: results_teaser
---
Illustrative products of the tutorial
```

Note that while the tutorial is fine-tuned for the AIfA telescope, it is perfectly possible to use the provided code when dealing with data from other instruments, contingent on minor adaptations that are either obvious or described in the text. 


## What's this "reduction"?

Image reduction can often be broadly split into two separate parts, which *may* comprise some of these steps: 

1) **Pre-reduction of the images**
 * Remove instrumental signatures using calibration frames
 * Mask (or flag) defects and missing data
 * Characterize the noise
 * Calibrate the images astrometrically and photometrically (and in wavelength, in case of spectra)
 * Model the sky background
 * Produce a stack, aka coaddition (sometimes), or even a mosaic


2) **Extracting the information of interest**
 * Object detection and photometry
 * Photometric calibration against a reference catalogue
 * Creation of a light curve
 * Production of a color image
 * etc ...

The present tutorial goes even a bit further than the reduction itself, as it also covers the analysis of the data (e.g., the comparison between an observed color-magnitude diagram and isochrones).

```{note}
The name "reduction" is somewhat misleading. It won't give you back disk space, on the contrary!
```

Many approaches and software solutions for data reduction exist. The focus of this particular tutorial is on:
* keeping it short and simple, suited for a lab course,
* preferring well documented and easily installable tools, so that the tutorial can be used on any platform,
* getting you to code a little bit, to interact with every step (versus a black-box automated pipeline),
* providing background information on the key concepts. Computational efficiency is less important.


## Overview of what we will use

The whole data reduction and analysis is done in Python (except for the astrometric calibration, which is based on a local installation of `astrometry.net` that we'll call from within python). We make use of the following professional Python packages, all under active development:

* `ccdproc` (framework for the image pre-reduction)
* `photutils` (for source detection and photometry)
* `astropy` (basis of the above, but also for manipulating catalogs)
* `matplotlib` (for visualization)

We no longer use SourceExtractor / SCAMP / SWarp or Theli, to make the installation as easy as possible (among other reasons). See [](more.md) if you are interested in these alternative solutions.


% ```{tableofcontents}
% ```
