
# AIfA telescope data reduction tutorial

This repository contains the source files of the tutorial.

Read the tutorial here: https://aifatelescope.github.io/datared

The website is build with Jupyter Book: 
https://jupyterbook.org/en/stable/intro.html


## Installation

Software to build the book:

Get anaconda or miniconda, and set up an environnment with:
```
conda create -n jupyter-book
conda activate jupyter-book
conda install -c conda-forge jupyter-book

pip install ghp-import # script to push the build html to a dedicated branch on github, for use by github-pages
```

## Building and updating the book

Currently GitHub Actions is not configured to build the book, we use ghp-import instead.

So the process is:

```
jb build book/
```

You can now preview the book in your local browser, as mentionned in the output of the above command.
If happy:

```
ghp-import -n -p -f book/_build/html
```

This pushes the book to the branch `gh-pages`. From there it is automatically served online (maybe with a few minutes delay).




