# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import zarr
import matplotlib.pyplot as plt
import numpy as np
import numcodecs

# %%
arr = zarr.open_array(
    "gs://ucl-hip-ct-35a68e99feaae8932b1d44da0358940b/LADAF-2020-27/heart/19.89um_complete-organ_bm18.ome.zarr/6"
)

# %%
arr.nbytes / 1e6

# %%
arr_npy = arr[:]
# Cast to float64 for higher precision processing
arr_npy = arr_npy.astype(np.float64)
# Clip from 1st > 99th percentile
arr_npy = np.clip(arr_npy, np.percentile(arr_npy, 1), np.percentile(arr_npy, 99))
# Scale from 0 > 255
arr_npy = arr_npy - arr_npy.min()
arr_npy = arr_npy * 255 / arr_npy.max()
# Cast to 8-bit
arr_npy = arr_npy.astype(np.uint8)

# %%
plt.ecdf(arr_npy.ravel())

# %%
plt.imshow(arr_npy[:, :, 30], cmap="plasma")

# %%
arr_npy.shape

# %%
new_zarr = zarr.save_array(
    "hoa_heart.zarr",
    arr_npy,
    chunks=(64, 64, 64),
    compressor=numcodecs.Blosc(cname="zstd", clevel=9),
)
