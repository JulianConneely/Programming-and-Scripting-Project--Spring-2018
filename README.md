# Programming-and-Scripting-Project--Spring-2018
Julian Conneely, 2018-04-11\
*This repository contains Python code\
*Download Anaconda here https://www.anaconda.com/download/ to run these exercises\
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
The Iris data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper *'The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis'.* [1]

![Ronald Fisher](ronald-fisher.png)
[6]

Multivariate analysis (MVA) is based on the statistical principle of multivariate statistics, which involves observation and analysis of more than one statistical outcome variable at a time. In design and analysis, the technique is used to perform trade studies across multiple dimensions while taking into account the effects of all variables on the responses of interest. [2].

The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). Four features were measured from each sample: the length and the width of the sepals and petals, in centimetres. Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other. [1]

It includes three Iris species with 50 samples each as well as some properties about each flower. One flower species is linearly separable from the other two, but the other two are not linearly separable from each other. [3]

![iris](iris-machinelearning.png)
[5]

The columns in this dataset are:

    Id
    SepalLengthCm
    SepalWidthCm
    PetalLengthCm
    PetalWidthCm
    Species


Colour coded Scatter Plot: Sepal Width vs. Sepal Length

![Colour coded Scatter Plot](http://www.pybloggers.com/wp-content/uploads/2015/09/ratherreadblog.comwp-contentuploads201509iris_scatter-9c511da385a5344b661e2153e84c28382116721d.png)
[4]

# Summary of investigations

Firstly all of the necessary Python libraries were imported to Python (see Section A of project.py script). \
Secondly I imported the Iris dataset to Python as a CSV file (see Section B of project.py script). \
Thirdly....

While calculating the max, min and the mean of each column is useful way of practising data analysis using Python libraries, it does not in my opinion provide any useful information that is meaningful in terms of analysing the Iris Data Set. 

A more useful set of data calculations to analyse would be the...


# References
[1] https://en.wikipedia.org/wiki/Iris_flower_data_set \
[2] https://en.wikipedia.org/wiki/Multivariate_analysis \
[3] https://www.kaggle.com/uciml/iris \
[4] http://www.pybloggers.com/wp-content/uploads/2015/09/ratherreadblog.comwp-contentuploads201509iris_scatter-9c511da385a5344b661e2153e84c28382116721d.png \
[5] http://www.lac.inpe.br/~rafael.santos/Docs/R/CAP394/WholeStory-Iris.html \
[6] http://www.nndb.com/people/763/000196175/ \
