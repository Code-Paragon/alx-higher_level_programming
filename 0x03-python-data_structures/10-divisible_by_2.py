#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """finds all multiples of 2 in a listfinds all multiples of 2 in a list

    Args:
        my_list: list to search

    Returns:
        a new list with True or False
    """
    new_list = []
    for i in my_list:
        if i % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return (new_list)
