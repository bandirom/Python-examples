"""
Python provides a more compact way for you to do optional annotation using symbols : and ->.
"""
from typing import List, Tuple, Dict
from typing import Union
from typing import Callable


def foo(n: int, s: str = 'Tom') -> str:
    """Repeat a string multiple times.
    Args:
        n(int): number of times
        s(string): target string
    Returns:
        (string): target string repeated n times.
    """
    return s * n


print(foo.__annotations__)

"""Variable Annotations
Apart from function arguments and return values, you can also annotate variables with a certain data type. 
You can also annotate variables without initialising them with any values!
"""
major: str = 'Tom'
i: int

"""
It is better to annotate variables using this built-in syntax instead of comments, 
as comments are often greyed out in many editors.

For annotating variables with more advanced types such as list, dict etc., 
you would need to import them from module typing. 
The name of the types are capitalised, such as List, Tuple, Dict etc..
"""

l: List[int] = [1, 2, 3]
t1: Tuple[float, str, int] = (1.0, 'two', 3)
t2: Tuple[int, ...] = (1, 2.0, 'three')
d: Dict[str, int] = {'uno': 1, 'doc': 2, 'tres': 3}

"""
The elements inside a list, tuple, or a dictionary can also be annotated. 
Those capitalised types take parameters in square brackets [] as shown above.

List takes one parameter, which is the type annotated for all elements inside the list. 
Elements in a fixed size tuple can be annotated one by one, 
whereas those in a variable size tuple can be annotated by ellipsis '...'. 
We can also specify types of keys and items in a dictionary as well.
"""

"""Advanced Annotations
We mentioned that List only takes one parameter. 
What about annotating a list that contains a mixture of int and float elements?
Union is the answer.
"""

l2: List[Union[int, float]] = [1, 2.0, 3]


class FancyContainer:
    def __init__(self):
        self.answer = 42


fc: FancyContainer = FancyContainer()


"""Callable
A callable can also be annotated using the above-mentioned techniques. 
A callable is something that can be called, like a function.
"""

my_func: Callable[[int, str], str] = foo
print(my_func(2, '5'))

