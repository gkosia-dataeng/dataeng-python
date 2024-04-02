import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,20,30,40,50]

fig = plt.figure()

# a grid with 6 rows and 1 column
# the plot start from 0,0
# the plot takes 2 rows and 1 column
ax1 = plt.subplot2grid((6,1),(0,0),rowspan=1, colspan=1)
ax2 = plt.subplot2grid((6,1),(1,0),rowspan=3, colspan=1, sharex=ax1)
ax3 = plt.subplot2grid((6,1),(4,0),rowspan=2, colspan=1, sharex=ax1)

ax1.plot(x,y)
ax2.plot(x,y)
ax3.plot(x,y)
plt.show()