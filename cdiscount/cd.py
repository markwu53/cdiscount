import xgboost as xgb
import numpy as np
import matplotlib.pyplot as plt
import zipfile
import bson
from skimage.data import imread
import io

path = "/Users/apple/Documents/Programs/kaggle/porto/"
path = "/Users/Public/Documents/Kaggle/porto/"
path = "/Users/T162880/Documents/Programs/kaggle/cdiscount/"

train_example = "train_example.bson"
data = bson.decode_file_iter(open(path+train_example, "rb"))

for item in data:
    product_id = item["_id"]
    category_id = item["category_id"]
    for index, img in enumerate(item["imgs"]):
        picture = imread(io.BytesIO(img["picture"]))
        filename = "{}-{}-{}.png".format(category_id, product_id, index+1)
        print(filename)
        plt.imsave(path+filename, picture)

