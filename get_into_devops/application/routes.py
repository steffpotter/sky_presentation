from flask import render_template
# terminal - pip3 install flask
from application import app


@app.route('/')
def index():
    return render_template('home.html')
