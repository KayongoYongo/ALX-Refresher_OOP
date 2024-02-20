#!/usr/bin/python3

class Square:
    """A class called square"""
    def __init__(self, size=0):
        """Instantiate a size property

        Args:
            size: The size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """A method that returns the areas of a square"""
        return (self.__size * self.__size)
