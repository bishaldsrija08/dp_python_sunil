# Aggregate functions in NumPy are used to perform operations on arrays and return a single value. These functions include sum, mean, median, standard deviation, minimum, maximum, and variance. Here is an example of how to use these aggregate functions with a NumPy array:

import numpy as np
import statistics

arr = np.array([10, 20, 30, 40, 50])

print(arr.sum()) # Sum of all elements
print(arr.mean()) # Average
print(arr.std()) # Standard deviation
print(arr.min()) # Minimum value
print(arr.max()) # Maximum value
print(arr.var()) # Variance
print(statistics.median(arr)) # Median value (requires scipy)

print(np.sum(arr)) # Sum of all elements
print(np.mean(arr)) # Average
print(np.std(arr)) # Standard deviation
print(np.min(arr)) # Minimum value
print(np.max(arr)) # Maximum value
print(np.var(arr)) # Variance
print(np.median(arr)) # Median value