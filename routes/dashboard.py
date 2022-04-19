from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_user, login_required, current_user
from utils.db import db
from forms.createMessage import createMessageForm
from forms.createProperty import createPropertyForm
from models.property import Property
from models.message import Message
from models.user import User

dashboard = Blueprint("dashboard", __name__)

@dashboard.route("/dashboard", methods=["GET", "POST"])
@login_required
def home():
    MessageList = Message.query.all()
    PropertyList = Property.query.all()
    if "admin" in current_user.rank:
        return render_template("dashboard.html", MessageList = MessageList, PropertyList = PropertyList)
    else:
        return redirect(url_for("home.home"))
    
    
@dashboard.route("/Propiedades", methods=["GET", "POST"])
@login_required
def property():
    form = createPropertyForm()
    if form.validate_on_submit():
        name = form.name.data
        category = form.category.data
        city = form.city.data
        size = form.size.data
        clasification = form.clasification.data
        price = form.price.data
        details = form.details.data
        banos = form.banos.data
        dormitorios = form.dormitorios.data
        parqueos = form.parqueos.data
        fotoperfil = form.fotoperfil.data
        foto1 = form.foto1.data
        foto2 = form.foto2.data
        foto3 = form.foto3.data
        foto4 = form.foto4.data
        newProperty = Property(name, category, city, size, clasification, price,
                               details, banos, dormitorios, parqueos, fotoperfil, foto1, foto2, foto3, foto4)
        db.session.add(newProperty)
        db.session.commit()
    form.name.data = ""
    form.category.data = ""
    form.city.data = ""
    form.size.data = ""
    form.clasification.data = ""
    form.price.data = ""
    form.details.data = ""
    form.banos.data = ""
    form.dormitorios.data = ""
    form.parqueos.data = ""
    form.fotoperfil.data = ""
    form.foto1.data = ""
    form.foto2.data = ""
    form.foto3.data = ""
    form.foto4.data = ""

    if "admin" in current_user.rank:
        return render_template("property.html", form = form)
    else:
        return redirect(url_for("home.home"))