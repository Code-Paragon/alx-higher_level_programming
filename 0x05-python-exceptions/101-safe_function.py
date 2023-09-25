#!/usr/bin/python3
def safe_function(fct, *args):
    """executes a function safely.

    Args:
        fct: a pointer to a function
        args: arguments

    Returns:
        the result of the function,
    """
    import sys

    try:
        results = fct(*args)
        return (results)
    except sys.exec_info()[0]:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
