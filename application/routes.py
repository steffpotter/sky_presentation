from flask import render_template
# terminal - pip3 install flask
from application import app
from candidatePage import CandidatePage
from subjectPage import SubjectPage
from subject import Subject
from candidate import Candidate
import mysql.connector
from mysql.connector import Error

@app.route('/')
def index():
    return render_template('home.html', title="Sky Get Into DevOps Course Notes")


@app.route('/subjects/<name>')
def subject(name):
    subject = getSubjectFromDatabase(name)
    return render_template('subject.html',  subjectPage=SubjectPage(name, "test.jpg", subject))


@app.route('/candidates/<name>')
def candidate(name):
    return render_template('candidate.html',  candidate=Candidate(name, "Potter - TEST", "I play rugby"))


def getSubjectFromDatabase(name): 
    sql_command = f"select * from Subject where subject_name = '{name}'"
    subject = getDataFromDatabase(sql_command)
    return Subject(subject["subject_name"], {"This is a paragraph", "This is another paragraph"})


def getCandidateFromDatabase(name): 
    sql_command = f"select * from Candidate where first_name = '{name}'"
    return getDataFromDatabase(sql_command)


def getDataFromDatabase(sql_command): 
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='db_devOpsNotes',
                                            user='root',
                                            password='password')
        
        if connection.is_connected():
            sql_select_Query = sql_command
            cursor = connection.cursor(dictionary=True)
            cursor.execute(sql_select_Query)
            return cursor.fetchone()

    except Error as e:
        print("Error while connecting to MySQL", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")