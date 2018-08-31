__author__ = 'suren'

from app import app
from flask import render_template, request, flash,redirect, url_for
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user
from app.models import User


# # Start from Requiring Users To Login int he Tutorial:
    # https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins

@app.route('/')
@app.route('/index')
def index():
    templateData = {
        'title' : 'Home Page'
    }
    return render_template('index.html', **templateData)
    #return "Hello World" + app.config.get('SECRET_KEY')

@app.route('/login', methods= ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm(request.form)
    # print(form.username.data)
    # print(form.validate_on_submit())
    if form.validate_on_submit():
       user = User.query.filter_by(username=form.username.data).first()
       if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
       else:
           login_user(user,remember=form.remember_me.data)
           return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user
    return redirect(url_for('index'))