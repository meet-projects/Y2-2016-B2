from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from database_setup import *

engine = create_engine('sqlite:///project.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()
print ('a')

# You can add some starter data for your database here.
Tehila = User()
Tehila.fullname="Tehila Pelled" 
Tehila.email="tehilapelled16@gmail.com"
Tehila.password="password"
Tehila.picture=r"ht"
			 

session.add(Tehila)
session.commit()

Amos = User(fullname="Amos Ro ", 
			  email="amosamos@gmail.com", 
			  password="password",
			  picture=r"https://www.google.co.il/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwiq1Pr7wKLOAhUBvRQKHR0XBNIQjRwIBw&url=https%3A%2F%2Fwww.pinterest.com%2Fexplore%2Fcute-dogs%2F&psig=AFQjCNFSpUH41w_oeORD9-R6D2h3YG0m0A&ust=1470219593279203" 
			  )
Amos2 = User(fullname="Amos Ro ", 
			  email="amosamos@gmail.com", 
			  password="password",
			  picture=r"https://www.google.co.il/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwiq1Pr7wKLOAhUBvRQKHR0XBNIQjRwIBw&url=https%3A%2F%2Fwww.pinterest.com%2Fexplore%2Fcute-dogs%2F&psig=AFQjCNFSpUH41w_oeORD9-R6D2h3YG0m0A&ust=1470219593279203" 
			  )

simple_q=['Whats your age?','Gender(male/female/other)?','Do you have brothers or sisters?How many?','Where do you learn? ', 'What is your nationality','Where do you live? ', ' Favourite color? ' ]
deep_q=['Favourite movie? ', 'Favourite food?', 'Do you have any pets? ','X-box or PlayStation? ', 'Favourite subject in school? ','What is your hobies? ', 'Are you religious or spirituals?','Do you consider yourself an introvert or an extrovert? ', 'Are you open minded or not? ', 'Is what you are doing now what you always wanted to do growing up? ', 'Describe you are relashionship with your parents in one word? ', 'Describe the meaning of life in one word? ','What kind of parent do you think you will be? ','Are you a leader or a follower ','What type of friend are you? ','on scale of 1-10 how onest are you? ', 'What are 2 things that you cannot live without? ','Do you prefer giving or receiving ', 'Describe yourself in two words? ']






