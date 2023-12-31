from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base

from scraper import settings

DeclarativeBase = declarative_base()


def db_connect() -> Engine:
    """
    Creates database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(URL(**settings.DATABASE))


class Items(DeclarativeBase):
    """
    Defines the items model
    """

    __tablename__ = "course"

    name = Column("name", String, primary_key=True)
    price = Column("price", Integer)