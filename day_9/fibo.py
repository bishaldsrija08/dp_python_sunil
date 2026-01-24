# 4. WAP to print the Fibonacci series up to n terms using for for [0 1 1 2 3 5 8 13.....]

n = int(input("Enter the number of terms for Fibonacci series: "))

a, b = 0, 1
print(a, b, end=" ")
for i in range(n):
    c = a + b
    print(c, end=" ")
    a = b
    b = c

# 0 1 1 2 3 5


# Asignment Q.no. 1

# 4. WAP to print the Fibonacci series up to n terms using for loop
# Fibonacci series: 0 1 1 2 3 5 8 13 ...

# Take input from the user
n = int(input("Enter the number of terms for Fibonacci series: "))

# Initialize first two terms
a, b = 0, 1

# Check if n is valid
if n <= 0:
    print("Please enter a positive number.")
elif n == 1:
    print(a)
else:
    # Print the first two terms
    print(a, b, end=" ")

    # Generate remaining terms
    for i in range(n - 2):
        c = a + b
        print(c, end=" ")
        a = b
        b = c
