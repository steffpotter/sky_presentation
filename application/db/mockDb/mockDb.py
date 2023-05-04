import os
import re
import logging
from application.db.exceptions.customDbExceptions import SubjectNotFoundError, CandidateNotFoundError

logger = logging.getLogger(__name__)

def readContentFile(subject):
    """
    Build up content file path using os.getcwd and append the remainder of the file path.
    NB - Content File needs to be in application/db/mockDb/ directory and needs to
    be titled "[INSERT SUBJECT NAME]Content.txt"
    """
    cwd = os.getcwd()
    cwdFragments = re.split("(sky_presentation)", cwd)
    path = ''.join([cwdFragments[0], f"/application/subjectContent/{subject}Content.txt"])
    file = open(path)
    content = file.read()
    file.close()
    return content


class MockDb:
    """
    Mock db implementation for mimicking a mySQL connector connection. Designed to allow for toggled use of an actual
    database as defined in the environment variables, this should also allow for faster development for beginners on the
    team.

    The data held within this mock db is based on the 'db_devOpsNotes.sql' file
    """

    def __init__(self):
        # returns the current working directory of the application we use this later to build up our content file paths
        self._baseContentFilePath = os.getcwd()
        self._allSubjectRows = [{'subject_id': 1,
                                 'subject_logo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python'
                                                 '-logo-notext.svg'
                                                 '/438px-Python-logo-notext.svg.png',
                                 'subject_name': 'Python',
                                 'subject_content': readContentFile(subject="Python"),
                                 'subject_questions': [
                                     {
                                         'question_id': 1,
                                         'question_text': 'When was the first version of Python released?',
                                         'answers': [
                                             {'answer_id': 1, 'answer_text': '1989'},
                                             {'answer_id': 2, 'answer_text': '1991'},
                                             {'answer_id': 3, 'answer_text': '1993'},
                                             {'answer_id': 4, 'answer_text': '1995'},
                                         ],
                                         'correct_answer_id': 2
                                     },
                                     {
                                         'question_id': 2,
                                         'question_text': 'What is Python\'s design philosophy?',
                                         'answers': [
                                             {'answer_id': 1, 'answer_text': 'Code optimization'},
                                             {'answer_id': 2, 'answer_text': 'Code obfuscation'},
                                             {'answer_id': 3, 'answer_text': 'Code readability'},
                                             {'answer_id': 4, 'answer_text': 'Code complexity'},
                                         ],
                                         'correct_answer_id': 3
                                     }
                                 ]},
                                {'subject_id': 2,
                                 'subject_logo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c'
                                                 '/Flask_logo.svg/640px'
                                                 '-Flask_logo.svg.png',
                                 'subject_name': 'Flask',
                                 'subject_content': readContentFile(subject="Flask"),
                                 'subject_questions': {}},
                                {'subject_id': 3,
                                 'subject_logo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/93'
                                                 '/Amazon_Web_Services_Logo.svg/768px-Amazon_Web_Services_Logo.svg'
                                                 '.png?20170912170050',
                                 'subject_name': 'AWS',
                                 'subject_content': readContentFile(subject="AWS"),
                                 'subject_questions': {}},
                                {'subject_id': 4,
                                 'subject_logo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Git-logo'
                                                 '.svg/640px-Git'
                                                 '-logo.svg.png',
                                 'subject_name': 'Git',
                                 'subject_content': readContentFile(subject="Git"),
                                 'subject_questions': {}},
                                {'subject_id': 5,
                                 'subject_logo': 'https://www.svgrepo.com/show/379764/agile.svg',
                                 'subject_name': 'Agile',
                                 'subject_content': readContentFile(subject="Agile"),
                                 'subject_questions': {}}, ]

        self._allCandidateRows = [{'candidate_id': 1,
                                   'first_name': 'Steff',
                                   'last_name': 'Potter',
                                   'fun_fact': 'I play rugby!',
                                   'git_username': 'steffpotter'},
                                  {'candidate_id': 2,
                                   'first_name': 'Deanne',
                                   'last_name': 'Clarke',
                                   'fun_fact': "I plan to visit every country in the world. I've been to 45 so far.",
                                   'git_username': 'DeanneC24'},
                                  {'candidate_id': 3,
                                   'first_name': 'Rach',
                                   'last_name': 'Wylie',
                                   'fun_fact': "This is my fun fact.",
                                   'git_username': 'rachelwylie'},
                                  {'candidate_id': 4,
                                   'first_name': 'Saynab',
                                   'last_name': 'Diini',
                                   'fun_fact': "This is my fun fact.",
                                   "git_username": "sdiini001"},
                                  {'candidate_id': 5,
                                   'first_name': 'Angel',
                                   'last_name': 'Surname',
                                   'fun_fact': "This is my fun fact.",
                                   'git_username': ""}]

    def getAllSubjects(self):
        return self._allSubjectRows

    def getAllCandidates(self):
        return self._allCandidateRows

    def getSubject(self, subjectId):
        # happy to talk through this line! It's a next generator to find the correct row using the subjectId

        try:
            subject = next(
                subjectRow for subjectRow in self._allSubjectRows if subjectRow.get("subject_id") == subjectId)

        except StopIteration as e:
            raise SubjectNotFoundError from e

        except Exception as e:
            logger.warning(msg=f"Could not retrieve subject with Id {subjectId},method failed with error:{e}")
            return None

        return subject

    def getSubjectByName(self, subjectName):
        # happy to talk through this line! It's a next generator to find the correct row using the subjectName

        try:
            subject = next(
                subjectRow for subjectRow in self._allSubjectRows
                if subjectRow.get("subject_name").lower() == subjectName.lower())

        except StopIteration as e:
            raise SubjectNotFoundError from e

        except Exception as e:
            logger.warning(msg=f"Could not retrieve subject with Id {subjectName},method failed with error:{e}")
            return

        return subject

    def getCandidateById(self, candidate_id):

        try:
            candidate = next(candidateRow for candidateRow in self._allCandidateRows
                         if candidateRow.get("candidate_id") == candidate_id)

        except StopIteration as e:
            raise CandidateNotFoundError from e

        return candidate
