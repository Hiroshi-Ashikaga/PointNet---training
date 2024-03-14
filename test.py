import laspy
import numpy as np
import findspark
findspark.init()
import warnings
warnings.filterwarnings('ignore')
import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

# app_name = "data processing with Pyspark"
# spark = SparkSession.builder.appName(app_name).master("local[*]").enableHiveSupport().getOrCreate()
las_file = laspy.file.File('dataset.las', mode = 'r')

num_points = las_file.header.count

print(las_file.shape)

# points_xyzic = np.empty((num_points, 5))

# for i in range(100):
#     print(i)
#     points_xyzic[i] = [las_file.x[i], las_file.y[i], las_file.z[i], las_file.intensity[i], las_file.classification[i]]

# unclassified = 1
# ground = 2


# filter_array = np.any([points_xyzic[:, 4] == unclassified,points_xyzic[:, 4] == ground,], axis=0)

# filtered_points = points_xyzic[filter_array]

# print(filtered_points)