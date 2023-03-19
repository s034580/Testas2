import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_mail import Mail

base_dir = os.path.dirname(__file__)

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY")
app.app_context().push()


basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "data.db")
app.config['SECRET_KEY'] = 'asdpasjdoaisd'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
bcrypt = Bcrypt(app)
mail = Mail(app)

from app.models import Groups
from app.models import Bills
from app.models import UserGroup
from app import views
from app.admin import *
