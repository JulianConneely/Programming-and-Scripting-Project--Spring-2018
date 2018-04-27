# Julian Conneely 27/04/18
#  Using numpy Calculate the maximum value of each column
import numpy
#read data file into array
data = numpy.genfromtxt('data/iris.csv', delimiter=',')

firstcol = (data[:,0]) # select all of the values in the first column of the numpy array
maxfirstcol = numpy.max(data[:,0]) #use numpy max function

secondcol = (data[:,1])
maxsecondcol = numpy.max(data[:,1])

thirdcol = (data[:,2])
maxthirdcol = numpy.max(data[:,2])

fourthcol = (data[:,3])
maxfourthcol = numpy.max(data[:,3])

print("The max of first column is: ",maxfirstcol)
print("The max of second column is: ",maxsecondcol)
print("The max of third column is: ",maxthirdcol)
print("The max of fourth column is: ",maxfourthcol)