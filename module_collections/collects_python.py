from time import time
from collections import deque  # queue
from func_runtime import get_func_time

# new_copy_x = list(reversed(x))

def deque_test():
    q = deque([3, 4, 5])
    print(q)
    q.appendleft(10)
    print(q)
    q.rotate(51)
    print(q)


@get_func_time
def list_functions():
    x = [10, 15, 2, 19, -5, 80, 10]
    y = ['first', 'second', 'third', 'fourth', 'sixth']
    x.sort(reverse=False)
    y.sort(reverse=True, key=len)
    print(x, y)


# list_functions()
# deque_test()

@get_func_time
def range_list_1(n):
    test = []
    for i in range(n):
        test.append(i)


@get_func_time
def range_list_2(n):
    test = [i for i in range(n)]


# range_list_1(5000000)
# range_list_2(5000000)


#  ################ Tuples ############
def tuples_():
    person = ('Nazarii', 'Romanchenko', 'March', 9, 1996)
    last_name = 1
    birthday = slice(2, None)  # [2:]
    last_name = person[last_name]
    birthday = person[birthday]
    print(last_name, birthday)

    from collections import namedtuple
    Person = namedtuple('Person', ['first_name', 'last_name', 'age'], )
    p = Person('Nazarii', 'Romanchenko', 24)
    print(p)
    get_name = (p.first_name, p.last_name, p.age)
    print(get_name)
    new = p._replace(first_name='Nazar')
    print(p[1])
    print(new)


# tuples_()

#  ################ Anotations ############


from typing import List, NamedTuple
from dataclasses import dataclass


def fib(n: int) -> List[int]:
    fib1: int = 1
    fib2: int = 2
    res = []
    for _ in range(n):
        res.append(fib1)
        fib1, fib2 = fib2, fib1
    print(res)
    return res


# fib(50)


# @dataclass(frozen=False)
class Person(NamedTuple):
    first_name: str
    last_name: str
    age: int


p = Person('Nazarii', 'Romanchenko', 24)

print(p.last_name)


