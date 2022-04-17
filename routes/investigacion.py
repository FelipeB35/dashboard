from flask import Blueprint, render_template, redirect, url_for
from utils.db import db

inv = Blueprint("investigacion", __name__)


@inv.route("/investigacion")
def investigacion():
    return render_template("investigacion.html")
