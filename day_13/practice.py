data = []

# add items
data.append("apple")
data.append("banana")
data.append("cherry")
data.append("date")
data.append("elderberry")

# Change an item
data[2] = "blackcurrant"

# Remove an item
del data[0]

# Get all
for x in data:
    print(x)

# clear all
data.clear()

print(data)