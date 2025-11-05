def upper_dec(func):
    def wrapper(*args, **kwargs):
        x = func()
        return x.upper()
    return wrapper


@upper_dec
def get_string():
    return "aaaaaaaa"



print(get_string())