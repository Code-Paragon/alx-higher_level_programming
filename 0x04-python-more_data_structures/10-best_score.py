#!/usr/bin/python3
def best_score(a_dictionary):
    """returns a key with the biggest integer value.

    Args:
        a_dictionary: a dict

    Returns:
        biggest integer value
    """
    high = -100000
    key = ''
    if a_dictionary is None or len(a_dictionary) == 0:
        return (None)
    for i in a_dictionary:
        if a_dictionary[i] > high:
            high = a_dictionary[i]
            key = i
    return (key)
