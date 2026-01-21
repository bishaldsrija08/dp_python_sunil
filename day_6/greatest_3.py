# WAP to check greatest of three numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a==b and b==c and a==c:
    print("All numbers are equal")
elif a>b and a>c:
    print(f"{a} is the greatest number")
elif b>a and b>c: # elif means else if helps to check another condition if the first condition is false
    print(f"{b} is the greatest number")
else:
    print(f"{c} is the greatest number")

"""
a=1, b=2, c =3
1>2 and 1>3 => false
2>1 and 2>3 => false
c=3 is the greatest number


a=3, b=2, c =1

3>2 and 3>1 => true

a=2, b=3, c=1
2>3 and 2>1 => false
3>2 and 3>1 => true
"""