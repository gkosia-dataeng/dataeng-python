from collections import defaultdict, namedtuple, Counter, ChainMap

# defaultdict
standar_dict = {}
try:
    print(standar_dict['aaa'])
except KeyError as e:
    print("Key not found in standar dict")

# get 0 or '' if the key not exists, with standar dict getting KeyError
d = defaultdict(str)
print(d['aaa'])


# namedtuple
Person = namedtuple('Person', ['name', 'age'])

p = Person('gab', 34)
print(f"I am nametuple Persion, my name is {p.name}, my age is {p.age}")


# counter: count hashable objects
word = 'missisipi'
c = Counter(word)
print(c)


# ChainMap: create a view of multiple dicts as one
view  = ChainMap({1:"a", 2: "b"}, {3:"c"}, {4: "d"})
print(str(view))