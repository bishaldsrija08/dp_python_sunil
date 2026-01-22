num = int(input("Enter a number to find its factorial: "))
i = 1  # initialization
fact = 1
while i <= num:  # condition
    fact = fact * i
    i = i + 1  # increment
print(f"Factorial of {num} is: {fact}")