#!/usr/bin/python3

""" Defines a rectagle subclass """
from models.base import Base


class Rectangle(Base):
    """ Represents a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize the new triangle.
           Args:
               width (int): The width of the new Rectangle.
               height (int): The height of the new Rectangle.
               x (int): The x coordinate of the new Rectangle.
               y (int): The y coordinate of the new Rectangle.
               id (int): The identity of the new Rectangle.
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter method for the width of the rectagle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter method for the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """getter method of the attribute x"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """getter method for x attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.height * self.width

    def display(self):
        """prints the Rectangle using thr '#' character"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        for h in range(self.height):
            [print("#", end="") for w in range(self.width)]
            print("")
