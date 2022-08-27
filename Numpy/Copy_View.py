import numpy as np
arr=np.array([1, 2, 3, 4])

# arr[0]=99
Copy=arr.copy()
arr[0]=99


# Changed element but it will not create change in copy becoz it' a copy of original before changing
print(Copy)
print(arr)


ad = np.array([1, 2, 3, 4, 5])


ad[4]=9899
pddp=ad.view()
# view  will shows what changes you did in original copy will not   

print(ad)
print(pddp)