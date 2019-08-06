name = "sweetpear"

# This package add .map to types list and tuple.
from forbiddenfruit import curse


def __work_with_string(x, member):
    """
    Return the result of x.#member or x.#member()
    where member is the name of the function/variable.

    :param x: Element to operate on
    :param member: Function or value member
    :return:
    """
    action = getattr(x, member)
    if callable(action):
        return action()
    else:
        return action


def __curse_list_map(self, fct):
    if type(fct) == str:
        return list(map(lambda x: __work_with_string(x, fct), self))
    return list(map(fct, self))


def __curse_tuple_map(self, fct):
    if type(fct) == str:
        return tuple(map(lambda x: __work_with_string(x, fct), self))
    return tuple(map(fct, self))


curse(list, "map", __curse_list_map)
curse(tuple, "map", __curse_tuple_map)
