'''
    Functions are first-class objects
    Can be assigned to variables or stored in data structures, passed throught arguments or returned as values from other function

'''


from typing import Any


def yell(text):
    return text.upper() + "!"



print(yell("Hello"))


'''  Functions are first-class objects'''


# Everything in python are objects, functions do so
# Since functions are also objects can be assigned to variables
# The bariable bark point to the function object reference 

bark = yell
print(bark("aaaaaa"))

# function name is a reference to the function
# since bark point also to the function we can delete yell and the function will be still available

del yell
print(bark("bbbb"))
#  print(yell("yyyy")) ## will trigger name 'yell' is not defined

# On creation of the function the interpriter attach the name on the function object
print(bark.__name__) # the initial name


'''  Functions can be stored in Data structures '''

funcs = [bark, str.lower, str.capitalize]

print(funcs)

for f in funcs:
    print(f(f"Hello from {f}"))


print(funcs[0]("aaaaa"))



'''  Functions can be passed to other functions '''
def greet(func):
    greeting = func("Hello from greet function")
    print(greeting)


greet(funcs[0])


# Functions that accept as arguments other functions are called Hier-order function
# One example is the map function, takes a function as argument and an iterable and execute the function on the iterable

print(list(map(bark, ["aa", "bb", "cc"])))


'''  Functions can be nested '''

def start_conversation(name):
    def capitalize_name(n):
        return n.capitalize()
    
    return capitalize_name(name)


print(start_conversation("gabriel"))


# Functions can return nested function
def get_calculate_method(total_amount):
    def calculate_retail(amount):
        return amount * 0.2
    
    def calculate_premium(amount):
        return amount * 0.7
    
    if total_amount > 1000:
        return calculate_premium
    else: 
        return calculate_retail
    

method = get_calculate_method(10000)
print(method(30000))


method = get_calculate_method(100)
print(method(120))


''' Inner functions can capture and remember the arguments of parent function when initiated '''

# This behaivior can be used to pre-configure a funtion
def make_adder(num):
    def addnum(inputt):
        return num + inputt
    
    return addnum


add_by_3 = make_adder(3)
add_by_5 = make_adder(5)

print(add_by_3(44))
print(add_by_5(44))



''' Classes can behaive as functions (not by default)'''
# we have to override __call__ method

class Added:
    def __init__(self, num):
        self.num = num

    def __call__(self, x):
        return self.num + x
    

adder_3 = Added(3)
adder_5 = Added(5)

print(adder_3(44))
print(adder_5(44))