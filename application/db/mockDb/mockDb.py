import os

import logging
logger = logging.getLogger(__name__)

def readContentFile(subject):
    """
    Build up content file path using os.getcwd and append the remainder of the file path.
    NB - Content File needs to be in application/db/mockDb/ directory and needs to
    be titled "[INSERT SUBJECT NAME]Content.txt"
    """
    file = open("".join([os.getcwd(), f"/application/db/mockDb/{subject}Content.txt"]))
    content = file.read()
    file.close()
    return content


class MockDb:
    """
    Mock db implementation for mimicking a mySQL connector connection. Designed to allow for toggled use of an actual
    database as defined in the environment variables, this should also allow for faster development for beginners on the
    team.

    The data held within this mock db is based on the db_devOpsNotes.sql file
    """

    def __init__(self):
        # returns the current working directory of the application we use this later to build up our content file paths
        self._baseContentFilePath = os.getcwd()
        self._allSubjectRows = [{'subject_id': 1,
                                 'subject_logo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python'
                                                 '-logo-notext.svg'
                                                 '/438px-Python-logo-notext.svg.png',
                                 'subject_name': 'Python',
                                 'subject_content': "Fun Python Content",
                                 'subject_questions': {}},
                                {'subject_id': 2,
                                 'subject_logo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c'
                                                 '/Flask_logo.svg/640px'
                                                 '-Flask_logo.svg.png',
                                 'subject_name': 'Flask',
                                 'subject_content': "Fun Flask Content",
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
                                 'subject_content': readContentFile(subject="Git"), # CHANGED THIS
                                 'subject_questions': {}},
                                {'subject_id': 5,
                                 'subject_logo': 'https://www.svgrepo.com/show/379764/agile.svg',
                                 'subject_name': 'Agile',
                                 'subject_content': readContentFile(subject="Agile"), # Changed this
                                 'subject_questions': {}}, ]

        self._allCandidateRows = [{'candidate_id': 1,
                                   'first_name': 'Steff',
                                   'last_name': 'Potter',
                                   'fun_fact': 'I play rugby!'},
                                  {'candidate_id': 2,
                                   'first_name': 'Deanne',
                                   'last_name': 'Clarke',
                                   'fun_fact': "I plan to visit every country in the world. I've been to 45 so far."}, ]

    def getAllSubjects(self):
        return self._allSubjectRows

    def getSubject(self, subjectId):
        # happy to talk through this line! It's a next generator to find the correct row using the subjectId

        try:
            subject = next(subjectRow for subjectRow in self._allSubjectRows if subjectRow.get("subject_id") == subjectId)

        except StopIteration as e:
            logger.warn( msg=f"Could not retrieve subject with Id {subjectId}")
            return None
        except Exception as e:
            logger.warn(msg=f"Could not retrieve subject with Id {subjectId},method failed with error:{e}")

        return subject

    def getCandidateByName(self, candidateName):
        candidate = next(candidateRow for candidateRow in self._allCandidateRows
                         if candidateRow.get("first_name") == candidateName)
        return candidate
