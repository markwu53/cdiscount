import numpy as np
import pandas as pd
from subprocess import check_output
path = "/Users/T162880/Documents/Programs/kaggle/cdiscount/"
print(check_output(["dir", path]).decode("utf8"))
import io
import bson
import matplotlib.pyplot as plt
from skimage.data import imread
import multiprocessing as mp
train_example = "train_example.bson"
data = bson.decode_file_iter(open(path+train_example, "rb"))

prod_to_category = dict()

for c, d in enumerate(data):
    product_id = d["_id"]
    category_id = d["category_id"] # This won"t be in Test data
    prod_to_category[product_id] = category_id
    for e, pic in enumerate(d["imgs"]):
        picture = imread(io.BytesIO(pic["picture"]))
        # do something with the picture, etc

prod_to_category = pd.DataFrame.from_dict(prod_to_category, orient="index")
prod_to_category.index.name = "_id"
prod_to_category.rename(columns={0: "category_id"}, inplace=True)
prod_to_category.head()
plt.imshow(picture)
