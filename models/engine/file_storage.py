#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel


class FileStorage:
    """
    Represent an abstracted storage engine.
    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):

        """Serialize __objects to the JSON file __file_path."""
        obdiction = {}
        for key, obj in FileStorage.__objects.items():
            obdiction[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obdiction, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path, "r") as f:
                objdict = json.load(f)

            from models.base_model import BaseModel
            for key, o in objdict.items():
                cls_name = o["__class__"]
                del o["__class__"]
                self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
