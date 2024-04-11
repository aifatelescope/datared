# Python tools


This pages gives a quick overview of the most important Python tools and objects that we will use in the following tutorial.


TO BE WRITTEN

## `ccdproc`

In principle, an image is just a 2D array, and we could use plain `numpy` to manipulate it.

We will however use the `ccdproc` package (https://ccdproc.readthedocs.io), which provides the framework for our pre-reduction. 
It has some convenient objects to handle images with uncertainties and masks.



ccdproc.ImageFileCollection

ccdproc.CCDData


```python

bias_files = ccdproc.ImageFileCollection(data_dir / "BIAS", keywords=header_keywords)

```





