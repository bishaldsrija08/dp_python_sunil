# lossless conversion from string to int
a = "6"
a = int(a)
a += 1
print(a)


# lossy conversion from float to int
b = 67.8
b = int(b)
print(b)


# lossless conversion from int to float
c = 56
c = float(c)
print(c)


# string to float
d = "45.67"
d = float(d)
print(d)

# float to string
e = 78.9
e = str(e)
print(e)


name = "Bishal"
name = int(name) # This will raise a ValueError
print(name)