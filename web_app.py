from flask import Flask, render_template, request, url_for, redirect
from flask import session as flask_session

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
		
		if user is not None and  user.password==user_password:
			flask_session['user_email'] = user_email
			return redirect(url_for('suggest_friends', user_id=user.id))
		else:
			return render_template('login.html')



@app.route('/signup', methods=['GET','POST'])
def sign_up():
	if request.method == 'GET':
		return render_template('signup.html')
	else:
		user_name = request.form['name']
		user_email=request.form['email']
		user_password=request.form['password']
		new_user = User(fullname = user_name, email= user_email, password=user_password)
		session.add(new_user)
		session.commit()
		flask_session['user_email'] = user_email
		return redirect(url_for('view_questions'))
 		


@app.route('/suggest/')
def suggest_friends():
	if 'user_email' in flask_session:
		user = session.query(User).filter_by(email = flask_session['user_email']).first()
		suggested_friends = []
		return render_template('suggest_friends.html',user=user,suggested_friends =suggested_friends )
	else:
		return redirect(url_for("log_in"))
	'''
	user=session.query(User).filter_by(id=user_id).first()
	suggests=session.query(User).all()
	for i in suggests:
		if user.id!=i.id:
			for 
	
	return render_template('suggest_friends.html', user=user)
	'''
@app.route('/profile/')	
def user_profile():
	if 'user_email' in flask_session:
		user = session.query(User).filter_by(email = flask_session['user_email']).first()
		return render_template('user_profile.html',user=user)
		
	else:
		return redirect(url_for("log_in"))
	
	
@app.route('/view_questions/', methods=['GET','POST'])	
def view_questions():
	if 'user_email' in flask_session:
		user = session.query(User).filter_by(email = flask_session['user_email']).first()
		simple_questions=session.query(Questions).filter_by(deep=False).all()
		deep_questions=session.query(Questions).filter_by(deep=True).all()
		if request.method == 'GET':
			return render_template('view_questions.html', user=user,simple_questions=simple_questions, deep_questions=deep_questions  )

		else:
			for q in simple_questions:
			
			
				question=session.query(Questions).filter_by(text=q.text).first()
				answer = request.form[q.text]
			
				a= User_questions(
					user_id=user_id,
					question_id=question.id,
					user_response=answer
					)
				session.add(a)
			
			session.commit()
			return redirect(url_for('suggest_friends', user_id=user.id))
	else:
		return redirect(url_for("log_in"))

@app.route('/friend_list/')
def friend_list():
	if 'user_email' in flask_session:
		user = session.query(User).filter_by(email = flask_session['user_email']).first()
		friends=user.my_friends
		
		return render_template('friend_list.html')
	else:
		return redirect(url_for("log_in"))

@app.route('/friend_profile/<int:friend_id>')
def friend_profile(friend_id):
	if 'user_email' in flask_session:
		user = session.query(User).filter_by(email = flask_session['user_email']).first()
		addfriend = request.form['addfriend']
		user.myfriends.append(addfriend)
		
		return render_template('friend_profile.html, friend_id = friend.id')

	else:
		
		return redirect(url_for("log_in"))
	
	
@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    flask_session.pop('username', None)
    return redirect(url_for('log_in'))	

@app.route('/delete_account', methods=['GET','POST'])
def delete_account():
	if 'user_email' in flask_session:
		user = session.query(User).filter_by(email = flask_session['user_email']).first()	
    		
    		if request.method == 'GET':
         		return render_template('delete_account.html', user = user)
		else:
			 session.delete(user)	
			 session.commit()
			 return redirect(url_for('user_profile'))

	else:
		
		return redirect(url_for("log_in"))
		
	
		

app.secret_key = 'u4yeoiuoxzic uoxzayw23'
if __name__ == '__main__':
    app.run(debug=True)
