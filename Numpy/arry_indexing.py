import numpy as np



# checking dimension number
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr.ndim)
# Count the numver of square brackets from (function paranthesis)


# Access 2-D Arrays
ad = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(ad[1,3],end="")



# Access 3-D Arrays
print(arr[1,0,1])


# -ve indexing arrays
print(arr[-1,0,-1])