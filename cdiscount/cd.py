import numpy as np
import pandas as pd
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
prod_cat_file = "prod_cat.txt"
cat_name_file = "category_names.csv"

data = bson.decode_file_iter(open(path+train_file, "rb"))

def prod_cat():
    with open(path+prod_cat_file, "w") as fd:
        count = 0
        for item in data:
            count += 1
            if count % 10000 == 0:
                print(count)
            product_id = item["_id"]
            category_id = item["category_id"]
            fd.write("{},{}\n".format(product_id, category_id))

def prod_cat_explore():
    with open(path+prod_cat_file) as fd: values = fd.readlines()
    values = np.array([ int(value.strip().split(",")[1]) for value in values ])
    plt.hist(values, bins=np.arange(1e9, 1e9+25000, 200))

def explore():
    prod_cat = pd.read_csv(path+prod_cat_file)
    prod_cat.columns = ["id", "cat"]
    counts = np.bincount(np.array(prod_cat["cat"]-1e9, dtype=np.int64))
    np.amax(counts) #79640
    np.argmax(counts) #18296 -> 1000018296
    cat_name = pd.read_csv(path+cat_name_file)
    clevel1 = set(cat_name["category_level1"])
    llevel1 = list(clevel1)
    ilevel1 = { name: index for index, name in enumerate(llevel1) }
    clevel2 = set(cat_name["category_level2"])
    clevel3 = set(cat_name["category_level3"])
    dlevel1 = dict(zip(cat_name["category_id"], cat_name["category_level1"]))
    vlevel1 = np.array([ ilevel1[dlevel1[value]] for value in values ])
    auto = [ value for value in values if ilevel1[dlevel1[value]] == 6 ]

def explore():
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

def explore():
    count = 0
    for item in data:
        category_id = item["category_id"]
        if category_id != "1000018296": continue
        count += 1
        if count == 1000: break
        product_id = item["_id"]
        for index, img in enumerate(item["imgs"]):
            picture = imread(io.BytesIO(img["picture"]))
            filename = "{}-{}-{}.png".format(category_id, product_id, index+1)
            print(filename)
            plt.imsave(path+"pic/"+filename, picture)

def dir_all():
    import os
    cat_name = pd.read_csv(path+cat_name_file)
    for index, content in cat_name.iterrows():
        dir_name = path+"pic/"+"/".join([level.strip().replace("/", "-").replace('"', '') for level in content[1:]])
        print(dir_name)
        os.makedirs(dir_name, exist_ok=True)

def cat_all_pic():
    cat_name = pd.read_csv(path+cat_name_file)
    dcat = {}
    for index, content in cat_name.iterrows():
        dir_name = path+"pic/"+"/".join([level.strip().replace("/", "-").replace('"', '') for level in content[1:]])
        #dcat["{}".format(content[0])] = dir_name
        dcat[content[0]] = dir_name
    data = bson.decode_file_iter(open(path+train_file, "rb"))
    for count, item in enumerate(data):
        if count % 1000 == 0: print(count)
        product_id = item["_id"]
        category_id = item["category_id"]
        for index, img in enumerate(item["imgs"]):
            picture = imread(io.BytesIO(img["picture"]))
            filename = "{}-{}-{}.png".format(category_id, product_id, index+1)
            plt.imsave(dcat[category_id]+"/"+filename, picture)

