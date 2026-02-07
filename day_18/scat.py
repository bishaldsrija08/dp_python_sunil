import matplotlib.pyplot as plt

# Example data (dummy data for learning)
areas = ["Bharatpur", "Ratnanagar", "Kalika", "Khairahani", "Madi"]
voter_density = [1200, 850, 600, 950, 300]   # voters per km²

# Convert area names to positions
x_pos = range(len(areas))

plt.figure(figsize=(8,5))

# Scatter plot
plt.scatter(x_pos, voter_density, color='blue', marker='o')

# Labels
plt.xlabel("Chitwan Areas")
plt.ylabel("Voter Density (per km²)")
plt.title("Chitwan District Voter Density Scatter Plot")

# Show area names on x-axis
plt.xticks(x_pos, areas)

# Grid
plt.grid(axis='y')

plt.show()
