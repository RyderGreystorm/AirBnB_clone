#!/usr/bin/python3
"""
Creating the instance of the File storage class
"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
