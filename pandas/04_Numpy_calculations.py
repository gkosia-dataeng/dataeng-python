# %% 
import numpy as np

a = np.array([[1,2,3], [4,5,6]])
print(a)
# %%
# mathematics is applyied to all elements
print(a*2 )
# %%
# calculations between matrix is allowed when have the same shape
# calculation is applied on the same positions
b = np.full((2,3), 2)
b*a
# %%
# stats
print(a)
print(np.min(a)) # of all table
print(np.min(a,axis=0)) # aggregate rows, return a value for each column
print(np.min(a,axis=1)) # aggregate columns, return a value for each row


# %%
