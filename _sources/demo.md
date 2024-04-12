# Test page

See the cheat sheet: https://jupyterbook.org/en/stable/reference/cheatsheet.html#myst-syntax-cheat-sheet


Math:

$$
\int_0^\infty \frac{x^3}{e^x-1}\,dx = \frac{\pi^4}{15}
$$

Code:

```python
dark = CCDData(np.random.normal(size=(10, 10)), unit="adu")
dark_sub = ccdproc.subtract_dark(image_1, dark,
                                 dark_exposure=30*u.second,
                                 data_exposure=15*u.second,
                                 scale=True)
```