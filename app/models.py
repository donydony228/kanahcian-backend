# Purpose: Define the database schema for the location table.

from sqlalchemy import Column, Integer, String
from .database import Base

# **地點資料表**
class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    lat = Column(String)
    lon = Column(String)
