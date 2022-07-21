#!/usr/bin/python3
"""Defines a class square"""


class Square:

    def __init__(self, size=0):
        """
           initilize  a new square
            Args: size (int) the size of the new square must be of type int
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
