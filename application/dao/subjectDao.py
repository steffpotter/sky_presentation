from application.dao.baseDao import BaseDao
from application.db.exceptions.customDbExceptions import SubjectNotFoundError
from application.model.subject import Subject
from application.model.question import Question
from application.model.answer import Answer

import logging

logger = logging.getLogger(__name__)


class SubjectDao(BaseDao):
    """
    DAO class for Subject objects - The DAO pattern offers a layer of abstraction between the database
    and the application. This gives the dev team the freedom to evolve the db and business/ application layer separately.
    """

    def __init__(self):
        super().__init__()

    def getAll(self):
        """ Returns a list of Subject objects."""
        subjects = self._db.getAllSubjects()
        subjectObjs = [self._createSubjectObjFromRawData(subject)
                       for subject in subjects]

        # returns list of dictionaries corresponding to Subject rows in db
        # map subject dictionaries to Subject Python object using a list comprehension

        return subjectObjs

    def getSubject(self, subjectId):
        try:
            subject = self._db.getSubject(subjectId)
            return self._createSubjectObjFromRawData(subject)

        except SubjectNotFoundError:
            logger.warning(msg=f"Subject with id {subjectId} could not be found in database.")

    def getSubjectByName(self, subjectName):
        try:
            subject = self._db.getSubjectByName(subjectName)
            return self._createSubjectObjFromRawData(subject)

        except SubjectNotFoundError:
            logger.warning(msg=f"Subject with name {subjectName} could not be found in database.")

    def _createSubjectObjFromRawData(self, subject):
        subject = Subject(subject.get("subject_id"),
                          subject.get("subject_name"),
                          subject.get("subject_logo"),
                          subject.get("subject_content"),
                          [Question(question.get("question_id"),
                                    question.get("question_text"),
                                    question.get("correct_answer_id"),
                                    [Answer(answer.get("answer_id"),
                                            answer.get("answer_text")) for answer in question.get("answers")])
                           for question in subject.get("subject_questions")])

        return subject

    # Can extend to have Added, Update and Delete functions below
