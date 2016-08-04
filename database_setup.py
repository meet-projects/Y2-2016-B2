from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String, Table, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

friend_association = Table('association', Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('friend_id', Integer, ForeignKey('user.id')))



class User(Base):
	__tablename__ = 'user'
	id = Column(Integer, primary_key = True)
	fullname = Column(String)
	email = Column(String)
	password = Column(String)
	# picture = Column(String, nullable = False)
	my_friends = relationship("User", 
							  secondary=friend_association, 
							  primaryjoin=id==friend_association.c.user_id,
							  secondaryjoin=id==friend_association.c.friend_id,
							  lazy=True)


class Questions(Base):
	__tablename__='questions'

	id = Column(Integer, primary_key = True)
	text=Column(String)
	deep=Column(Boolean)
	


class User_questions(Base):
	__tablename__='user_questions'
	id = Column(Integer, primary_key = True)
	user_id=Column(Integer, ForeignKey("user.id"))
	user = relationship("User")
	question_id=Column(Integer, ForeignKey("questions.id"))
	user_response=Column(String, nullable = False)


  	
   		   
	    
