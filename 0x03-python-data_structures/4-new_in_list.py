#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """replaces an element in list at a index without change to original list

    Args:
        my_list: the list to replace element at
        idx: the index of elemnt to be replaced
        element: element to be replaced

    Returns:
       list with its element at index replace
    """
    if my_list is None or len(my_list) == 0:
        return ([])
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list[:])
    rep_list = my_list[:]
    rep_list[idx] = element
    return (rep_list)
