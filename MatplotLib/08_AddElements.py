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
ax1.plot(x1,y1,0)

ax1.text(2,5,'Text at 2,5')

ax1.annotate('Bad news', (2,4), xytext=(0.8,0.9), textcoords='axes fraction',arrowprops=dict(facecolor='grey', color='grey'))
plt.show()