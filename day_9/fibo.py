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