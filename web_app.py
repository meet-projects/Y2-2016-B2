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
		print(new_user.fullname)
		session.add(new_user)
		session.commit()
		all_questions=session.query(Questions).all()
		for i in all_questions:
			a= User_questions(
					user_id=new_user.id,
					question_id=i.id,
					user_response=" "
					)
			session.add(a)

		session.commit()
		flask_session['user_email'] = user_email
		return redirect(url_for('view_questions'))



@app.route('/suggest/')
def suggest_friends():
	if 'user_email' in flask_session:
		user = session.query(User).filter_by(email = flask_session['user_email']).first()

	

		my_questions= session.query(User_questions).filter_by(user_id=user.id).all()
		people=session.query(User).all()
		counter_deep=[]
		counter_not_deep=[]
		for i in people:
			counter_deep.append(0)
			counter_not_deep.append(0)
		suggested_friends=[]

		for i in range(len(my_questions)):
			for j in range(len(people)):
				if user.id!=people[j].id:
					my_answer=session.query(User_questions).filter_by(id=my_questions[i].id).first()
					friend_answer=session.query(User_questions).filter_by(question_id=my_questions[i].question_id,user_id=people[j].id).first()
					if my_answer.user_response!=" " and friend_answer.user_response!=" ":

						if my_answer.user_response!=friend_answer.user_response and session.query(Questions).filter_by(id=my_answer.question_id).first().deep==False:
							counter_not_deep[j]+=1
						if my_answer.user_response==friend_answer.user_response and session.query(Questions).filter_by(id=my_answer.question_id).first().deep==True:
							counter_deep[j]+=1


		for x in range(len(people)):
			if counter_deep[x]>5 and counter_not_deep[x]>3:
				suggested_friends.append(people[x])

		return render_template('suggest_friends.html',user=user,suggested_friends =suggested_friends )



	else:
		return redirect(url_for("log_in"))
	
@app.route('/profile/', methods=['GET','POST'])
def user_profile():
	if 'user_email' in flask_session:
		user = session.query(User).filter_by(email = flask_session['user_email']).first()
		if request.method == 'GET':
			
			return render_template('user_profile.html',user=user)
		else:
			about=request.form['about']
			print (about)
			user.about_myself=about
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


				
				answer = request.form[q.text]
				print(answer)
				print('we are here')
				if answer!=" ":
					question=session.query(User_questions).filter_by(question_id=q.id, user_id=user.id).first()
					question.user_response=answer
				
			for q in deep_questions:


				answer = request.form[q.text]
				if answer!=" ":
					question=session.query(User_questions).filter_by(question_id=q.id, user_id=user.id).first()
					question.user_response=answer


			session.commit()
			return redirect(url_for('suggest_friends', user_id=user.id))
	else:
		return redirect(url_for("log_in"))

@app.route('/friend_list')
def friend_list():
	if 'user_email' in flask_session:
		user = session.query(User).filter_by(email = flask_session['user_email']).first()
		print("we are here")
		friends=user.my_friends


		return render_template('friend_list.html',user=user)
		#return render_template('friend_list.html', user=user)
	else:
		return redirect(url_for("log_in"))

@app.route('/friend_profile/<int:friend_id>',methods=['GET','POST'] )
def friend_profile(friend_id):
		if 'user_email' in flask_session:
			user = session.query(User).filter_by(email = flask_session['user_email']).first()
			if request.method == 'GET':
				friend=session.query(User).filter_by(id=friend_id).first()
				return render_template('friend_profile.html', friend = friend)
			else:
				new_friend=session.query(User).filter_by(id=friend_id).first()
				print(new_friend.fullname)
				user.my_friends.append(new_friend)
				print("we made it!")

				friend=session.query(User).filter_by(id=friend_id).first()
				session.commit()
				
				return render_template('friend_list.html',user=user)

		else:

			return redirect(url_for("log_in"))


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    flask_session.pop('username', None)
    return redirect(url_for('log_in'))

#@app.route('/delete_account', methods=['GET','POST'])
#def delete_account():
#if 'user_email' in flask_session:
#user = session.query(User).filter_by(email = flask_session['user_email']).first()
#if request.method == 'GET':
#return render_template('delete_account.html', user.my_friends= user.my_friends)
#else:
#session.delete(user)
#session.commit()
#return redirect(url_for('user_profile'))
#else:
#return redirect(url_for("log_in"))


	 


app.secret_key = 'u4yeoiuoxzic uoxzayw23'
if __name__ == '__main__':
    app.run(debug=True)
