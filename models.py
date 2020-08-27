from sqlalchemy import Column, Integer, String
from database import Base

class Pet(Base):
    __tablename__ = 'pets'

    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    kind = Column(String(25), nullable=True)
    color = Column(String())