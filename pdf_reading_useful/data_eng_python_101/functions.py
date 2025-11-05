# lambda functions
lfunc  = lambda x,y: x+y
print(lfunc(2,4))

# map
x = [1,2,3,4,5]
y = [6,7,8,9]
print(f"map: {list(map(lfunc, x, y))}")

# filter
print(f"filter: {list(filter(lambda x: x>5, x))}")


# types annotations
def method_with_types(age: int, name: str) -> str:
    return f"{name} is {age} years old"

print(f"method_with_types {method_with_types(34, 'gab')}")

# any: check if eny of items has true condition
any_even = any(_x%2 == 0 for _x in x)
print(f"any_even {any_even}")

# all: check if all items has true condition
all_even = all(_x%2 == 0 for _x in x)
print(f"all_even {all_even}")

# sorted: sort a list using a key function
print(sorted(x, key = lambda x: x * -1))