myset = {"apple", "banana", "cherry", "mango", "orange", "kiwi", "grape"}
tropical = {"pineapple", "mango", "papaya"}


myset.add("watermelon")
myset.add("papaya")

myset.update(tropical)

myset.remove("banana")
myset.discard("apple")
myset.pop()
myset.clear()
del myset
print(myset)

