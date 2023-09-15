#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """replaces all occurrences of an element by another in a new list

    Args:
        my_list: is the initial list
        search: is the element to replace in the list
        replace: is the new element

    Returns:
        new list with eeplaced elements
    """
    if my_list is None or len(my_list) == 0:
        return(None)
    new_list = []
    for element in my_list:
        if element == search:
            new_list.append(replace)
        else:
            new_list.append(element)
    return(new_list)
