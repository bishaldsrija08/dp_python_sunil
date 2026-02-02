thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict.pop("model") # removes specific item
thisdict.popitem() # removes last inserted item
del thisdict["brand"] # Use [] to delete specific item

print(thisdict)