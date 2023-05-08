from flask import render_template
# terminal - pip3 install flask
from application import app
from application.dao.candidateDao import CandidateDao
from application.dao.subjectDao import SubjectDao

candidateDao = CandidateDao()
subjectDao = SubjectDao()


# default route for the homepage
@app.route('/')
def index():
    subjects = subjectDao.getAll()
    candidates = candidateDao.getAll()
    return render_template('home.html', is_home_page=True, title="Sky Get Into DevOps", subjects=subjects, candidates=candidates)


# individual subject page
# reads the name in as a URL parameter and uses it to fetch subject data from the db and create a Subject object from it
@app.route('/subjects/<subjectName>')
def subject(subjectName):
    subjectObj = subjectDao.getSubjectByName(subjectName)
    if subjectObj:
        return render_template('subject.html', subjectPage=subjectObj, title=subjectName)
    else:
        return render_template('subjectNotFound.html', subjectName=subjectName, title='Subject Not Found')


# individual candidate page
# reads the id in as a URL parameter and uses this to get the candidate from the datasource
@app.route('/candidates/<int:candidateId>')
def candidate(candidateId):
    candidateObj = candidateDao.getCandidateById(candidateId)
    return render_template('candidate.html', is_home_page=False, candidate=candidateObj)
