import random

"""Seeding Random Numbers
As we discussed in the above section, the random module takes a number as input and generates a random number for it. 
This initial value is known as a seed, and the procedure is known as seeding.
The numbers we generate through pseudo-random number generators are deterministic. 
This means they can be replicated using the same seed."""

print('Random Number 1=>', random.random())
print('Random Number 2=>', random.random())

random.seed(42)
print('Random Number 1=>', random.random())
random.seed(42)
print('Random Number 2=>', random.random())

"""uniform()
The uniform() function of the random module takes starting and ending values of 
a range as arguments and returns a floating-point random number in the range [starting, ending]:"""

print('Random Number in range(2,8)=>', random.uniform(2, 8))

"""randint()
This function is similar to the uniform() function. 
The only difference is that the uniform() function returns floating-point random numbers, 
and the randint() function returns an integer. 
It also returns the number in the range [starting, ending]:"""

print('Random Number in a range(2,8)=>', random.randint(2, 8))

"""choice() & choices() 
are the two functions provided by the random module that we can use for randomly selecting values from a list. 
Both of these functions take a list as an argument and randomly select a value(s) from it. 
Can you guess what the difference between choice() and choices() is?

choice() only picks a single value from a list whereas choices() picks multiple values from a list with replacement. 
One fantastic thing about these functions is that they work on a list containing strings too. 
Let’s see them in action:"""

a = [5, 9, 20, 10, 2, 8]
print('Randomly picked number=>', random.choice(a))
print('Randomly picked number=>', random.choices(a, k=3))

"""As you can see, choice() returned a single value from a and choices() returned three values from a. 
Here, k is the length of the list returned by choices().

One more thing you can notice in the responses returned by choices() is that each value occurs only once. 
You can increase the probability of each value being picked by passing an array as weights to the choices() function. 
So, let’s increase the probability of 10 to as much as thrice of others and see the results:"""

for _ in range(5):
    print('Randomly picked number=>', random.choices(a, weights=[1, 1, 1, 3, 1, 1], k=3))

"""Shuffling a List
Let’s say we don’t want to pick values from a list but you just want to reorder them. 
We can do this using the shuffle() function from the random module. 
This shuffle() function takes the list as an argument and shuffles the list in-place:"""

print('Original list=>', a)
random.shuffle(a)

print('Shuffled list=>', a)

"""gauss()
Let’s start with the most common probability distribution, i.e., normal distribution. 
gauss() is a function of the random module used for generating random numbers according to a normal distribution. 
It takes mean and standard deviation as an argument and returns a random number:

Here, I plotted 1000 random numbers generated by the gauss() function for mean equal to 0 and standard deviation as 1. 
You can see above that all the points are spread around the mean 
and they are not widely spread since the standard deviation is 1."""

for _ in range(5):
    print(random.gauss(0, 1))

"""expovariate()
Exponential distribution is another very common probability distribution that you’ll encounter. 
The expovariate() function is used for getting a random number according to the exponential distribution. 
It takes the value of lambda as an argument and returns a value from 0 to positive infinity if lambda is positive, 
and from negative infinity to 0 if lambda is negative:"""

print('Random number from exponential distribution=>', random.expovariate(10))
