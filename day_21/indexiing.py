import numpy as np

arr = np.array([[10, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0][0] + arr[0][1])

print(arr[0][0]+arr[1][4])

print(arr[0,1])
print(arr[1,3])

# 3d array
arr3d = np.array([[[1, 2, 3], [4,5,6]], [[7, 8, 9], [10, 11, 12]], [[13, 14, 15], [10, 11, 12]]])

print(arr3d[-2][0][-2])