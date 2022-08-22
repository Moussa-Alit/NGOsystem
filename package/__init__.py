from flask import Flask, after_this_request, render_template, redirect, send_file, url_for, request, flash, make_response, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask_migrate import Migrate


app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:batata@localhost/database1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://vmfbelplxyvepj:a2979b6807823c413e08a119955da592e94ab4f38696d568553ef3b11dbac674@ec2-54-87-179-4.compute-1.amazonaws.com:5432/deljs855e01f1t'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'FW3434ff545h4RFE55$#f$t%yhtFF'


db = SQLAlchemy(app)
migrate = Migrate(app, db)
#Flask_login Stuff

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from package import routes, dbmodels, functions
