thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

# thistuple[0]= "Grapes"
# print(thistuple)

# change tuple to list
this_list = list(thistuple)
print(this_list, type(this_list))

# changes to list
this_list[0] = "Grapes"
this_list.append("Pineapple")
this_list.insert(1, "Strawberry")
this_list.remove("kiwi")
del this_list[2]

# convert back to tuple
thistuple = tuple(this_list)
print(thistuple, type(thistuple))