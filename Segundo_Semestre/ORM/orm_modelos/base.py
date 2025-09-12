from typing import Type, Any
from sqlalchemy import Column, String
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base


class BaseClass:
    __abstract__ = True
    __name__ = str

    @declared_attr  # type: ignore
    def __tablename__(cls) -> str:
        return cls.__name__.lower()  # type: ignore


Base: Type[Any] = declarative_base(cls=BaseClass)


class BaseModel(Base):
    __abstract__ = True
