#!/usr/bin/python3
"""Review class here"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Defintion of the class"""
    place_id = ""
    user_id = ""
    text = ""
