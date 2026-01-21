# WAP to check whether a number is positive, negative or zero.


"""
Logic:
0 = zero
any>0 = positive
any<0 = negative
"""

num = float(input("Enter a number: "))

if num ==0:
    print("The number is zero")
elif num>0:
    print("The number is positive")
else:
    print("The number is negative")
    
    
"""
num = 0
0==0 = true => zero

num = 5
5==0 => false
5>0 => true => positive

num = -3
-3==0 => false
-3>0 => false => negative
"""