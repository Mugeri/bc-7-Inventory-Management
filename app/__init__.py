from flask.ext.login import LoginManager
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

login_manager.init_app(app)

def create_app(config_name):
	login_manager.init_app(app)
	bootstrap.init_app(app)


from app import views, models