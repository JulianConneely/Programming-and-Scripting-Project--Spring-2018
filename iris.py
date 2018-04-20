# Julian Conneely 28/03/18
# Iris data set, Exercise 5

# With knows files, auto closes so no need to close

#1 Open Iris data set csv
with open("data/iris.csv") as f: # create a block of python code with f as the name of the file that is open (iris.csv)
  for line in f:                 # loop through the lines in f 
    
    # splits out and print elements 0 to 3 of f
    # assigns 3 spaces to each element, with 2 spaces assigned for the decimal and one for the space between columns
    print('{:3} {:3} {:3} {:3}'.format(line.split(',')[0], line.split(',')[1], line.split(',')[2], line.split(',')[3]))     

#2 Calculate mean for each colum, not working yet
import statistics
#statistics.mean([0, 1, 2, 3])
#print("The mean of column 1 is:",statistics.mean(0))

#3 Import via Pandas method to use DataFrame on CSV inc. with row numbers
import pandas  # load library
iris = pandas.read_csv("data/iris.csv") # the iris dataset is now a Pandas DataFrame
print(iris) # prints all 150 rows and 5 columns of iris dataset
