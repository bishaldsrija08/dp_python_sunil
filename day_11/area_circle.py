# WAP to calclulate area of cirecle.

def area(r):
    pi = 3.14
    return pi * r ** 2

radius = float(input("Enter the radius of the circle: "))
# radius = 5

result = area(radius)

print(f"The area of the circle with radius {radius} is: {result}")