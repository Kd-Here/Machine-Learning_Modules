import numpy as np



arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)
# TO check the shape of elements of array



ad=np.array([1,2,3,4,5,6,7,8,9] ,ndmin=5)
print(ad.shape)


# Reshape chaning shape of array frrom 1d to 3d
new_pa = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

#reshape is used to 2 arrays that contains 3 arrays, each with 2 elements 
newarr = new_pa.reshape(2, 3, 2)
print(newarr)

# 2 arrays that contains 3 arrays, each with if we don't have one element we will use -1 for unkonw place
ps=new_pa.reshape(2,3,-1)
print(ps)