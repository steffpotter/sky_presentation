from flask import render_template
# terminal - pip3 install flask
from application import app
from candidate import Candidate
from subject import Subject

@app.route('/')
def index():
    return render_template('home.html', title="Sky Get Into DevOps Course Notes")


@app.route('/subjects/<name>')
def subject(name):
    # can we get these from a database?
    return render_template('subject.html',  subject=Subject("name - TEST", {"Here is some content", "And some more content"}))


@app.route('/candidates/<name>')
def candidate(name):
    return render_template('candidate.html',  candidate=Candidate(name, "Potter - TEST", "I play rugby"))