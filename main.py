from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import  DataRequired,email, length

from flask_bootstrap import Bootstrap

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), email()])
    password = PasswordField(label='Password', validators=[DataRequired(), length(min=8)])
    submit = SubmitField(label='Log in')

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    app.secret_key = "any-string-you-want-just-keep-it-secret"
    return app
app = create_app()
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET","POST"])
def login():
    default_email = 'admin@email.com'
    default_password = '12345678'
    login_form = LoginForm()
    if login_form.validate_on_submit():
        print(login_form.email.data)

        if login_form.email.data == default_email and login_form.password.data == default_password:
            return render_template('success.html')
        else:
            return render_template('denied.html')


    return render_template('login.html',form=login_form)


if __name__ == '__main__':
    app.run(debug=True)