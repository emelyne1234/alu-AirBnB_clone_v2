#!/usr/bin/python3
""" Review module for the HBNB project """
import models
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Review(BaseModel, Base):
    """ Review classto store review information """
    if models.storage_t == 'db':
    __tablename__='reviews'
    place_id = Column(String(60), nullable=False, ForeignKey='places.id')
    user_id = Column(String(60), nullable=False, ForeignKey='users.id')
    text = Column(String(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)
