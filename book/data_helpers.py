from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.axes import Axes
import numpy.typing as npt


def plot_slice(array: npt.ArrayLike, *, z_idx: int, ax: Axes | None = None) -> None:
    if ax is None:
        _, ax = plt.subplots()
    ax.imshow(array[:, :, z_idx], cmap="Grays_r")
    ax.set_title(f"Slice at z={z_idx}")
    ax.axis("off")


def get_directory_contents(dirpath: Path) -> list[str]:
    if not dirpath.is_dir():
        raise ValueError(f"{dirpath} is not a directory")

    return sorted(d.relative_to(dirpath).name for d in dirpath.glob("*"))
