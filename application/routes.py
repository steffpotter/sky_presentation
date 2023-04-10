from flask import render_template
# terminal - pip3 install flask
from application import app
from application.dao.candidateDao import CandidateDao
from application.dao.subjectDao import SubjectDao

# These are DAO objects - see DAO pattern. They provide a layer of abstraction between our app and the database
# To use the mock database, set useMock parameter to True, set it to False to use the MySQL db in mySqlDb.py
candidateDao = CandidateDao(useMock=True)
subjectDao = SubjectDao(useMock=True)




# default route for the homepage
@app.route('/')
def index():
    subjects = subjectDao.getAllSubjects()
    return render_template('home.html', title="Sky Get Into DevOps", subjects=subjects)


# individual subject page
# reads the name in as a URL parameter and uses this object to get the subject id and data from the datasource


# def get_subject():
#     # Some code that returns a valid `Subject` object instead of `None`
#     return Subject(1234)

@app.route('/subjects/<int:subjectId>')
def subject(subjectId):
    subjectObj = subjectDao.getSubject(subjectId)
    if subjectObj:
        return render_template('subject.html', subjectPage=subjectObj, title=subjectObj.get_subject_id())
    else:
        return f"Subject with Id {subjectId} does not exist"
    # change subject_name to subject_id



# individual candidate page
# reads the name in as a URL parameter and uses this to get the candidate from the datasource 
@app.route('/candidates/<name>')
def candidate(name):
    candidateObj = candidateDao.getCandidateByName(name)
    return render_template('candidate.html', candidate=candidateObj)
