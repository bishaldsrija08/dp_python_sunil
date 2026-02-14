import numpy as np

arr = np.array([1, 2, 3, 4])
arr_float = np.array([1.0, 2.0, 3.0, 4.0])
names = np.array(['Alice', 'Bob', 'Charlie', 'David'])
print(names.dtype) # Output: <U7 (or similar, depending on the system)
print(arr_float.dtype)
print(arr.dtype) # Output: int64 (or int32 depending on the system)