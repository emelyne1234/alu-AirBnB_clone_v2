#!/usr/bin/python3

""" database storage"""


import os

import sqlalchemy
from sqlalchemy.orm import relationship, sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class DBStorage(): 
    """private class attributes"""
    __engine = None
    __session = None


def __init__(self):
    user = os.getenv('HBNB_MYSQL_USER')
    password = os.getenv('HBNB_MYSQL_PWD')
    host = os.getenv('HBNB_MYSQL_HOST')
    database = os.getenv('HBNB_MYSQL_DB')

    self.__engine = sqlalchemy.create_engine(
            'mysql+mysqldb://{}:{}@{}:3306/{}'
            .format(user,
                    password,
                    host,
                    database), pool_pre_ping=True)


    if os.getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)



def all(self, cls=None):
    """gets all objs"""
    classes = {
            'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        obj_dict = {}
    if cls is not None and cls in classes:
        class_objects = self.__session.query(classes[cls]).all()
        for obj in class_objects:
            key = obj.__class__.__name__ + "." + obj.id
            obj_dict[key] = obj
    if cls is None:
        for cls in classes:
            class_objects = self.__session.query(classes[cls]).all()
            for obj in class_objects:
                key = obj.__class__.__name__ + "." + obj.id
                obj_dict[key] = obj

    return obj_dict
def new(self, obj):
        """Adding the object"""
    self.__session.add(obj)

def save(self):
        """saving commits"""
    self.__session.commit()

def delete(self, obj=None):
        """Deleting from the current database"""
    if obj is not None:
        self.__session.delete(obj)

def reload(self):
    """creating all tables"""
    Base.metadata.create_all(self.__engine)
    session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
    session = scoped_session(session_factory)
    self.__session = session()


