#!/usr/bin/python3
"""My base class, all common attributes and methodes are here"""
import uuid
from datetime import datetime

class BaseModel:
    """The definition of the base class"""

    def __init__(self, *args, **kwargs):
        """
        To initalize common attributes
        """
        if kwargs is  not None:
           for key, value in kwargs.items():
               if k
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Overriding str func"""
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        """ To update attribute updated_at"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """To  get dictionnary representation of self"""
        mydict = self.__dict__
        mydict["__class__"] = "BaseModel"
        mydict["created_at"] = (self.created_at).isoformat()
        mydict["updated_at"] = self.updated_at.isoformat()
        return mydict
