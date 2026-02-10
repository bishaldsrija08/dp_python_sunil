import matplotlib.pyplot as plt

x = ["A", "B", "C", "D"]
y = [3, 7, 5, 2]


plt.barh(x, y, color = "blue", height = 0.1)
plt.xlabel("Values")
plt.ylabel("Categories")
plt.title("Horizontal Bar Chart")
plt.show()