#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import shlex


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete, delete-orphan',
                          backref='state')

    @property
    def cities(self):
        """Getter for cities attribute"""
        from models import storage
        c_list = []
        cities_list = []
        for elem in storage.all():
            city = elem.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                c_list.append(storage.all()[elem])
        for c in c_list:
            if c.state_id == self.id:
                cities_list.append(c)
        return (cities_list)
