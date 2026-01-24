"""
1234 => 1+2+3+4 = 10
"""

num = int(input("Enter a number: "))
sum = 0

while num!=0:
    # extract last digit
    last = num % 10
    
    # add last digit to sum => Main logic
    sum = sum + last
    
    # remove last digit
    num = num // 10

print("Sum of digits is:", sum)