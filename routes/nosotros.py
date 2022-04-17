from flask import Blueprint, render_template, redirect, url_for
from utils.db import db

about = Blueprint("nosotros", __name__)


@about.route("/nosotros")
def nosotros():
    return render_template("nosotros.html")
