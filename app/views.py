from flask import render_template, flash, redirect, session, url_for, request, g, Flask
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db
from .models import User
from .forms import LoginForm, RegistrationForm
from werkzeug.security import generate_password_hash,check_password_hash

@app.route('/login', methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user is not None and check_password_hash(user.password_hash, form.password.data):
			#login_user(user, form.remember_me.data)
			#import pdb; pdb.set_trace()
			return redirect(url_for('user', username=str(user.username)))

	flash('Invalid username or password.')
	return render_template('/login.html', form=form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('/index'))

@app.route('/register', methods=['GET','POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		# import pdb; pdb.set_trace()
		user = User(email=form.email.data, username=form.username.data, \
			password_hash=generate_password_hash(form.password.data), level=1)
		db.session.add(user)
		db.session.commit()
		flash('You can now login.')
		return redirect(url_for('login'))
	return render_template('register.html', form=form)

@app.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first()
    if user == None:
        flash('User %s not found.' % username)
        return redirect(url_for('index'))
    if user.level == 1:
    	return render_template('admin.html', user=user)
    return render_template('user.html', user=user)