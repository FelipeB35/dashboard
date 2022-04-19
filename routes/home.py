from flask import Blueprint, render_template, redirect, url_for
from utils.db import db
from models.property import Property

house = Blueprint("home", __name__)


@house.route("/")
def home():
    propertyList = Property.query.all()
    listCasas = Property.query.filter_by(clasification="Casa").all()
    listApartamentos = Property.query.filter_by(clasification="Apartamento").all()
    listRanchos = Property.query.filter_by(clasification="Rancho").all()
    return render_template("home.html", casas = listCasas, apartamentos = listApartamentos, ranchos = listRanchos)
