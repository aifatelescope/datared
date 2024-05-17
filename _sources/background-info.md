# Background information on image reduction

Before dwelving into code, we need some definitions and a theoretical overview. It's kept as short as possible, and should help you understand what follows.


## CCD and CMOS cameras

* Full-well capacity
* ADU, ADC, bias
* Gain
* Bit depth
* Dark current

## Astronomical images

```{figure} ./figures/image_basics.png
---
width: 75%
name: image_basics
---
Illustration of some basic image properties. Top: two stars (one has twice the flux of the other, but their FWHM is the same), and one galaxy. Bottom: horizontal section across the image, with pixel value on the y-axis.
```

* Images of stars are not "point-like", but follow the profile of the *Point Spread Function* (PSF). For images obtained by simple ground-based telescopes, the origin of the PSF is dominated by **astronomical seeing**, that is by refraction in bubbles of air with varying refractive index, which are rapidly moving through the line of sight due to atmospheric turbulence. The images we record through those telescopes get blurred by this PSF. Mathematically, the observed image can be seen as a convolution of the actual scene with this PSF, sampled on the pixel array of the detector.

* The PSF is wavelength-dependent. In a medium with normal dispersion (such as air), refraction is stronger for shorter wavelengths. Therefore ground-based images obtained through a red filter will be significantly sharper than images in a blue band.

* On a ground-based image from an idealized detector, the PSF is relatively close to a Gaussian. If stars have the same spectrum (or if you use a very narrow filter) then these profiles have *the same width*, for example as measured by the *Full Width at Half Maximum* (**FWHM**, see figure above) of the stars. The same holds for the standard-deviation of a 2D-Gaussian fitted to these stars.

* When displaying an image, brighter stars do have wider *isophotes* (i.e., curve around the star at a given brightness level) and therefore appear "larger", even if the FWHM is the same for stars (see figure above).

* Sources of noise: 
    * photon noise aka "shot noise" (photons hitting each pixel follow a poisson process), from the source but also from the so-called "background" (in fact, a foreground: sky brightness).
    * readout noise of electronics



## FITS

* HDU

## Calibration frames

* Flat difficulty, color dependence

## Artifacts and cosmic rays ?

* Hot pixels

## WCS, distortions

## Coaddition


* reprojection techniques
* average vs median combination, little demo that avg is better in terms of noise.


```{sidebar} Average or median?
Assuming an ideal situation without any outliers, is it better to average-combine or median-combine images?

For a large number of samples from a normal distribution, the standard error of the median will be $\sqrt{\pi/2} = 1.25$ times higher, or 25% greater, than the standard error of the mean.

https://en.wikipedia.org/wiki/Median
```

````{admonition} Question
Why is combining several exposures usually better than taking a single exposure with a long exposure time?
```{hint}
:class: dropdown
Saturation, tracking, cosmic rays
```
````


## Photometry

The brightness measurement of objects on an image is called *photometry*. There are two main approaches to photometry on CCD images: digital aperture photometry, and PSF fitting.


{cite}`Chromey:2016`


Digital aperture photometry
: Definition

  PSF homogeneization

PSF fitting
: Definition

In this tutorial, we make use of **forced photometry**, meaning that we perform photometry by placing apertures at specific pre-defined locations of an image, without first "detecting" sources in that particular image. These locations are defined in sky coordinates in a reference catalog that we build from a reference image. This makes the subsequent analysis particularly easy, as we get consistent photometric catalogs for each exposure.


```{note}
For the sake of simplicity, we ignore here the effect that distortions have on photometry. For the curious: flatfielding links the pixel scale inhomogeneity of the detector to a systematic photometric bias, that in principle needs to be accounted for (either a posteriori or by reprojecting the images on a distortion-free pixel grid).
```

## Mini Python intro ? 

