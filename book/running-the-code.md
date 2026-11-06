# Running the book's code examples

If you'd like to run the book's code examples locally on your computer, follow the steps below. 
Otherwise, skip straight to [chapter 1](./1-storage.md).

## Clone the book's github repository
```
git clone https://github.com/ome-zarr-py/ome-zarr-book
cd ome-zarr-book
```

## Install the python dependencies

We recommend using `uv` for the fastest installation, but if you'd prefer to use a different python package manager, you can follow the `pip` instructions instead.

### Uv

- Install uv using the instructions in [uv's docs](https://docs.astral.sh/uv/getting-started/installation/)
- Run `uv run --no-dev jupyter lab` to install the required dependencies and open jupyter lab in your default web browser

### Pip
- We recommend creating a new virtual environment with your preferred tool e.g. [conda](https://docs.conda.io/projects/conda) or [venv](https://docs.python.org/3/library/venv.html).
- Run `pip install -r requirements.txt` to install the book's dependencies
- Run `jupyter lab` to open jupyter lab in your default web browser

## Open the chapters as jupyter notebooks
- Navigate to the `book` directory using the file browser on the left hand side
- Right click on the markdown file (`.md`) of one of the chapters and select `Open With > Notebook`

You can now run all the code directly in a [jupyter notebook](https://jupyter-notebook.readthedocs.io/en/latest/).
Click on a code cell, then click the play button in the top toolbar (or `Shift + Enter`) to run it.

