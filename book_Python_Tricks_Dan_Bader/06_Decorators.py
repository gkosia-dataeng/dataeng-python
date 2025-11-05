'''
    Allows to extend the behavior of a callable (function, method or class) without modify the callable

    Common use cases:
        loggin
        enforce access control
        timing functions
        rate-limit
        cache..
'''

def make_it_upper(func):
    ''' make_it_upper decorator '''
    def wrapper(*args, **kwargs):
        res =  func(*args, **kwargs)
        return res.upper()
    return wrapper


def double_it(func):
    ''' double_it decorator '''
    def wrapper(*args, **kwargs):        
        res = func(*args, **kwargs)
        return res + " " + res
    return wrapper


@double_it
@make_it_upper
def a_fun():
    ''' a_fun function '''
    return "hello man"

# would be like executing double_it(make_it_upper(a_fun))
print(a_fun())
