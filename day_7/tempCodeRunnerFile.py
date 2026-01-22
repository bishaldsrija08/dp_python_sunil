# WAP to print factorial of a given number using for loop
num = int(input("Enter a number to find its factorial: "))
# 5! = 5x4x3x2x1=120
fact = 1
for i in range(1, num+1, 1):
    fact = fact * i
print(f"Factorial of {num} is: {fact}")