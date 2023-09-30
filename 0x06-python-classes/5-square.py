#!/usr/bin/python3
""" a module that defines a Class: Square
"""


class Square:
    """a class the defines a square

    Attributes:
        area: calculates the area of square
        size: square size
        my_print: prints out the square filled with #
    """
    def __init__(self, size=0):
        """initializes the square size

        Args:
            size (int): the size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """calculates the area of square

        Args:
             None
        Return:
            the area of the square
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """getter for the size private instance attribute"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """setter for the size attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """prints to stdout the square using #

        Args:
            None

        Return:
            None
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for m in range(self.__size):
                    print('#', end='')
                print()
