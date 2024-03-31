class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_my_name(self):
        print(self.name)


p  = Person("Gab", 33)
p.say_my_name()


# Inheritance
class Man(Person):
   def say_something(self):
        print("I am a man")

m = Man("Gab_man",35)
m.say_my_name()


# Polymorphism
class Woman(Person):

    def say_something(self):
        print("I am a woman")