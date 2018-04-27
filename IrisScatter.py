# Julian Conneely 28-04-2018
# Iris Data Set project - Scatter plot
# Reference: https://machinelearningmastery.com/machine-learning-in-python-step-by-step/

# Load libraries
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import seaborn as sns


# Load dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv(url, names=names)

# scatter plot matrix
scatter_matrix(dataset)
plt.show()

