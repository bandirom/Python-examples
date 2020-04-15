"""
This function, accumulate(iterable[, func, *, initial=None]),
makes an iterator that returns accumulated results of the binary functions (i.e., functions that take two arguments)
by specifying the func argument.
The optional initial argument is to set an extra value of the output iterable at its beginning.
This function may sound a little confusing at the first glance, but the example below will help you understand it.

Suppose that you bought a Tesla car for $50,000 with a monthly payment of $2,000 and a monthly interest rate of 0.3%.
We want to track the remaining balance on a monthly basis.
The following code shows how we can do that with the accumulate() function.
One thing to note is that we use a lambda function, which takes exactly two arguments,
as the binary function to work on consecutive elements to produce accumulated results.
"""

from itertools import accumulate

cash_records = [50000, -2000, -2000, -2000, -2000, -2000]
rate = 1.003

for mounthly_record in accumulate(cash_records, lambda amount, pmt: amount*rate + pmt):
    print(mounthly_record)


