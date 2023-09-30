#!/usr/bin/python3
"""a module that defines a class Sqaure
"""


class Square:
    """a class Square that defines a square by: (based on 2-square.py)
    """

    def __init__(self, size=0):
        """initializes the size

        Args:
            size (int): size of sqaure
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns the Squares Area

        Args:
            None

        Returns:
            Area ofa Square
        """
        return (self.__size ** 2)
