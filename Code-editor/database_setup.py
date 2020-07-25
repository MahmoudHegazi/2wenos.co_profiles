#!/usr/bin/env python3
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

"""File name: database_setup.py

That's Database Setup file:
    1. run this file to setup your database
    2. run after this lotsofcar.py    

More details can be found in the README.md file,
which is included with this project. this is 2wenos.co Developers storgae App
"""


Base = declarative_base()

#accounts info
class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(350), nullable=False)    
    email = Column(String(100), unique=True, nullable=False)
    gender = Column(String(15), nullable=False)
    login_times = Column(Integer)
    login_date = Column(String(200))
    image = Column(String(100))
    password = Column(String(100))
    user_info = Column(String(450))
    job = Column(String(100))
    storage = Column(String(100))
    #ady el connects ya upwork
    connects = Column(Integer)
    is_verified = Column(Integer, default=0)
    #url = relationship('newUrls', backref='users', lazy='dynamic')
    
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'image': self.code,
            'job': self.job,
            'storage': self.storage
        }

# user skills
class Skills(Base):
    __tablename__ = 'skills'
    name = Column(String(20))
    id = Column(Integer, primary_key=True)
    info = Column(String(250))
    user_id = Column(Integer, ForeignKey('users.id'))
    
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'info': self.info,
            'user_id': self.user_id
        }

    
    
# table for handle the storage and url asigning 
class newUrls(Base):
    __tablename__ = 'newurls'

    id = Column(Integer, primary_key=True)
    name = Column(String(350), nullable=False)    
    code = Column(String(90000), nullable=False)
    url = Column(String(200), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(Users)
    
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'code': self.code,
            'url': self.url            
        }




    




engine = create_engine('sqlite:///mpasta.db')
Base.metadata.create_all(engine)
