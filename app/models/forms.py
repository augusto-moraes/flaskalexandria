from flask_wtf import FlaskForm
from wtforms import IntegerField ,DateField, StringField, PasswordField, BooleanField, FileField, SubmitField
from wtforms.validators import DataRequired


class CadForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    confirmPassword = PasswordField("confirmPassword", validators=[DataRequired()])
    city = StringField("city", validators=[DataRequired()])
    state = StringField("state", validators=[DataRequired()])
    cep = IntegerField("cep", validators=[DataRequired()])
    end = StringField("end", validators=[DataRequired()])
    born = IntegerField("born")
    profileImg = FileField("profileImg")
    cadSubmit = SubmitField("cadSubmit")

class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    logSubmit = SubmitField("logSubmit")
