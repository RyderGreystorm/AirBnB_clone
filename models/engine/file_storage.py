#!/usr/bin/python3
import json
<<<<<<< HEAD
from models.base_model import BaseModel


class FileStorage:
    """
    Represent an abstracted storage engine.
    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
=======
"""
used for serializing and deserializing
objects to and from JSON format
"""

class FileStorage:
>>>>>>> refs/remotes/origin/main
    """
    filepath is a private class attribute showing path to
    json where objects will be stored.
    objects is a private class sttribure empty dictionary
    to store objects by class name and id.
    """
    __file_path = "file.json" 
    __objects = {}

    def all(self):
        """
        dictionary, which contains all the objects
        stored in the FileStorage.
        """
        return self.__objects

    def new(self, obj):
        """
        adds new object  to objects dictionary.
        takes obj as argument. class name and id
        used as  key in dictionary to store object
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
<<<<<<< HEAD

        """Serialize __objects to the JSON file __file_path."""
        obdiction = {}
        for key, obj in FileStorage.__objects.items():
            obdiction[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obdiction, f)
=======
        data = {}
        for key, obj in self.__objects.items():
            data[key] = obj.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(data, file)
>>>>>>> refs/remotes/origin/main

    def reload(self):
        try:
<<<<<<< HEAD
            with open(FileStorage.__file_path, "r") as f:
                objdict = json.load(f)

            from models.base_model import BaseModel
            for key, o in objdict.items():
                cls_name = o["__class__"]
                del o["__class__"]
                self.new(eval(cls_name)(**o))
=======
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                for key, obj_dict in data.items():
                    class_name, obj_id = key.split(".")
                    module = __import__("models." + class_name, fromlist=[class_name])
                    cls = getattr(module, class_name)
                    obj = cls(**obj_dict)
                    self.__objects[key] = obj
>>>>>>> refs/remotes/origin/main
        except FileNotFoundError:
            pass

