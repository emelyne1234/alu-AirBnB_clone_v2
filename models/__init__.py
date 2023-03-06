#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.engine.db_storage import DBStorage
from os import getenv


if storage_t == 'db':
    storage = DBStorage()

else:
    storage = FileStorage()
storage.reload()
