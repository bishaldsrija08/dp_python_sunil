import numpy as np
# Array is a data structure that can hold more than one value at a time. It is a collection of items stored at contiguous memory locations. The idea is to store multiple items of the same type together. This makes it easier to calculate the position of each element by simply adding an offset to a base value, i.e., the memory location of the first element of the array (generally denoted by the name of the array). The offset is typically the index of the element multiplied by the size of each element.

arr = np.array([1, 2, 3, 4, 5])
print(type(arr))

print(np.__version__)