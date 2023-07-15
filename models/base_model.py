#!/usr/bin/python3
<<<<<<< HEAD
"""
Base class for our project.
Ths Base class contains most of the information and logic other
classes would need
"""

import uuid
=======
"""Defines the BaseModel class."""
import models
from uuid import uuid4
>>>>>>> refs/remotes/origin/main
from datetime import datetime


class BaseModel:
    """Represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.
        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
<<<<<<< HEAD
        Each time the class is instantaited, it will
        have all the attributes listed below
        """
        from models import storage
        if kwargs:
            """removing the __class__"""
            kwargs.pop("__class__", None)
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    """ Converting back to object"""
                    setattr(self,
                            key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                            )
=======
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
>>>>>>> refs/remotes/origin/main
                else:
                    self.__dict__[k] = v
        else:
<<<<<<< HEAD
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def get_id(self):
        """
        getter to get the id of the model created
        """
        return str(self.id)

    def get_created_at(self):
        """
        method that returns the date at which the object was
        created
        """

        return self.created_at.isoformat()

    def get_updated_at(self):
        """
        getter to get the date the item was last updated
        """

        return self.updated_at.isoformat()

    def __str__(self):
        """
        returns the string representation of the object
        """

        return f"[{type(self).__name__}] ({self.get_id}) {self.__dict__}"

    def save(self):
        from models import storage
        """
        saves the updates made to the instance of our baseModel  class
        """

        self.updated_at = datetime.now()
        storage.save()
=======
            models.storage.new(self)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()
>>>>>>> refs/remotes/origin/main

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.
        Includes the key/value pair __class__ representing
        the class name of the object.
        """
<<<<<<< HEAD
        returns the dictionary representation of an object
        """
        obj_dic = dict(self.__dict__)
        obj_dic["__class__"] = type(self).__name__
        obj_dic["created_at"] = self.get_created_at()
        obj_dic["updated_at"] = self.get_updated_at()
        obj_dic["id"] = str(self.id)
        obj_dict.pop('_sa_instance_state', None)
        return obj_dic
=======
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
>>>>>>> refs/remotes/origin/main
