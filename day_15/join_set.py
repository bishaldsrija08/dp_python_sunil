set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

# Union of two sets
set3 = set1.union(set2)
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3, "c", "d"}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

set5 = set1.union(set2, set3, set4)
print(set5)


set1 = {"a", "b", "c"}
set2 = {1, 2, 3, "c", "d"}

setx = set1.intersection(set2)
print(setx)  # Output: {'c'}