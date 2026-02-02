thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"] # Access key
print(x)

# Access key
x = thisdict.get("model")
print(x)

# keys
x = thisdict.keys()
print(x)

# Values
x = thisdict.values()
print(x)