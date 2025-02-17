from sqlalchemy import Column, Integer, String, Boolean
from database.database import Base

class Location(Base):
    __tablename__ = "locations"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    status = Column(String)
    description = Column(String)