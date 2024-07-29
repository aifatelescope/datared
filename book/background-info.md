# Introduction to optical observations

This page summarizes important concepts concerning observations in optical astronomy, gives definitions that are essential to understanding the tutorial, and touches some very practical points. It's kept as short as possible.



## Telescope optics

A reflecting telescope uses a combination of (curved) mirrors to form an image in its so-called focal plane, also known as the image plane.
The optical design of the AIfA telescope is a **variation of a Cassegrain** telescope, illustrated below.


```{figure} ./figures/cassegrain.png
---
width: 80%
name: cassegrain
---
Optical layout of a Cassegrain telescope
```

The in-falling light first meets the concave primary mirror (M1) to be then re-reflected by the convex secondary mirror (M2). The light gets collimated in the focal plane, after passing through an opening in M1. Due to the folding of its optical path, such a Cassegrain system allows for a compact construction. More precisely, the AIfA telescope is a  "corrected Dall-Kirkham" telescope, where M1 is ellipsoidal with a diameter of 35 cm (the **aperture** of the telescope), M2 is spherical, and an additional lens group located before the focal plane, roughly in the opening of M1, corrects the design against aberrations on a wide and flat focal plane.

## Resolution

Due to diffraction, a telescope has a finite [angular resolution](https://en.wikipedia.org/wiki/Angular_resolution). Note that this notion of resolution is *not* related to the sampling by a camera (i.e., pixel size), discussed later. Instead, it is a fundamental property of the optical system. 

The light distribution in the image plane resulting from an (apparently) point-like source (star) is termed **point-spread function (PSF)**.
In the idealised (so-called *diffraction-limited*) case, the PSF of a circular aperture is given by the Airy disc. Using the Rayleigh criterion for spatial resolution, a telescope of primary aperture $D$ at a wavelength $\lambda$ is in principle capable of resolving structure with an angular separation (in radians) of

$$
\Delta \theta = 1.22 \frac{\lambda}{D}. 
$$

````{admonition} Question
What's the diffraction-limited angular resolution of a telescope with an aperture of 35 cm, at a wavelength of 700 nm, in arcseconds?
````

As we'll see in the following, for simple ground-based telescopes, the actual resolution will be lower, due to the effects of Earth’s atmosphere.


## Seeing and airmass

For ground-based astronomical observations, Earth’s atmosphere has to be considered as part of the optical system, leading to numerous effects. Most importantly, turbulence in the atmosphere leads to variations of the refractive index on short spatial and temporal scales. The "instantaneous" image of a star seen in the telescope is no longer an Airy disc, but has an irregular shape that randomly changes and moves around. When integrating an image with any exposure time longer than a few tens of a second, this results in a blurring of the PSF. The PSF of such a long exposure can to some extent be represented by a two-dimensional Gaussian (a better approximation is given by the Moffat profile).

The size of such a stellar image, as given by the **full width at half maximum (FWHM)** of the Gaussian, is called the **seeing** of the image and measures the actual resolution in a particular observation. The less turbulent the atmosphere, the higher the resolution and thus the data quality that can be achieved. For Bonn, a seeing of 2 arcsec is a very rare and good value, while in excellent locations like Hawaii or the Atacama desert 0.5 arcsec are common.

The best possible observing conditions are achieved near the zenith, where the length of the light path through the atmosphere is minimal. On the contrary, extinction and disturbing seeing effects get worse for observations at lower elevations. These effects are often expressed in terms of the object’s **airmass** $a$, which tells you through how much atmosphere (column density) the light travels compared to vertical in-fall. For an angular distance $z$ from the zenith (zenith = in vertical direction from the ground) it can in good approximation be computed as $a = 1 / \cos(z)$ such that $a = 1$ for an object at the zenith and formally $a = \infty$ at the horizon.


```{hint}
Both the diffraction-limited resolution of a telescope and the seeing are wavelength-dependent!
The diffraction-limited image would be sharpest for shorter wavelength. But refraction of visible light in the atmosphere (that is a medium with normal dispersion) is stronger for short wavelenghts than it is for long wavelengths. An image in a red (or infrared) filter will be sharper than an image in a blue filter!
```

## Imaging instrument: the camera

A **camera** is an instrument attached to the telescope, such that the camera's imaging sensor (sometimes also called detector) lies in the focal plane of the telescope. The sensor in the camera will *sample* the image, by recording the intensity of the light in an array of *pixels* (short for picture elements).

An important characteristic of a camera, when attached to a telescope, is the resulting pixel scale. It corresponds to the angular size a pixel subtends on the sky, and is expressed in arcseconds. 

Binning



## Imaging detectors (CCD or CMOS)

Modern optical cameras use electronic sensors: the incoming photons create free electrons in silicon, and these free electrons are collected in potential wells. Two "competing" types of sensors for optical astronomy cameras are CCD and CMOS chips. A key difference between these is about where and how the collected charges in each pixel are amplified and converted to a digital signal: for the CCD, many pixels are read out by a single amplifier one after the other (with the charges of these pixels being transfered pixel to pixel towards the amplifier), while for the CMOS, each pixel has its own amplifier.

The difference in 
In the scope of this tutorial, 

the charges in each pixel get moved pixel by pixel towards 



 known as CCD or CMOS chips. We will briefly comment on the difference between CCD and CMOS
Photons create free electrons in silicon
• Collected in potential wells



There are two 


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

