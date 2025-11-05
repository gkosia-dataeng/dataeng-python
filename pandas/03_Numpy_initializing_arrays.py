# %%
import numpy as np

# initialize with zeros, once
# schema
np.zeros((2,5),'int')

# initialize with other number
np.full((2,3),-99)
# %%
# random numbers
np.random.rand(2,3) # r,c
np.random.randint(30,90, size=(3,4)) # max number, shape
# %%
# copy arrays

a = np.array([1,2,3,4])
b = a # reference to the same location of a
b[2] = 99
print(a)

# to create a copy instance
b = a.copy()
b[:] = -1
print(a)
print(b)
# %%
