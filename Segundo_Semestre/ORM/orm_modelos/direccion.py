from sqlalchemy import Column, Integer, String, ForeignKey
from orm_modelos.base import BaseModel


class Direccion(BaseModel):
    id_direccion = Column(Integer, primary_key=True)
    id_comuna = Column(Integer, ForeignKey('comuna.id_comuna'), nullable=False)
    calle = Column(String(50), nullable=False)
    numero = Column(String(10), nullable=True)
    departamento = Column(String(10), nullable=True)
