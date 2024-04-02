import matplotlib.pyplot as plt
import numpy as np

# get reference to figure in order to customize it
fig = plt.figure()

# set the figure to grid allows to have more than one plots
# (1,1): the shape of the grip
# (0,0): the position of the ax1 subplot
ax1 = plt.subplot2grid((1,1), (0,0))



x1 = [1,2,3,4]
y1 = np.array([5,7,4,8])
ax1.plot(x1,y1)

# 
# x1: what datapoints
# y1: until what value
# 6: from where to start on y until the line
# where: rule to select 
ax1.fill_between(x1,y1,5, where=(y1 > 5), color='g', alpha=0.3)
ax1.fill_between(x1,y1,5, where=(y1 < 5), color='r',alpha=0.3)

# iterate over the lables of the x axis and make something
for label in ax1.xaxis.get_ticklabels():
    print(label)

plt.subplots_adjust(left=0.09, bottom=0.2, right=0.93, wspace=0.2, hspace=0)
plt.title('Subplots')
plt.show()
