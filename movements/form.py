from flask_wtf import FlaskForm
from wtforms import IntegerField, DateField, StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, Length

class MovementForm(FlaskForm):
    id = IntegerField("id")
    fecha = DateField("fecha", validators=[DataRequired()])
    concepto = StringField("concepto", validators=[DataRequired(), Length(min=10, message="El concepto debe tener mas de 10 caracteres")])
    cantidad = FloatField("cantidad", validators=[DataRequired()])

    submit = SubmitField("aceptar")