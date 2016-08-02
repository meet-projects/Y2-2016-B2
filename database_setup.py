from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class friends(Base):
	__tablename__=friends
	id=Column(Integer, primary_key=True)
	person=Column('id', Integer, ForeignKey("user.id"))
	friend=Column('id', Integer, ForeignKey("user.id"))
	

