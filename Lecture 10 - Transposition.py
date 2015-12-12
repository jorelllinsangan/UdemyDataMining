import numpy as np 


arr = np.arange(50).reshape((10,5))

print(arr)

arr.T


print(np.dot(arr.T, arr))


arr3d = np.arange(50).reshape((5,5,2))

print(arr3d)

print(arr3d.transpose(1,0,2))

arr = np.array([[1,2,3]])

print(arr)

arr = arr.swapaxes(0,1)

print(arr)