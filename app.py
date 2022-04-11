from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from utils.loginManagerService import login_manager
from utils.db import db
from flask_migrate import Migrate
from routes.auth import auth
from routes.dashboard import dashboard

app = Flask(__name__)

app.config.from_object("config.BaseConfig")

SQLAlchemy(app)
Migrate(app, db)
Bcrypt(app)
login_manager.init_app(app)


app.register_blueprint(dashboard)
app.register_blueprint(auth)