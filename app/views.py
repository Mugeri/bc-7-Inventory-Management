from flask import render_template, flash, redirect, session, url_for, request, g, Flask
#from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db
from .models import User, Assets
from .forms import LoginForm, RegistrationForm
from werkzeug.security import generate_password_hash,check_password_hash

@app.route('/login', methods=['GET','POST'])
def login():
	form = LoginForm()
	if request.method == 'POST':
		
		if form.validate_on_submit():
			user = User.query.filter_by(username=form.username.data).first()
			if user is not None and check_password_hash(user.password_hash, form.password.data):
				session['username']=form.username.data
				return redirect(url_for('user', username=str(user.username)))

	flash('Invalid username or password.')
	return render_template('/login.html', form=form)

@app.route('/logout')
def logout():
	session.pop('username', None)
	return redirect(url_for('/login'))

@app.route('/register', methods=['GET','POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		
		user = User(email=form.email.data, username=form.username.data, \
			password_hash=generate_password_hash(form.password.data))
		db.session.add(user)
		db.session.commit()
		flash('You can now login.')
		return redirect(url_for('login'))
	return render_template('register.html', form=form)

@app.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first()
    users = User.query.all()
    assets = Assets.query.all()
    if user == None:
        flash('User %s not found.' % username)
        return redirect(url_for('login'))
    else:
    	if user.level == 1:
    		return render_template('admin.html', user=user, users=users, assets=assets)
		if user.level == 2:
			return render_template('jadmin.html', user=user, assets=assets)
		else:
			return render_template('user.html', user=user)

@app.route('/asset', methods=['GET','POST'])
def asset():
	if request.method == 'POST':
		import pdb; pdb.set_trace()
		if request.form['assetName'] is not None:
			form = {'assetname': request.form['assetName'],
					'assetdescription': request.form['description'],
					'serialnumber': request.form['serialno'],
					'andelaserial': request.form['serialcode'],
					'available': True
					}

			asset = Assets(**form)
			db.session.add(asset)
			db.session.commit()
			flash('asset successfully added')

			return redirect(url_for('user', username=session['username']))
	flash('Asset not added')
	return redirect(url_for('user', username=session['username']))

@app.route('/assigned', methods=['GET', 'POST'])
def assigned():
	if request.method == 'POST':
		if request.form['userid']:
			form = {'user_id': request.form['userid'],
					'assetid': request.form['assetid'],
					'reclaim': request.form['reclaim']
					}

			assign = Assigned(**form)
			db.session.add(assign)
			db.session.commit()
			asset = Assets.query.filter_by(assetid=request.form['assetid']).first()
			asset.available=False
			db.session.add(asset)
			db.session.commit()
			flash('asset successfully assigned')
			reload
	return redirect(url_for('user', username=session['username']))