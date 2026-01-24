# 3. WAP to print the reverse of a given number using for loop and check whether it is a palindrome or not.

"""
123 = 321
121 = 121 (palindrome)
MOM =MOM (palindrome)
"""

num = int(input("Enter a number to reverse: "))
og = num  # original number
rev = 0

while num!=0:
    # extract last digit
    last = num % 10
    
    # build reverse number => Main logic
    rev = rev * 10 +last #4, 43, 432, 4321
    
    # remove last digit
    num = num // 10

print("Reversed Number is:", rev)

# check palindrome
if rev == og:
    print(og, "is a Palindrome")
else:
    print(og, "is not a Palindrome")