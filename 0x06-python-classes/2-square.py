#!/usr/bin/python3
"""a module that defines the class Square
"""


class Square:
    """a class Square that defines a square by: (based on 1-square.py)
    """

    def __init__(self, size=0):
        """initializes the size of the sqaure
        and checks if it is less than 0 amd an integer
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
