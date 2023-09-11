#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """deletes the item at a specific position in a list

    Args:
        idx: position of element to be deleted
        my_list: list to delete from

    Returns:
        New list without the element
    """
    if my_list is None or len(my_list) == 0:
        return (None)
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)
    del my_list[idx]
    return (my_list)
