import matplotlib.pyplot as plt

x = [1,2,3,4]

teama = [1,2,3,4]
teamb = [2,3,4,5]
teamc = [5,6,7,8]


# an empty plot to add legend 
plt.plot([],[],color='red', label='teama')
plt.plot([],[],color='black', label='teamb')
plt.plot([],[],color='orange', label='teamc')
plt.legend()


# canot have legent on stackplot
plt.stackplot(x,teama,teamb,teamc, colors=['red', 'black', 'orange'] )
plt.show()