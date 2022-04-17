from flask import Blueprint, render_template, redirect, url_for
from utils.db import db

prop = Blueprint("propiedad", __name__)


@prop.route("/propiedad")
def propiedad():
    return render_template("propiedad.html")
