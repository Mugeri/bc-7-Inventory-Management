from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from . import login_manager

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(120), index=True, unique=True)
    level = db.Column(db.Integer, index=True, unique=False)

    @login_manager.user_loader
    def load_user(user_id):
    	return User.query.get(int(user_id))

	# @property
	# def password(self):
	# 	raise AttributeError("password is not a readable attribute")

	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)

    #for registration
	confirmed = db.Column(db.Boolean, default=False)
	def generate_confirmation_token(self, expiration=3600):
		s = Serializer(current_app.config['SECRET_KEY'], expiration)
		return s.dumps({'confirm': self.id})

	def confirm(self, token):
		s = Serializer(current_app.config['SECRET_KEY'])
		try:
			data = s.loads(token)
		except:
			return False
		if data.get('confirm') != self.id:
			return False
		self.confirmed = True
		db.session.add(self)
		return True

    def __repr__(self):
        return '<User %r> password_hash %r email %r' % (self.username, self.password_hash, self.email)

    	

class Assets(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	assetname = db.Column(db.String(64), index=True, unique=False)
	assetdescription = db.Column(db.String(500), index=True, unique=False)
	serialnumber = db.Column(db.String(50), index=True, unique=True)
	andelaserial = db.Column(db.String(50), index=True, unique=True)
	datebought = db.Column(db.DateTime)

	def __repr__(self):
		return '<Asset %r>' % (self.assetname)

class Assigned(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	assetid = db.Column(db.Integer, db.ForeignKey('assets.id'))
	reclaim = db.Column(db.DateTime)

	def __repr__(self):
		return '<User %r><Asset %r>' %(self.user_id, self.assetid)
		

		