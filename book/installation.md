# Requirements and installation

:::{note}
You can skip this part when working with a computer in the AIfA lab room, everything is already installed there!
Just make sure to execute `conda activate datared` in your terminal/shell, in order to use the right environment. 
:::

The software tools that we'll use for the data reduction are easy to install, on any platform (with the exception of `astrometry.net` on Windows, as detailed below). 


First, download and install Miniforge, from here: https://conda-forge.org/download/ . This will allow you to set up a small isolated environment containing everything needed for the data reduction.

Then, open a terminal, and run the following commands.
* The first line creates a new environment, called "datared", and installs Python version 3.12.
* The second line activates this environment (it makes the software available). You'll have to activate it in every terminal window you want to work in.
* The third line takes a little longer, and will ask you to confirm the installation. It's a good idea to install all those packages in "one shot" as done here, to better manage dependencies.


```none
conda create -n datared python=3.12.8
conda activate datared
conda install -c conda-forge numpy=2.2.2 scipy=1.15.1 astropy=7.0.1 ccdproc=2.4.3 photutils=2.1.0 matplotlib=3.10.0 astroquery=0.4.9 ipympl=0.9.6 ipykernel=6.29.5 jupyterlab=4.3.5
```

## Using Python with notebooks: JupyterLab

The above also installs [JupyterLab](https://docs.jupyter.org), a tool to interactively work with notebooks from within your browser. If you want work with notebooks, such as the ones provided later in this tutorial, you can launch JupyterLab with the following command.

```none
cd /where/your/notebooks/are/

jupyter lab
```



## Astrometric calibration: astrometry.net

A reliable tool to perform astrometric calibration of an image is the software `astrometry.net`. It will blindly "plate solve" the image (i.e., identify stars in your image and find out what part of the sky our image covers) and compute a good and standards-compliant WCS solution for it (i.e., give you a mathematical transform between pixel coordinates and sky coordinates, taking into account optical distortions of the telescope). For details, see https://astrometry.net, and http://data.astrometry.net for how to get the index files.

On Linux and macOS, you can easily install `astrometry.net` with conda, using the environment created above:

```none
conda activate datared
conda install -c conda-forge astrometry=0.97
```

You'll then have to download some index files.
Below are the ones useful for our telescope (48 arcmin x 32 arcmin field), from larger to small scales (small to large files), all within 1 deg.

```
cd /your_path_to/miniforge3/envs/datared/data/

curl https://portal.nersc.gov/project/cosmo/temp/dstn/index-5200/LITE/index-5205-[00-47].fits --remote-name
curl https://portal.nersc.gov/project/cosmo/temp/dstn/index-5200/LITE/index-5206-[00-47].fits --remote-name


# Just for reference, the next ones would be below.
# But they do seem to harm the quality of the SIP!
# (Maybe due to misidentifications when the index density gets too high?)
# Don't install those without checking details!
#curl https://portal.nersc.gov/project/cosmo/temp/dstn/index-5200/LITE/index-5204-[00-47].fits --remote-name
#curl https://portal.nersc.gov/project/cosmo/temp/dstn/index-5200/LITE/index-5203-[00-47].fits --remote-name
#curl https://portal.nersc.gov/project/cosmo/temp/dstn/index-5200/LITE/index-5202-[00-47].fits --remote-name
#curl https://portal.nersc.gov/project/cosmo/temp/dstn/index-5200/LITE/index-5201-[00-47].fits --remote-name
#curl https://portal.nersc.gov/project/cosmo/temp/dstn/index-5200/LITE/index-5200-[00-47].fits --remote-name

# Description and advice on these index files: http://astrometry.net/doc/readme.html

```


We do not provide instructions to install `astrometry.net` on Windows (but this might well be possible, we just don't support it as the current conda package does not work on Windows).

