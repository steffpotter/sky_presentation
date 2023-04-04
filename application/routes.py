from flask import render_template
# terminal - pip3 install flask
from application import app
from subject import Subject
from candidate import Candidate
import mysql.connector
from mysql.connector import Error

# default route for the homepage 
@app.route('/')
def index():
    subjectsList = getSubjectsFromDatabase()
    return render_template('home.html', title="Sky Get Into DevOps Course Notes", subjects=subjectsList)


# individual subject page 
# reads the name in as a URL parameter and uses this to get the subject data from the datasource
@app.route('/subjects/<id>')
def subject(id):
    subject = getSubjectFromDatabase(id)
    return render_template('subject.html',  subjectPage=subject)


# individual candidate page
# reads the name in as a URL parameter and uses this to get the candidate from the datasource 
@app.route('/candidates/<name>')
def candidate(name):
    return render_template('candidate.html',  candidate=Candidate(name, "Potter - TEST", "I play rugby"))


# get all subjects from the database
def getSubjectsFromDatabase(): 
    sql_command = f"select * from Subject"
    subjects = getDataFromDatabase(sql_command, False)
    subjectsList = []

    for row in subjects: 
        subjectsList.insert(len(subjectsList), Subject(row["subject_id"], row["subject_name"], row["subject_logo"]))

    return subjectsList


# get the subject from the database and bind the values to the Subject class object
def getSubjectFromDatabase(id): 
    sql_command = f"select * from Subject where subject_id = '{id}'"
    subject = getDataFromDatabase(sql_command, True)

    # TODO - Get the text paragraphs from the database

    return Subject({id}, subject["subject_name"], subject["subject_logo"])


# get the candidate from the database and bind the values to the Candidate class object
def getCandidateFromDatabase(name): 
    sql_command = f"select * from Candidate where first_name = '{name}'"
    return getDataFromDatabase(sql_command, True)


# generic database access method which will return one row 
# which is the result of the query which is passed in
def getDataFromDatabase(sql_command, fetch_one): 
    try:
        # database connection details 
        connection = mysql.connector.connect(host='localhost',
                                            database='db_devOpsNotes',
                                            user='root',
                                            password='password')
        
        # if the connection is successful execute the SQL command and return the first row
        if connection.is_connected():
            sql_select_Query = sql_command
            cursor = connection.cursor(dictionary=True)
            cursor.execute(sql_select_Query)
            if fetch_one == True: 
                return cursor.fetchone()
            else: 
                return cursor.fetchall()

    except Error as e:
        print("Error while connecting to MySQL", e)

    finally:
        # make sure the connection is closed
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")