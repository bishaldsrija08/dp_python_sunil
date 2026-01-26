# Nested loop is a loop inside another loop.

for i in range(3): # Outer loop
    for j in range(2): # Inner loop
        for k in range(2): # Innermost loop
            print(f"Outer loop iteration {i}, Inner loop iteration {j}, Innermost loop iteration {k}")