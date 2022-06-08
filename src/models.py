import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()
class User(Base):
    __tablename__= 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstName = Column(String(250), nullable=False)
    lastName = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

class Favorites(Base):
    __tablename__= 'favorites'
    id = Column(Integer, primary_key=True)
    userId = Column(Integer, ForeignKey('user.id'), nullable=False)
    characterId = Column(Integer, ForeignKey('character.id'), nullable=True)
    planetId = Column(Integer, ForeignKey('planet.id'), nullable=True)
    vehicleId = Column(Integer, ForeignKey('vehicle.id'), nullable=True)

class Planets(Base):
    __tablename__='planet'
    id = Column(Integer, primary_key=True)
    name = Column(String) 
    terrain = Column(String)
    population = Column(Integer)
    diameter = Column(Integer) 
    surfaceWater = Column(Integer) 
    gravity = Column(String)
    climate = Column(String) 
    orbitalPeriod = Column(Integer)
    rotationPeriod = Column(Integer)

class Characters(Base):
    __tablename__='character'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    gender = Column(String)
    hairColor = Column(String)
    eyeColor = Column(String)
    mass = Column(Integer)
    height = Column(Integer)
    birthYear = Column(String) 
    planet_id = Column(Integer, ForeignKey('planet.id'))

class Vehicles(Base):
    __tablename__='vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    model = Column(String)
    vehicleClass = Column(String)
    manufacturers = Column(String)
    cost = Column(Integer)
    length = Column(Integer)
    crew = Column(Integer)
    passengers = Column(Integer)
    pilots_id = Column(Integer, ForeignKey('character.id'))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')