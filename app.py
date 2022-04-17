from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from utils.loginManagerService import login_manager
from utils.db import db
from flask_migrate import Migrate
from routes.auth import auth
from routes.dashboard import dashboard
from routes.home import house
from routes.contacto import contact
from routes.investigacion import inv
from routes.nosotros import about
from routes.propiedad import prop

app = Flask(__name__)

app.config.from_object("config.BaseConfig")

SQLAlchemy(app)
Migrate(app, db)
Bcrypt(app)
login_manager.init_app(app)


app.register_blueprint(dashboard)
app.register_blueprint(auth)
app.register_blueprint(house)
app.register_blueprint(contact)
app.register_blueprint(inv)
app.register_blueprint(about)
app.register_blueprint(prop)
