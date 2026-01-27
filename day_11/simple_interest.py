# WAP to calculate the simple interest using the formula SI = (P * R * T) / 100 using functions.
p = float(input("Enter the principal amount: "))
t = float(input("Enter the time in years: "))
r = float(input("Enter the rate of interest: "))

def si(p,t,r):
    return (p * r * t) / 100

result = si(p,t,r)
print("The simple interest is:", result)