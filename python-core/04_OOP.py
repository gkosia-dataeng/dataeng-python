class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_my_name(self):
        print(self.name)


p  = Person("Gab", 33)
p.say_my_name()


# Inheritance: inheriting from a class and extend it as other instance
class Man(Person):
   
    def __init__(self, name, age):
        super().__init__(name, age)

    def say_gender(self):    
        print("I am a man")

m = Man("Gab_man",35)
m.say_my_name()


# Polymorphism: two classes treated the same as an object of higher class
class Woman(Person):

    def __init__(self, name, age):
       super().__init__(name, age)
    
    def say_gender(self):    
        print("I am a woman")


def introduce_self(person: Person):
    person.say_my_name()

person1 = Man("Gab", 34)
person2 = Woman("Anna", 32)


introduce_self(person1)
introduce_self(person2)


# Encapsulation: hiding fields of the class and provide methods to access them
class Balance:

    def __init__(self, init_balance):
        self.__balance = init_balance

    def deposit(self, amount):
        self.__balance+=amount

    def get_current_balance(self):
        return self.__balance
    
bal = Balance(10)
bal.deposit(15)
print(bal.get_current_balance())


# Constructors and Destructors
class Car:
    def __init__(self, color):
        self.__color = color
        print(f"A car with {color} color has been created")

    def __del__(self):
        print(f"The car with {self.__color} color has been deleted")

mycar = Car("red")
del mycar


# Methods overritng: the children overrite the method of parent to provide more specific implementation
#                    method should have the same name, params and return type
person1.say_gender()
person2.say_gender()


# Abstract classes: we cannot create instances of abstract class, when we inherit we have to implement these classes
from abc import abstractclassmethod
from typing import Any

class Shape:
    @abstractclassmethod
    def what_shape(self):
        pass

class Circle(Shape):
    def what_shape(self):
        print("I am a circle")

crl = Circle()
crl.what_shape()


# Compositions: a class contains other objects
# Static methods: are methods that are common to all instaces, they are accessed by class name
class Engine():

    def start_engine(self):
        print("Engine started")

class CarWithEngine():
    def __init__(self):
        self.engine = Engine()

    def start_engine(self):
        self.engine.start_engine()

    def say_type():
        print("I am a car")

    
carengine = CarWithEngine()
carengine.start_engine()
CarWithEngine.say_type()