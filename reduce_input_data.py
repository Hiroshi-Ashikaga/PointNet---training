import json
import pdal

subsampling_pipeline_json = """
{
  "pipeline": [
    "dataset.las",
    {
      "type": "filters.sample",
      "radius": 0.1
    },
    "output_subsampled.las"
  ]
}
"""

pipeline = pdal.Pipeline(json.dumps(json.loads(subsampling_pipeline_json)))
try:
    pipeline.execute()
except RuntimeError as e:
    print('Runtime error occurred:', str(e))