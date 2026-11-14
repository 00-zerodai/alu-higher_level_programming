#!/usr/bin/python3
"""Base model for all classes in the almost_a_circle project."""

import json


class Base:
    """Base class that manages shared object ID behavior."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the object with an identifier."""
        if id is not None:
            self.id = id
        else:
            Base._Base__nb_objects += 1
            self.id = Base._Base__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of objects to a file."""
        filename = f"{cls.__name__}.json"
        if list_objs is None:
            list_objs = []
        data = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w", encoding="utf-8") as file:
            file.write(cls.to_json_string(data))

    @staticmethod
    def from_json_string(json_string):
        """Convert a JSON string to a list of dictionaries."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance from a dictionary of attributes."""
        if cls.__name__ == "Rectangle":
            obj = cls(1, 1)
        elif cls.__name__ == "Square":
            obj = cls(1)
        else:
            obj = cls()

        for key, value in dictionary.items():
            setattr(obj, key, value)
        return obj

    @classmethod
    def load_from_file(cls):
        """Load a list of instances from a JSON file."""
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, "r", encoding="utf-8") as file:
                data = file.read()
        except FileNotFoundError:
            return []

        list_dicts = cls.from_json_string(data)
        return [cls.create(**obj_dict) for obj_dict in list_dicts]
