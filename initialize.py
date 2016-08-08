from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from database_setup import *

engine = create_engine('sqlite:///project.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# You can add some starter data for your database here.
Tehila = User()
Tehila.fullname="Tehila Pelled" 
Tehila.email="tehilapelled16@gmail.com"
Tehila.password="password"
Tehila.about_myself = "Hi my name is Tehila and I like scuba diving, programming and i am 16 years old."
Tehila.photo = "https://www.colourbox.com/preview/8103563-cute-girl-cartoon.jpg"

			 




Amos = User(fullname="Amos Ro ", 
			  email="amosamos@gmail.com", 
			  password="password",
  			  about_myself = "Hi I am Amos",
			  photo = "https://www.colourbox.com/preview/8103563-cute-girl-cartoon.jpg" 
	)
Amos2 = User(fullname="Amos Ro ", 
			  email="amosamos@gmail.com", 
			  password="password",
			  #about_myself = "Hi I am Amos"
			  )

simple_q=['When were you born?','Gender(Male/Female)?', 'What is your major?','Where do you learn? ', 'What is your nationality?','Where do you live? ', ' Favorite sport? ' ]
deep_q=['Favorite movie? ', 'If you could live in another country where would you live?', 'Favorite food?', 'Do you have any pets? ', 'Coke or Pepsi?', 'X-box or PlayStation? ', 'PC or Laptop?', 'DC or Marvel?', 'IOS or Android?', 'Classic or modern music?', 'Favorite subject in school? ','What are your hobbies? ', 'Are you religious or spiritual?', 'Do you consider yourself an introvert or an extrovert? ', 'Are you open minded or not? ', 'Is what you are doing now what you always wanted to do growing up? ', 'Describe your relationship with your parents in one word? ', 'Describe the meaning of life in one word? ','What kind of parent do you think you will be? ','Are you a leader or a follower ','What type of friend are you? ','on scale of 1-10 how honest are you? ', 'What are 2 things that you cannot live without? ','Are you greedy or generous?', 'How happy are you with your social status?', 'Describe yourself in two words' ]


for i in simple_q:
    a=Questions(
        text=i,
        deep=False
        )
    session.add(a)

for i in deep_q:
    a=Questions(
        text=i,
        deep=True
        )
    session.add(a)



session.add(Tehila)
session.add(Amos)
#Amos.my_friends.append(Tehila)

session.commit()

