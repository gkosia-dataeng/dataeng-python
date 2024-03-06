'''
    Numpy use fixed types: so an array in numpy has integers 
                           in an array i can have only one data type
                           array stored in continusly memory

    Python data types are like structs: so for a list each element has  size, reference count, object type, object value
                                        also in python when we iterate over a list there is the type checking because in a list we can have multiple data types                                        

'''

# %% 
import numpy as np

# %%

a = np.array([1,2,3,4,5], dtype='int16')
print(a)
# %%
two_dim = np.array([[1,1,1],[2,2,2]])
print(two_dim)

# check how many dimensions is the array
print(two_dim.ndim)
#rows, cols
print(two_dim.shape)
#type and size
print(two_dim.dtype)
print(two_dim.itemsize)
print(two_dim.size * two_dim.itemsize)
# %%
