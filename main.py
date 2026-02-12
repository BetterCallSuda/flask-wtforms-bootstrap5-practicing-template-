from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField
from wtforms.validators import DataRequired, URL
import csv


app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        name = form.username.data
        password = form.password.data
        print(name, password)
        return redirect(url_for('home'))
    return render_template("login.html", form=form)

@app.route('/')
def home():
    return "<h1>Welcome home</h1>"




if __name__ == '__main__':
    app.run(debug=True)
