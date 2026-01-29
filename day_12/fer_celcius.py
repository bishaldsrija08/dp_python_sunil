
# WAP to convert Fahrenheit to Celsius using function.

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5.0/9.0
    return celsius

print("The temperature in Celsius is:", fahrenheit_to_celsius(100))
print("The temperature in Celsius is:", fahrenheit_to_celsius(32))
print("The temperature in Celsius is:", fahrenheit_to_celsius(212))