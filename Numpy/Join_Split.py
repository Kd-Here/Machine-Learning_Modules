import numpy as np

import cv2
print("To check version of opencv",cv2.__version__)



arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))


ad = np.concatenate((arr1, arr2))

print(ad)
print(arr)



# Split -----------------------------------------------


arr = np.array([1, 2, 3, 4, 5, 6])
ad=np.array_split(arr,4)
print(ad)
print(ad[0])
print(ad[3])
print(ad[1])
print(ad[2])
# split the aray in 4 parts