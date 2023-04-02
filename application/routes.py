from flask import render_template
# terminal - pip3 install flask
from application import app


@app.route('/')
def index():
    return render_template('home.html', title="Sky Get Into DevOps Course Notes")


@app.route('/agile')
def agile():
    return render_template('agile.html',  title="Agile")


@app.route('/flask')
def flask():
    return render_template('flask.html',  title="Flask")


@app.route('/html')
def html():
    return render_template('html.html',  title="HTML")


@app.route('/git')
def git():
    return render_template('git.html',  title="Git")


@app.route('/python')
def python():
    return render_template('python.html',  title="Python")
