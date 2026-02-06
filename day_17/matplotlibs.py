import matplotlib.pyplot as plt

x =  [1, 2, 3, 4, 5] # x values
y = [1, 4, 9, 16, 25] # y values

plt.plot(x, y, marker = "+") # plot the points
plt.xlabel("x values") # label for x-axis
plt.ylabel("y values") # label for y-axis
plt.title("Plot of y = x^2") # title of the plot
plt.show() # display the plot