from flask import Blueprint, render_template, redirect, url_for
from utils.db import db

post = Blueprint("post", __name__)


@post.route("/post")
def home():
    return render_template("ejemplo1.html")