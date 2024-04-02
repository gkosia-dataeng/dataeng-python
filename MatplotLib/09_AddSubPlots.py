import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,20,30,40,50]

fig = plt.figure()


# vertica, horizontal, position
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(212)

ax1.plot(x,y)
ax2.plot(x,y)
ax3.plot(x,y)

plt.show()