#!/usr/bin/python3
"""My base class, all common attributes and methodes are here"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """The definition of the base class"""

    def __init__(self, *args, **kwargs):
        """
        To initalize common attributes
        """
        if kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "id":
                        self.id = value
                    elif key == "created_at":
                        self.created_at = datetime.fromisoformat(value)
                    elif key == "updated_at":
                        self.updated_at = datetime.fromisoformat(value)
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Overriding str func"""
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """ To update attribute updated_at"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """To  get dictionnary representation of self"""
        mydict = dict(self.__dict__)
        class_name = self.__class__.__name__
        mydict['__class__'] = class_name
        creat = self.created_at.isoformat()
        upd = self.updated_at.isoformat()
        mydict['created_at'] = creat
        mydict['updated_at'] = upd
        return mydict
