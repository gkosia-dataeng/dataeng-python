# lambda

lmd = lambda x,y: x+y
print(lmd(2,3))



l = [1,2,3,4,5,6,7,8,9]

# map
def times2(x):
    return x*2

new_l = map(times2,l)
print(list(new_l))    # map return a map object so we have to convert it to a list,set,or duple

# reduce
def filter_evens(x):
    return x%2 == 0

evens_l = filter(filter_evens, l)
print(list(evens_l))


# reduce
from functools import reduce


# a is the accumulator and b is the current value
def sum(a,b):
    return a+b

sum_l = reduce(sum,l)
print(sum_l)