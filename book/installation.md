# Requirements and installation

:::{note}
You can skip this part when working with a computer in the AIfA lab room, everything is already installed there!
Just make sure to execute `conda activate datared` in your terminal/shell, in order to use the right environment. 
:::

The software tools that we'll use the the data reduction is very easy to install, on any platform (with the exception of `astrometry.net` on Windows, as detailed below). 


First, install miniconda, from here: https://docs.anaconda.com/free/miniconda/index.html

Then, open a terminal, and run the following commands.
* The first line creates a new environment, called "datared", and installs Python version 3.11 (this particular version is currently needed for compatibility between all those packages).
* The second line activates this environment (it makes the software available). You'll have to activate it in every terminal window you want to work in.
* The third line takes a little longer, and will ask you to confirm the installation. It's a good idea to install all those packages in "one shot" as done here, to better manage dependencies.


```none
conda create -n datared python=3.11
conda activate datared
conda install -c conda-forge ccdproc photutils matplotlib ipykernel ipympl astroquery
```

## Optional: jupyterlab

If you plan to work with notebooks

```none
conda install -c conda-forge jupyterlab
```

You can then 

```none
cd /where/your/notebooks/are/

jupyter lab
```

to launch JupyterLab.



## Optional: astrometry.net

A reliable tool to perform astrometric calibration of an image is the software `astrometry.net`. It will blindly "plate solve" the image (i.e., identify stars in your image and find out what part of the sky our image covers) and compute a good and standards-compliant WCS solution for it (i.e., give you a mathematical transform between pixel coordinates and sky coordinates, taking into account optical distortions of the telescope). For details, see https://astrometry.net, and http://data.astrometry.net for how to get the index files.

On Linux and macOS, you can easily install `astrometry.net` with conda, using the environment created above:

```none
conda activate datared
conda install -c conda-forge astrometry
```

You'll then have to download some index files. Below are the ones useful for our telescope (TODO: optimize this):

```
cd /your_path_to/miniconda3/envs/datared/data/

# The bare minimum seems to be
curl https://portal.nersc.gov/project/cosmo/temp/dstn/index-5200/LITE/index-5205-[00-47].fits --remote-name
curl https://portal.nersc.gov/project/cosmo/temp/dstn/index-5200/LITE/index-5206-[00-47].fits --remote-name


# From larger to small scales (small to large files), all within 1 deg:

curl https://portal.nersc.gov/project/cosmo/temp/dstn/index-5200/LITE/index-5206-[00-47].fits --remote-name
curl https://portal.nersc.gov/project/cosmo/temp/dstn/index-5200/LITE/index-5205-[00-47].fits --remote-name
curl https://portal.nersc.gov/project/cosmo/temp/dstn/index-5200/LITE/index-5204-[00-47].fits --remote-name
curl https://portal.nersc.gov/project/cosmo/temp/dstn/index-5200/LITE/index-5203-[00-47].fits --remote-name

# For now I have not installed those, I guess we don't need them, to be seen
curl https://portal.nersc.gov/project/cosmo/temp/dstn/index-5200/LITE/index-5202-[00-47].fits --remote-name
curl https://portal.nersc.gov/project/cosmo/temp/dstn/index-5200/LITE/index-5201-[00-47].fits --remote-name
curl https://portal.nersc.gov/project/cosmo/temp/dstn/index-5200/LITE/index-5200-[00-47].fits --remote-name

```


We do not provide instructions to install `astrometry.net` on Windows (but this might well be possible, we just don't support it as the current conda package does not work on Windows).


## Further comments

python=3.12 currently leads to an issue with ccdproc / astroscrappy.
