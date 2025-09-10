# Database manager

from os import path, PathLike
from typing import Self

from sqlite3 import connect as sqlconnect, Connection, Cursor


## DATABASE CREATION FUNCTION
class SKUerDatabase:
    """
    
    """

    def __init__(self: Self) -> None:
        self.cursor:Cursor = None

    
    def create(self: Self, filepath:str | PathLike) -> bool:
        """
        Create a new SKUerDatabase store file at the path. Returns a bool indicating success or failure
        """

        abspath:str = path.abspath(filepath)

        # Try to create the database
        try:
            db:Connection = sqlconnect(abspath)
            self.cursor = db.cursor()
        except Exception as _:
            return False
        
        # Now that the database exists, build out entire database