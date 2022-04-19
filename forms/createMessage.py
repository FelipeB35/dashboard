from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import InputRequired, Length, ValidationError

class createMessageForm(FlaskForm):
    name = StringField(
        validators=[
            InputRequired(),
            Length(min=3, max=50),
        ],
        render_kw={"placeholder": "Nombre"},
    )

    mail = StringField(
        validators=[
            InputRequired(),
            Length(min=3, max=20),
        ],
        render_kw={"placeholder": "Correo"},
    )

    message = StringField(
        validators=[
            InputRequired(),
            Length(min=3, max=200),
        ],
        render_kw={"placeholder": "mensaje"},
    )

    submit = SubmitField("Send")