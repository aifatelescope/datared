# Requirements and installation

:::{note}
You can skip this part when working with a computer in AIfA lab room!
:::

The whole data reduction and analysis is done in Python, using a series of professional packages mostly affiliated to astropy.
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


Note that in case you want to perform an astrometric calibration (that is "plate solving" and obtaining a good WCS solution), you can also easily install atrometry.net locally with

```none
conda activate datared
conda install -c conda-forge astrometry
```

You'll then have to download some index files:

```
cd /path_to/miniconda3/envs/datared/data/
curl https://portal.nersc.gov/project/cosmo/temp/dstn/index-5200/LITE/index-5205-[00-47].fits --remote-name
curl https://portal.nersc.gov/project/cosmo/temp/dstn/index-5200/LITE/index-5206-[00-47].fits --remote-name
```

This is how you could then run astrometry.net (for example):

```none
solve-field --overwrite --downsample 4 -v -t 3 --guess-scale bla.fits 
```



## Further comments

python=3.12 currently leads to an issue with ccdproc / astroscrappy.
