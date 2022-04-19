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

    def __init__(self, name, category, city, size, clasification ,price, details) -> None:
        self.name = name
        self.category = category
        self.city = city
        self.size = size
        self.clasification = clasification
        self.price = price
        self.details = details
