#!/usr/bin/env python3
"""
Base class for our project.
Ths Base class contains most of the information and logic other
classes would need
"""

import uuid
from datetime import datetime

class BaseModel:
    """
    This is the main model from which other classes will
    inherit from
    """

    def __init__(self, *args, **kwargs):
        """
        Each time the class is instantaited, it will
        have all the attributes listed below
        """

        if kwargs:
            """removing the __class__"""
            kwargs.pop("__class__", None)
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    """ Converting back to object"""
                    setattr(self, key,datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.id = uuid.uuid4()
            self.created_at = datetime.now()
            self.updated_at = self.created_at

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
        """
        saves the updates made to the instance of our baseModel  class
        """

        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns the dictionary representation of an object
        """
        self.__dict__["__class__"] = type(self).__name__
        self.__dict__["created_at"] = self.get_created_at()
        self.__dict__["updated_at"] = self.get_updated_at()
        return self.__dict__
