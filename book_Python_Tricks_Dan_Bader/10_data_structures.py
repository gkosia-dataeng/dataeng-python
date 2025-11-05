## Dictionaries

# Standar python dictioanries
my_dict = {'a':1, 'b': 2}
another_dict = dict()
print(another_dict)

from collections import OrderedDict, defaultdict

# OrderedDict: remember the order inserted, if the order is important
ord_dict = OrderedDict(a = 2, b= 3)
ord_dict['fout'] = 4
print(f"ord_dict: {ord_dict}")
print(ord_dict.keys())

# defaultdict: return a value if key not found
# argument should be a callable (list, str, int, ...) and will return the default value
def_dict = defaultdict(int)
print(def_dict['gab'],def_dict['za'] )



## Arrays
# fixed size records accessed by index

# Lists
# mutable, dynamic array (not fixed sized), can store multiple type of data

ls = ["one", "two", "three"]
print(ls[1])

#Tuples
# immutable, objects defined at creation time, can store multiple type of data
tpl = "one", "two", "three"
print(tpl)

# str
# immutable array of characters
st = 'abc'
st = 'c'  # copy the element and modify value



# dict or map
# store objects mapped with a unique key
# no protection againsta wrong field names
car = {
     'color': 'red'
    ,'mileage': 3840    
}

print(car['color'])

car['birthdate'] = 123
print(car)

# named tuples
# are immutable, allows to defina fields names
from collections import namedtuple

Person  = namedtuple('Person', 'name age')
p = Person('gab', 30)
print(p)

# Or a better object
# build simple objects, allows type hint
from typing import NamedTuple

class Frouit(NamedTuple):
    name: str
    color: str

apple = Frouit('apple', 'red')
print(apple)


# Sets
# no order, unique elements collection
# used to check the existance of a value in a set or to union, intersect two sets

aset = {'a', 'b', 'c'}
bset = {a for a in range(10)}
emptySet = set()
print(aset, bset)
print('q' in aset)
aset.add('q')
print(len(aset))

# Multisets
# Counter: its a set that keep track how many times inserted a value in the set
from collections import Counter

cnt = Counter()
odds = {2,4,6}
more_orrds = {4,6,8}

cnt.update(odds)
print(cnt)

cnt.update(more_orrds)
print(cnt)