# Julian Conneely 28/03/18
# Iris data set, Exercise 5

# With knows files, auto closes so no need to close

with open("data/iris.csv") as f: # create a block of python code with f as the name of the file that is open (iris.csv)
  for line in f:                 # loop through the lines in f 
    
    # splits out and print elements 0 to 3 of f
    # assigns 3 spaces to each element, with 2 spaces assigned for the decimal and one for the space between columns
    print('{:3} {:3} {:3} {:3}'.format(line.split(',')[0], line.split(',')[1], line.split(',')[2], line.split(',')[3]))     

import statistics
#statistics.mean([0, 1, 2, 3])
#print("The mean of column 1 is:",statistics.mean(0))