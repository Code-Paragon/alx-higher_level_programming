#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """replaces or adds key/value in a dictionary.

    Args:
        a_dictionary: dict to be added to
        key: key to be assigned
        value: value

    Returns:
        updated dict
    """
    if a_dictionary is None:
        return ({})
    a_dictionary[key] = value
    return (a_dictionary)
