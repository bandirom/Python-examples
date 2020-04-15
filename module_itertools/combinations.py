"""
This function, combinations(iterable, r), takes an iterable and an integer
and returns subsequences of elements with a length of r.
These subsequences of elements are in the form of tuples.
One thing to note that the order of the elements
in these tuples will reflect their original order in the initial iterable.

Suppose that we have some coins of different denominations, and we want to find out all possible combinations
using a certain number of coins. Look familiar?
You’re right — I got the idea from my 8-year-old daughter’s math homework.
Feel free to use the code for your in-house tutoring work.

"""

from itertools import combinations


def combine_coins(coins, number):
    possible_sums = set()
    for selected_coins in combinations(coins, number):
        print(selected_coins)
        possible_sums.add(sum(selected_coins))
    return sorted(possible_sums)


print(combine_coins([5, 5, 1, 1, 25, 10, 25], 3))

print(combine_coins([1, 1, 10, 5, 25, 25], 2))
