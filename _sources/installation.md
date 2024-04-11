# Requirements and installation

:::{note}
You can skip this part when working with a computer in the AIfA lab room, everything is already installed there!
:::


A big advantage of this choice is that everything should be very easy to install, on any platform!

First, install miniconda, from here: https://docs.anaconda.com/free/miniconda/index.html

Then, open a terminal, and run the following commands.
* The first line creates a new environnment, called "datared", and installs Python version 3.11 (this particular version is currently needed for compatibility between all those packages).
* The second line activates this environnment (it makes the software available). You'll have to activate it in every terminal window you want to work in.
* The third line takes a little longer, and will ask you to confirm the installation. It's a good idea to install all those packages in "one shot", to better manage dependencies.


```none
conda create -n datared python=3.11
conda activate datared
conda install -c conda-forge ccdproc photutils matplotlib ipykernel ipympl astroquery
````


## Optional: astrometry.net

A reliable tool to perform astrometric calibration of an image is the software `astrometry.net`. It will blindly "plate solve" the image (i.e., identify stars in your image and find out what part of the sky our image covers) and compute a good and standards-complient WCS solution for it (i.e., give you a mathematical transform between pixel coordinates and sky coordinates, taking into account optical distortions of the telescope). For details, see https://astrometry.net, and http://data.astrometry.net for how to get the index files.


With conda, you can easily install `astrometry.net` locally, using the environnment created above:

```none
conda activate datared
conda install -c conda-forge astrometry
```

You'll then have to download some index files. Below are the ones useful for our telescope (TODO: optimize this):

```
cd /your_path_to/miniconda3/envs/datared/data/
curl https://portal.nersc.gov/project/cosmo/temp/dstn/index-5200/LITE/index-5205-[00-47].fits --remote-name
curl https://portal.nersc.gov/project/cosmo/temp/dstn/index-5200/LITE/index-5206-[00-47].fits --remote-name
```

This is how you could then use `astrometry.net` to write a WCS into the header of a FITS image:

```none
solve-field -h 

solve-field --overwrite --downsample 4 -v -t 3 --guess-scale myimage.fits 
```



## Further comments

python=3.12 currently leads to an issue with ccdproc / astroscrappy.
