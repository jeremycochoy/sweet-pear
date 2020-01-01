from forbiddenfruit import curse
import cytoolz


def __curse_count(self):
    """
    Count the number of items in sequence.

    Like the builtin ``len``.
    """
    return cytoolz.count(self)


def __curse_groupby(self, fct):
    """
    Concatenate zero or more iterables, any of which may be infinite.

    An infinite sequence will prevent the rest of the arguments from
    being included.

    >>> [[], [1], [2, 3]].flatten()
    [1, 2, 3]

    >>> [[(1, 2)], (3, 4)].flatten()
    [[(1, 2)], 3, 4]

    """
    return cytoolz.groupby(fct, self)


for stype in [list, range, tuple, str, dict]:
    curse(stype, "count", __curse_count)
    curse(stype, "groupby", __curse_groupby)


def __curse_list_flatten(self):
    """
    Flatten a list. Only the type `list` is affected.

    >>> [1, [2], [[3]], (4, 5)].flatten()
    [1, 2, 3, (4, 5)]

    """
    def __flatten(x):
        return __flatten(x[0]) + (__flatten(x[1:]) if len(x) > 1 else []) if type(x) is list else [x]

    return __flatten(self)


curse(list, "flatten", __curse_list_flatten)
