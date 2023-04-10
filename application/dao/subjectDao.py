from application.dao.baseDao import BaseDao
from application.model.subject import Subject
from application.db.exceptions.customDbExceptions import SubjectNotFoundError

import logging

logger = logging.getLogger(__name__)


class SubjectDao(BaseDao):
    """
    DAO class for Subject objects - The DAO pattern offers a layer of abstraction between the database
    and the application. This gives the dev team the freedom to evolve the db and business/ application layer separately.
    """

    def __init__(self, useMock):
        super().__init__(useMock)

    def getAll(self):
        """ Returns a list of Subject objects."""
        subjects = self._db.getAllSubjects()

        # returns list of dictionaries corresponding to Subject rows in db
        # map subject dictionaries to Subject Python object using a list comprehension
        subjectObjs = [self._createSubjectObjFromRawData(subject)
                       for subject in subjects]
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

    def _createSubjectObjFromRawData(self, rawSubjectData):
        return Subject(rawSubjectData.get("subject_id"),
                       rawSubjectData.get("subject_name"),
                       rawSubjectData.get("subject_logo"),
                       rawSubjectData.get("subject_content"),
                       rawSubjectData.get("subject_questions"))

    # Can extend to have Add, Update and Delete functions below
