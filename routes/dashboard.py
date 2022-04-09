from flask import Blueprint, render_template, redirect, url_for
from utils.db import db
from forms.createMessage import createMessageForm
from forms.createProperty import createPropertyForm
from models.property import Property
from models.message import Message

dashboard = Blueprint("dashboard", __name__)

@dashboard.route("/", methods=["GET", "POST"])
def home():
    form = createMessageForm()
    MessageList = Message.query.all()
    if form.validate_on_submit():
        name = form.name.data
        mail = form.mail.data
        message = form.message.data
        newMessage = Message(name, mail, message)
        db.session.add(newMessage)
        db.session.commit()
    form.name.data = ""
    form.mail.data = ""
    form.message.data = ""
    return render_template("dashboard.html", form = form, MessageList = MessageList)

@dashboard.route("/Propiedades", methods=["GET", "POST"])
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
        newProperty = Property(name, category, city, size, clasification, price, details)
        db.session.add(newProperty)
        db.session.commit()
    return render_template("property.html", form = form)