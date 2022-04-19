from flask import Blueprint, render_template
from utils.db import db
from models.property import Property

house = Blueprint("home", __name__)


@house.route("/", methods=["GET", "POST"])
def home():
    PropertyList = Property.query.all()
    ListCasas = Property.query.filter_by(clasification="Casa").all()
    ListApartamentos = Property.query.filter_by(clasification="Apartamento").first()
    ListRanchos = Property.query.filter_by(clasification="Rancho").first()
    return render_template("home.html", ListCasas = ListCasas, ListApartamentos = ListApartamentos, ListRanchos = ListRanchos, PropertyList = PropertyList)
