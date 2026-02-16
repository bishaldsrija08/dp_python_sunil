import numpy as np

arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])

new_arr_2d = np.insert(arr_2d, 1, [10, 11, 12], axis=0) # Insert [10, 11, 12] as a new row at index 1
# axios=0 means we are inserting a new row, if it were axis=1, we would be inserting a new column
print(new_arr_2d)