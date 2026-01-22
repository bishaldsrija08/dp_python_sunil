"""
1. for loop
syntax:
for variable in iterable (initialization; condition; increment/decrement):
    # code block to be executed
"""

# WAP to print your name 5 times using for loop

for i in range(1, 6, 1):
    print("Bishal Rijal")

# WAP to print numbers from 1 to 10 using for loop
for i in range(1, 11, 1):
    print(i)

# WAP to print 10 to 1 using for loop
for i in range(10, 0, -1):
    print(i)

# WAP to print even numbers from 1 to 20 using for loop
for i in range(2,21,2):
    print(i)

# WAP to print odd numbers from 1 to 20 using for loop
for i in range(1, 20, 2):
    print(i)

# WAP to print sum of first 10 natural numbers using for loop
# 1+2+3+4+5+6+7+8+9+10 = 55
sum = 0
for i in range(1, 11, 1):
    sum = sum + i
print("Sum of first 10 natural numbers is:", sum)

# WAP to print multiplication table of a given number using for loop
num = int(input("Enter a number to print its multiplication table: "))
# num =5
for i in range(1, 11, 1):
    mul = num * i
    print(f"{num}x{i}={mul}")

# WAP to print factorial of a given number using for loop
num = int(input("Enter a number to find its factorial: "))
# 5! = 5x4x3x2x1=120
fact = 1
for i in range(1, num+1, 1):
    fact = fact * i
print(f"Factorial of {num} is: {fact}")