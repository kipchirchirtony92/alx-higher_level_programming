#!/usr/bin/python3

""" Defines the class model class """
import json
import csv
import turtle

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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + ".csv"

        with open(filename, mode='w', newline="") as file:
            writer = csv.writer(file)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    row = [obj.id, obj.width, obj.height, obj.x, obj.y]
                elif cls.__name__ == "Square":
                    row = [obj.id, obj.size, obj.x, obj.y]
                else:
                    raise ValueError("Ivalid class for csv serailization")
                writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize the instances from the CSV return a list of instances loaded from a file"""
        filename = cls.__name__+ ".csv"
        instance_list = []

        try:
            with open(filename, mode='r', newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        instance = cls(int(row[0]), int(row[1]), int(row[2]), int(row[3]), int(row[4]))
                    elif cls.__name__ == "Square":
                        instance = cls(int(row[0]), int(row[1]), int(row[2]), int(row[3]))
                    else:
                        raise ValueError("Invalid class type for csv deserialization")
                instance_list.append(instance)
        except FileNotFoundError:
            pass  # If the file doesn't exist, return an empty list
        return instance_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw rectangles and squares using Turtle graphics.

        Args:
            list_rectangles (list): A list of Rectangle instances.
            list_squares (list): A list of Square instances.

        Returns:
            None
        """
        screen = turtle.Screen()
        screen.bgcolor("white")
        screen.title("Draw Rectangles and Squares")

        t = turtle.Turtle()
        t.speed(2)

        for rectangle in list_rectangles:
            t.penup()
            t.goto(rectangle.x, rectangle.y)
            t.pendown()
            t.color("blue")
            for _ in range(2):
                t.forward(rectangle.width)
                t.left(90)
                t.forward(rectangle.height)
                t.left(90)

        for square in list_squares:
            t.penup()
            t.goto(square.x, square.y)
            t.pendown()
            t.color("red")
            for _ in range(4):
                t.forward(square.size)
                t.left(90)

        turtle.done()
