# WAP to check smallest of three numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a==b and b==c and a==c:
    print("All numbers are equal")
elif a<b and a<c:
    print(f"{a} is the smallest number")
elif b<a and b<c: # elif means else if helps to check another condition if the first condition is false
    print(f"{b} is the smallest number")
else:
    print(f"{c} is the smallest number")
