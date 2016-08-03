from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

# SQLAlchemy stuff
### Add your tables here!
# For example:
# from database_setup import Base, Potato, Monkey
from database_setup import Base , User, Friends

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


@app.route('/suggest<int:user_id>')
def suggest_friends(user_id):
	#user=session.query(Friends).filter_by(person=user_id).frist()
	return render_template('suggest_friends.html')



if __name__ == '__main__':
    app.run(debug=True)
