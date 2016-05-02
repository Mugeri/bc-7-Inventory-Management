WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

'''
	the following are db configurations
	The SQLALCHEMY_DATABASE_URI is required 
	by the Flask-SQLAlchemy extension. 
	This is the path of our database file.
	The SQLALCHEMY_MIGRATE_REPO is the folder 
	where we will store the SQLAlchemy-migrate data files.
'''
import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')