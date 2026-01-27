# WAP to calculate factoral of a number using function.
from math import factorial
def facto(n):
    if n == 0 or n ==1:
        return 1
    else:
        fact = 1
        for i in range(1, n+1):
            fact = fact * i
        return fact
num = int(input("Enter a number to find factorial: "))
result = facto(num)
print(f"The factorial of {num} is {result}.")

print("Using math module:", factorial(11))