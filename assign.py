import math

# Ask the user how far the summation should go
# Larger N = better accuracy, but slower computation
N = int(input("Enter value of N (e.g., 10, 20, 30): "))

M = 0.0  # Madelung constant sum

# Loop over the cubic lattice
for i in range(-N, N + 1):
    for j in range(-N, N + 1):
        for k in range(-N, N + 1):

            # Skip the origin (0,0,0) to avoid division by zero
            if i == 0 and j == 0 and k == 0:
                continue

            # Distance from origin
            r = math.sqrt(i**2 + j**2 + k**2)

            # Charge sign: alternating (+/-)
            sign = (-1) ** (i + j + k)

            # Add contribution to Madelung constant
            M += sign / r

# Print result
print(f"\nApproximate Madelung Constant (NaCl) for N={N}:")
print(M)