import numpy

pythonArray = [[1,2,3], [9,8,7]]

# convert python array to numpy array
npArray = numpy.array(pythonArray)

# print the dimensions of the data
print(npArray.shape)

# print first row
print(npArray[0])

# print first column
print(npArray[:, 1])
