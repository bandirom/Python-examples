"""
This function, permutations(iterable, r=None),
takes an iterable and an integer and returns successive r length permutations of elements from the iterable.
If the optional r argument is omitted, this function will return all possible permutations of the specified iterable.
This function is similar to the combinations() in the sense that both produce combinations of the elements.
The difference is that the order matters in the permutations() function, but not in the combinations() function.
See below for an illustration.

In terms of a practical example,
let’s suppose that four countries in South America are in the same group for the qualifying games for the World Cup,
and we want to know all possible matches.
Each team will have a home and an away match with each of other teams, and thus the order of each team pair matters.
So we may want to use the permutations() function.
"""

from itertools import combinations, permutations

numbers = [1, 2, 3]
print(list(combinations(numbers, 2)))
print(list(permutations(numbers, 3)))

teams = ['Brazil', 'Peru', 'Chile', 'Argentina']
for match in permutations(teams, 2):
    print(match)

matches = [match for match in permutations(teams, 2)]
print(matches)

