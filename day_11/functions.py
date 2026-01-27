"""
Functions are those code blocks that perform specific tasks and can be reused throughout the program.

Syntax for defining a function in Python:
def function_name(parameters):
    functio_body
    return value

Types of Functions:
1. Functins without parameters and without return value
2. Functions with parameters and without return value
3. Functions without parameters and with return value

Built-in Functions vs User-defined Functions:
- Built-in Functions: These are pre-defined functions provided by Python, such as print(), len(), type(), etc.
- User-defined Functions: These are functions created by the user to perform specific tasks as per their needs.
"""

# 1. Functions without parameters and without return value

def greet(): # function definition
    print("Hello, welcome to the world of functions!") # function body

greet() # function call
greet()
greet()

# 2. Functions with parameters and without return value

def sum(a,b): # function definition with parameters
    result = a + b # function body
    print("The sum is:", result)

sum(5,6) # function call with arguments

# 3. Functions with parameters and with return value

def multiply(x,y): # function definition with parameters
    return x * y # function body with return value

result = multiply(4,5) # function call with arguments
result_2 = multiply(7,3)
print("The product is:", result_2)
print("The product is:", result)

# WAP to make a function that print somethng.
# value = "Hello World!"

def bishal(value):
    print(value)

# bishal("Hello World!")