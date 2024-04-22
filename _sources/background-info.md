# Background information on image reduction

Before dwelving into code, we need some definitions and a theoretical overview. It's kept as short as possible, and should help you understand what follows.


## CCD and CMOS cameras

* Full-well capacity
* ADU, ADC, bias
* Gain
* Bit depth
* Dark current

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

Once the

```{sidebar} Average or median?
Assuming an ideal situation without any outliers, is it better to average-combine or median-combine images?

For a large number of samples from a normal distribution, the variance of the median will by $\pi/2 = 1.57$ times higher than the variance of the mean.

The standard error of the median will be $\sqrt{\pi/2} = 1.25$ times higher, or 25% greater, than the standard error of the mean

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

* aperture vs fitting



## Mini Python intro ? 

