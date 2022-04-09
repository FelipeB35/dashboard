from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import InputRequired, Length, ValidationError

class createPropertyForm(FlaskForm):
    name = StringField(
        validators=[
            InputRequired(),
            Length(min=3, max=50),
        ],
        render_kw={"placeholder": "Nombre"},
    )
    
    category = StringField(
        validators=[
            InputRequired(),
            Length(min=3, max=50),
        ],
        render_kw={"placeholder": "categoria"},
    )
    
    city = StringField(
        validators=[
            InputRequired(),
            Length(min=3, max=200),
        ],
        render_kw={"placeholder": "ciudad"},
    )

    size = IntegerField(
        validators=[
            InputRequired()
        ],
        render_kw={"placeholder": "tamaño"},
    )
    
    clasification = StringField(
        validators=[
            InputRequired(),
            Length(min=3, max=200),
        ],
        render_kw={"placeholder": "clasificacion"},
    )
    
    price = IntegerField(
        validators=[
            InputRequired()
        ],
        render_kw={"placeholder": "precio"},
    )
    
    details = StringField(
        validators=[
            InputRequired(),
            Length(min=3, max=500),
        ],
        render_kw={"placeholder": "detalles"},
    )
    submit = SubmitField("crear")