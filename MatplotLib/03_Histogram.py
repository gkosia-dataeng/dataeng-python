import matplotlib.pyplot as plt

x1 = [18,25,30,35,36,40,47,49,50,55,56,60,66,70,75,77,78,79]

bins = [15,25,35,45,55,65,75,85]

plt.hist(x1,bins, histtype='bar', rwidth=0.8)

plt.title("Histogram chart")
plt.show()