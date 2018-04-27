# Julian Conneely 28-04-2018
# Iris Data Set project - Scatter plots
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

# Generate a scatterplot of the variables
# https://www.kaggle.com/farheen28/iris-dataset-analysis-using-knn
iris = sns.load_dataset("iris")
sns.FacetGrid(iris, hue="species", size=5).map(plt.scatter, "sepal_length", "sepal_width").add_legend() #Configuration of scatterplot
plt.show()
