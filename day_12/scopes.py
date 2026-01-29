# Scope in Python
num1 = 10
def abc():
    num2 =20
    print("Hello, World!")
    print(num1, "from outside the function")
    print(num2, "from inside the function")

abc()
print(num2, "from outside the function") # This will raise an error because num2 is not defined in this scope