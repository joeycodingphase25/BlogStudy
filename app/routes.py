from flask import render_template
from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    title = 'Home'
    user = {'username':'joseph'}
    return render_template('index.html', title=title, user=user)