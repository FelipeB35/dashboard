from flask import Blueprint, render_template, redirect, url_for
from utils.db import db

house = Blueprint("home", __name__)


@house.route("/home")
def home():
    return render_template("home.html")
