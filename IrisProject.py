# Julian Conneely 27/04/18

# Section A - Load libraries
import pandas as pd   # abbreviate library to simplify code
import numpy as np
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt


# Section B - Imported dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv(url, names=names)
print(dataset.head(50))
