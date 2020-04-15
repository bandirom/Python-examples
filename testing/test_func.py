import itertools

def rle(iterable):
    """Apply run-length encoding to an iterable.
    >>> list(rle("mississippi")) # doctest: *ELLIPSIS
    [('m', 1), ... ('i', 1)]
    """
    for item, g in itertools.groupby(iterable):
        yield item, sum(1 for _ in g)

#print((list(rle('mississippi'))))
assert list(rle("")) == []
assert list(rle('foo')) == [('f', 1), ('o', 2)], list(rle('foo'))
