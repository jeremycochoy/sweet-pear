from forbiddenfruit import curse
import cytoolz


def __curse_count(self):
    """
    Count the number of items in sequence.

    Like the builtin ``len``.
    """
    return cytoolz.count(self)


for stype in [list, range, tuple, str, dict]:
    curse(stype, "count", __curse_count)


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
