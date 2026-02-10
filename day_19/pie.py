import matplotlib.pyplot as plt

x= [1, 2, 3, 4]
y = ['A', 'B', 'C', 'D']

myexplode = [0, 0, 0, 0.3]
mycolors = ["black", "hotpink", "b", "#4CAF50"]

plt.pie(x, labels=y, autopct='%1.1f%%', startangle = 90, explode=myexplode, shadow = True, colors=mycolors)
plt.legend()
plt.show()