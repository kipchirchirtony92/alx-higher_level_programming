#!/usr/bin/python3

""" Defines the class model class """
import json

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

    def to_json_string(list_dictionaries):
        if list_dictionaries:
            return json.dumps(list_dictionaries)            
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """save all the instances that inherit from the Base class  to a file in JSON format """
        filename =  cls.__name__+".json"

        json_list = []
        if list_objs is not None:
            for obj in list_objs:
                json_list.append(obj.to_dictionary())
        with open(filename, 'w') as file:
            file.write(cls.to_json_string(json_list))

    @staticmethod
    def from_json_string(json_string):
        """
           static method to return list of the JSON string representation
        """
        if json_string is  None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            dummy_instance = cls()
        dummy_instance.update(**dictionary)
        return dummy_instance


    @classmethod
    def load_from_file(cls):
        
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                content = file.read()
                dict_list = cls.from_json_string(content)
                for d in dict_list:
                    instance_list = [cls.create(**d)]
                    return instance_list
        except FileNotFoundError:
            return []
