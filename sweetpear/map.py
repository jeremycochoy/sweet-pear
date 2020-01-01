from forbiddenfruit import curse


def __access_member_by_string(x, member):
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
    """
    Apply a function to each element of a sequence.
    """
    if type(fct) == str:
        return list(map(lambda x: __access_member_by_string(x, fct), self))
    return list(map(fct, self))


def __curse_tuple_map(self, fct):
    """
    Apply a function to each element of a sequence.
    """
    if type(fct) == str:
        return tuple(map(lambda x: __access_member_by_string(x, fct), self))
    return tuple(map(fct, self))


def __curse_dict_map(self, fct):
    """
    Apply a function to each pair (key, value) of a dictionary.
    """
    if type(fct) == str:
        return dict(map(lambda kv: (kv[0], __access_member_by_string(kv[1], fct)), self.items()))
    return dict(map(lambda kv: (kv[0], fct(kv[1])), self.items()))


curse(list, "map", __curse_list_map)
curse(str, "map", __curse_list_map)
curse(range, "map", __curse_list_map)
curse(tuple, "map", __curse_tuple_map)
curse(dict, "map", __curse_dict_map)
