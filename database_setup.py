from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Friends(Base):
	__tablename__='friends'
	id=Column(Integer, primary_key=True)
	person=Column(Integer, ForeignKey("user.id"))
	friend=Column(Integer, ForeignKey("user.id"))
	

class User(Base):
	__tablename__ = 'user'
	id = Column(Integer, primary_key = True)
	fullname = Column(String)
	email = Column(String)
	password = Column(String)
	picture = Column(String, nullable = False)
	answer1 = Column(String, nullable = False)
	answer2 = Column(String, nullable = False) 
	answer3 = Column(String, nullable = False) 
	answer4 = Column(String, nullable = False) 
	answer5 = Column(String, nullable = False) 
	answer6 = Column(String, nullable = False) 
	answer7 = Column(String, nullable = False)
	answer8 = Column(String, nullable = False)
	answer9 = Column(String, nullable = False) 
	answer10 = Column(String, nullable = False)    
