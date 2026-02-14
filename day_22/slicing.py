# slicing
"""
arr[start:stop-1: step]
"""
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[0:6:2])  # This will raise an error because arr is 1D

print(arr[:6])
print(arr[0:])
print(arr[::-1]) # This will reverse the array
print(arr[-2:-6:-1]) # This will print the last 4 elements in reverse order