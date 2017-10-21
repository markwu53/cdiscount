import numpy as np
import matplotlib.pyplot as plt
import zipfile
import bson
from skimage.data import imread
import io

path = "/Users/apple/Documents/Programs/kaggle/porto/"
path = "/Users/T162880/Documents/Programs/kaggle/cdiscount/"
path = "/Users/Public/Documents/Kaggle/cdiscount/"

train_example = "train_example.bson"
train_file = "train.bson" #7069896
test_file = "test.bson" #1768182
#180*180 pic
data = bson.decode_file_iter(open(path+train_file, "rb"))

count = 0
for item in data:
    count += 1
    if count == 1000: break
    product_id = item["_id"]
    category_id = item["category_id"]
    for index, img in enumerate(item["imgs"]):
        picture = imread(io.BytesIO(img["picture"]))
        filename = "{}-{}-{}.png".format(category_id, product_id, index+1)
        print(filename)
        plt.imsave(path+"pic/"+filename, picture)

