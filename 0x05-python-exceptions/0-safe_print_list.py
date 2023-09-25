#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """safe prints x elements of a list

    Args:
        my_list: the list
        x: number of elements to be printed

    Returns:
        real number of elements printed
    """
    m = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end='')
            m = m + 1
        except IndexError:
            print("")
            return (m)
    print("")
    return (m)
