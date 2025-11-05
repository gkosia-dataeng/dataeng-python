# %% 
import numpy as np

# %%
a = np.array([[1,2,3,4,5,6,7], [8,9,10,11,12,13,14]])

# %% 

# select specific element a[r,c]
# i can use slicer like lists
a[1,1]
a[1, :] # specific row
a[:,2] # specific column

a[0, 1:5:1]
# %%
# change element
a[1,2] = 99 # specific position
a[:,3] = -1 # the 3rd column or all rows
a[:,2] = [99,98] # the second column of all rows each value
print(a)
# %%
