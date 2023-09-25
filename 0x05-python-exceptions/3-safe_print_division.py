#!/usr/bin/python3
def safe_print_division(a, b):
    """divides 2 integers and prints the result.

    Args:
        a: integer
        b: integer

    Returns:
        the value of the division, otherwise: None
    """
    try:
        div = a / b
    except ZeroDivisionError:
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)
