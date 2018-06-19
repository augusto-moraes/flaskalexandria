from app import app, db
from flask import render_template

from app.models.forms import CadForm
from app.models.forms import LoginForm

@app.route("/index", methods=["POST", "GET"])
@app.route("/", methods=["POST", "GET"])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
    else:
        print(form.errors)
    return render_template('index.html',
                            form=form)

@app.route("/cadastro", methods=["POST", "GET"])
def cadastro():
    form = CadForm()
    if form.validate_on_submit():
        print(form.name.data)
        print(form.username.data)
        print(form.password.data)
        print(form.confirmPassword.data)
        print(form.city.data)
        print(form.state.data)
        print(form.cep.data)
        print(form.end.data)
        print(form.born.data)
    else:
        print(form.errors)
    return render_template('cadastro.html',
                            form=form)
