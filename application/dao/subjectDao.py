from application.dao.baseDao import BaseDao
from subject import Subject


class SubjectDao(BaseDao):

    """
    DAO class for Subject objects - The DAO pattern offers a layer of abstraction between the database
    and the application. This gives the dev team the freedom to evolve the db and business/ application layer separately.
    """

    def __init__(self, useMock):
        super().__init__(useMock)

    def getAllSubjects(self):
        subjects = self._db.getAllSubjects()  # returns list of dictionaries corresponding to Subject rows in db
        # map subject dictionaries to Subject Python object using a list comprehension
        subjectObjs = [Subject(subject.get("subject_id"), subject.get("subject_name"), subject.get("subject_logo"))
                       for subject in subjects]
        return subjectObjs

    def getSubject(self, subjectId):
        subject = self._db.getSubject(subjectId)  # todo - test how mysql connector handles error when no subject found
        return Subject(subjectId, subject.get("subject_name"), subject.get("subject_logo"))

    # Can extend to have Add, Update and Delete functions below
