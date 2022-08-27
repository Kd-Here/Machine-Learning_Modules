import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Start to 4not include 
print(arr[:4])

# Till end
print(arr[1:])

# Steps
print(arr[1::2])

# -ve slicing
# print(arr[-4:-1],reversed=True)


arr2D = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr2D[0:,1:])
# 0: means select from first to second arrays , means slicing of both array from 1st element to last

print(arr2D[0:2,::2])
# 0:2 means taking both arry and ::2 means start to end with steps 2


# for better understanding
# https://towardsdatascience.com/slicing-numpy-arrays-like-a-ninja-e4910670ceb0
print(arr2D[1,2:4])