from functools import partial, Counter

# partial: always call the function with 5,7 as the first two arguments
add_always_five_seven = partial(lambda x,y,z: x+y+z,5, 7)
print(add_always_five_seven(11))


