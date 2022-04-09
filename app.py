from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from utils.db import db
from routes.dashboard import dashboard
from flask_migrate import Migrate

app = Flask(__name__)

app.config.from_object("config.BaseConfig")

SQLAlchemy(app)
Migrate(app, db)
app.register_blueprint(dashboard)
