# Programming-and-Scripting-Project--Spring-2018
Julian Conneely, 2018-04-11\
*This repository contains Python code\
*Download Anaconda here https://www.anaconda.com/download/ to run the Python script(s)\
*I recommend you run these scripts in Visual Studio Code


# Project Plan
Incremental tasks checklist to be completed on the way to project completion
- [x] Research background information about the data set and write a summary of it
- [ ] Keep a list of references used in completing the project
- [ ] Download the data set and write some Python code to investigate it
- [ ] Summarise the data set using a Python script e.g. calculating the maximum, minimum and
mean of each column of the data set
- [ ] Write a summary of investigations
- [ ] Include supporting tables and graphics as necessary


# Background and Summary of the Data Set

A data set is a collection of data. Most commonly a data set corresponds to the contents of a single database table, or a single statistical data matrix, where every column of the table represents a particular variable, and each row corresponds to a given member of the data set in question. [7] The Iris flower data set is considered a classic data set for use in statistics.

The Iris data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper *'The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis'.* [1]

![Ronald Fisher](ronald-fisher.png)
[6]

Multivariate analysis (MVA) is based on the statistical principle of multivariate statistics, which involves observation and analysis of more than one statistical outcome variable at a time. In design and analysis, the technique is used to perform trade studies across multiple dimensions while taking into account the effects of all variables on the responses of interest. [2]

The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). Four features were measured from each sample: the length (column 1) and the width (column 2) of the sepals; the length (column 3) and the width (column 4) of the petals in centimetres. Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other. [1]

It includes three Iris species with 50 samples each as well as some properties about each flower. One flower species is linearly separable from the other two, but the other two are not linearly separable from each other. [3]

If we look at the colour coded scatter plot below, a set of points is said to be linearly separable if there exists at least one line in the plane with all of the red points (Iris-setosa) on one side of the line and all the points (green Iris-versicolor and blue Iris-virginica) on the other side.


![iris](iris-machinelearning.png)
[5]


Colour coded Scatter Plot: Sepal Width vs. Sepal Length
![Colour coded Scatter Plot](http://www.pybloggers.com/wp-content/uploads/2015/09/ratherreadblog.comwp-contentuploads201509iris_scatter-9c511da385a5344b661e2153e84c28382116721d.png)
[4]

# Summary of investigations

Setup: \
Firstly all of the necessary Python libraries were imported to Python (see Section A of IrisProject.py script). \
Secondly I imported the Iris dataset to Python as a CSV file (see Section B of IrisProject.py script). \
Thirdly I used numpy to calculate the max, min and mean of each column ( (see IrisMax, IrisMin and IrisMean scripts). \
Fourthly I used matplotlib.pyplot to generate some graphs and visual representations of the data set. \

Analysis: \

I was unsure as to whether to use multiple different py scripts or to incorporate all into one.

I used Matplotlib to generate a barplot of the anatomical features of the Iris species, this barplot shows how the three species of Iris differ distinctly on the basis of their four anatomical features (see Section D of IrisProject script)

While calculating the max, min and the mean of each column is useful way of practising data analysis using Python libraries, it does not in my opinion provide particularly useful information that is meaningful in terms of analysing the Iris Data Set. Indeed looking at *Figure_1 Histogram of Iris Column 1.png* you can see that column 1 (sepal length in cm) of the Iris Data set has 3 distinct peaks (between 4.7 and 5.0cm; between 5.4 and 5.6cm; and between 6.1 and 6.5cm). An example of a much more insightful graphic display of the data set. This histogram was created using the matplotlib.pyplot library and utilising the pl.hist and pl.show commands (see section B of IrisMean.py)

A more useful set of data calculations to analyse would be the...

New learnings while completing this project: Using new Python libraries e.g. NumPy, Pandas, Matplotllib; Learning how to produce and create visual outputs e.g. histograms, scatter plots while also understanding the outputs; Calculating the min, max and values; Running iPython as an active terminal to test code and outputs before committing them to scripts; Learning new GitHUb functonality e.g. Markdown and the Issues tab.


# References
[1] https://en.wikipedia.org/wiki/Iris_flower_data_set \
[2] https://en.wikipedia.org/wiki/Multivariate_analysis \
[3] https://www.kaggle.com/uciml/iris \
[4] http://www.pybloggers.com/wp-content/uploads/2015/09/ratherreadblog.comwp-contentuploads201509iris_scatter-9c511da385a5344b661e2153e84c28382116721d.png \
[5] http://www.lac.inpe.br/~rafael.santos/Docs/R/CAP394/WholeStory-Iris.html \
[6] http://www.nndb.com/people/763/000196175/ \
[7] https://en.wikipedia.org/wiki/Data_set \
[8] 
