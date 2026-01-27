from typing import Dict, List, Optional

'''
    Add types to variables, parameters, functions return for better documentation (python will not enforce these types)


    use  mypy: check the type annotations and let me know if i have type missmatch
               mypy ./python-general/module_typing.py
'''


# Basics

# type annotation
name : str = "gab"
name = 5 # get an error in mypy




def afunc(name: str, age: int) -> str:
    return f"{name} is {age}"


def anotherf(name: str, age: int) -> None:
    print("aaaaa")



# More complex
from typing import List, Dict, Set, Optional, Any, Tuple, Callable

x: List[List[int]] = [[1,2], [3,4]]

l: Dict[str, Any] = {"a": "aa"}

s: Set[int] = {1,2,3}


t: Tuple[int, int, int] = (1,2,3)



def funcWithOptional(name: Optional[str] = "default"):
    pass

# Callable[[input params],return_type]
def func_wrapper(func: Callable[[int, int, Optional[int]],str]):
    func(1,2,3)


f = lambda x,y,z: x+y


func_wrapper(f(1,2,3))


from typing import TypeVar # generic object <placeholder: any element``> 

T = TypeVar['T']

def get_timer(lst: List[T]) -> T:
    return lst[0]