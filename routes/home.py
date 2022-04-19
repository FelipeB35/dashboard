from flask import Blueprint, render_template, redirect, url_for
from utils.db import db
from models.property import Property

house = Blueprint("home", __name__)


@house.route("/")
def home():
    x = "Casa"
    propertyList = Property.query.all()
    listCasas = Property.query.filter_by(clasification=x).all()
    listApartamentos = Property.query.filter_by(clasification="Apartamento").all()
    listRanchos = Property.query.filter_by(clasification="Rancho").all()
    print(listCasas)
    return render_template("home.html", casas = listCasas, apartamentos = listApartamentos, ranchos = listRanchos, property = propertyList)
