
# WAP to print sum of first 10 natural numbers using for loop
# 1+2+3+4+5+6+7+8+9+10 = 55
sum = 0
for i in range(1, 11, 1):
    print(i, end = " ")
    sum = sum + i
print("\nSum of first 10 natural numbers is:", sum)