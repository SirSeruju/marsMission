from flask import Flask, render_template, redirect
from data.db_session import *
from data.jobs import Jobs
from data.users import User
from forms.user import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route("/")
def index():
	db_sess = create_session()
	jobs = db_sess.query(Jobs, User)
	jobs = jobs.join(User, Jobs.team_leader == User.id)
	jobs = jobs.all()
	return render_template("index.html", jobs=jobs)

@app.route('/register', methods=['GET', 'POST'])
def reqister():
	form = RegisterForm()
	if form.validate_on_submit():
		if form.password.data != form.password_again.data:
			return render_template('register.html', title='Registration',
								   form=form,
								   message="Passwords does not match.")
		db_sess = create_session()
		if db_sess.query(User).filter(User.email == form.email.data).first():
			return render_template('register.html', title='Registration',
								   form=form,
								   message="User already exist.")
		user = User(
			surname = form.surname.data,
			name = form.name.data,
			age = form.age.data,
			position = form.position.data,
			speciality = form.speciality.data,
			address = form.address.data,
			email = form.email.data,
		)
		user.set_password(form.password.data)

		db_sess.add(user)
		db_sess.commit()
		return redirect('/login')
	return render_template('register.html', title='Регистрация', form=form)


def main():
	global_init("db/mars_explorer.db")
	app.run()

if __name__ == '__main__':
	main()
