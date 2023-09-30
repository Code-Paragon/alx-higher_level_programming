#!/usr/bin/python3
"""a module defining a Class: Square
"""


class Square:
    """ a class Square that defines a square by: (based on 3-square.py)
    """
    def __init__(self, size=0):
        """initializes the size of the square

        Args:
            size (int): size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns the area of square

        Args:
            None

        Return:
            area of square(int)
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """getter that gets size attribute"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """sets the value of size

        Args:
            Value (int): mew value of size

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
