import matplotlib.pyplot as plt

x = [80, 85, 90, 95, 100, 105, 110, 115, 120, 125]
y = [240, 250, 260, 270, 280, 290, 300, 310, 320, 330]


font1 ={
    'family':'serif',
    'color':'blue',
    'size':20
}

font2 ={
    'family':'serif',
    'color':'darkred',
    'size':15
}

plt.plot(x,y)
plt.title('Sports data', fontdict=font1)
plt.xlabel('X-axis', fontdict=font2)
plt.ylabel('Y-axis', fontdict=font2)
plt.show()