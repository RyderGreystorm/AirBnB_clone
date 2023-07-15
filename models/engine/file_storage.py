#!/usr/bin/python3
import json
"""
used for serializing and deserializing
objects to and from JSON format
"""

class FileStorage:
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
        data = {}
        for key, obj in self.__objects.items():
            data[key] = obj.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(data, file)

    def reload(self):
        try:
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                for key, obj_dict in data.items():
                    class_name, obj_id = key.split(".")
                    module = __import__("models." + class_name, fromlist=[class_name])
                    cls = getattr(module, class_name)
                    obj = cls(**obj_dict)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass

