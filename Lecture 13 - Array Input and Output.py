import numpy as np

arr = np.arange(5)

print(arr)

np.save('myarray',arr)

arr = np.arange(10)

print(arr)

np.load('myarray.npy')

arr1 = np.load('myarray.npy')
print(arr1)

arr2 = arr

np.savez('ziparray.npz', x=arr1, y=arr2)


archive_array = np.load('ziparray.npz')

print(archive_array['x'])
print(archive_array['y'])


arr = np.array([[1,2,3],[4,5,6]])
print(arr)

np.savetxt('arraytext.txt', arr,delimiter= ',')


arr = np.loadtxt('arraytext.txt', delimiter = ',')

print(arr)