import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# plt1
plt.subplot(2, 4, 1)
plt.plot(x, y)
plt.title("INCOME")

x2 = [1, 2, 3, 4, 5]
y2 = [1, 20, 27, 64, 125]

# plt2
plt.subplot(2, 4, 2)
plt.plot(x2, y2)
plt.title("INCOME 2") 


x3 = [1, 2, 3, 4, 5]
y3 = [1, 8, 27, 64, 125]

# plt3
plt.subplot(2, 4, 3)
plt.plot(x3, y3)
plt.title("INCOME 3")

x4 = [1, 2, 3, 4, 5]
y4 = [1, 16, 81, 256, 625]

# plt4
plt.subplot(2, 4, 4)
plt.plot(x4, y4)

plt.suptitle("Subplots Example")
plt.show()