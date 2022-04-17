from flask import Blueprint, render_template, redirect, url_for
from utils.db import db
from models.property import Property

prop = Blueprint("propiedad", __name__)


@prop.route("/propiedad/<int:propertyId>", methods=["GET", "POST"])
def propiedad(propertyId):
    property = Property.query.filter_by(id=propertyId).first()
    return render_template("propiedad.html", property = property)
