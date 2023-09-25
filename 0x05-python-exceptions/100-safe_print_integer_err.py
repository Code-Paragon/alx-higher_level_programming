#!/usr/bin/python3
def safe_print_integer_err(value):
    """Safe integer print with error message

    Args:
        value: can be any type (integer, string, etc.)

    Returns:
        True if value has been correctly printed
        (it means the value is an integer)
	Otherwise, returns False and prints in stderr
	the error precede by Exception:
    """
    import sys

    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        sys.stderr.write("Exception: {}\n".format(sys.exec_info()[1]))
        return (False)
