from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Jin'}
    posts = [
        {
            'author': {'username': 'Jin'},
            'body': 'Beautiful day in Toronto'
        },      
        {
            'author': {'username': 'Summer'},
            'body': 'Beautiful dragon I am'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)

