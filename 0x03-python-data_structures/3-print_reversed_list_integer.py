#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """function that prints all integers of a list, in reverse order.

    Args:
        my_list: list to be reversed

    Returns:
        NULL
    """
    if my_list is None or len(my_list) == 0:
        return ('')
    my_list.reverse()
    for i in my_list:
        print("{:d}".format(i))
