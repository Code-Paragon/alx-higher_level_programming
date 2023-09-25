#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """prints the first x elements of a list and only integers.

    Args:
        my_list: list to be printed
        x: the number of element to be printed

    Returns:
        the real number of integers printed
    """
    if my_list is None or x < 0:
        return (0)
    m = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            m += 1
        except IndexError:
            print("IndexError: list index out of range")
        except (TypeError, ValueError):
            continue
    print('')
    return (m)
