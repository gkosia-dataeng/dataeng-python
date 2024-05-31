'''
    Passing an iterable item (list, tuple, generator) with * to a function will unpack and pass individual item as param
    Passing a dict with ** to a function will unpack the dict to keyword arguments
'''

def foo(x,y,z):
    print(f"x: {x}, y: {y}, z: {z}")

# unpack positional arguments
params = (1,2,3)
foo(*params)


# unpack keyword arguments
di = {'x':5, "y":6, "z":7}
foo(**di)
