from flask import Flask, after_this_request, render_template, redirect, send_file, url_for, request, flash, make_response, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask_migrate import Migrate
from flask_mail import Mail, Message
#from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
#csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:batata@localhost/database1'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'FW3434ff545h4RFE55$#f$t%yhtFF'
app.config['TESTING'] = False
app.config['MAIL_SERVER'] = 'smtp.office365.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
#app.config['MAIL_DEBUG'] = True
app.config['MAIL_USERNAME'] = 'moussaalit@outlook.com'
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_DEFAULT_SENDER'] = 'moussaalit@outlook.com'
app.config['MAIL_MAX_EMAILS'] = 1
#app.config['MAIL_SUPPRESS_SEND'] = False #TRUE LAW BAS 3AM 2A3MIL TESTS MWA22ATE HAYK SHI
app.config['MAIL_ASCII_ATTACHEMENTS'] = False



db = SQLAlchemy(app)
migrate = Migrate(app, db)

#mail

mail = Mail(app)

#Flask_login Stuff

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from package import routes # bn3ouz l import lal routesla2an bidounoun lm server bibattil yet3arraf 3a 2ayya path #, dbmodels, functions
