name = "sweetpear"

# This package add .map to types list and tuple.
from forbiddenfruit import curse


def __curse_list_map(self, fct):
    if type(fct) == str:
        return list(map(lambda x: getattr(x, fct)(), self))
    return list(map(fct, self))


def __curse_tuple_map(self, fct):
    if type(fct) == str:
        return tuple(map(lambda x: getattr(x, fct)(), self))
    return tuple(map(fct, self))


curse(list, "map", __curse_list_map)
curse(tuple, "map", __curse_tuple_map)
