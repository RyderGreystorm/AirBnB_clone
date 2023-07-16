#!/usr/bin/python3

import json
import importlib
import os
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
        """
        dictionary, which contains all the objects
        stored in the FileStorage.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        adds new object  to objects dictionary.
        takes obj as argument. class name and id
        used as  key in dictionary to store object
        """
        key = str(type(obj).__name__) + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):

        """Serialize __objects to the JSON file __file_path."""
        with open(self.__file_path, "w") as file:
            obj_dic = {}
            for key, value in FileStorage.__objects.items():
                obj_dic[key] = FileStorage.__objects[key].to_dict()
            json.dump(obj_dic, file)

    def reload(self):
        """ deserializes the JSON file to __objects """

        if not os.path.exists(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, "r") as file:
            content = file.read()
            if content is None:
                return
            objects_dict = json.loads(content)
            FileStorage.__objects = {}
            for key, value in objects_dict.items():
                if "User" in key:
                    FileStorage.__objects[key] = User(**objects_dict[key])
                    continue
                elif "State" in key:
                    FileStorage.__objects[key] = State(**objects_dict[key])
                    continue
                elif "City" in key:
                    FileStorage.__objects[key] = City(**objects_dict[key])
                    continue
                elif "Place" in key:
                    FileStorage.__objects[key] = Place(**objects_dict[key])
                    continue
                elif "Amenity" in key:
                    FileStorage.__objects[key] = Amenity(**objects_dict[key])
                    continue
                elif "Review" in key:
                    FileStorage.__objects[key] = Review(**objects_dict[key])
                    continue
                FileStorage.__objects[key] = BaseModel(**objects_dict[key])
