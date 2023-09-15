#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """returns a new dictionary with all values multiplied by 2

    Args:
        a_dictionary: a dict

    Returns:
        new dict with values doubled
    """
    if a_dictionary is None or a_dictionary == {}:
        return ({})
    new_dict = {}
    for x in a_dictionary:
        new_dict[x] = a_dictionary[x] * 2
    return (new_dict)
