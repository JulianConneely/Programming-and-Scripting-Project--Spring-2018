# Julian Conneely 27/04/18

#  Section A - Using numpy Calculate the mean of each column

import numpy
#read data file into array
data = numpy.genfromtxt('data/iris.csv', delimiter=',')

firstcol = (data[:,0]) # select all of the values in the first column of the numpy array
meanfirstcol = numpy.mean(data[:,0]) #use numpy mean function

secondcol = (data[:,1])
meansecondcol = numpy.mean(data[:,1])

thirdcol = (data[:,2])
meanthirdcol = numpy.mean(data[:,2])

fourthcol = (data[:,3])
meanfourthcol = numpy.mean(data[:,3])

print("The mean of first column is: ",meanfirstcol)
print("The mean of second column is: ",meansecondcol)
print("The mean of third column is: ",meanthirdcol)
print("The mean of fourth column is: ",meanfourthcol)

# Section B - Using matplotlib.pyplot to generate a barplot
import matplotlib.pyplot as pl
pl.hist(firstcol)
pl.show()
