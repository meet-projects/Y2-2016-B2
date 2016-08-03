from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

friend_association = Table('association', Base.metadata,
    Column('friend_1', Integer, ForeignKey('friends.id')),
    Column('friend_2', Integer, ForeignKey('friends.id')))




class User(Base):
	__tablename__ = 'user'
	id = Column(Integer, primary_key = True)
	fullname = Column(String)
	email = Column(String)
	password = Column(String)
	#status_=Column(String)
	picture = Column(String, nullable = False)
	my_friends=relationship("User",secondary=friend_association)

class Questions(Base):
	__tablename__='questions'

	id = Column(Integer, primary_key = True)
	text=Column(String)
	deep=Column(Boolean)
	


class User_questions(Base):
	__tablename__='user_questions'
	id = Column(Integer, primary_key = True)
	user_id=Column(Integer, ForeignKey("user.id"))
	question_id=Column(Integer, ForeignKey("questions.id"))
	user_response=Column(String)


  	
   		   
	    
