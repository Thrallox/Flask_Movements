from flask_wtf import FlaskForm
from wtforms import IntegerField, DateField, StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, Length

class MovementForm(FlaskForm):
    id = IntegerField("id")
    fecha = DateField("Fecha", validators=[DataRequired()])
    concepto = StringField("Concepto", validators=[DataRequired(), Length(min=10, message="El concepto debe tener mas de 10 caracteres")])
    cantidad = FloatField("Cantidad", validators=[DataRequired()])

    submit = SubmitField("Aceptar")