
A jupyter book about data reduction at the AIfA telescope.

Read the book here: https://aifatelescope.github.io/datared

# Installation

Software to build the book:

```
conda create -n jupyter-book
conda activate jupyter-book
conda install -c conda-forge jupyter-book

pip install ghp-import # script to push the build html to a dedicated branch on github, for use by github-pages
```

# Updating the book

Currently GitHub Actions is not configured to build the book, we use ghp-import instead.

So the process is:

```
cd book
ghp-import -n -p -f _build/html
```

This pushes the book to the branch `gh-pages`.




