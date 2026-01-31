data = ()

# Change it to list
data_list = list(data)
print(type(data_list))

# append
data_list.append(10)
data_list.append(20)

# insert
data_list.insert(1, 15)

# remove
data_list.remove(10)

# delete
del data_list[0]

# convert back to tuple
data = tuple(data_list)
print(data)
print(type(data))