import pdal
import numpy as np

json = """
[
    "output_subsampled.las",
    {
        "type": "filters.sort",
        "dimension": "X"
    }
]
"""

pipeline = pdal.Pipeline(json)

try:
    pipeline.execute()
except RuntimeError as e:
    print('Runtime error occurred:', str(e))
arrays = pipeline.arrays
array = arrays[0]

print("Fields available:", array.dtype.names)

classifications = array['Classification']
intensities = array['Intensity']
return_numbers = array['ReturnNumber']

has_color_fields = all(field in array.dtype.names for field in ['Red', 'Green', 'Blue'])
if has_color_fields:
    red_values = array['Red']
    green_values = array['Green']
    blue_values = array['Blue']
else:
    print("Warning: RGB fields not found in the LAS file")

points_with_attributes = np.vstack((array['X'], array['Y'], array['Z'], classifications, intensities, return_numbers)).transpose()
print(points_with_attributes)
print(points_with_attributes.shape)