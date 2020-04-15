"""
This function, product(*iterables, repeat=1), takes one or more iterables
and returns the Cartesian product of these iterables.
This function is pretty much like nested for loops by creating a single iterator that “flattens” the nested loops.
The optional repeat argument is to repeat the only input iterator for the specified number.
In other words, the product(a_list, repeat=3) is the same as product(a_list, a_list, a_list).

Suppose that you’re going to have a nephew, and your sister asks you to name the baby boy.
We know that he’ll have the last name Thompson.
We have two lists of names for first and middle names, respectively.
Let’s find out the possible combinations.
In the end, we probably decide to pick the name John Elliot Thompson, because the initials JET is really cool for a boy
"""

from itertools import product

first_names = ['John', 'Adam', 'Danny']
middle_names = ['Douglas', 'Elliot']

for name in product(first_names, middle_names, ['Thompson']):
    full_name = " ".join(name)
    initials = "".join((x[0] for x in name))
    print(f'Full name: {full_name}; Initials: {initials}')

