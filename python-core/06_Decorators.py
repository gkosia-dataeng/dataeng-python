

def decorator_fnc(original_function):
    def wrapper(*args, **kwargs):
        print("Before original")
        original_function(args[0])
        print("After original")
    return wrapper


def original_function(name):
    print(f"I am {name} function")

decorated_function = decorator_fnc(original_function)
decorated_function("original_function")

# OR

@decorator_fnc
def other_function(name):
    print(f"I am {name} function")



other_function("other_function")