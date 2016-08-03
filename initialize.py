from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from database_setup import *

engine = create_engine('sqlite:///project.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# You can add some starter data for your database here.
Tehila = User(fullname="Tehila Pelled", 
			  email="tehilapelled16@gmail.com", 
			  password="password",
			  picture="https://www.google.co.il/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwiq1Pr7wKLOAhUBvRQKHR0XBNIQjRwIBw&url=https%3A%2F%2Fwww.pinterest.com%2Fexplore%2Fcute-dogs%2F&psig=AFQjCNFSpUH41w_oeORD9-R6D2h3YG0m0A&ust=1470219593279203",
			  status_="hiiiiiiiiiiiiiiiiii",
			 answer1 = '',answer2='',answer3='',answer4='',answer5='',answer6='',answer7='',answer8='',answer9='',answer10='')

Amos = User(fullname="Amos Ro ", 
			  email="amosamos@gmail.com", 
			  password="password",
			  picture="https://www.google.co.il/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwiq1Pr7wKLOAhUBvRQKHR0XBNIQjRwIBw&url=https%3A%2F%2Fwww.pinterest.com%2Fexplore%2Fcute-dogs%2F&psig=AFQjCNFSpUH41w_oeORD9-R6D2h3YG0m0A&ust=1470219593279203",
			  status_="hello hereeee",
			  answer1='',answer2='',answer3='',answer4='',answer5='',answer6='',answer7='',answer8='', answer9='',answer10='')

 

friend_amos=Friends(
	person=Amos.id,
	friend=Tehila.id
	)

friend_tehila=Friends(
	person=Tehila.id,
	friend=Amos.id
	)


session.commit()
