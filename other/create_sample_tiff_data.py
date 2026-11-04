from pathlib import Path
import zarr
import imageio.v3 as iio

# path to the output from create_sample_zarr_data.py
data_path = (Path(__file__).parents[1] / "book" / "data" / "hoa_heart.zarr").resolve()

arr_zarr = zarr.open_array(store=data_path, mode="r")
iio.imwrite("hoa_heart.tiff", arr_zarr[:], plugin='tifffile')
