#!/usr/bin/python3
""" State Module for HBNB project """
import os
import sqlalchemy
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
import models

class Amenity(BaseModel, Base):
    """Amenities of a place"""

    if models.storage_t == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializing"""
        super().__init__(*args, **kwargs)
