import numpy as np 
import matplotlib.pyplot as plt
from numpy.random import randn


#set one side of the grid

points = np.arange(-5,5,0.01)

#points x points grid

dx, dy = np.meshgrid(points,points)

print(dx)
print(dy)

z = (np.sin(dx) + np.sin(dy))

print(z)

# plt.imshow(z);

# plt.colorbar()
# plt.title("Plot for sin(x) + sin(y)")
# plt.show()


A = np.array([1,2,3,4])
B = np.array([100,200,300,400])

condition = np.array([True,True,False,False])

answer = [(A_val if cond else B_val) for A_val, B_val, cond in zip(A,B,condition)]


print(answer)

answer2 = np.where(condition, A,B)

print(answer2)

arr = randn(5,5)

print(arr)

result = np.where(arr<0, 0, arr)

print(result)

arr = np.array([[1,2,3], [4,5,6], [7,8,9]])


print(arr.sum())

