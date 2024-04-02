import matplotlib.pyplot as plt

x1 = [2,4,6,8,10]
y1 = [3,6,7,8,9]

x2 = [3,5,7,9,11]
y2 = [4,5,6,7,8]

plt.bar(x1,y1,label='Bar1', color='blue')
plt.bar(x2,y2,label='Bar2', color='red')

plt.xlabel('x')
plt.ylabel('y')
plt.title("Bar chart")
plt.show()