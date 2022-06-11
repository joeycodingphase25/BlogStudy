from flask import flash, redirect, render_template, url_for
from flask import render_template
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    title = 'Home'
    user = {'username':'joseph'}
    posts = [
        {
            'author': {'username':'John'},
            'body': 'Beautiful day in Paradise'
        },
        {
            'author': {'username':'Suze'},
            'body': 'I am a blogger for real'
        }
    ]
    return render_template('index.html', title=title, user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', form=form, title="Sign-in")