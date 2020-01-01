from forbiddenfruit import curse
import cytoolz


def __curse_tail_gen(selected_type):
    def __curse_tail(self, n):
        """
        The last n elements of a sequence

        >>> [10, 20, 30, 40, 50].tail(2)
        [40, 50]

        See Also:
            drop
            take
        """
        return selected_type(cytoolz.tail(n, self))
    return __curse_tail


def __curse_drop_gen(selected_type):
    def __curse_drop(self, n):
        """
        The sequence following the first n elements

       >>> [10, 20, 30, 40, 50].drop(2)
        [30, 40, 50]

        See Also:
            take
            tail
        """
        return selected_type(cytoolz.drop(n, self))
    return __curse_drop


def __curse_take_gen(selected_type):
    def __curse_take(self, n):
        """
        Help on cython_function_or_method in module cytoolz.itertoolz:

        The first n elements of a sequence

        >>> [10, 20, 30, 40, 50].take(2)
        [10, 20]

        See Also:
            drop
            tail
        """
        return selected_type(cytoolz.take(n, self))
    return __curse_take


def __curse_first_gen(selected_type):
    def __curse_first(self):
        """
        Help on cython_function_or_method in module cytoolz.itertoolz:

        The first element in a sequence

        >>> 'ABC'.first()
        'A'
        """
        return selected_type(cytoolz.first(self))
    return __curse_first


def __curse_concat_gen(selected_type):
    def __curse_concat(self):
        """
        Concatenate zero or more iterables, any of which may be infinite.

        An infinite sequence will prevent the rest of the arguments from
        being included.

        >>> [[], [1], [2, 3]].flatten()
        [1, 2, 3]

        >>> [[(1, 2)], (3, 4)].flatten()
        [[(1, 2)], 3, 4]

        """
        return selected_type(cytoolz.concat(self))
    return __curse_concat


def __to_gen(selected_type):
    def __to(x):
        if selected_type == str:
            if isinstance(x, str):
                return x
            else:
                return ''.join(x)
        else:
            return selected_type(x)
    return __to


for stype in [list, range, tuple, str]:
    curse(stype, "tail", __curse_tail_gen(__to_gen(stype)))
    curse(stype, "take", __curse_take_gen(__to_gen(stype)))
    curse(stype, "drop", __curse_drop_gen(__to_gen(stype)))
    curse(stype, "first", __curse_first_gen(__to_gen(stype)))
    curse(stype, "concat", __curse_concat_gen(__to_gen(stype)))
