#!/usr/bin/python3
"""User class to store users"""
from models.base_model import BaseModel


class User(BaseModel):
    """Definition of a user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
