# Iterating through 

import numpy as np

arr = np.array([1, 2, 3])
for x in arr:
  print(x)


ad = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in ad:
  print("x represents the 2-D array:")
  print(x)



vs = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(vs):
  print(x)


for idx, x in np.ndenumerate(vs):
  print(idx, x)
