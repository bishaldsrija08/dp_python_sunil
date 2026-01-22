""" "
While loop syntax:

initialization
while condition:
    # code block to be executed
    increment/decrement
"""

# WAP to print your name 5 times using for loop

i = 1  # initialization
while i <= 5:  # condition
    print("Bishal Rijal")
    i = i + 1  # increment

# WAP to print numbers from 1 to 10 using while loop

i = 1  # initialization
while i <= 10:  # condition
    print(i, end=" ")
    i = i + 1  # increment

# WAP to print 10 to 1 using while loop
i = 10  # initialization
while i >= 1:  # condition
    print(i, end=" ")
    i = i - 1  # decrement

# WAP to print even numbers from 1 to 20 using while loop

i = 2  # initialization
while i <= 20:  # condition
    print(i, end=" ")
    i = i + 2  # increment

# WAP to print odd numbers from 1 to 20 using while loop
i = 1  # initialization
while i <= 20:  # condition
    print(i, end=" ")
    i = i + 2  # increment

# WAP to print sum of first 10 natural numbers using while loop

i = 1  # initialization
sum = 0
while i <= 10:  # condition
    sum = sum + i
    i = i + 1  # increment
print("Sum is:", sum)

# WAP to print multiplication table of a given number using for loop

num = int(input("Enter a number to print its multiplication table: "))
i = 1  # initialization
mul = 1
while i <= 10:  # condition
    mul = num * i
    print(f"{num}x{i}={mul}")
    i = i + 1  # increment

# WAP to print factorial of a given number using while loop
# 5! = 5x4x3x2x1=120
num = int(input("Enter a number to find its factorial: "))
i = 1  # initialization
fact = 1
while i <= num:  # condition
    fact = fact * i
    i = i + 1  # increment
print(f"Factorial of {num} is: {fact}")


# WAP to print the sum of all even numbers from 1 to 50 using while loop

i = 2 # initialization
sum = 0
while i<=50: # condition
    sum = sum + i
    i = i + 2 # increment
print("Sum of all even numbers from 1 to 50 is:", sum)

# WAP to print the sum of all odd numbers from 1 to 50 using while loop