import matplotlib.pyplot as plt

# data
x1 = [1,2,3]
y1 = [5,7,4]

x2 = [2,4,6]
y2 = [5,6,8]

# visualization
plt.plot(x1,y1, label= 'first line')
plt.plot(x2,y2, label= 'Second line')
plt.xlabel('Axis x',)
plt.ylabel('Axis y')
plt.title('Simple Line chart')
plt.show()