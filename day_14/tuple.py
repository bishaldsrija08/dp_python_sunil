


data = (1, 2, 3, 4, 5)
print(data[0])
print(data[-1], "is the last item")

# data[0]= 10 # This will raise a TypeError because tuples are immutable
# print(data)

# length of tuple
print(len(data))

# loop through tuple
for item in data:
    print(item)

# Range of indices
print(data[1:4])  # Slicing from index 1 to 3



thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

print(thistuple[2:])

# Type
print(type(thistuple))

# 