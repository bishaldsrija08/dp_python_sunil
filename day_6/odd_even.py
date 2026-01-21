# WAP to check whether a number is odd or even.

num = int(input("Enter a number: "))

# % -> 5 % 2 = 1, anynumber % 2 ==0  -> even number else odd number

if num % 2 == 0: # check for even number
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")
    
"""
num = 5
5 % 2 = 1 (remainder)
1 == 0 -> False -> odd number
"""