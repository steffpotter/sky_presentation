from unittest import TestCase

from application.dao.subjectDao import SubjectDao
from application.model.subject import Subject


class SubjectDaoTests(TestCase):

    @classmethod
    def setUpClass(cls):
        # Class method to set up attributes for use within test methods
        # Instantiate an instance of SubjectDao that we will use in all tests
        cls._subjectDao = SubjectDao()

    def testGetAll(self):
        # Given SubjectDao instance
        # When I call the following method
        subjects = self._subjectDao.getAll()
        # Then the following assertions should be true
        self.assertTrue(isinstance(subjects, list))
        self.assertEqual(len(subjects), 5)

    def testGetCandidateById(self):
        # Given SubjectDao instance
        # When I call the following method
        subject = self._subjectDao.getSubject(1)
        # Then the following assertions should be true
        self.assertTrue(isinstance(subject, Subject))
        self.assertEqual(subject.get_subject_name(), 'Python')
