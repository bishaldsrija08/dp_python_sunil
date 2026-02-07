import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x,y, marker = 'o', linestyle = 'dashed', color = 'blue')
plt.title('Prime Numbers')
plt.xlabel('Index')
plt.ylabel('Value')
plt.grid(axis='y', linestyle='--')
plt.show()