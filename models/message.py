from utils.db import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    mail = db.Column(db.String(200), nullable=False)
    message = db.Column(db.String(200), nullable=False)

    def __init__(self, name, mail, message) -> None:
        self.name = name
        self.mail = mail
        self.message = message
