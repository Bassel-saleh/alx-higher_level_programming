#!/usr/bin/python3
"""Square module"""


class Square:
    """square"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """property for the length of a Square"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter for the length of square"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Area of square"""
        return self.__size ** 2

    def my_print(self):
        """print the length of square"""
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="\n" if j is self size - 1 and i != j else "")
                print()
