#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """prints a dictionary by ordered keys.

    Args:
        a_dictionary: dict keys to be printed

    Returns:
        void
    """
    sorted_keys = sorted(a_dictionary)
    pair = []
    for i in sorted_keys:
        pair.append(a_dictionary[i])
    for m in range(len(sorted_keys)):
        print("{}: {}".format(sorted_keys[m], pair[m]))
