#!/usr/bin/python3
"""This module defines the DBStorage class for managing the database storage"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """This class manages storage of hbnb models using SQLAlchemy"""

    __engine = None
    __session = None

    def __init__(self):
        """Creates the database engine and session"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(getenv('HBNB_MYSQL_USER'),
                                             getenv('HBNB_MYSQL_PWD'),
                                             getenv('HBNB_MYSQL_HOST'),
                                             getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Queries all objects depending on class name"""
        objects = dict()
        classes = [User, State, City, Amenity, Place, Review]
        if cls is None:
            for c in classes:
                query = self.__session.query(c)
                for obj in query:
                    key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                    objects[key] = obj
        else:
            query = self.__session.query(cls)
            for obj in query:
                key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                objects[key] = obj
        return objects

    def new(self, obj):
        """Adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables and creates a new session"""
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine,
                               expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()

    def close(self):
        """Closes the storage engine."""
        self.__session.close()
