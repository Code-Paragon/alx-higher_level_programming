#!/usr/bin/python3
def element_at(my_list, idx):
    """retrieves an element from a list like in C.

    Args:
        my_list: list comtaining element

    Returns:
        element: the element at the index
    """
    if idx < 0 or idx > (len(my_list) - 1):
        return (None)
    element = my_list[idx]
    return (element)
