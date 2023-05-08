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
    try:
        cwd = os.getcwd()
        cwdFragments = re.split("(sky_presentation)", cwd)
        path = ''.join([cwdFragments[0], f"/application/subjectContent/{subject}Content.txt"])
        logger.warning(f"Cwd: {cwd}")
        logger.warning(f"Retrieving subject content from path: {path}")
        file = open(path)
        content = file.read()
        file.close()
        return content
    except FileNotFoundError as e:
        logger.warning("Unable to retrieve subject content due to non existent path")


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
                                 'subject_questions': [
                                    {
                                         'question_id': 1,
                                         'question_text': 'What is Flask?',
                                         'answers': [
                                             {'answer_id': 1, 'answer_text': 'A popular Python web framework'},
                                             {'answer_id': 2, 'answer_text': 'A database management system'},
                                             {'answer_id': 3, 'answer_text': 'A cloud-based storage solution'},
                                             {'answer_id': 4, 'answer_text': 'A machine learning library'},
                                        ],
                                        'correct_answer_id': 1
                                    },
                                    {
                                         'question_id': 2,
                                         'question_text': 'What are some advantages of using Flask?',
                                         'answers': [
                                             {'answer_id': 1, 'answer_text': 'It is easy to deploy and maintain'},
                                             {'answer_id': 2, 'answer_text': 'It can only be used with Python'},
                                             {'answer_id': 3, 'answer_text': 'It provides advanced machine learning features'},
                                             {'answer_id': 4, 'answer_text': 'It is a heavyweight framework'},
                                         ],
                                         'correct_answer_id': 1
                                     }
                                 ]},
                                {'subject_id': 3,
                                 'subject_logo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/93'
                                                 '/Amazon_Web_Services_Logo.svg/768px-Amazon_Web_Services_Logo.svg'
                                                 '.png?20170912170050',
                                 'subject_name': 'AWS',
                                 'subject_content': readContentFile(subject="AWS"),
                                 'subject_questions': [
                                    {
                                         'question_id': 1,
                                         'question_text': 'What is AWS?',
                                         'answers': [
                                             {'answer_id': 1, 'answer_text': 'A cloud computing platform'},
                                             {'answer_id': 2, 'answer_text': 'A database management system'},
                                             {'answer_id': 3, 'answer_text': 'A machine learning library'},
                                             {'answer_id': 4, 'answer_text': 'An antivirus software'},
                                        ],
                                        'correct_answer_id': 1
                                    },
                                    {
                                         'question_id': 2,
                                         'question_text': 'What services does AWS provide?',
                                         'answers': [
                                             {'answer_id': 1, 'answer_text': 'Computing power, storage, databases, and networking'},
                                             {'answer_id': 2, 'answer_text': 'Video editing and animation tools'},
                                             {'answer_id': 3, 'answer_text': 'Game development engines'},
                                             {'answer_id': 4, 'answer_text': 'Accounting software'},
                                         ],
                                         'correct_answer_id': 1
                                     },
                                     {
                                         'question_id': 3,
                                         'question_text': 'What are some benefits of using AWS?',
                                         'answers': [
                                             {'answer_id': 1, 'answer_text': 'Reduced IT costs and improved agility'},
                                             {'answer_id': 2, 'answer_text': 'Increased hardware requirements and longer deployment times'},
                                             {'answer_id': 3, 'answer_text': 'Limited scalability and flexibility'},
                                             {'answer_id': 4, 'answer_text': 'Inability to integrate with other tools and services'},
                                         ],
                                         'correct_answer_id': 1
                                     }
                                 ]},

                                {'subject_id': 4,
                                 'subject_logo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Git-logo'
                                                 '.svg/640px-Git'
                                                 '-logo.svg.png',
                                 'subject_name': 'Git',
                                 'subject_content': readContentFile(subject="Git"),
                                 'subject_questions': [
                                     {
                                         'question_id': 1,
                                         'question_text': 'What is GitHub?',
                                         'answers': [
                                             {'answer_id': 1, 'answer_text': 'A web-based platform for version control and collaboration'},
                                             {'answer_id': 2, 'answer_text': 'A database management system'},
                                             {'answer_id': 3, 'answer_text': 'A cloud-based storage solution'},
                                             {'answer_id': 4, 'answer_text': 'A machine learning library'},
                                         ],
                                         'correct_answer_id': 1
                                     },
                                     {
                                         'question_id': 1,
                                         'question_text': 'What can developers do with GitHub?',
                                         'answers': [
                                             {'answer_id': 1, 'answer_text': 'Create and store code repositories'},
                                             {'answer_id': 2, 'answer_text': 'Collaborate on code with other team members'},
                                             {'answer_id': 3, 'answer_text': 'Manage software development projects'},
                                             {'answer_id': 4, 'answer_text': 'All of the above'},
                                         ],
                                         'correct_answer_id': 4
                                     },
                                     {
                                         'question_id': 2,
                                         'question_text': 'What project management tools does GitHub provide?',
                                         'answers': [
                                             {'answer_id': 1, 'answer_text': 'Issue tracking, milestone tracking, and project boards'},
                                             {'answer_id': 2, 'answer_text': 'Video editing and animation tools'},
                                             {'answer_id': 3, 'answer_text': 'Game development engines'},
                                             {'answer_id': 4, 'answer_text': 'Accounting software'},
                                         ],
                                         'correct_answer_id': 1
                                     }
                                 ]}, 
                                {'subject_id': 5,
                                 'subject_logo': 'https://www.svgrepo.com/show/379764/agile.svg',
                                 'subject_name': 'Agile',
                                 'subject_content': readContentFile(subject="Agile"),
                                 'subject_questions': [
                                     {
                                         'question_id': 1,
                                         'question_text': 'What are Agile practices?',
                                         'answers': [
                                             {'answer_id': 1, 'answer_text': 'A set of values and principles used in software development'},
                                             {'answer_id': 2, 'answer_text': 'A database management system'},
                                             {'answer_id': 3, 'answer_text': 'A cloud-based storage solution'},
                                             {'answer_id': 4, 'answer_text': 'A machine learning library'},
                                         ],
                                         'correct_answer_id': 1
                                     },
                                     {
                                         'question_id': 1,
                                         'question_text': 'What is Scrum?',
                                         'answers': [
                                             {'answer_id': 1, 'answer_text': 'An Agile methodology that uses short iterations called sprints to deliver working software'},
                                             {'answer_id': 2, 'answer_text': 'A project management tool used to manage financial accounts'},
                                             {'answer_id': 3, 'answer_text': 'A database management system'},
                                             {'answer_id': 4, 'answer_text': 'A machine learning algorithm'},
                                         ],
                                         'correct_answer_id': 1
                                     },
                                     {
                                         'question_id': 2,
                                         'question_text': 'What are some benefits of using Agile practices?',
                                         'answers': [
                                             {'answer_id': 1, 'answer_text': 'Improved project success rates, reduced time-to-market, and enhanced customer satisfaction'},
                                             {'answer_id': 2, 'answer_text': 'Longer development times and higher costs'},
                                             {'answer_id': 3, 'answer_text': 'Reduced collaboration and flexibility'},
                                             {'answer_id': 4, 'answer_text': 'Inability to respond to changes in requirements'},
                                         ],
                                         'correct_answer_id': 1
                                     }
                                 ]}, ]

        self._allCandidateRows = [{'candidate_id': 1,
                                   'first_name': 'Steff',
                                   'last_name': 'Potter',
                                   'fun_fact': 'I have played rugby for over 20 years',
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
                                   'last_name': 'Momoh',
                                   'fun_fact': "I have climbed 3 volcanos",
                                   'git_username': "angelangela1"}]

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
