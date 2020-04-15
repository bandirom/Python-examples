"""
This function, groupby(iterable, key=None), takes an iterable and a key,
which is a function that specifies how the elements in the iterable should be grouped.
One thing to note is that if the elements haven’t been sorted beforehand, this groupby()
function won’t group your elements using the key function as you may have expected.
In other words, it’s usually necessary to use the same function to sort
the iterable before using the groupby() function.

Suppose that we have some new employees attending their orientation session,
and we want to group them by their last names’ initials such that they can check in to get their badges quicker.
Here’s the code showing how we can use the groupby() function to achieve the desired results
"""

from itertools import groupby

employees = ['John Smith', 'Jennifer Brown', 'Zack Dani', 'Peter Shine', 'Aaron Dawson', 'Holly Shaw']
grouped_employees = {}

name_key = lambda x: x.split()[-1][0]
sorted_employees = sorted(employees, key=name_key)

for k, names in groupby(sorted_employees, key=name_key):
    grouped_employees[k] = list(names)

print(grouped_employees)

