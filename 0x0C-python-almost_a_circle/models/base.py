#!/usr/bin/python3

""" Defines the class model class """

class Base:
    """
       Represents the base model.
       Attribute:
                __nb_objects (init): The number of instantiated Bases
     """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialization of a new Base object
        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
