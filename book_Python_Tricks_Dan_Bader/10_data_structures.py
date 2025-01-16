# Dictionaries

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



5.2 Array Data Structures