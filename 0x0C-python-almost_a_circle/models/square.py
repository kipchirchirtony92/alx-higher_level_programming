#!/usr/bin/env python3
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size,  x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def  __str__(self):
        return "[Square] ({}) {}{} - {}".format(self.id, self.x,
                                                self.y, self.size)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        new_list = ['id', 'size', 'x', 'y']
        if args:
            for i in range(len(args)):
                setattr(self, new_list[i], args[i])
        else:
            for key, value in kwargs.items():
                if key in new_list:
                    setattr(self , key, value)
    def to_dictionary(self):
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
    
