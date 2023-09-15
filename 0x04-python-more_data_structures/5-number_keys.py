#!/usr/bin/python3
def number_keys(a_dictionary):
    """returns the number of keys in a dictionary.

    Args:
        a_dictionary: dictionary to be operated

    Returns:
        number of keys
    """
    if a_dictionary == {} or a_dictionary is None:
        return (0)
    key_list = list(a_dictionary)
    return (len(key_list))
