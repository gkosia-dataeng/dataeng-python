# %% 
import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

# union two arrays
print(np.vstack([a,b]))

# merge two arrays
print(np.hstack([a,b]))

# reshape
print(a.reshape(3,1))
# %%
