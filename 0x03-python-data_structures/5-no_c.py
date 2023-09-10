#!/usr/bin/python3
def no_c(my_string):
    """removes all characters c and C from a string.

    Args:
        my_string: the string to delete Cs from

    Returns:
        the new string
    """
    new_string = ''
    for i in range(len(my_string)):
        if (ord(my_string[i]) == 67) or (ord(my_string[i]) == 99):
            continue
        else:
            new_string = new_string + my_string[i]
    return (new_string)
