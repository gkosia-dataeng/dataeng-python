'''
    Comparin two objects with ==, is
'''

a = [1,2,3]
b=a

print(a)
print(b)
c = list(a)
print(c)

print(a==c)   # true if two objects referenced by the variables have the same content
print(a is c) # true if two variables point to the same object


'''
    toString:can use __repr__ or __str__
'''

class  Car:
    def __init__(self, color,age ):
        self.color = color
        self.age   = age
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}.{self.color}, {self.age}"

myCar = Car('red', 5)
print(myCar)
        

'''
    Custom exceptions
'''
class CustomNameError(ValueError):
    pass

if 1 != 2:
    try:
        raise CustomNameError("Custom Name Error Exception")
    except CustomNameError as  e:
        print(e)


'''
    Clonig objects
'''

# Cloning set,list,tuple
# can be clone calling the factory function: this will create a shallow copy
# shallow copy: clone only the first level 
# deep clone  : clone all levels, also the data objects
a = [1,2,3]
b = a  # b is pointing to the same list as a
c = list(a) # c points to a copy list of a
a[2]=99


d = {"a":1, "b":2}
dc = dict(d)

t = (1,2,3)
tc = tuple(t)


# shallow copy vs deep copy
a = [[1,2], [3,4], [5,6]]
b = list(a) # shallow copy, first level is the pointers to the lists

a[1][1]= 99
print(b) # b will show 99 at that position because the 2nd level didnt cloned, its the same


import copy

c = copy.deepcopy(a)
a[0][1] = 99
print(c)  ## c will not show 99 at this position because its a deep copy, all levels cloned



# Absctract classes 
# Using the abc we are getting error in case a class not implement all abstract methods and we try to initialize an instace
from abc import ABC, abstractmethod

class Base(ABC):
    @abstractmethod
    def foo(self):
        pass
    
    @abstractmethod
    def bar(self):
        pass

class Concrete(Base):
    def foo(self):
        pass

# uncomment to see the error
#c = Concrete()



# nametuples: tuples with string indexes
# nametuples implemented as regular classes so we can inherit from them and create subclasses
from collections import namedtuple

Person = namedtuple("Person", ["name", "age"])
p = Person("gab", 34)
print(f"name: {p.name}, age: {p[1]}")

class Boy(Person):
    pass

b = Boy('b',18)
print(f"name: {b.name}, age: {b.age}")

# nametuple helper functions
print(b._asdict())


# Class methods, instance methods, static methods

class MyMethodsClass:

    def inst_method(self):
        # self is a pointer to the specific instance when called
        # can access class methods and variables by self.__class__
        return "Instance methods called",self

    @classmethod
    def class_method(cls):
        # cls is a pointer to the class
        return "Class method callad", cls
    
    @staticmethod
    def static_method():
        # cannot modify instance of calss state
        return "Static method called"
    

obj = MyMethodsClass()
print(obj.inst_method())
print(obj.class_method())
print(obj.static_method())
print(MyMethodsClass.static_method())