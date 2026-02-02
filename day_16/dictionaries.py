name = "Bishal Rijal"
age = 24
address = "Kathmandu, Nepal"
education = "Bachelor's in Computer Science"


# Dictionaries
# Dictionaries stores data in key-value pairs
# CRUD = Create, Read, Update, Delete

person = {
    "name": "Bishal Rijal",
    "age": 24,
    "address": "Kathmandu, Nepal",
    "education": "Bachelor's in Computer Science",
    "is_student": False,
    "skils": ["Python", "Java", "C++"],
    "details": {
        "height": "5.9 ft",
        "weight": "70 kg"
    }
}

print(person["name"])

for key, value in person.items():
    print(f"{key}: {value}")
   

for x in person:
    print(f"{x}: {person[x]}")
    
    
print(person["details"]["height"])


print(person.items())