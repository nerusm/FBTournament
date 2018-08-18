__author__ = 'suren'

from app import app
from flask import render_template, request, flash,redirect, url_for
from app.forms import LoginForm


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
    form = LoginForm(request.form)
    print(form.username.data)
    print(form.validate_on_submit())
    if form.validate_on_submit():
        print('inside if')
        flash('Login Request Received for User: {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    print('hi')
    return render_template('login.html', title='Sign In', form=form)