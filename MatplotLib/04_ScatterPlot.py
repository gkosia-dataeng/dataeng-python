import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9]
y = [18,25,30,35,36,40,47,49,50]
size = [10,20,40,40,60,20,10,10,10]

plt.scatter(x,y,label='age', color='red', marker='*', s=size)

plt.title("Scatter plot chart")
plt.show()