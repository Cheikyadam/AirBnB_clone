#!/usr/bin/python3
"""Test for base_model"""
import unittest
from models.base_model import BaseModel
import sys


class BaseTestCase(unittest.TestCase):
    """Test casee for base model"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_isStringId(self):
        mod = BaseModel()
        typ = type(mod.id)
        self.assertEqual(typ, str)

    def test_str_output(self):
        mod = BaseModel()
        with captured_output() as (out, err):
            print(mod)
        output = out.getvalue()
        self.assertEqual(output, f"[BaseModel] ({mod.id}) {mod.__dict__}\n")
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        with captured_output() as (out, err):
            print(my_model)
        output = out.getvalue()
        self.assertEqual(output, f"[BaseModel] ({my_model.id}) {my_model.__dict__}\n")
        my_model.save()
        with captured_output() as (out, err):
            print(my_model)
        output = out.getvalue()
        self.assertEqual(output, f"[BaseModel] ({my_model.id}) {my_model.__dict__}\n")

    def test_todict(self):
        my_model = BaseModel()
        dico = my_model.to_dict()
        dic_t = type(dico)
        self.assertEqual(dic_t, dict)


from contextlib import contextmanager
from io import StringIO

@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

if __name__ == '__main__':
    unittest.main()
