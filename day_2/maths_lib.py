import math
print(math.pi)
print(math.pow(4,2))
print(math.sqrt(16))
print(math.ceil(4.1))
print(math.floor(4.9))
print(math.factorial(5))
print(math.gcd(30, 20))
print(math.lcm(4,6))
print(math.sin(math.radians(90)))
print(math.cos(math.radians(0)))
print(math.tan(math.radians(45)))
print(math.log10(1000))
print(math.exp(2))
print(math.radians(90))
print(math.degrees(math.pi/2))
print(math.isqrt(29), "Integer Square Root of 29")
print(math.comb(5, 2))  # Combination: 5 choose 2
print(math.perm(5, 2))  # Permutation: 5 permute 2
print(math.dist((1,2), (4,6)))  # Distance between two points

# underroot a+b whole square
a = 3
b = 4
result = math.sqrt(math.pow((a+b), 2))
print(result)