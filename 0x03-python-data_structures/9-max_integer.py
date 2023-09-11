#!/usr/bin/python3
def max_integer(my_list=[]):
    """finds the biggest integer of a list

    Args:
        my_list: list to search

    Returns:
        the maximum value
    """
    if len(my_list) == 0 or my_list is None:
        return (None)
    sort_list = my_list[:]
    sort_list.sort()
    return (sort_list[-1])
