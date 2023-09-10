#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """a function replaces an element of a list at a specific position

    Args:
        my_list: the list of elements to be replaced
        element: the new element to replace the old
        idx: index of element to be replaced

    Returns:
        the new list
    """
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)
    my_list[idx] = element
    return (my_list)
