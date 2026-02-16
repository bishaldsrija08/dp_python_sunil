import numpy as np

arr = np.array([1,2,3,4,5])

new_arr = np.insert(arr, 2, 10, axis=0) # Insert 10 at index 2
print(new_arr)