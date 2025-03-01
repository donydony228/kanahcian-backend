# Purpose: Define the database schema for the location table.

from sqlalchemy import Column, Integer, String
from .database import Base

# **地點資料表**
class Location(Base):
    __tablename__ = "Location"

    LocationID = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    Latitude = Column(String)
    Longitude = Column(String)
    Address = Column(String)


class Villager(Base):
    __tablename__ = "Villager"

    VillagerID = Column(Integer, primary_key=True)
    Name = Column(String)
    Gender = Column(String)
    Job = Column(String)
    BriefDescription = Column(String)
    URL = Column(String)
    Photo = Column(String)

class Account(Base):
    __tablename__ = "Account"

    AccountID = Column(Integer, primary_key=True)
    Name = Column(String)
    Password = Column(String)
    EntrySemester = Column(String)
    Photo = Column(String)

class Record(Base):
    __tablename__ = "Record"

    RecordID = Column(Integer, primary_key=True)
    Semester = Column(String)
    Date = Column(Date)
    Photo = Column(String)
    Description = Column(String)
    Location = Column(Integer, )

# test git