from webbrowser import BackgroundBrowser

from click import BadOptionUsage
from utils.db import db

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(200), nullable=False)
    size = db.Column(db.String(200), nullable=False)
    clasification = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    details = db.Column(db.String(500), nullable=False)
    banos = db.Column(db.Integer, nullable=False)
    dormitorios = db.Column(db.Integer, nullable = False)
    parqueos = db.Column(db.Integer, nullable = False)
    fotoperfil = db.Column(db.String(1000), nullable = False)
    foto1 = db.Column(db.String(1000), nullable = False)
    foto2 = db.Column(db.String(1000), nullable = False)
    foto3 = db.Column(db.String(1000), nullable = False)
    foto4 = db.Column(db.String(1000), nullable = False)

    def __init__(self, name, category, city, size, clasification, price, details, banos, dormitorios, parqueos, fotoperfil, foto1, foto2, foto3, foto4) -> None:
        self.name = name
        self.category = category
        self.city = city
        self.size = size
        self.clasification = clasification
        self.price = price
        self.details = details
        self.banos = banos
        self.dormitorios = dormitorios
        self.parqueos = parqueos
        self.fotoperfil = fotoperfil
        self.foto1 = foto1
        self.foto2 = foto2
        self.foto3 = foto3
        self.foto4 = foto4
