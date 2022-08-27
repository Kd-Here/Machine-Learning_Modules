# NumPy Searching Arrays
# You search for element in array and you will get a index as return

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
y = np.where(arr%2 == 0)
z = np.where(arr%2 == 1)
print(x)
print(y)
print(z)



# ----------------------------------------------Search sorted
# It returns the index where number should inserted to maintain soerting order:-

arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2,3,4])
print(x)


# ----------------------------------------Sorting 


arr=np.array((2,3,5,6,7,8,9,1,4))
asd=np.sort(arr)


arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))





print("\n Learning Filter:-")
# ----------------------------------------filter
# Filter will only put value at output which are True

import numpy as np

arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newarr = arr[x]

print(newarr)


# Other way to print all even number
y=[]
for i in arr:
    if i%2==0:
        y.append(i)
print(f'Only the even numbers in arrays:- {y}')



filter_arr = arr > 42
newarr = arr[filter_arr]

print(filter_arr)
print(newarr)