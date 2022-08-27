# First install numpy with pip:-
# pip install numpy

# If already installed check version
import numpy 
print(numpy.__version__)


ad=numpy.array([1,2,3,4,5,6,7,8,9,10])
# here we are passing list in array
print(ad)



import numpy as np 
ada=np.array((1,2,3,4,5,6,7,8,9,10))
# here we are passing tuple in python
print(ada)


d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(d.ndim)
# To see dimension of arrary


arr = np.array([1, 2, 3, 4], ndmin=5)
# this creates an array of dimension 5
print(arr)