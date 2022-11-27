#!/usr/bin/python3
"""
BaseModel Module
Contains the Base class for the AirBNB clone
"""

from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:

    def __init__(self, *args, **kwargs):
        """Initialization of a Base instance.
        Args:
            *args: list of arguments
            **kwargs: dict of key-value
        """

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ Returns a string representation of the BaseModel instance"""
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates the updated_at attribute with the current datetime"""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ returns a dictionary representation of an instance"""

        my_dict = self.__dict__.copy()
        my_dict['__class__'] = type(self).__name__
        my_dict['created_at'] = my_dict["created_at"].isoformat()
        my_dict['updated_at'] = my_dict["updated_at"].isoformat()
        return my_dict
