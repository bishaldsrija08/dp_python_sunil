# Boolean masking is a powerful technique in NumPy that allows you to filter elements of an array based on a condition. When you apply a condition to an array, it returns a boolean array of the same shape, where each element is True if the condition is met and False otherwise. You can then use this boolean array to index the original array and retrieve only the elements that satisfy the condition.

import numpy as np

arr = np.array([10, 20, 30, 40, 50])
result = arr+5
print(result)

print(arr[arr<25])
print(arr[arr%20==0])
print(arr[arr%2==0])