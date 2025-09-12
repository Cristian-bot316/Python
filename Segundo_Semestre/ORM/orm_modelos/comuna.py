from sqlalchemy import Column, Integer, String
from orm_modelos.base import BaseModel
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()


class Comuna(BaseModel):
    # __tablename__ = 'comuna'
    id_comuna = Column(Integer, primary_key=True)
    codigo_comuna = Column(String(5))
    nombre_comuna = Column(String(50))
