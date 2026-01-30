data = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(data, "before change")


data.remove("kiwi") # remove by value
data.pop(0) # remove by index
del data[2] # remove by index using del
data.clear() # remove all items

print(data, "after change")