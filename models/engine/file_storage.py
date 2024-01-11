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
            to_save[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump(to_save, f)

    def reload(self):
        """To reload object"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                in_file = f.read()
            self.__objects = json.loads(in_file)
        except FileNotFoundError:
            pass
