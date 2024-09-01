# Setting up the data

## Download

Raw data acquired by the telescope gets synced to sciebo, and can be downloaded from here:

https://uni-bonn.sciebo.de/s/aKDd5Y3ln79Gg9W

On the `fprak`-computers in the lab room, we keep all this in the directory `~/Data`.

Save the directory you want to work with on your system, and extract/decompress it if needed, for example using `unzip`:

```none
mv Downloads/2024-06-05.zip Data/
cd Data
unzip 2024-06-05.zip
```


## Configuring the reduction

Some settings that will get reused for different reduction steps are conveniently written in a dedicated python module.

* Download the module {download}`dataredconfig.py <./dataredconfig.py>` and save it where you will be running the reduction code.
* Then edit this file, to adapt the relevant path to where your raw data is.


