from flask import Blueprint, render_template, redirect, url_for
from utils.db import db
from forms.createMessage import createMessageForm
from models.message import Message

contact = Blueprint("contacto", __name__)


@contact.route("/contacto", methods=["GET", "POST"])
def contacto():
    form = createMessageForm()
    if form.validate_on_submit():
        name = form.name.data
        mail = form.mail.data
        message = form.message.data
        newMessage = Message(name, mail, message)
        db.session.add(newMessage)
        db.session.commit()
        return redirect(url_for("contacto.contacto"))
    return render_template("contacto.html", form = form)
