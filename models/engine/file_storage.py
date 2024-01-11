#!/bin/usr/python3
"""Class to serialize and deserialize"""
import json


class FileStorage:
    """Definition of the class"""
    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """To return the dictionary"""
        return self.__objects

    def new(self, obj):
        """To save a new object"""
        key = str(type(obj).__name__)
        key += "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """To save objects if file path"""
        to_save = dict()
        for key, value in self.__objects.items():
            if type(value) is not dict:
                value_dict = value.to_dict()
                to_save[key] = value_dict
            else:
                to_save[key] = value
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump(to_save, f)

    def reload(self):
        """To reload object"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                in_file = f.read()
            if in_file is not None and len(in_file) != 0:
                self.__objects = json.loads(in_file)
        except FileNotFoundError:
            pass
