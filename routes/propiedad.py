from flask import Blueprint, render_template, redirect, url_for
from utils.db import db
from models.property import Property

prop = Blueprint("propiedad", __name__)


<<<<<<< HEAD
@prop.route("/propiedad/<int:id>")
def propiedad(id):
    propertyList = Property.query.filter_by(id=id).first()
    return render_template("propiedad.html", propiedad = propertyList)
=======
@prop.route("/propiedad")
def propiedad():
    return render_template("propiedad.html")
>>>>>>> af97a94de024b2f4f6844b363a43a74c95aacc42
