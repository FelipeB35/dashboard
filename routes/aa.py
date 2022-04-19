from flask import Blueprint, render_template, redirect, url_for
from utils.db import db
from models.property import Property

aa = Blueprint("aa", __name__)


@aa.route("/", methods=["GET", "POST"])
def home():
    propertyList = Property.query.all()
    return render_template("aa.html", property = propertyList)
