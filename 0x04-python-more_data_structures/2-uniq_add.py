#!/usr/bin/python3
def uniq_add(my_list=[]):
    """adds all unique integers in a list (only once for each integer)

    Args:
        my_list: list to be operated

    Returns:
        the sum
    """
    if my_list is None or len(my_list) == 0:
        return (0)
    uniq = sorted(set(my_list))
    return (sum(uniq))
