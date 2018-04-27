# Julian Conneely 27/04/18
#  Using numpy Calculate the mimimum value of each column
import numpy
#read data file into array
data = numpy.genfromtxt('data/iris.csv', delimiter=',')

firstcol = (data[:,0]) # select all of the values in the first column of the numpy array
minfirstcol = numpy.min(data[:,0]) #use numpy min function

secondcol = (data[:,1])
minsecondcol = numpy.min(data[:,1])

thirdcol = (data[:,2])
minthirdcol = numpy.min(data[:,2])

fourthcol = (data[:,3])
minfourthcol = numpy.min(data[:,3])

print("The min of first column is: ",minfirstcol)
print("The min of second column is: ",minsecondcol)
print("The min of third column is: ",minthirdcol)
print("The min of fourth column is: ",minfourthcol)