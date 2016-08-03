from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

# SQLAlchemy stuff
### Add your tables here!
# For example:
# from database_setup import Base, Potato, Monkey
from database_setup import Base , User, friend_association, Questions,User_questions

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///project.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


#YOUR WEB APP CODE GOES HERE




@app.route('/', methods=['GET','POST'])
def log_in():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		user_email=request.form['email']
		user_password=request.form['password']
		print(user_email)
		print(user_password)
		user=session.query(User).filter_by(email=user_email).first()
		print(user.password)
		print(user_email)
		print(user.email)
		if user.password==user_password:
			return redirect(url_for('suggest_friends', user_id=user.id))
		else:
			return render_template('login.html')



@app.route('/signup')
def sign_up():
	return render_template('signup.html')


@app.route('/suggest/<int:user_id>')
def suggest_friends(user_id):
	return render_template('suggest_friends.html')
	'''
	user=session.query(User).filter_by(id=user_id).first()
	suggests=session.query(User).all()
	for i in suggests:
		if user.id!=i.id:
			for 
	
	return render_template('suggest_friends.html', user=user)
	'''
@app.route('/profile/<int:user_id>')	
def user_profile():
	return render_template('user_profile.html', )
	
@app.route('/view_questions/<int:user_id>', methods=['GET','POST'])	
def view_questions(user_id):
	user=session.query(User).filter_by(id=user_id).first()
	simple_questions=session.query(Questions).filter_by(deep=False).all()
	deep_questions=session.query(Questions).filter_by(deep=True).all()
	if request.method == 'GET':
		return render_template('view_questions.html', user=user,simple_questions=simple_questions, deep_questions=deep_questions  )
	
		
		


	
if __name__ == '__main__':
    app.run(debug=True)
